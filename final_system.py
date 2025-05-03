# Importa módulos necessários do sistema
import os
import sys
import json

# Define constantes para os nomes dos arquivos JSON que armazenam os dados
CAMINHO_ARQUIVO_ESTUDANTE = 'arquivo_estudante.json'
CAMINHO_ARQUIVO_DISCIPLINA = 'arquivo_disciplina.json'
CAMINHO_ARQUIVO_PROFESSOR = 'arquivo_professor.json'
CAMINHO_ARQUIVO_TURMA = 'arquivo_turma.json'
CAMINHO_ARQUIVO_MATRICULA = 'arquivo_matricula.json'

# Função para limpar a tela do terminal (Windows e outros SO)
def limpar_terminal():
    os.system('cls') if sys.platform == 'win32' else os.system('clear')

# Função para limpar um número específico de linhas anteriores no terminal
def limpar_linha(qtd):
    for _ in range(qtd):
        print("\033[F\033[K", end="")

# Opções do menu principal
opcoes_menu_principal = {
    '1': 'Estudante',
    '2': 'Disciplina',
    '3': 'Professor',
    '4': 'Turma',
    '5': 'Matrícula',
    '6': 'Sair',
}

# Opções dos menus secundários
opcoes_menu_secundario = {
    '1': 'Incluir',
    '2': 'Listar',
    '3': 'Excluir',
    '4': 'Alterar',
    '5': 'Voltar',
}

# Função para exibir o menu principal
def MenuPrincipal():
    limpar_terminal()
    print('MENU PRINCIPAL')
    print(14*'-')
    for digito, menu in opcoes_menu_principal.items():
        print(f'{digito}. {menu}'.ljust(14) + '|')
        print(14*'-')

# Função para exibir um menu secundário, baseado na opção principal escolhida
def MenuSecundario(menu):
    limpar_terminal()
    print(f'MENU - {menu}')

    if menu == 'Sair': # Exibe opções específicas para a saída do sistema
        print(43*'-')
        print('(S) > Confirmar desligamento do sistema.'.ljust(43) + '|')
        print(43*'-')
        print('(V) > Voltar ao Menu Principal.'.ljust(43) + '|')
        print(43*'-')
    else: # Exibe as opções CRUD padrão
        print(14*'-')
        for digito, funcao in opcoes_menu_secundario.items():
            print(f'{digito}. {funcao}'.ljust(14) + '|')
            print(14*'-')

# Função para carregar dados de um arquivo JSON
def carregar_dados(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'r') as a:
            return json.load(a)
    # Se o arquivo não existir ou o JSON for inválido, retorna uma lista vazia
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Função para salvar dados em um arquivo JSON
def salvar_dados(dados, caminho_do_arquivo):
    with open(caminho_do_arquivo, 'w', encoding='utf8') as a:
        json.dump(dados, a, indent=2)

# Função para validar e obter o nome do estudante (apenas letras e espaços)
def validar_e_obter_nome():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o nome do estudante'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        # Obtém o nome, remove espaços extras e aplica capitalização de nome
        nome = input('Nome do estudante: ').strip().title()

        # Permite cancelar a operação
        if nome == 'Cancelar' or nome is None:
            return None

        # Verifica se o nome contém apenas letras após remover espaços
        nome_sem_espacos = nome.replace(' ', '')
        if nome_sem_espacos.isalpha() and nome:
            return nome
        else:
            print('\n--- Nome inválido ---')
            print('(O nome deve conter apenas letras e espaços.)')
            print('(Não pode ser vazio.)')
            input('Pressione Enter para tentar novamente...')

# Função para validar e obter o Registro Acadêmico (RA) do estudante (apenas números)
def validar_e_obter_ra():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o Registro Acadêmico (RA)'.center(45) + '|')
        print('(Apenas números)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        # Obtém o RA, remove espaços extras e capitaliza (para 'Cancelar')
        ra_input = input('Registro Acadêmico (RA): ').strip().capitalize()

        # Permite cancelar a operação
        if ra_input == 'Cancelar':
            return None

        try:
            # Tenta converter a entrada para inteiro
            ra = int(ra_input)
            return ra
        except ValueError:
            # Exibe mensagem de erro se a conversão falhar
            print('\n--- RA Inválido ---')
            print('(Insira apenas números para o Registro Acadêmico.)')
            input('Pressione Enter para tentar novamente...')

# Função para validar e obter o CPF do estudante (11 dígitos numéricos, não repetidos)
def validar_e_obter_cpf():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o CPF (11 dígitos, sem pontuação)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        # Obtém o CPF, remove espaços extras e capitaliza (para 'Cancelar')
        cpf = input('CPF (somente números): ').strip().capitalize()

        # Permite cancelar a operação
        if cpf == 'Cancelar':
            return None

        # Verifica se tem 11 dígitos e são todos numéricos
        if len(cpf) == 11 and cpf.isnumeric():
            # Verifica se todos os dígitos são iguais (CPF inválido)
            if cpf == cpf[0] * 11:
                 print('\n--- CPF Inválido ---')
                 print('(CPF com todos os dígitos iguais não é válido.)')
                 input('Pressione Enter para tentar novamente...')
            else:
                 return cpf
        else:
            # Exibe mensagem de erro se o formato for inválido
            print('\n--- CPF Inválido ---')
            print('(O CPF deve conter exatamente 11 dígitos numéricos.)')
            print('(Não inclua pontos ou traços.)')
            input('Pressione Enter para tentar novamente...')

# Função para incluir um novo estudante no arquivo JSON
def incluir_estudantes():
    # Carrega a lista de estudantes existente
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    while True:
        limpar_terminal()
        print('--- Cadastro de Novo Estudante ---')

        # Obtém e valida o nome
        nome = validar_e_obter_nome()
        if nome is None: # Se o usuário cancelou
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        # Obtém e valida o RA
        ra = validar_e_obter_ra()
        if ra is None: # Se o usuário cancelou
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        # Obtém e valida o CPF
        cpf = validar_e_obter_cpf()
        if cpf is None: # Se o usuário cancelou
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        # Carrega dados de professores para verificar CPF duplicado
        professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
        # Verifica se o CPF já existe entre os professores
        if any(p['cpf'] == cpf for p in professores):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado para um professor! ---')
             input('Pressione Enter para tentar novamente...')
             continue

        # Verifica se o CPF já existe entre os estudantes
        if any(e['cpf'] == cpf for e in estudantes):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado para um estudante! ---')
             input('Pressione Enter para tentar novamente...')
             continue

        # Verifica se o RA já existe entre os estudantes
        if any(e['ra'] == ra for e in estudantes):
            print(f'\n--- Erro: RA < {ra} > já cadastrado! ---')
            input('Pressione Enter para tentar novamente...')
            continue

        # Adiciona o novo estudante à lista
        estudantes.append({'nome': nome, 'ra': ra, 'cpf': cpf})
        salvar_dados(estudantes, CAMINHO_ARQUIVO_ESTUDANTE)

        # Exibe mensagem de sucesso com os dados cadastrados
        limpar_terminal()
        print('--- Estudante Cadastrado com Sucesso! ---')
        print(f'Nome: {nome}')
        print(f'RA: {ra}')
        print(f'CPF: {cpf}')
        print('-----------------------------------------')

        # Pergunta se deseja adicionar outro estudante
        while True:
            continuar = input('Deseja adicionar outro estudante? (S/N): ').strip().upper()
            if continuar in ['S', 'N']:
                break # Sai do loop de confirmação
            else:
                # Mensagem de erro para opção inválida
                print('--- Opção inválida ---\n'
                'Digite (S) para Sim ou (N) para Não.'
                )
                input('Pressione Enter para continuar...')
                limpar_linha(4)

        if continuar == 'N':
             break

    return # Retorna ao menu anterior

# Função para listar todos os estudantes cadastrados
def listar_estudantes():
    # Carrega a lista de estudantes
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    limpar_terminal()
    print('--- Lista de Estudantes Cadastrados ---')

    # Verifica se a lista está vazia
    if not estudantes:
        print('\n< Nenhum estudante cadastrado no momento >')
    else:
        # Imprime o cabeçalho da tabela
        print('-' * 65)
        print(f'{'#':<3} | {'Nome':<25} | {'RA':<12} | {'CPF':<15} |')
        print('-' * 65)

        # Itera sobre a lista de estudantes e mostra cada um formatado
        for indice, estudante in enumerate(estudantes):
            nome_str = str(estudante['nome'])
            ra_str = str(estudante['ra'])
            cpf_str = str(estudante['cpf'])
            print(f"{indice:<3} | {nome_str:<25} | {ra_str:<12} | {cpf_str:<15} |")

        print('-' * 65)

# Função para excluir um estudante da lista
def excluir_estudante():
    # Carrega a lista de estudantes
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    # Exibe a lista para o usuário escolher quem excluir
    listar_estudantes()

    # Se não houver estudantes, informa e retorna
    if not estudantes:
        input('Pressione Enter para voltar ao menu Estudante...')
        return

    # Loop para obter o índice do estudante a ser excluído
    while True:
        print(60*'-')
        print('Digite o índice < # > do estudante que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(60*'-')
        # Obtém o índice ou 'Cancelar'
        indice_estudante_input = input('Índice: ').strip().capitalize()

        # Permite cancelar a operação
        if indice_estudante_input == 'Cancelar':
            break

        try:
            # Tenta converter o índice para inteiro
            indice_estudante = int(indice_estudante_input)

            # Verifica se o índice é válido
            if 0 <= indice_estudante < len(estudantes):
                # Remove o estudante da lista pelo índice e guarda os dados do excluído
                estudante_excluido = estudantes.pop(indice_estudante)
                # Salva a lista atualizada
                salvar_dados(estudantes, CAMINHO_ARQUIVO_ESTUDANTE)
                # Exibe mensagem de sucesso
                print(f'\nEstudante: {estudante_excluido['nome']} | Foi excluído')
                input('Pressione Enter para continuar...')
                return # Retorna ao menu anterior
            else:
                # Levanta um erro se o índice estiver fora do intervalo
                raise IndexError

        # Captura erros de valor (não número) ou índice inválido
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)

# Função para atualizar os dados de um estudante existente
def atualizar_cadastro_estudante():
    # Carrega a lista de estudantes
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    # Exibe a lista para o usuário escolher quem atualizar
    listar_estudantes()

    # Se não houver estudantes, informa e retorna
    if not estudantes:
        input('\nPressione Enter para voltar ao menu Estudante...')
        return

    # Loop para obter o índice do estudante a ser atualizado
    while True:
        print(60*'-')
        print('Digite o índice < # > do estudante que deseja atualizar'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(60*'-')
        # Obtém o índice ou 'Cancelar'
        indice_estudante_input = input('Índice: ').strip().capitalize()

        # Permite cancelar a operação
        if indice_estudante_input == 'Cancelar':
            break

        try:
            # Tenta converter o índice para inteiro
            indice_estudante = int(indice_estudante_input)
            # Verifica se o índice é válido
            if 0 <= indice_estudante < len(estudantes):
                # Seleciona o estudante a ser atualizado
                estudante_selecionado = estudantes[indice_estudante]

                # Exibe os dados atuais do estudante selecionado
                print('\n--- Estudante Selecionado ---')
                print(f'Nome: {estudante_selecionado['nome']}')
                print(f'RA: {estudante_selecionado['ra']}')
                print(f'CPF: {estudante_selecionado['cpf']}')
                print('-----------------------------')

                # Controle para indicar se alguma alteração foi feita
                alteracao_feita = False
                # Loop para escolher qual campo atualizar
                while True:
                    print()
                    print(79 * '-')
                    print('Digite o número da ação desejada no campo abaixo'.center(79) + '|')
                    print('(1) Alterar Nome - (2) Alterar RA - (3) Alterar CPF - (4) Alterar tudo'.center(79) + '|')
                    print(79 * '-')
                    acao_usuario_atualizar = input('Ação: ').strip().upper()

                    # Opção 1: Alterar Nome
                    if acao_usuario_atualizar == '1':
                        novo_nome = validar_e_obter_nome() # Obtém e valida novo nome
                        if novo_nome is not None: # Se não cancelou
                            estudante_selecionado['nome'] = novo_nome
                            alteracao_feita = True
                        break

                    # Opção 2: Alterar RA
                    if acao_usuario_atualizar == '2':
                        novo_ra = validar_e_obter_ra() # Obtém e valida novo RA
                        if novo_ra is not None: # Se não cancelou
                            # Verifica se o novo RA já existe em outro estudante
                            if any(e['ra'] == novo_ra for i, e in enumerate(estudantes) if i != indice_estudante):
                                print(f'\n--- Erro: RA < {novo_ra} > já cadastrado para outro estudante! ---')
                                input('Pressione Enter para tentar novamente...')
                            else: # Se RA é único
                                estudante_selecionado['ra'] = novo_ra
                                alteracao_feita = True
                                break # Sai do loop de escolha de campo
                        break # Sai do loop de escolha de campo (mesmo se cancelou)

                    # Opção 3: Alterar CPF
                    if acao_usuario_atualizar == '3':
                        novo_cpf = validar_e_obter_cpf() # Obtém e valida novo CPF
                        if novo_cpf is not None: # Se não cancelou
                            professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
                            # Verifica se o novo CPF já existe em professor
                            if any(p['cpf'] == novo_cpf for p in professores):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para um professor! ---')
                                input('Pressione Enter para tentar novamente...')
                                break # Volta a pedir a ação (1, 2, 3 ou 4)
                            # Verifica se o novo CPF já existe em outro estudante
                            if any(e['cpf'] == novo_cpf for i, e in enumerate(estudantes) if i != indice_estudante):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para outro estudante! ---')
                                input('Pressione Enter para tentar novamente...')
                            else: # Se CPF é único
                                estudante_selecionado['cpf'] = novo_cpf
                                alteracao_feita = True
                                break # Sai do loop de escolha de campo
                        break # Sai do loop de escolha de campo (mesmo se cancelou)

                    # Opção 4: Alterar Tudo
                    if acao_usuario_atualizar == '4':
                        print("\n--- Alterando Nome ---")
                        novo_nome = validar_e_obter_nome()
                        if novo_nome is None: break # Cancela a alteração de tudo

                        print("\n--- Alterando RA ---")
                        novo_ra = validar_e_obter_ra()
                        if novo_ra is None: break # Cancela a alteração de tudo

                        # Verifica duplicidade do RA
                        if any(e['ra'] == novo_ra for i, e in enumerate(estudantes) if i != indice_estudante):
                            print(f'\n--- Erro: RA < {novo_ra} > já pertence a outro estudante! ---')
                            input('Pressione Enter para voltar...')
                            break # Volta a pedir a ação (1, 2, 3 ou 4)

                        print("\n--- Alterando CPF ---")
                        novo_cpf = validar_e_obter_cpf()
                        if novo_cpf is None: break # Cancela a alteração de tudo

                        # Verifica duplicidade do CPF com professores
                        professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
                        if any(p['cpf'] == novo_cpf for p in professores):
                            print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para um professor! ---')
                            input('Pressione Enter para voltar...')
                            break # Volta a pedir a ação

                        # Verifica duplicidade do CPF com outros estudantes
                        if any(e['cpf'] == novo_cpf for i, e in enumerate(estudantes) if i != indice_estudante):
                            print(f'\n--- Erro: CPF < {novo_cpf} > já pertence a outro estudante! ---')
                            input('Pressione Enter para voltar...')
                            break # Volta a pedir a ação

                        # Se todas as validações passaram, atualiza os dados
                        estudante_selecionado['nome'] = novo_nome
                        estudante_selecionado['ra'] = novo_ra
                        estudante_selecionado['cpf'] = novo_cpf
                        input('Nome, Registro Acadêmico e CPF foram alterados com sucesso!\nPressione Enter para continuar...')
                        alteracao_feita = True
                        break # Sai do loop de escolha de campo

                    # Se a ação digitada não for 1, 2, 3 ou 4
                    else:
                        print('--- Ação Inválida ---\n'
                            'Deve ser digitado apenas o número referente à ação\n'
                            'Ex: > 1 < para atualizar o nome')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(10)

                # Se alguma alteração foi realizada com sucesso
                if alteracao_feita:
                    salvar_dados(estudantes, CAMINHO_ARQUIVO_ESTUDANTE) # Salva os dados
                    print("\nAlterações salvas.")
                    input("Pressione Enter para voltar ao menu Estudante...")
                    return
                else: # Se nenhuma alteração foi feita (cancelou ou erro)
                    limpar_terminal()
                    listar_estudantes() # Apenas relista os estudantes

            else:
                # Levanta erro se o índice inicial for inválido
                raise IndexError

        # Captura erros de valor ou índice no input inicial do índice
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)

# Função para incluir uma nova disciplina
def incluir_disciplina():
    # Carrega a lista de disciplinas
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    limpar_terminal()
    print(40*'-')
    print('Cadastramento de Disciplinas'.center(40) + '|')
    print('(Digite "Cancelar" para voltar)'.center(40) + '|')
    print(40*'-')
    print()

    # Loop para obter e validar o nome da disciplina
    while True:
        nome = input('Nome da disciplina: ').capitalize().strip()
        # Permite cancelar
        if nome == 'Cancelar':
            input('Operação cancelada.\n'
                  'Pressione Enter para voltar ao menu Disciplina...'
                  )
            return
        # Valida se o nome não é numérico ou vazio
        if nome.isnumeric() or nome == '':
            input('--- Nome Inválido ---\n'
                'O nome da disciplina deve conter letras\n'
                'Pressione Enter para tentar novamente...'
                )
            limpar_linha(4)
            continue
        # Valida se o nome já existe (ignorando maiúsculas/minúsculas)
        if any(d['disciplina'].lower() == nome.lower() for d in disciplinas):
             input(f'--- Erro: Disciplina "{nome}" já cadastrada! ---\n'
                   'Pressione Enter para tentar novamente...')
             limpar_linha(3)
             continue
        break # Nome válido e único

    # Loop para obter e validar a data de abertura (dd/mm/aaaa, ano >= 2024)
    while True:
        abertura = input('Insira a data de abertura (dd/mm/aaaa): ').strip()
        # Permite cancelar
        if abertura.lower() == 'cancelar':
            input('Operação cancelada.\n'
                  'Pressione Enter para voltar ao menu Disciplina...'
                  )
            return
        try:
            # Extrai dia, mês e ano
            dia1 = int(abertura[:2])
            mes1 = int(abertura[3:5])
            ano1 = int(abertura[6:10])
            # Verifica formato, separadores, limites de dia/mês e ano mínimo
            if len(abertura) == 10 and abertura[2] == '/' and abertura[5] == '/' \
               and 0 < dia1 <= 31 and 0 < mes1 <= 12 and ano1 >= 2025:
                # Cria tupla para comparação posterior
                data_abertura_valida = (ano1, mes1, dia1)
                break # Data válida
            else:
                raise ValueError # Formato ou valores inválidos
        except (ValueError, IndexError): # Captura erro na conversão ou acesso a índice
            input('\n--- Data Inválida ---\n'
                'Formato: dd/mm/aaaa (ex: 24/10/2025).\n'
                'Verifique os separadores "/" e os valores.\n'
                'Pressione Enter para tentar novamente...'
                )
            limpar_linha(6)
            continue

    # Loop para obter e validar a data de fechamento (dd/mm/aaaa, >= data de abertura)
    while True:
        fechamento = input('Insira a data de fechamento (dd/mm/aaaa): ').strip()
        # Permite cancelar
        if fechamento.lower() == 'cancelar':
            input('Operação cancelada.\n'
                  'Pressione Enter para voltar ao menu Disciplina...'
                  )
            return
        try:
            # Extrai dia, mês e ano
            dia2 = int(fechamento[:2])
            mes2 = int(fechamento[3:5])
            ano2 = int(fechamento[6:10])
            # Verifica formato, separadores, limites de dia/mês e ano mínimo (igual ao de abertura)
            if len(fechamento) == 10 and fechamento[2] == '/' and fechamento[5] == '/' \
               and 0 < dia2 <= 31 and 0 < mes2 <= 12 and ano2 >= ano1:
                # Cria tupla para comparação
                data_fechamento_valida = (ano2, mes2, dia2)
                # Verifica se a data de fechamento é igual ou posterior à de abertura
                if data_fechamento_valida >= data_abertura_valida:
                    break # Data válida
                else:
                    # Data de fechamento anterior à de abertura
                    raise ValueError
            else:
                # Formato ou valores inválidos
                raise ValueError
        except (ValueError, IndexError): # Captura erro na conversão, índice ou data inválida
            input('\n--- Data Inválida ---\n'
                  'Formato: dd/mm/aaaa.\n'
                  'Verifique os separadores "/" e os valores.\n'
                  'Pressione Enter para tentar novamente...'
                  )
            limpar_linha(6)
            continue

    # Loop para obter e validar a carga horária (número inteiro positivo)
    while True:
        carga_horaria_input = input('Carga horária (Apenas números positivos): ').strip()

        # Permite cancelar
        if carga_horaria_input.lower() == 'cancelar':
            input('Operação cancelada.\n'
                  'Pressione Enter para voltar ao menu Disciplina...'
                  )
            return
        try:
            # Tenta converter para inteiro
            carga_horaria = int(carga_horaria_input)
            # Verifica se é positiva
            if carga_horaria > 0:
                break # Carga horária válida
            else:
                raise ValueError # Número não positivo
        except ValueError: # Captura erro na conversão ou valor negativo
            input('--- Carga horária Inválida ---\n'
                'Insira apenas números inteiros positivos.\n'
                'Pressione Enter para tentar novamente...'
                )
            limpar_linha(4)
            continue

    # Adiciona a nova disciplina à lista
    disciplinas.append({'disciplina': nome, 'abertura': abertura, 'fechamento': fechamento, 'carga_horaria': carga_horaria})
    # Salva a lista atualizada
    salvar_dados(disciplinas, CAMINHO_ARQUIVO_DISCIPLINA)
    # Exibe mensagem de sucesso
    input(f'\nDisciplina: ({nome}) cadastrada com sucesso!\n'
          'Pressione Enter para continuar...'
          )

# Função para listar todas as disciplinas cadastradas
def listar_disciplinas():
    # Carrega a lista de disciplinas
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    limpar_terminal()
    print('--- Lista de Disciplinas Cadastradas ---')

    # Verifica se a lista está vazia
    if not disciplinas:
        print('\n< Nenhuma disciplina cadastrada no momento >')
    else:
        # Imprime o cabeçalho da tabela
        print('-' * 84)
        print(f'{'#':<3} | {'Disciplina':<35} | {'Abertura':<10} | {'Fechamento':<10} | {'Carga Horária':<12} |')
        print('-' * 84)

        # Itera sobre a lista e imprime cada disciplina formatada
        for indice, disciplina in enumerate(disciplinas):
            disciplina_nome = str(disciplina['disciplina'])
            disciplina_abertura = str(disciplina['abertura'])
            disciplina_fechamento = str(disciplina['fechamento'])
            disciplina_carga_horaria = str(disciplina['carga_horaria'])
            print(f'{indice:<3} | {disciplina_nome:<35} | {disciplina_abertura:<10} | {disciplina_fechamento:<10} | {disciplina_carga_horaria:<13} |')

        print('-' * 84)

# Função para excluir uma disciplina da lista
def excluir_disciplina():
    # Carrega a lista de disciplinas
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    # Exibe a lista para o usuário escolher qual excluir
    listar_disciplinas()

    # Se não houver disciplinas, informa e retorna
    if not disciplinas:
        input('\nPressione Enter para voltar ao menu Disciplina...')
        return

    # Loop para obter o índice da disciplina a ser excluída
    while True:
        print(60*'-')
        print('Digite o índice < # > da disciplina que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(60*'-')
        # Obtém o índice ou 'Cancelar'
        indice_disciplina_input = input('Índice: ').strip().capitalize()

        # Permite cancelar a operação
        if indice_disciplina_input == 'Cancelar':
            break

        try:
            # Tenta converter o índice para inteiro
            indice_disciplina = int(indice_disciplina_input)
            # Verifica se o índice é válido
            if 0 <= indice_disciplina < len(disciplinas):
                # Remove a disciplina da lista e guarda os dados da excluída
                disciplina_excluida = disciplinas.pop(indice_disciplina)
                # Salva a lista atualizada
                salvar_dados(disciplinas, CAMINHO_ARQUIVO_DISCIPLINA)
                # Exibe mensagem de sucesso
                print(f'\nDisciplina: {disciplina_excluida['disciplina']} | Foi excluída')
                input('Pressione Enter para continuar...')
                return # Retorna ao menu anterior
            else:
                # Levanta um erro se o índice estiver fora do intervalo
                raise IndexError

        # Captura erros de valor (não número) ou índice inválido
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(5)

# Função para atualizar os dados de uma disciplina existente
def atualizar_cadastro_disciplina():
    # Carrega a lista de disciplinas
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    # Exibe a lista para o usuário escolher qual atualizar
    listar_disciplinas()

    # Se não houver disciplinas, informa e retorna
    if not disciplinas:
        input('\nPressione Enter para voltar ao menu Disciplina...')
        return

    # Loop para obter o índice da disciplina a ser atualizada
    while True:
        print(60*'-')
        print('Digite o índice < # > da disciplina que deseja atualizar'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(60*'-')
        # Obtém o índice ou 'Cancelar'
        indice_disciplina_input = input('Índice: ').strip().capitalize()

        # Permite cancelar a operação
        if indice_disciplina_input == 'Cancelar':
            break

        try:
            # Tenta converter o índice para inteiro
            indice_disciplina = int(indice_disciplina_input)
            # Verifica se o índice é válido
            if 0 <= indice_disciplina < len(disciplinas):
                # Seleciona a disciplina a ser atualizada
                disciplina_selecionada = disciplinas[indice_disciplina]

                # Exibe os dados atuais da disciplina selecionada
                print('\n--- Disciplina Selecionada ---')
                print(f'Disciplina: {disciplina_selecionada['disciplina']}')
                print(f'Abertura: {disciplina_selecionada['abertura']}')
                print(f'Fechamento: {disciplina_selecionada['fechamento']}')
                print(f'Carga Horária: {disciplina_selecionada['carga_horaria']}')
                print('-----------------------------')

                # Flag para indicar se alguma alteração foi feita
                alteracao_feita = False
                # Loop para escolher qual campo atualizar
                while True:
                    print()
                    print(100 * '-')
                    print('Digite o número da ação desejada'.center(100) + '|')
                    print('(1) Alterar Nome - (2) Alterar Abertura - (3) Alterar Fechamento - (4) Alterar Carga Horária'.center(100) + '|')
                    print(100 * '-')
                    # Obtém a ação desejada
                    acao_usuario_atualizar = input('Ação: ').strip().upper()

                    # Opção 1: Alterar Nome
                    if acao_usuario_atualizar == '1':
                        while True: # Loop interno para validar o novo nome
                            novo_nome = input('Nome atualizado da disciplina ("Cancelar" para voltar): ').capitalize().strip()
                            if novo_nome == 'Cancelar': break # Sai do loop interno
                            # Valida se não é numérico ou vazio
                            if novo_nome.isnumeric() or novo_nome == '':
                                input('--- Nome Inválido ---\n'
                                    'O nome da disciplina deve conter letras\n'
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(4)
                            # Valida se o nome já existe em outra disciplina
                            elif any(d['disciplina'].lower() == novo_nome.lower() for i, d in enumerate(disciplinas) if i != indice_disciplina):
                                input(f'--- Erro: Disciplina "{novo_nome}" já existe. ---\n'
                                      'Pressione Enter para tentar novamente...')
                                limpar_linha(3)
                            else: # Nome válido e único
                                disciplina_selecionada['disciplina'] = novo_nome
                                alteracao_feita = True
                                break # Sai do loop interno
                        break # Sai do loop de escolha de campo

                    # Opção 2: Alterar Data de Abertura
                    elif acao_usuario_atualizar == '2':
                        # Tenta obter a data de fechamento atual para validação cruzada
                        try:
                            fechamento_atual = disciplina_selecionada['fechamento']
                            dia_f = int(fechamento_atual[:2]); mes_f = int(fechamento_atual[3:5]); ano_f = int(fechamento_atual[6:10])
                            data_fechamento_atual = (ano_f, mes_f, dia_f)
                        except: data_fechamento_atual = None # Se não conseguir, ignora por enquanto

                        while True: # Loop interno para validar a nova data de abertura
                            abertura = input('Insira a data atualizada de abertura (dd/mm/aaaa ou "Cancelar"): ').strip()
                            if abertura.lower() == 'cancelar': break # Sai do loop interno
                            try:
                                # Valida formato e valores da nova data
                                dia1 = int(abertura[:2]); mes1 = int(abertura[3:5]); ano1 = int(abertura[6:10])
                                if len(abertura) == 10 and abertura[2] == '/' and abertura[5] == '/' \
                                   and 0 < dia1 <= 31 and 0 < mes1 <= 12 and ano1 >= 2025:
                                    data_abertura_nova = (ano1, mes1, dia1)
                                    # Verifica se a nova data de abertura é <= à data de fechamento atual (se existir)
                                    if data_fechamento_atual is None or data_abertura_nova <= data_fechamento_atual:
                                        disciplina_selecionada['abertura'] = abertura
                                        alteracao_feita = True
                                        break # Sai do loop interno (data válida)
                                    else: raise ValueError # Data de abertura posterior ao fechamento
                                else: raise ValueError # Formato ou valores inválidos
                            except (ValueError, IndexError): # Captura erros
                                input('\n--- Data Inválida ---\n'
                                    'Formato: dd/mm/aaaa. Verifique valores e separadores.\n'
                                    'OBS: Verifique as datas.\n' # Avisa sobre possível conflito com fechamento
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(6)
                                continue # Tenta novamente
                        break # Sai do loop de escolha de campo

                    # Opção 3: Alterar Data de Fechamento
                    elif acao_usuario_atualizar == '3':
                        # Tenta obter a data de abertura atual para validação cruzada
                        try:
                            abertura_atual = disciplina_selecionada['abertura']
                            dia_a = int(abertura_atual[:2]); mes_a = int(abertura_atual[3:5]); ano_a = int(abertura_atual[6:10])
                            data_abertura_atual = (ano_a, mes_a, dia_a)
                        except: data_abertura_atual = None # Se não conseguir, ignora por enquanto

                        while True: # Loop interno para validar a nova data de fechamento
                            fechamento = input('Insira a data atualizada de fechamento (dd/mm/aaaa ou "Cancelar"): ').strip()
                            if fechamento.lower() == 'cancelar': break # Sai do loop interno
                            try:
                                # Valida formato e valores da nova data
                                dia2 = int(fechamento[:2]); mes2 = int(fechamento[3:5]); ano2 = int(fechamento[6:10])
                                if len(fechamento) == 10 and fechamento[2] == '/' and fechamento[5] == '/' \
                                   and 0 < dia2 <= 31 and 0 < mes2 <= 12 and ano2 >= 2025: # Ano 2025 ou maior
                                    data_fechamento_nova = (ano2, mes2, dia2)
                                    # Verifica se a nova data de fechamento é >= à data de abertura atual (se existir)
                                    if data_abertura_atual is None or data_fechamento_nova >= data_abertura_atual:
                                        disciplina_selecionada['fechamento'] = fechamento
                                        alteracao_feita = True
                                        break # Sai do loop interno (data válida)
                                    else: raise ValueError # Data de fechamento anterior à abertura
                                else: raise ValueError # Formato ou valores inválidos
                            except (ValueError, IndexError):
                                input('\n--- Data Inválida ---\n'
                                    'Formato: dd/mm/aaaa. Verifique valores e separadores.\n'
                                    'OBS: Verifique as datas.\n'
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(6)
                                continue # Tenta novamente
                        break # Sai do loop de escolha de campo

                    # Opção 4: Alterar Carga Horária
                    elif acao_usuario_atualizar == '4':
                         while True: # Loop interno para validar a nova carga horária
                            carga_horaria_input = input('Carga horária atualizada (Apenas números positivos ou "Cancelar"): ').strip()
                            if carga_horaria_input.lower() == 'cancelar': break # Sai do loop interno
                            try:
                                # Tenta converter e valida se é positiva
                                carga_horaria = int(carga_horaria_input)
                                if carga_horaria > 0:
                                    disciplina_selecionada['carga_horaria'] = carga_horaria
                                    alteracao_feita = True
                                    break # Sai do loop interno (carga horária válida)
                                else:
                                    raise ValueError # Não é positiva
                            except ValueError: # Captura erros
                                input('--- Carga Horária Inválida ---\n'
                                        'Insira apenas números inteiros positivos.\n'
                                        'Pressione Enter para tentar novamente...'
                                        )
                                limpar_linha(4)
                                continue # Tenta novamente
                         break # Sai do loop de escolha de campo

                    # Se a ação digitada não for 1, 2, 3 ou 4
                    else:
                        print('\n--- Ação Inválida ---')
                        print('Digite 1, 2, 3 ou 4.')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(10)

                # Se alguma alteração foi realizada com sucesso
                if alteracao_feita:
                    salvar_dados(disciplinas, CAMINHO_ARQUIVO_DISCIPLINA) # Salva os dados
                    print("\nAlterações salvas.")
                    input("Pressione Enter para voltar ao menu Disciplina...")
                    # Chama a própria função novamente para mostrar a lista atualizada
                    return atualizar_cadastro_disciplina()
                else: # Se nenhuma alteração foi feita (cancelou ou erro)
                    limpar_terminal()
                    listar_disciplinas() # Apenas relista as disciplinas

            else:
                # Levanta erro se o índice inicial for inválido
                raise IndexError

        # Captura erros de valor ou índice no input inicial do índice
        except (ValueError, IndexError):
            print('--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(8)

# Função para validar e obter o nome do professor (similar ao estudante)
def validar_e_obter_nome_professor():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o nome do professor'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        nome = input('Nome do professor: ').strip().title()

        # Permite cancelar
        if nome == 'Cancelar':
            return None

        # Valida se contém apenas letras e espaços e não está vazio
        nome_sem_espacos = nome.replace(' ', '')
        if nome_sem_espacos.isalpha() and nome:
            return nome
        else:
            print('\n--- Nome inválido ---\n'
                'O nome deve conter apenas letras e espaços.\n'
                '(Não pode ser vazio.)')
            input('Pressione Enter para tentar novamente...')
            continue

# Função para validar e obter a Matrícula Funcional (MF) do professor (apenas números)
def validar_e_obter_mf_professor():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite a Matrícula Funcional (MF)'.center(45) + '|')
        print('(Apenas números)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        mf_input = input('Matrícula Funcional (MF): ').strip().capitalize()

        # Permite cancelar
        if mf_input == 'Cancelar':
            return None

        try:
            # Tenta converter para inteiro
            mf = int(mf_input)
            return mf
        except ValueError: # Captura erro na conversão
            print('\n--- MF Inválida ---')
            print('(Insira apenas números para a Matrícula Funcional.)')
            input('Pressione Enter para tentar novamente...')

# Função para validar e obter o CPF do professor (similar ao estudante)
def validar_e_obter_cpf_professor():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o CPF (11 dígitos, sem pontuação)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        cpf = input('CPF (somente números): ').strip().capitalize()

        # Permite cancelar
        if cpf == 'Cancelar':
            return None

        # Valida tamanho, se é numérico e se não tem dígitos repetidos
        if len(cpf) == 11 and cpf.isnumeric():
            if cpf == cpf[0] * 11:
                 print('\n--- CPF Inválido ---')
                 print('(CPF com todos os dígitos iguais não é válido.)')
                 input('Pressione Enter para tentar novamente...')
            else:
                 return cpf
        else:
            print('\n--- CPF Inválido ---')
            print('(O CPF deve conter exatamente 11 dígitos numéricos.)')
            print('(Não inclua pontos ou traços.)')
            input('Pressione Enter para tentar novamente...')

# Função para incluir um novo professor
def incluir_professor():
    # Carrega a lista de professores
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    while True:
        limpar_terminal()
        print('--- Cadastro de Novo Professor ---')
        # Obtém e valida nome
        nome = validar_e_obter_nome_professor()
        if nome is None: # Cancela
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Professor...')
            return

        # Obtém e valida MF
        mf = validar_e_obter_mf_professor()
        if mf is None: # Cancela
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Professor...')
            return

        # Obtém e valida CPF
        cpf = validar_e_obter_cpf_professor()
        if cpf is None: # Cancela
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Professor...')
            return

        # Carrega estudantes para verificar CPF duplicado
        estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
        # Verifica se CPF já existe em estudante
        if any(e['cpf'] == cpf for e in estudantes):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado para um estudante! ---')
             input('Pressione Enter para tentar novamente...')
             continue # Volta ao início do loop

        # Verifica se CPF já existe em outro professor
        if any(p['cpf'] == cpf for p in professores):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado para um professor! ---')
             input('Pressione Enter para tentar novamente...')
             continue # Volta ao início do loop

        # Verifica se MF já existe em outro professor
        if any(p['mf'] == mf for p in professores):
            print(f'\n--- Erro: MF < {mf} > já cadastrado! ---')
            input('Pressione Enter para tentar novamente...')
            continue # Volta ao início do loop

        # Adiciona o novo professor à lista
        professores.append({'nome': nome, 'mf': mf, 'cpf': cpf})
        # Salva a lista atualizada
        salvar_dados(professores, CAMINHO_ARQUIVO_PROFESSOR)

        # Exibe mensagem de sucesso
        limpar_terminal()
        print('--- Professor Cadastrado com Sucesso! ---')
        print(f'Nome: {nome}')
        print(f'MF: {mf}')
        print(f'CPF: {cpf}')
        print('-----------------------------------------')

        # Pergunta se deseja adicionar outro professor
        while True:
            continuar = input('Deseja adicionar outro professor? (S/N): ').strip().upper()
            if continuar in ['S', 'N']:
                break
            else:
                print('--- Opção inválida ---\n'
                'Digite (S) para Sim ou (N) para Não.'
                )
                input('Pressione Enter para continuar...')
                limpar_linha(4)

        if continuar == 'N':
             break

    return # Retorna ao menu anterior

# Função para listar todos os professores cadastrados
def listar_professores():
    # Carrega a lista de professores
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    limpar_terminal()
    print('--- Lista de Professores Cadastrados ---')

    # Verifica se a lista está vazia
    if not professores:
        print('\n< Nenhum professor cadastrado no momento >')
    else:
        # Imprime o cabeçalho da tabela
        print('-' * 65)
        print(f'{'#':<3} | {'Nome':<25} | {'MF':<12} | {'CPF':<15} |')
        print('-' * 65)

        # Itera sobre a lista e imprime cada professor formatado
        for indice, professor in enumerate(professores):
            nome_str = str(professor['nome'])
            mf_str = str(professor['mf'])
            cpf_str = str(professor['cpf'])
            print(f"{indice:<3} | {nome_str:<25} | {mf_str:<12} | {cpf_str:<15} |")

        # Imprime o rodapé da tabela
        print('-' * 65)

# Função para excluir um professor da lista
def excluir_professores():
    # Carrega a lista de professores
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    # Exibe a lista para o usuário escolher quem excluir
    listar_professores()

    # Se não houver professores, informa e retorna
    if not professores:
        input('\nPressione Enter para voltar ao menu Professor...')
        return

    # Loop para obter o índice do professor a ser excluído
    while True:
        print(59*'-')
        print('Digite o índice < # > do professor que deseja excluir'.ljust(59) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(59) + '|')
        print(59*'-')
        # Obtém o índice ou 'Cancelar'
        indice_professor_input = input('Índice: ').strip().capitalize()

        # Permite cancelar
        if indice_professor_input == 'Cancelar':
            break # Sai do loop de exclusão

        try:
            # Tenta converter o índice para inteiro
            indice_professor = int(indice_professor_input)
            # Verifica se o índice é válido
            if 0 <= indice_professor < len(professores):
                # Remove o professor da lista e guarda os dados do excluído
                professor_excluido = professores.pop(indice_professor)
                # Salva a lista atualizada
                salvar_dados(professores, CAMINHO_ARQUIVO_PROFESSOR)
                # Exibe mensagem de sucesso
                print(f'\nProfessor: {professor_excluido['nome']} | Foi excluído')
                input('Pressione Enter para continuar...')
                return # Retorna ao menu anterior
            else:
                # Levanta um erro se o índice estiver fora do intervalo
                raise IndexError
        # Captura erros de valor ou índice inválido
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---\n'
                'O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)
            continue # Tenta novamente

# Função para atualizar os dados de um professor existente
def atualizar_cadastro_professor():
    # Carrega a lista de professores
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    # Exibe a lista para o usuário escolher quem atualizar
    listar_professores()

    # Se não houver professores, informa e retorna
    if not professores:
        input('\nPressione Enter para voltar ao menu Professor...')
        return

    # Loop para obter o índice do professor a ser atualizado
    while True:
        print(59*'-')
        print('Digite o índice < # > do professor que deseja atualizar'.ljust(59) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(59) + '|')
        print(59*'-')
        # Obtém o índice ou 'Cancelar'
        indice_professor_input = input('Índice: ').strip().capitalize()

        # Permite cancelar
        if indice_professor_input == 'Cancelar':
            break # Sai do loop de atualização

        try:
            # Tenta converter o índice para inteiro
            indice_professor = int(indice_professor_input)
            # Verifica se o índice é válido
            if 0 <= indice_professor < len(professores):
                # Seleciona o professor a ser atualizado
                professor_selecionado = professores[indice_professor]

                # Exibe os dados atuais do professor selecionado
                print('\n--- Professor Selecionado ---')
                print(f'Nome: {professor_selecionado['nome']}')
                print(f'MF: {professor_selecionado['mf']}')
                print(f'CPF: {professor_selecionado['cpf']}')
                print('-----------------------------')

                # Flag para indicar se alguma alteração foi feita
                alteracao_feita = False
                # Loop para escolher qual campo atualizar
                while True:
                    print()
                    print(79 * '-')
                    print('Digite o número da ação desejada no campo abaixo'.center(80) + '|')
                    print('(1) Alterar Nome - (2) Alterar MF - (3) Alterar CPF - (4) Alterar tudo'.center(80) + '|')
                    print(79 * '-')
                    # Obtém a ação desejada
                    acao_usuario_atualizar = input('Ação: ').strip().upper()

                    # Opção 1: Alterar Nome
                    if acao_usuario_atualizar == '1':
                        novo_nome = validar_e_obter_nome_professor() # Obtém e valida novo nome
                        if novo_nome is not None: # Se não cancelou
                            professor_selecionado['nome'] = novo_nome
                            alteracao_feita = True
                        break # Sai do loop de escolha de campo

                    # Opção 2: Alterar MF
                    if acao_usuario_atualizar == '2':
                        novo_mf = validar_e_obter_mf_professor() # Obtém e valida nova MF
                        if novo_mf is not None: # Se não cancelou
                            # Verifica se a nova MF já existe em outro professor
                            if any(p['mf'] == novo_mf for i, p in enumerate(professores) if i != indice_professor):
                                print(f'\n--- Erro: MF < {novo_mf} > já cadastrado para outro professor! ---')
                                input('Pressione Enter para tentar novamente...')
                                # Não sai do loop, pede a ação novamente
                            else: # MF única
                                professor_selecionado['mf'] = novo_mf
                                alteracao_feita = True
                                break # Sai do loop de escolha de campo
                        break # Sai do loop de escolha de campo (mesmo se cancelou)

                    # Opção 3: Alterar CPF
                    if acao_usuario_atualizar == '3':
                        novo_cpf = validar_e_obter_cpf_professor() # Obtém e valida novo CPF
                        if novo_cpf is not None: # Se não cancelou
                            estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
                            # Verifica se o novo CPF já existe em estudante
                            if any(e['cpf'] == novo_cpf for e in estudantes):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para um estudante! ---')
                                input('Pressione Enter para tentar novamente...')
                                break # Volta a pedir a ação
                            # Verifica se o novo CPF já existe em outro professor
                            if any(p['cpf'] == novo_cpf for i, p in enumerate(professores) if i != indice_professor):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para outro professor! ---')
                                input('Pressione Enter para tentar novamente...')
                                # Não sai do loop, pede a ação novamente
                            else: # CPF único
                                professor_selecionado['cpf'] = novo_cpf
                                alteracao_feita = True
                                break # Sai do loop de escolha de campo
                        break # Sai do loop de escolha de campo (mesmo se cancelou)

                    # Opção 4: Alterar Tudo
                    if acao_usuario_atualizar == '4':
                        print("\n--- Alterando Nome ---")
                        novo_nome = validar_e_obter_nome_professor()
                        if novo_nome is None: break # Cancela alteração de tudo

                        print("\n--- Alterando MF ---")
                        novo_mf = validar_e_obter_mf_professor()
                        if novo_mf is None: break # Cancela alteração de tudo

                        # Verifica duplicidade da MF
                        if any(p['mf'] == novo_mf for i, p in enumerate(professores) if i != indice_professor):
                            print(f'\n--- Erro: MF < {novo_mf} > já pertence a outro professor! ---')
                            input('Pressione Enter para voltar...')
                            break # Volta a pedir a ação

                        print("\n--- Alterando CPF ---")
                        novo_cpf = validar_e_obter_cpf_professor()
                        if novo_cpf is None: break # Cancela alteração de tudo

                        # Verifica duplicidade do CPF com estudantes
                        estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
                        if any(e['cpf'] == novo_cpf for e in estudantes):
                            print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para um estudante! ---')
                            input('Pressione Enter para voltar...')
                            break # Volta a pedir a ação

                        # Verifica duplicidade do CPF com outros professores
                        if any(p['cpf'] == novo_cpf for i, p in enumerate(professores) if i != indice_professor):
                            print(f'\n--- Erro: CPF < {novo_cpf} > já pertence a outro professor! ---')
                            input('Pressione Enter para voltar...')
                            break # Volta a pedir a ação

                        # Se todas as validações passaram, atualiza os dados
                        professor_selecionado['nome'] = novo_nome
                        professor_selecionado['mf'] = novo_mf
                        professor_selecionado['cpf'] = novo_cpf
                        alteracao_feita = True
                        break # Sai do loop de escolha de campo

                    # Se a ação digitada não for 1, 2, 3, 4 ou C
                    else:
                        print('--- Ação Inválida ---\n'
                            'Deve ser digitado apenas o número referente à ação\n'
                            'Ex: > 1 < para atualizar o nome')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(10)

                # Se alguma alteração foi realizada com sucesso
                if alteracao_feita:
                    salvar_dados(professores, CAMINHO_ARQUIVO_PROFESSOR) # Salva os dados
                    print('\nAlterações salvas.')
                    input('Pressione Enter para voltar ao menu Professor...')
                    # Chama a própria função novamente para mostrar a lista atualizada
                    return atualizar_cadastro_professor()
                else: # Se nenhuma alteração foi feita (cancelou ou erro)
                    limpar_terminal()
                    listar_professores() # Apenas relista os professores

            else:
                # Levanta erro se o índice inicial for inválido
                raise IndexError

        # Captura erros de valor ou índice no input inicial do índice
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9) # Limpa erro e input
            continue # Tenta novamente obter o índice do professor

# Função para incluir uma nova turma (associando disciplina e professor)
def incluir_turma():
    limpar_terminal()
    # Carrega dados necessários
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    turma = carregar_dados(CAMINHO_ARQUIVO_TURMA) # Carrega turmas existentes

    # Verifica se existem disciplinas cadastradas
    if not disciplinas:
        input('< Não há disciplinas cadastradas no momento >\n'
              'Pressione Enter para continuar...'
              )
        return # Retorna se não houver disciplinas

    # Verifica se existem professores cadastrados
    if not professores:
        input('< Não há professores cadastrados no momento >\n'
              'Pressione Enter para continuar...'
              )
        return # Retorna se não houver professores

    # Loop para obter e validar o código da turma
    while True:
        print(45*'-')
        print('Crie um código para a turma no campo abaixo'.center(45) + '|')
        print('(Padrão alfanumérico)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        # Obtém o código, converte para maiúsculo e remove espaços
        cod_turma = input('Código da turma: ').upper().strip()

        # Permite cancelar
        if cod_turma == 'CANCELAR':
            return

        # Verifica se o código não está vazio
        if cod_turma == '':
            input('--- Código Inválido ---\n'
                    'Pressione Enter para tentar novamente...'
                    )
            limpar_linha(8) # Limpa erro e input
            continue
        # TODO: Adicionar verificação se código da turma já existe
        else:
            break # Código válido (não vazio)

    # Lista as disciplinas para seleção
    listar_disciplinas()
    # Loop para selecionar a disciplina da turma
    while True:
        print(70*'-')
        print('Digite o índice < # > da disciplina que deseja adicionar a turma'.center(70) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.center(70) + '|')
        print(70*'-')
        # Obtém o índice ou 'Cancelar'
        indice_disciplina_input = input('Índice: ').strip().capitalize()

        # Permite cancelar
        if indice_disciplina_input == 'Cancelar':
            return

        try:
            # Converte e valida o índice
            indice_disciplina = int(indice_disciplina_input)
            if 0 <= indice_disciplina < len(disciplinas):
                # Obtém o nome da disciplina selecionada
                disciplina_da_turma = disciplinas[indice_disciplina]['disciplina']
                break # Índice válido, sai do loop
            else:
                raise Exception # Índice fora do intervalo

        except Exception: # Captura erro de conversão ou índice inválido
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)
            continue # Tenta novamente

    # Lista os professores para seleção
    listar_professores()
    # Loop para selecionar o professor da turma
    while True:
        print(70*'-')
        print('Digite o índice < # > do professor que deseja adicionar a turma'.center(70) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.center(70) + '|')
        print(70*'-')
        # Obtém o índice ou 'Cancelar'
        indice_professor_input = input('Índice: ').strip().capitalize()

        # Permite cancelar
        if indice_professor_input == 'Cancelar':
            return

        try:
            # Converte e valida o índice
            indice_professor = int(indice_professor_input)
            if 0 <= indice_professor < len(professores):
                # Obtém o nome do professor selecionado
                professor_da_turma = professores[indice_professor]['nome']
                break # Índice válido, sai do loop
            else:
                raise Exception # Índice fora do intervalo
        except Exception: # Captura erro de conversão ou índice inválido
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)
            continue # Tenta novamente

    try:
        limpar_terminal()
        # Adiciona a nova turma à lista (carregada no início da função)
        turma.append({'codigo_de_turma': cod_turma, 'disciplina': disciplina_da_turma, 'professor': professor_da_turma})
        # Salva a lista atualizada de turmas
        salvar_dados(turma, CAMINHO_ARQUIVO_TURMA)
        # Exibe mensagem de sucesso
        print(50*'-')
        print('--- Turma Criada com Sucesso ---'.center(50) + '|')
        print(f'Turma: {cod_turma}'.center(50) + '|')
        print(f'Disciplina: {disciplina_da_turma}'.center(50) + '|')
        print(f'Professor: {professor_da_turma}'.center(50) + '|')
        print(50*'-')
        input('Pressione Enter para continuar...')
        return
    except: # Captura erro genérico ao salvar (pouco provável aqui)
        print('--- Erro Inesperado ---')
        input('Pressione Enter para refazer a criação da turma...')
        # Chama a função novamente em caso de erro
        return incluir_turma()

# Função para listar todas as turmas cadastradas
def listar_turmas():
    # Carrega a lista de turmas
    turmas = carregar_dados(CAMINHO_ARQUIVO_TURMA)
    limpar_terminal()
    print('--- Lista de Turmas Cadastradas ---')

    # Verifica se a lista está vazia
    if not turmas:
        print('\n< Nenhuma turma cadastrado no momento >')
        return # Retorna se não houver turmas

    else:
        # Imprime o cabeçalho da tabela
        print('-' * 98)
        print(f'{'#':<3} | {'Código de Turma':<20} | {'Disciplina':<35} | {'Professor':<30} |')
        print('-' * 98)

        # Itera sobre a lista e imprime cada turma formatada
        for indice, turma_item in enumerate(turmas):
            codigo_str = str(turma_item['codigo_de_turma'])
            disciplina_str = str(turma_item['disciplina'])
            professor_str = str(turma_item['professor'])
            print(f"{indice:<3} | {codigo_str:<20} | {disciplina_str:<35} | {professor_str:<30} |")

        print('-' * 98)

# Função para excluir uma turma da lista
def excluir_turma():
    # Carrega a lista de turmas
    turmas = carregar_dados(CAMINHO_ARQUIVO_TURMA)
    # Exibe a lista para o usuário escolher qual excluir
    listar_turmas()

    # Se não houver turmas, informa e retorna
    if not turmas:
        input('\nPressione Enter para voltar ao menu Turma...')
        return

    # Loop para obter o índice da turma a ser excluída
    while True:
        print(59*'-')
        print('Digite o índice < # > da turma que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        # Obtém o índice ou 'Cancelar'
        indice_turma_input = input('Índice: ').strip().capitalize()

        # Permite cancelar
        if indice_turma_input == 'Cancelar':
            break # Sai do loop de exclusão

        try:
            # Tenta converter o índice para inteiro
            indice_turma = int(indice_turma_input)

            # Verifica se o índice é válido
            if 0 <= indice_turma < len(turmas):
                # Remove a turma da lista e guarda os dados da excluída
                turma_excluida = turmas.pop(indice_turma)
                # Salva a lista atualizada
                salvar_dados(turmas, CAMINHO_ARQUIVO_TURMA)
                # Exibe mensagem de sucesso
                print(f'\nTurma: {turma_excluida['codigo_de_turma']} | Foi excluída')
                input('Pressione Enter para continuar...')
                return # Retorna ao menu anterior
            else:
                # Levanta um erro se o índice estiver fora do intervalo
                raise IndexError

        # Captura erros de valor ou índice inválido
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)

# Função para atualizar os dados de uma turma existente (código, disciplina, professor)
def atualizar_cadastro_turma():
    # Carrega dados necessários
    turmas = carregar_dados(CAMINHO_ARQUIVO_TURMA)
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)

    # Exibe a lista de turmas para seleção
    listar_turmas()

    # Se não houver turmas, informa e retorna
    if not turmas:
        input('\nPressione Enter para voltar ao menu Turma...')
        return

    # Loop para obter o índice da turma a ser atualizada
    while True:
        print(60*'-')
        print('Digite o índice < # > da turma que deseja atualizar'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(60*'-')
        # Obtém o índice ou 'Cancelar'
        indice_turma_input = input('Índice: ').strip().capitalize()

        # Permite cancelar
        if indice_turma_input == 'Cancelar':
            break # Sai do loop de atualização

        try:
            # Tenta converter e validar o índice
            indice_turma = int(indice_turma_input)
            if 0 <= indice_turma < len(turmas):
                # Seleciona a turma
                turma_selecionada = turmas[indice_turma]

                # Exibe os dados atuais da turma
                limpar_terminal()
                print('--- Turma Selecionada ---')
                print(f'Índice: {indice_turma}')
                print(f'Código de Turma: {turma_selecionada['codigo_de_turma']}')
                print(f'Disciplina: {turma_selecionada['disciplina']}')
                print(f'Professor: {turma_selecionada['professor']}')
                print('--------------------------')

                # Flag para indicar se houve alteração
                alteracao_feita = False
                # Loop para escolher o que alterar
                while True:
                    print()
                    print(79 * '-')
                    print('Digite o número da ação desejada no campo abaixo'.center(79) + '|')
                    print('(1) Alterar Código - (2) Alterar Disciplina - (3) Alterar Professor'.center(79) + '|')
                    print(79 * '-')
                    # Obtém a ação
                    acao_usuario_atualizar = input('Ação: ').strip().upper()

                    # Opção 1: Alterar Código da Turma
                    if acao_usuario_atualizar == '1':
                        while True: # Loop interno para validar novo código
                            limpar_terminal()
                            print(55*'-')
                            print('Digite o código atualizado para a turma'.center(55) + '|')
                            print('(Padrão alfanumérico)'.center(55) + '|')
                            print('(Digite "Cancelar" para voltar)'.center(55) + '|')
                            print(55*'-')
                            novo_cod_turma = input('Código da turma atualizado: ').upper().strip()

                            # Permite cancelar a alteração do código
                            if novo_cod_turma == 'CANCELAR':
                                return # Volta ao menu turma (cancela toda a atualização)

                            # Valida se não está vazio
                            if novo_cod_turma == '':
                                input('--- Código Inválido (Não pode ser vazio) ---\n'
                                        'Pressione Enter para tentar novamente...'
                                        )
                                limpar_linha(3)
                                continue # Tenta novamente

                            # Valida se o código já existe em outra turma
                            if any(t['codigo_de_turma'] == novo_cod_turma for i, t in enumerate(turmas) if i != indice_turma):
                                print(f'\n--- Erro: Código de Turma < {novo_cod_turma} > já cadastrado! ---')
                                input('Pressione Enter para tentar novamente...')
                                limpar_linha(3)
                                continue # Tenta novamente
                            else: # Código válido e único
                                turma_selecionada['codigo_de_turma'] = novo_cod_turma
                                alteracao_feita = True
                                break # Sai do loop interno
                        break # Sai do loop de escolha de campo

                    # Opção 2: Alterar Disciplina
                    if acao_usuario_atualizar == '2':
                        # Verifica se existem disciplinas cadastradas
                        if not disciplinas:
                            limpar_terminal()
                            input('< Não há disciplinas cadastradas no momento >\n'
                                  'Pressione Enter para voltar...')
                            break # Sai do loop de escolha de campo

                        while True: # Loop interno para selecionar nova disciplina
                            limpar_terminal()
                            listar_disciplinas() # Mostra disciplinas disponíveis
                            print(70*'-')
                            print('Digite o índice < # > da NOVA disciplina para esta turma'.center(70) + '|')
                            print('Digite "Cancelar" no campo abaixo para cancelar a operação'.center(70) + '|')
                            print(70*'-')
                            indice_disciplina_input = input('Índice da Disciplina: ').strip().capitalize()

                            # Permite cancelar a alteração da disciplina
                            if indice_disciplina_input == 'Cancelar':
                                return # Volta ao menu turma

                            try:
                                # Converte e valida o índice
                                indice_disciplina = int(indice_disciplina_input)
                                if 0 <= indice_disciplina < len(disciplinas):
                                    nova_disciplina = disciplinas[indice_disciplina]['disciplina']
                                    turma_selecionada['disciplina'] = nova_disciplina
                                    alteracao_feita = True
                                    break # Sai do loop interno (disciplina selecionada)
                                else:
                                    raise ValueError # Índice inválido
                            except (ValueError, IndexError): # Captura erros
                                print('\n--- Índice inválido ---')
                                print('O índice deve ser um número correspondente à coluna # da lista.')
                                input('Pressione Enter para tentar novamente...')
                                limpar_linha(5)
                                continue # Tenta novamente
                        break # Sai do loop de escolha de campo

                    # Opção 3: Alterar Professor
                    if acao_usuario_atualizar == '3':
                        # Verifica se existem professores cadastrados
                        if not professores:
                            limpar_terminal()
                            input('< Não há professores cadastrados no momento >\n'
                                  'Pressione Enter para voltar...')
                            break # Sai do loop de escolha de campo

                        while True: # Loop interno para selecionar novo professor
                            limpar_terminal()
                            listar_professores() # Mostra professores disponíveis
                            print(70*'-')
                            print('Digite o índice < # > do NOVO professor para esta turma'.center(70) + '|')
                            print('Digite "Cancelar" no campo abaixo para cancelar a operação'.center(70) + '|')
                            print(70*'-')
                            indice_professor_input = input('Índice do Professor: ').strip().capitalize()

                            # Permite cancelar a alteração do professor
                            if indice_professor_input == 'Cancelar':
                                return # Volta ao menu turma

                            try:
                                # Converte e valida o índice
                                indice_professor = int(indice_professor_input)
                                if 0 <= indice_professor < len(professores):
                                    novo_professor = professores[indice_professor]['nome']
                                    turma_selecionada['professor'] = novo_professor
                                    alteracao_feita = True
                                    break # Sai do loop interno (professor selecionado)
                                else:
                                    raise ValueError # Índice inválido
                            except (ValueError, IndexError): # Captura erros
                                print('\n--- Índice inválido ---')
                                print('O índice deve ser um número correspondente à coluna # da lista.')
                                input('Pressione Enter para tentar novamente...')
                                limpar_linha(5)
                                continue # Tenta novamente
                        break # Sai do loop de escolha de campo

                    # Se a ação digitada não for 1, 2 ou 3
                    else:
                        print('--- Ação Inválida ---\n'
                            'Deve ser digitado 1, 2, 3')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(4)
                        # Reexibe os dados da turma selecionada antes de pedir a ação novamente
                        limpar_terminal()
                        print('--- Turma Selecionada ---')
                        print(f'Índice: {indice_turma}')
                        print(f'Código de Turma: {turma_selecionada['codigo_de_turma']}')
                        print(f'Disciplina: {turma_selecionada['disciplina']}')
                        print(f'Professor: {turma_selecionada['professor']}')
                        print('--------------------------')

                # Se alguma alteração foi realizada com sucesso
                if alteracao_feita:
                    salvar_dados(turmas, CAMINHO_ARQUIVO_TURMA) # Salva as alterações
                    limpar_terminal()
                    print('\n--- Alterações salvas com sucesso! ---')
                    input('Pressione Enter para voltar ao menu Turma...')
                    return # Retorna ao menu Turma
                else: # Se nenhuma alteração foi feita (cancelou todas as etapas)
                    limpar_terminal()
                    listar_turmas() # Apenas relista as turmas

            else:
                # Levanta erro se o índice inicial da turma for inválido
                raise IndexError

        # Captura erros de valor ou índice no input inicial do índice da turma
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(5)
            # Limpa e relista as turmas antes de pedir o índice novamente
            limpar_terminal()
            listar_turmas()

# Função para incluir uma nova matrícula (associando estudante a uma turma)
def incluir_matricula():
    # Carrega dados necessários
    matriculas = carregar_dados(CAMINHO_ARQUIVO_MATRICULA)
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    turmas = carregar_dados(CAMINHO_ARQUIVO_TURMA)

    limpar_terminal()
    print('--- Nova Matrícula ---')

    # Verifica se existem estudantes cadastrados
    if not estudantes:
        print('\n< Não há estudantes cadastrados para realizar matrícula >')
        input('Pressione Enter para voltar ao menu Matrícula...')
        return

    # Verifica se existem turmas cadastradas
    if not turmas:
        print('\n< Não há turmas cadastradas para realizar matrícula >')
        input('Pressione Enter para voltar ao menu Matrícula...')
        return

    # Loop para selecionar a turma
    while True:
        listar_turmas() # Mostra turmas disponíveis
        if not turmas: # Checagem dupla (caso turmas sejam excluídas enquanto a função roda)
            input('\nPressione Enter para voltar ao menu Matrícula...')
            return

        print(70*'-')
        print('Digite o índice < # > da turma para a matrícula'.ljust(70) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(70) + '|')
        print(70*'-')
        # Obtém o índice ou 'Cancelar'
        indice_turma_input = input('Índice da Turma: ').strip().capitalize()

        # Permite cancelar
        if indice_turma_input == 'Cancelar':
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Matrícula...')
            return

        try:
            # Converte e valida o índice
            indice_turma = int(indice_turma_input)
            if 0 <= indice_turma < len(turmas):
                # Seleciona a turma e obtém seu código
                turma_selecionada = turmas[indice_turma]
                codigo_turma_selecionada = turma_selecionada['codigo_de_turma']
                break # Turma selecionada com sucesso
            else:
                raise IndexError # Índice inválido
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_terminal() # Limpa para mostrar a lista de turmas novamente
            continue # Tenta selecionar a turma novamente

    # Loop para selecionar o estudante
    while True:
        listar_estudantes() # Mostra estudantes disponíveis
        if not estudantes: # Checagem dupla
             input('\nPressione Enter para voltar ao menu Matrícula...')
             return

        print(70*'-')
        print('Digite o índice < # > do estudante para a matrícula'.ljust(70) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(70) + '|')
        print(70*'-')
        # Obtém o índice ou 'Cancelar'
        indice_estudante_input = input('Índice do Estudante: ').strip().capitalize()

        # Permite cancelar
        if indice_estudante_input == 'Cancelar':
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Matrícula...')
            return

        try:
            # Converte e valida o índice
            indice_estudante = int(indice_estudante_input)
            if 0 <= indice_estudante < len(estudantes):
                # Seleciona o estudante e obtém seu RA
                estudante_selecionado = estudantes[indice_estudante]
                ra_estudante_selecionado = estudante_selecionado['ra']

                # Verifica se já existe matrícula desse estudante nessa turma
                matricula_existente = False
                for mat in matriculas:
                    if mat['ra_estudante'] == ra_estudante_selecionado and mat['codigo_turma'] == codigo_turma_selecionada:
                        matricula_existente = True
                        break # Encontrou matrícula existente

                # Se a matrícula já existe, informa o erro
                if matricula_existente:
                    limpar_terminal()
                    print('\n--- Erro: Matrícula Existente ---')
                    print(f'O estudante {estudante_selecionado['nome']} (RA: {ra_estudante_selecionado})')
                    print(f'já está matriculado na turma {codigo_turma_selecionada}.')
                    input('Pressione Enter para tentar novamente...')
                    limpar_terminal() # Limpa para mostrar a lista de estudantes novamente
                    # Não usa 'continue' aqui, o loop while True já faz tentar de novo
                else:
                    break # Estudante selecionado e matrícula não existe, sai do loop
            else:
                raise IndexError # Índice inválido
        except (ValueError, IndexError): # Captura erros
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_terminal() # Limpa para mostrar a lista de estudantes novamente
            continue # Tenta selecionar o estudante novamente

    # Gera um código único para a matrícula (simples, baseado no tamanho atual da lista)
    proximo_id = len(matriculas) + 1
    codigo_matricula_gerado = f"MAT-{proximo_id:03}" # Formata com zeros à esquerda

    # Loop para obter e validar a data da matrícula
    while True:
        data_matricula_input = input('Insira a data da matrícula (dd/mm/aaaa): ').strip()
        # Permite cancelar
        if data_matricula_input.lower() == 'cancelar':
             print('Operação cancelada.')
             input('Pressione Enter para voltar ao menu Matrícula...')
             return
        try:
            # Extrai e valida dia, mês, ano, formato e separadores
            dia = int(data_matricula_input[:2])
            mes = int(data_matricula_input[3:5])
            ano = int(data_matricula_input[6:10])
            if len(data_matricula_input) == 10 and data_matricula_input[2] == '/' and data_matricula_input[5] == '/' \
               and 0 < dia <= 31 and 0 < mes <= 12 and ano >= 2025:
                data_matricula_valida = data_matricula_input # Guarda a data como string válida
                break # Data válida
            else:
                raise ValueError # Formato ou valores inválidos
        except (ValueError, IndexError): # Captura erros
            input('\n--- Data Inválida ---\n'
                  'Formato: dd/mm/aaaa (ex: 24/10/2025).\n'
                  'Verifique os separadores "/" e os valores.\n'
                  'Pressione Enter para tentar novamente...'
                  )
            limpar_linha(6)
            continue # Tenta obter a data novamente

    # Cria o dicionário da nova matrícula
    nova_matricula = {
        'codigo_matricula': codigo_matricula_gerado,
        'ra_estudante': ra_estudante_selecionado,
        'codigo_turma': codigo_turma_selecionada,
        'data_matricula': data_matricula_valida
    }

    # Adiciona a nova matrícula à lista
    matriculas.append(nova_matricula)
    # Salva a lista atualizada
    salvar_dados(matriculas, CAMINHO_ARQUIVO_MATRICULA)

    # Exibe mensagem de sucesso
    limpar_terminal()
    print('--- Matrícula Realizada com Sucesso! ---')
    print(f'Código da Matrícula: {codigo_matricula_gerado}')
    print(f'Estudante (RA): {ra_estudante_selecionado}')
    print(f'Turma (Código): {codigo_turma_selecionada}')
    print(f'Data: {data_matricula_valida}')
    print('----------------------------------------')

    # Pergunta se deseja realizar outra matrícula
    while True:
            continuar = input('Deseja realizar outra matrícula? (S/N): ').strip().upper()
            if continuar in ['S', 'N']:
                break
            else:
                print('--- Opção inválida ---\n'
                'Digite (S) para Sim ou (N) para Não.'
                )
                input('Pressione Enter para continuar...')
                limpar_linha(4)

    # Se não quiser continuar, retorna ao menu Matrícula
    if continuar == 'N':
        return

# Função para listar todas as matrículas realizadas
def listar_matricula():
    # Carrega a lista de matrículas
    matriculas = carregar_dados(CAMINHO_ARQUIVO_MATRICULA)
    limpar_terminal()
    print('--- Lista de Matrículas Realizadas ---')

    # Verifica se a lista está vazia
    if not matriculas:
        print('\n< Nenhuma matrícula realizada no momento >')
    else:
        # Imprime o cabeçalho da tabela
        print('-' * 84)
        print(f'{'#':<3} | {'Código Matrícula':<18} | {'RA Estudante':<15} | {'Código Turma':<20} | {'Data Matrícula':<15} |')
        print('-' * 84)

        # Itera sobre a lista e imprime cada matrícula formatada
        for indice, matricula in enumerate(matriculas):
            codigo_mat_str = str(matricula['codigo_matricula'])
            ra_est_str = str(matricula['ra_estudante'])
            cod_turma_str = str(matricula['codigo_turma'])
            data_mat_str = str(matricula['data_matricula'])
            print(f"{indice:<3} | {codigo_mat_str:<18} | {ra_est_str:<15} | {cod_turma_str:<20} | {data_mat_str:<15} |")

        print('-' * 84)

# Função para excluir uma matrícula da lista
def excluir_matricula():
    # Carrega a lista de matrículas
    matriculas = carregar_dados(CAMINHO_ARQUIVO_MATRICULA)
    # Exibe a lista para o usuário escolher qual excluir
    listar_matricula()

    # Se não houver matrículas, informa e retorna
    if not matriculas:
        input('\nPressione Enter para voltar ao menu Matrícula...')
        return

    # Loop para obter o índice da matrícula a ser excluída
    while True:
        print(60*'-')
        print('Digite o índice < # > da matrícula que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(60*'-')
        # Obtém o índice ou 'Cancelar'
        indice_matricula_input = input('Índice: ').strip().capitalize()

        # Permite cancelar
        if indice_matricula_input == 'Cancelar':
            break # Sai do loop de exclusão

        try:
            # Tenta converter o índice para inteiro
            indice_matricula = int(indice_matricula_input)

            # Verifica se o índice é válido
            if 0 <= indice_matricula < len(matriculas):
                # Remove a matrícula da lista e guarda os dados da excluída
                matricula_excluida = matriculas.pop(indice_matricula)
                # Salva a lista atualizada
                salvar_dados(matriculas, CAMINHO_ARQUIVO_MATRICULA)
                # Exibe mensagem de sucesso
                print(f'\nMatrícula: {matricula_excluida['codigo_matricula']} | Foi excluída')
                input('Pressione Enter para continuar...')
                return # Retorna ao menu anterior
            else:
                # Levanta um erro se o índice estiver fora do intervalo
                raise IndexError

        # Captura erros de valor ou índice inválido
        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)

# Função para atualizar a data de uma matrícula existente
def atualizar_cadastro_matricula():
    # Carrega a lista de matrículas
    matriculas = carregar_dados(CAMINHO_ARQUIVO_MATRICULA)
    # Exibe a lista para seleção
    listar_matricula()

    # Se não houver matrículas, informa e retorna
    if not matriculas:
        input('\nPressione Enter para voltar ao menu Matrícula...')
        return

    # Loop para obter o índice da matrícula a ser atualizada
    while True:
        print(66*'-')
        print('Digite o índice < # > da matrícula que deseja atualizar a data'.ljust(66) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(66) + '|')
        print(66*'-')
        # Obtém o índice ou 'Cancelar'
        indice_matricula_input = input('Índice: ').strip().capitalize()

        # Permite cancelar
        if indice_matricula_input == 'Cancelar':
            break # Sai do loop de atualização

        try:
            # Converte e valida o índice
            indice_matricula = int(indice_matricula_input)
            if 0 <= indice_matricula < len(matriculas):
                # Seleciona a matrícula
                matricula_selecionada = matriculas[indice_matricula]
                limpar_terminal()
                # Exibe os dados atuais da matrícula
                print('--- Matrícula Selecionada ---')
                print(f'Código Matrícula: {matricula_selecionada['codigo_matricula']}')
                print(f'RA Estudante: {matricula_selecionada['ra_estudante']}')
                print(f'Código Turma: {matricula_selecionada['codigo_turma']}')
                print(f'Data Matrícula Atual: {matricula_selecionada['data_matricula']}')
                print('------------------------------------------------')
                print('< Apenas a data da matrícula pode ser alterada >') # Informa a limitação

                # Flag para indicar se a alteração foi feita
                alteracao_feita = False
                # Loop para obter a nova data (só há uma opção de alteração)
                while True:
                    data_matricula_input = input('Insira a data da matrícula atualizada (dd/mm/aaaa ou "Cancelar"): ').strip()
                    # Permite cancelar a alteração da data
                    if data_matricula_input.lower() == 'cancelar':
                        break # Sai do loop de obter data

                    try:
                        # Valida a nova data (formato, valores, ano)
                        dia = int(data_matricula_input[:2])
                        mes = int(data_matricula_input[3:5])
                        ano = int(data_matricula_input[6:10])
                        if len(data_matricula_input) == 10 and data_matricula_input[2] == '/' and data_matricula_input[5] == '/' \
                           and 0 < dia <= 31 and 0 < mes <= 12 and ano >= 2025:
                            # Atualiza a data na matrícula selecionada
                            matricula_selecionada['data_matricula'] = data_matricula_input
                            alteracao_feita = True
                            break # Sai do loop de obter data (data válida)
                        else:
                            raise ValueError # Formato ou valores inválidos
                    except (ValueError, IndexError): # Captura erros
                        input('\n--- Data Inválida ---\n'
                              'Formato: dd/mm/aaaa (ex: 24/10/2025).\n'
                              'Verifique os separadores "/" e as datas.\n'
                              'Pressione Enter para tentar novamente...'
                              )
                        limpar_linha(6)
                        continue # Tenta obter a data novamente

                # Se a data foi alterada com sucesso
                if alteracao_feita:
                    salvar_dados(matriculas, CAMINHO_ARQUIVO_MATRICULA) # Salva as alterações
                    limpar_terminal()
                    print('\n--- Data da Matrícula alterada com sucesso! ---')
                    input('Pressione Enter para continuar...')
                    # Chama a função novamente para permitir outra atualização ou voltar
                    return atualizar_cadastro_matricula()
                else: # Se cancelou a alteração da data
                    limpar_terminal()
                    listar_matricula() # Apenas relista as matrículas
            else:
                # Levanta erro se o índice inicial for inválido
                raise IndexError
        except (ValueError, IndexError): # Captura erros no índice inicial
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)

# --- Loop Principal do Programa ---
while True:
    # Exibe o menu principal
    MenuPrincipal()
    # Obtém a escolha do usuário para o menu principal
    escolha_menu_principal = input('Insira o dígito correspondente à opção desejada: ').strip()

    # Valida se a escolha está nas opções definidas
    if escolha_menu_principal not in opcoes_menu_principal:
        print('--- Opção inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Estudante')
        input('Pressione Enter para continuar...')
        continue # Volta ao início do loop principal

    # Loop do Menu Secundário
    while True:
        # Obtém o texto da opção principal escolhida (ex: 'Estudante')
        opcao_texto = opcoes_menu_principal[escolha_menu_principal]

        # --- Tratamento da Opção 'Sair' ---
        if opcao_texto == 'Sair':
            escolha_sair = ''
            # Loop de confirmação da saída
            while escolha_sair not in ['S', 'V']:
                MenuSecundario(opcao_texto) # Mostra o menu de sair (S/V)
                escolha_sair = input('Confirmar saída (S) ou voltar (V): ').strip().upper()
                if escolha_sair not in ['S', 'V']:
                    print('--- Opção inválida --- Digite S ou V.')
                    input('Pressione Enter para continuar...')
                    limpar_linha(3)

            # Se confirmou a saída (S)
            if escolha_sair == 'S':
                limpar_terminal()
                print('Desligando o sistema...')
                sys.exit() # Encerra o programa
            else: # Se escolheu voltar (V)
                break # Sai do loop do menu secundário, voltando ao menu principal

        # --- Tratamento da Opção 'Estudante' ---
        elif opcao_texto == 'Estudante':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            # Chama a função correspondente à escolha
            if escolha_menu_secundario == '1':   # Incluir
                incluir_estudantes()
            elif escolha_menu_secundario == '2': # Listar
                listar_estudantes()
                input('\nPressione Enter para voltar ao menu Estudante...') # Pausa após listar
            elif escolha_menu_secundario == '3': # Excluir
                excluir_estudante()
            elif escolha_menu_secundario == '4': # Alterar
                atualizar_cadastro_estudante()
            elif escolha_menu_secundario == '5': # Voltar
                break # Sai do loop do menu secundário, voltando ao principal
            else: # Opção inválida no menu secundário
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # --- Tratamento da Opção 'Disciplina' ---
        elif opcao_texto == 'Disciplina':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1':   # Incluir
                incluir_disciplina()
            elif escolha_menu_secundario == '2': # Listar
                listar_disciplinas()
                input('\nPressione Enter para voltar ao menu Disciplina...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_disciplina()
            elif escolha_menu_secundario == '4': # Alterar
                atualizar_cadastro_disciplina()
            elif escolha_menu_secundario == '5': # Voltar
                break
            else: # Opção inválida
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # --- Tratamento da Opção 'Professor' ---
        elif opcao_texto == 'Professor':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1':   # Incluir
                incluir_professor()
            elif escolha_menu_secundario == '2': # Listar
                listar_professores()
                input('\nPressione Enter para voltar ao menu Professor...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_professores()
            elif escolha_menu_secundario == '4': # Alterar
                atualizar_cadastro_professor()
            elif escolha_menu_secundario == '5': # Voltar
                break
            else: # Opção inválida
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # --- Tratamento da Opção 'Turma' ---
        elif opcao_texto == 'Turma':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1':   # Incluir
                incluir_turma()
            elif escolha_menu_secundario == '2': # Listar
                listar_turmas()
                input('\nPressione Enter para voltar ao menu Turma...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_turma()
            elif escolha_menu_secundario == '4': # Alterar
                atualizar_cadastro_turma()
            elif escolha_menu_secundario == '5': # Voltar
                break
            else: # Opção inválida
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # --- Tratamento da Opção 'Matrícula' ---
        elif opcao_texto == 'Matrícula':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1':   # Incluir
                incluir_matricula()
            elif escolha_menu_secundario == '2': # Listar
                listar_matricula()
                input('\nPressione Enter para voltar ao menu Matrícula...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_matricula()
            elif escolha_menu_secundario == '4': # Alterar (apenas data)
                atualizar_cadastro_matricula()
            elif escolha_menu_secundario == '5': # Voltar
                break
            else: # Opção inválida
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')
