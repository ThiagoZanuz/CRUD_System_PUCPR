import os
import sys
import json

CAMINHO_ARQUIVO_ESTUDANTE = 'arquivo_estudante.json'
CAMINHO_ARQUIVO_DISCIPLINA = 'arquivo_disciplina.json'
CAMINHO_ARQUIVO_PROFESSOR = 'arquivo_professor.json'
CAMINHO_ARQUIVO_TURMA = 'arquivo_turma.json'
CAMINHO_ARQUIVO_MATRICULA = 'arquivo_matricula.json'

# Função para limpar o terminal (Windows, MacOS e Linux)
def limpar_terminal():
    os.system('cls') if sys.platform == 'win32' else os.system('clear')

# Função para limpar quantas linhas acima desejar
def limpar_linha(qtd):
    for _ in range(qtd):
        print("\033[F\033[K", end="")

# --- Dicionários de Menu ---
opcoes_menu_principal = {
    '1': 'Estudante',
    '2': 'Disciplina',
    '3': 'Professor',
    '4': 'Turma',
    '5': 'Matrícula',
    '6': 'Sair',
}

opcoes_menu_secundario = {
    '1': 'Incluir',
    '2': 'Listar',
    '3': 'Excluir',
    '4': 'Alterar',
    '5': 'Voltar',
}

# --- Funções de Menu ---
# Exibe o Menu Principal na tela
def MenuPrincipal():
    limpar_terminal()
    print('MENU PRINCIPAL')
    print(14*'-')
    for digito, menu in opcoes_menu_principal.items():
        print(f'{digito}. {menu}'.ljust(14) + '|')  # Formata a exibição
        print(14*'-')

# Exibe o Menu Secundário com base na opção escolhida no menu principal
def MenuSecundario(menu):
    limpar_terminal()
    print(f'MENU - {menu}')  # Indica a aba atual

    if menu == 'Sair':  # Caso o usuário tenha escolhido a opção de sair
        print(43*'-')
        print('(S) > Confirmar desligamento do sistema.'.ljust(43) + '|')
        print(43*'-')
        print('(V) > Voltar ao Menu Principal.'.ljust(43) + '|')
        print(43*'-')
    else:
        print(14*'-')
        for digito, funcao in opcoes_menu_secundario.items():
            print(f'{digito}. {funcao}'.ljust(14) + '|')
            print(14*'-')

# --- Funções JSON ---
def carregar_dados(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'r') as a:
            return json.load(a)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(dados, caminho_do_arquivo):
    with open(caminho_do_arquivo, 'w', encoding='utf8') as a:
        json.dump(dados, a, indent=2)

# --- Funções de Validação dos Estudantes ---

# Valida e obtém o nome do estudante
def validar_e_obter_nome():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o nome do estudante'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        nome = input('Nome do estudante: ').strip().title()

        if nome == 'Cancelar':
            return None

        nome_sem_espacos = nome.replace(' ', '')
        if nome_sem_espacos.isalpha() and nome: # Verifica se não está vazio e contém apenas letras/espaços
            return nome # Retorna o Nome
        else:
            print('\n--- Nome inválido ---')
            print('(O nome deve conter apenas letras e espaços.)')
            print('(Não pode ser vazio.)')
            input('Pressione Enter para tentar novamente...')

# Valida o Registro Acadêmico (RA)
def validar_e_obter_ra():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o Registro Acadêmico (RA)'.center(45) + '|')
        print('(Apenas números)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        ra_input = input('Registro Acadêmico (RA): ').strip().capitalize()

        if ra_input == 'Cancelar':
            return None

        try:
            ra = int(ra_input) # Tenta converter para inteiro
            return ra # Retorna o RA
        except ValueError:
            print('\n--- RA Inválido ---')
            print('(Insira apenas números para o Registro Acadêmico.)')
            input('Pressione Enter para tentar novamente...')

# Valida o CPF
def validar_e_obter_cpf():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o CPF (11 dígitos, sem pontuação)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        cpf = input('CPF (somente números): ').strip().capitalize()

        if cpf == 'Cancelar':
            return None

        # Verifica se tem 11 dígitos e se todos são numéricos
        if len(cpf) == 11 and cpf.isnumeric():
            # Verifica se todos os dígitos são iguais
            if cpf == cpf[0] * 11:
                 print('\n--- CPF Inválido ---')
                 print('(CPF com todos os dígitos iguais não é válido.)')
                 input('Pressione Enter para tentar novamente...')
            else:
                 return cpf # Retorna o CPF
        else:
            print('\n--- CPF Inválido ---')
            print('(O CPF deve conter exatamente 11 dígitos numéricos.)')
            print('(Não inclua pontos ou traços.)')
            input('Pressione Enter para tentar novamente...')


# --- Funções de Cadastramento de Estudantes ---

# Adiciona estudantes, validando Nome, RA e CPF
def incluir_estudantes():
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    while True:
        limpar_terminal()
        print('--- Cadastro de Novo Estudante ---')

        nome = validar_e_obter_nome()
        if nome is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        ra = validar_e_obter_ra()
        if ra is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        cpf = validar_e_obter_cpf()
        if cpf is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
        if any(p['cpf'] == cpf for p in professores):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado para um professor! ---')
             input('Pressione Enter para tentar novamente...')
             continue

        if any(e['cpf'] == cpf for e in estudantes):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado para um estudante! ---')
             input('Pressione Enter para tentar novamente...')
             continue

        if any(e['ra'] == ra for e in estudantes):
            print(f'\n--- Erro: RA < {ra} > já cadastrado! ---')
            input('Pressione Enter para tentar novamente...')
            continue

        estudantes.append({'nome': nome, 'ra': ra, 'cpf': cpf})
        salvar_dados(estudantes, CAMINHO_ARQUIVO_ESTUDANTE)

        limpar_terminal()
        print('--- Estudante Cadastrado com Sucesso! ---')
        print(f'Nome: {nome}')
        print(f'RA: {ra}')
        print(f'CPF: {cpf}')
        print('-----------------------------------------')

        while True:
            continuar = input('Deseja adicionar outro estudante? (S/N): ').strip().upper()
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

    return

# Mostra a lista de estudantes cadastrados
def listar_estudantes():
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    limpar_terminal()
    print('--- Lista de Estudantes Cadastrados ---')

    if not estudantes:
        print('\n< Nenhum estudante cadastrado no momento >')
        # O input foi movido para o loop principal para consistência
    else:
        # Cabeçalho
        print('-' * 65)
        print(f'{'#':<3} | {'Nome':<25} | {'RA':<12} | {'CPF':<15} |')
        print('-' * 65)

        # Dados dos estudantes
        for indice, estudante in enumerate(estudantes):
            nome_str = str(estudante['nome'])
            ra_str = str(estudante['ra'])
            cpf_str = str(estudante['cpf'])
            print(f"{indice:<3} | {nome_str:<25} | {ra_str:<12} | {cpf_str:<15} |")

        print('-' * 65)

# Mostra a lista de estudantes cadastrados dando a opção de excluir
def excluir_estudante():
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    listar_estudantes()

    if not estudantes:
        # Se a lista está vazia após listar, apenas informa e retorna
        # A função listar_estudantes já imprime a mensagem de vazio
        input('\nPressione Enter para voltar ao menu Estudante...')
        return

    while True:
        print(59*'-')
        print('Digite o índice < # > do estudante que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        indice_estudante_input = input('Índice: ').strip().capitalize()

        if indice_estudante_input == 'Cancelar':
            break

        try:
            indice_estudante = int(indice_estudante_input)
            # Validação completa do índice
            if 0 <= indice_estudante < len(estudantes):
                estudante_excluido = estudantes.pop(indice_estudante)
                salvar_dados(estudantes, CAMINHO_ARQUIVO_ESTUDANTE)
                print(f'\nEstudante: {estudante_excluido['nome']} | Foi excluído')
                input('Pressione Enter para continuar...')
                # Removida recursão, retorna ao menu
                return
            else:
                raise IndexError # Força ir para o except de índice inválido

        except (ValueError, IndexError): # Captura erro de conversão ou índice fora do range
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(5) # Ajuste a quantidade se necessário

# Atualiza cadastro de estudante
def atualizar_cadastro_estudante():
    estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
    listar_estudantes()

    if not estudantes:
        input('\nPressione Enter para voltar ao menu Estudante...')
        return

    while True:
        print(59*'-')
        print('Digite o índice < # > do estudante que deseja atualizar'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        indice_estudante_input = input('Índice: ').strip().capitalize()

        if indice_estudante_input == 'Cancelar':
            break

        try:
            indice_estudante = int(indice_estudante_input)
            if 0 <= indice_estudante < len(estudantes):
                estudante_selecionado = estudantes[indice_estudante]

                print('\n--- Estudante Selecionado ---')
                print(f'Nome: {estudante_selecionado['nome']}')
                print(f'RA: {estudante_selecionado['ra']}')
                print(f'CPF: {estudante_selecionado['cpf']}')
                print('-----------------------------')

                alteracao_feita = False
                while True:
                    print()
                    print(79 * '-')
                    print('Digite o número da ação desejada no campo abaixo'.center(80) + '|')
                    print('(1) Alterar Nome - (2) Alterar RA - (3) Alterar CPF - (4) Alterar tudo - (C) Cancelar Ação'.center(80) + '|')
                    print(79 * '-')
                    acao_usuario_atualizar = input('Ação: ').strip().upper()

                    if acao_usuario_atualizar == 'C':
                        print("Alteração cancelada.")
                        input("Pressione Enter para voltar...")
                        break

                    if acao_usuario_atualizar == '1':
                        novo_nome = validar_e_obter_nome()
                        if novo_nome is not None:
                            estudante_selecionado['nome'] = novo_nome
                            input('Nome alterado com sucesso!\nPressione Enter para continuar...')
                            alteracao_feita = True
                        break

                    if acao_usuario_atualizar == '2':
                        novo_ra = validar_e_obter_ra()
                        if novo_ra is not None:
                            if any(e['ra'] == novo_ra for i, e in enumerate(estudantes) if i != indice_estudante):
                                print(f'\n--- Erro: RA < {novo_ra} > já cadastrado para outro estudante! ---')
                                input('Pressione Enter para tentar novamente...')
                            else:
                                estudante_selecionado['ra'] = novo_ra
                                input('Registro Acadêmico alterado com sucesso!\nPressione Enter para continuar...')
                                alteracao_feita = True
                                break
                        break

                    if acao_usuario_atualizar == '3':
                        novo_cpf = validar_e_obter_cpf()
                        if novo_cpf is not None:
                            professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
                            if any(p['cpf'] == novo_cpf for p in professores):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para um professor! ---')
                                input('Pressione Enter para tentar novamente...')
                                break
                            if any(e['cpf'] == novo_cpf for i, e in enumerate(estudantes) if i != indice_estudante):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para outro estudante! ---')
                                input('Pressione Enter para tentar novamente...')
                            else:
                                estudante_selecionado['cpf'] = novo_cpf
                                input('CPF alterado com sucesso!\nPressione Enter para continuar...')
                                alteracao_feita = True
                                break
                        break

                    if acao_usuario_atualizar == '4':
                        print("\n--- Alterando Nome ---")
                        novo_nome = validar_e_obter_nome()
                        if novo_nome is None: break

                        print("\n--- Alterando RA ---")
                        novo_ra = validar_e_obter_ra()
                        if novo_ra is None: break

                        if any(e['ra'] == novo_ra for i, e in enumerate(estudantes) if i != indice_estudante):
                            print(f'\n--- Erro: RA < {novo_ra} > já pertence a outro estudante! ---')
                            input('Pressione Enter para voltar...')
                            break

                        print("\n--- Alterando CPF ---")
                        novo_cpf = validar_e_obter_cpf()
                        if novo_cpf is None: break

                        professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
                        if any(p['cpf'] == novo_cpf for p in professores):
                            print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para um professor! ---')
                            input('Pressione Enter para voltar...')
                            break

                        if any(e['cpf'] == novo_cpf for i, e in enumerate(estudantes) if i != indice_estudante):
                            print(f'\n--- Erro: CPF < {novo_cpf} > já pertence a outro estudante! ---')
                            input('Pressione Enter para voltar...')
                            break

                        estudante_selecionado['nome'] = novo_nome
                        estudante_selecionado['ra'] = novo_ra
                        estudante_selecionado['cpf'] = novo_cpf
                        input('Nome, Registro Acadêmico e CPF foram alterados com sucesso!\nPressione Enter para continuar...')
                        alteracao_feita = True
                        break

                    else:
                        print('--- Ação Inválida ---\n'
                            'Deve ser digitado apenas o número referente à ação\n'
                            'Ex: > 1 < para atualizar o nome')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(10)

                if alteracao_feita:
                    salvar_dados(estudantes, CAMINHO_ARQUIVO_ESTUDANTE)
                    print("\nAlterações salvas.")
                    input("Pressione Enter para voltar ao menu Estudante...")
                    return
                else:
                    limpar_terminal()
                    listar_estudantes()

            else:
                raise IndexError

        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(6)

# ----------------------------------------------------------------------------------------------------------
# --- Funções Disciplinas ---

def incluir_disciplina():
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    limpar_terminal()
    print(40*'-')
    print('Cadastramento de Disciplinas'.center(40) + '|')
    print('(Digite "Cancelar" para voltar)'.center(40) + '|')
    print(40*'-')
    print()

    while True:
        nome = input('Nome da disciplina: ').capitalize().strip()
        if nome == 'Cancelar':
            input('Operação cancelada.\n'
                  'Pressione Enter para voltar ao menu Disciplina...'
                  )
            return
        if nome.isnumeric() or nome == '':
            input('--- Nome Inválido ---\n'
                'O nome da disciplina deve conter letras\n'
                'Pressione Enter para tentar novamente...'
                )
            limpar_linha(4)
            continue
        # Validação de duplicidade (opcional, mas boa prática)
        if any(d['disciplina'].lower() == nome.lower() for d in disciplinas):
             input(f'--- Erro: Disciplina "{nome}" já cadastrada! ---\n'
                   'Pressione Enter para tentar novamente...')
             limpar_linha(3)
             continue
        break

    while True:
        abertura = input('Insira a data de abertura (dd/mm/aaaa): ').strip()
        if abertura.lower() == 'cancelar':
            input('Operação cancelada.\n'
                  'Pressione Enter para voltar ao menu Disciplina...'
                  )
            return
        try:
            dia1 = int(abertura[:2])
            mes1 = int(abertura[3:5])
            ano1 = int(abertura[6:10])
            if len(abertura) == 10 and abertura[2] == '/' and abertura[5] == '/' \
               and 0 < dia1 <= 31 and 0 < mes1 <= 12 and ano1 >= 2024: # Ano mínimo pode ser ajustado
                data_abertura_valida = (ano1, mes1, dia1)
                break
            else:
                raise ValueError("Formato ou valor inválido.")
        except (ValueError, IndexError):
            input('\n--- Data Inválida ---\n'
                'Formato: dd/mm/aaaa (ex: 24/10/2024).\n'
                'Verifique os separadores "/" e os valores.\n'
                'Pressione Enter para tentar novamente...'
                )
            limpar_linha(6)
            continue

    while True:
        fechamento = input('Insira a data de fechamento (dd/mm/aaaa): ').strip()
        if fechamento.lower() == 'cancelar':
            input('Operação cancelada.\n'
                  'Pressione Enter para voltar ao menu Disciplina...'
                  )
            return
        try:
            dia2 = int(fechamento[:2])
            mes2 = int(fechamento[3:5])
            ano2 = int(fechamento[6:10])
            if len(fechamento) == 10 and fechamento[2] == '/' and fechamento[5] == '/' \
               and 0 < dia2 <= 31 and 0 < mes2 <= 12 and ano2 >= ano1:
                data_fechamento_valida = (ano2, mes2, dia2)
                if data_fechamento_valida >= data_abertura_valida:
                    break
                else:
                    raise ValueError("Data de fechamento não pode ser anterior à de abertura.")
            else:
                raise ValueError("Formato ou valor inválido.")
        except (ValueError, IndexError) as e:
            input(f'\n--- Data Inválida ---\n{e}\n'
                  'Formato: dd/mm/aaaa. Não pode ser anterior à abertura.\n'
                  'Pressione Enter para tentar novamente...'
                  )
            limpar_linha(6)
            continue

    while True:
        carga_horaria_input = input('Carga horária (Apenas números positivos): ').strip()
        if carga_horaria_input.lower() == 'cancelar':
            input('Operação cancelada.\n'
                  'Pressione Enter para voltar ao menu Disciplina...'
                  )
            return
        try:
            carga_horaria = int(carga_horaria_input)
            if carga_horaria > 0:
                break
            else:
                raise ValueError("Carga horária deve ser positiva.")
        except ValueError as e:
            input(f'--- Carga horária Inválida ---\n{e}\n'
                    'Insira apenas números inteiros positivos.\n'
                    'Pressione Enter para tentar novamente...'
                    )
            limpar_linha(5)
            continue

    disciplinas.append({'disciplina': nome, 'abertura': abertura, 'fechamento': fechamento, 'carga_horaria': carga_horaria})
    salvar_dados(disciplinas, CAMINHO_ARQUIVO_DISCIPLINA)
    input(f'\nDisciplina: ({nome}) cadastrada com sucesso!\n'
          'Pressione Enter para continuar...'
          )

def listar_disciplinas():
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    limpar_terminal()
    print('--- Lista de Disciplinas Cadastradas ---')

    if not disciplinas:
        print('\n< Nenhuma disciplina cadastrada no momento >')
        # Input movido para o loop principal
    else:
        # Cabeçalho
        print('-' * 84)
        print(f'{'#':<3} | {'Disciplina':<35} | {'Abertura':<10} | {'Fechamento':<10} | {'Carga Horária':<12} |')
        print('-' * 84)

        # Dados das disciplinas
        for indice, disciplina in enumerate(disciplinas):
            disciplina_nome = str(disciplina.get('disciplina', 'N/A'))
            disciplina_abertura = str(disciplina.get('abertura', 'N/A'))
            disciplina_fechamento = str(disciplina.get('fechamento', 'N/A'))
            disciplina_carga_horaria = str(disciplina.get('carga_horaria', 'N/A'))
            print(f'{indice:<3} | {disciplina_nome:<35} | {disciplina_abertura:<10} | {disciplina_fechamento:<10} | {disciplina_carga_horaria:<13} |')

        print('-' * 84)

def excluir_disciplina():
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    listar_disciplinas()

    if not disciplinas:
        input('\nPressione Enter para voltar ao menu Disciplina...')
        return

    while True:
        print(59*'-')
        print('Digite o índice < # > da disciplina que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        indice_disciplina_input = input('Índice: ').strip().capitalize()

        if indice_disciplina_input == 'Cancelar':
            break

        try:
            indice_disciplina = int(indice_disciplina_input)
            if 0 <= indice_disciplina < len(disciplinas):
                disciplina_excluida = disciplinas.pop(indice_disciplina)
                salvar_dados(disciplinas, CAMINHO_ARQUIVO_DISCIPLINA)
                print(f'\nDisciplina: {disciplina_excluida.get("disciplina", "N/A")} | Foi excluída')
                input('Pressione Enter para continuar...')
                # Removida recursão, retorna ao menu
                return
            else:
                raise IndexError

        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(5)

def atualizar_cadastro_disciplina():
    disciplinas = carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA)
    listar_disciplinas()

    if not disciplinas:
        input('\nPressione Enter para voltar ao menu Disciplina...')
        return

    while True:
        print(60*'-')
        print('Digite o índice < # > da disciplina que deseja atualizar'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(60*'-')
        indice_disciplina_input = input('Índice: ').strip().capitalize()

        if indice_disciplina_input == 'Cancelar':
            break

        try:
            indice_disciplina = int(indice_disciplina_input)
            if 0 <= indice_disciplina < len(disciplinas):
                disciplina_selecionada = disciplinas[indice_disciplina]

                print('\n--- Disciplina Selecionada ---')
                print(f'Disciplina: {disciplina_selecionada.get("disciplina", "N/A")}')
                print(f'Abertura: {disciplina_selecionada.get("abertura", "N/A")}')
                print(f'Fechamento: {disciplina_selecionada.get("fechamento", "N/A")}')
                print(f'Carga Horária: {disciplina_selecionada.get("carga_horaria", "N/A")}')
                print('-----------------------------')

                alteracao_feita = False
                while True:
                    print()
                    print(100 * '-')
                    print('Digite o número da ação desejada'.center(100) + '|')
                    print('(1) Alterar Nome - (2) Alterar Abertura - (3) Alterar Fechamento - (4) Alterar Carga Horária - (C) Cancelar'.center(100) + '|')
                    print(100 * '-')
                    acao_usuario_atualizar = input('Ação: ').strip().upper()

                    if acao_usuario_atualizar == 'C':
                        print("Alteração cancelada.")
                        input("Pressione Enter para voltar...")
                        break

                    elif acao_usuario_atualizar == '1':
                        while True:
                            novo_nome = input('Nome atualizado da disciplina ("Cancelar" para voltar): ').capitalize().strip()
                            if novo_nome == 'Cancelar': break
                            if novo_nome.isnumeric() or novo_nome == '':
                                input('--- Nome Inválido ---\n'
                                    'O nome da disciplina deve conter letras\n'
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(4)
                            elif any(d['disciplina'].lower() == novo_nome.lower() for i, d in enumerate(disciplinas) if i != indice_disciplina):
                                input(f'--- Erro: Disciplina "{novo_nome}" já existe. ---\n'
                                      'Pressione Enter para tentar novamente...')
                                limpar_linha(3)
                            else:
                                disciplina_selecionada['disciplina'] = novo_nome
                                print('Nome atualizado com sucesso!!!')
                                input('Pressione Enter para continuar...')
                                alteracao_feita = True
                                break
                        break

                    elif acao_usuario_atualizar == '2':
                        try:
                            fechamento_atual = disciplina_selecionada['fechamento']
                            dia_f = int(fechamento_atual[:2]); mes_f = int(fechamento_atual[3:5]); ano_f = int(fechamento_atual[6:10])
                            data_fechamento_atual = (ano_f, mes_f, dia_f)
                        except: data_fechamento_atual = None

                        while True:
                            abertura = input('Insira a data atualizada de abertura (dd/mm/aaaa ou "Cancelar"): ').strip()
                            if abertura.lower() == 'cancelar': break
                            try:
                                dia1 = int(abertura[:2]); mes1 = int(abertura[3:5]); ano1 = int(abertura[6:10])
                                if len(abertura) == 10 and abertura[2] == '/' and abertura[5] == '/' \
                                   and 0 < dia1 <= 31 and 0 < mes1 <= 12 and ano1 >= 2024:
                                    data_abertura_nova = (ano1, mes1, dia1)
                                    if data_fechamento_atual is None or data_abertura_nova <= data_fechamento_atual:
                                        disciplina_selecionada['abertura'] = abertura
                                        print('Data de abertura atualizada com sucesso!!!')
                                        input('Pressione Enter para continuar...')
                                        alteracao_feita = True
                                        break
                                    else: raise ValueError("Não pode ser posterior ao fechamento atual.")
                                else: raise ValueError("Formato/valor inválido.")
                            except (ValueError, IndexError) as e:
                                input(f'\n--- Data Inválida ---\n{e}\n'
                                    'Formato: dd/mm/aaaa. Verifique valores e separadores.\n'
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(6)
                                continue
                        break

                    elif acao_usuario_atualizar == '3':
                        try:
                            abertura_atual = disciplina_selecionada['abertura']
                            dia_a = int(abertura_atual[:2]); mes_a = int(abertura_atual[3:5]); ano_a = int(abertura_atual[6:10])
                            data_abertura_atual = (ano_a, mes_a, dia_a)
                        except: data_abertura_atual = None

                        while True:
                            fechamento = input('Insira a data atualizada de fechamento (dd/mm/aaaa ou "Cancelar"): ').strip()
                            if fechamento.lower() == 'cancelar': break
                            try:
                                dia2 = int(fechamento[:2]); mes2 = int(fechamento[3:5]); ano2 = int(fechamento[6:10])
                                if len(fechamento) == 10 and fechamento[2] == '/' and fechamento[5] == '/' \
                                   and 0 < dia2 <= 31 and 0 < mes2 <= 12 and ano2 >= 2024:
                                    data_fechamento_nova = (ano2, mes2, dia2)
                                    if data_abertura_atual is None or data_fechamento_nova >= data_abertura_atual:
                                        disciplina_selecionada['fechamento'] = fechamento
                                        print('Data de fechamento atualizada com sucesso!!!')
                                        input('Pressione Enter para continuar...')
                                        alteracao_feita = True
                                        break
                                    else: raise ValueError("Não pode ser anterior à abertura atual.")
                                else: raise ValueError("Formato/valor inválido.")
                            except (ValueError, IndexError) as e:
                                input(f'\n--- Data Inválida ---\n{e}\n'
                                    'Formato: dd/mm/aaaa. Verifique valores e separadores.\n'
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(6)
                                continue
                        break

                    elif acao_usuario_atualizar == '4':
                         while True:
                            carga_horaria_input = input('Carga horária atualizada (Apenas números positivos ou "Cancelar"): ').strip()
                            if carga_horaria_input.lower() == 'cancelar': break
                            try:
                                carga_horaria = int(carga_horaria_input)
                                if carga_horaria > 0:
                                    disciplina_selecionada['carga_horaria'] = carga_horaria
                                    print('Carga horária atualizada com sucesso!!!')
                                    input('Pressione Enter para continuar...')
                                    alteracao_feita = True
                                    break
                                else:
                                    raise ValueError("Carga horária deve ser positiva.")
                            except ValueError as e:
                                input(f'--- Carga Horária Inválida ---\n{e}\n'
                                        'Insira apenas números inteiros positivos.\n'
                                        'Pressione Enter para tentar novamente...'
                                        )
                                limpar_linha(5)
                                continue
                         break

                    else:
                        print('\n--- Ação Inválida ---')
                        print('Digite 1, 2, 3, 4 ou C.')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(5)

                if alteracao_feita:
                    salvar_dados(disciplinas, CAMINHO_ARQUIVO_DISCIPLINA)
                    print("\nAlterações salvas.")
                    input("Pressione Enter para voltar ao menu Disciplina...")
                    return
                else:
                    limpar_terminal()
                    listar_disciplinas()

            else:
                raise IndexError

        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(6)

# ----------------------------------------------------------------------------------------------------------
# --- Funções Professor ---

def validar_e_obter_nome_professor():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o nome do professor'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        nome = input('Nome do professor: ').strip().title()

        if nome == 'Cancelar':
            return None

        nome_sem_espacos = nome.replace(' ', '')
        if nome_sem_espacos.isalpha() and nome: # Verifica se não está vazio e contém apenas letras/espaços
            return nome # Retorna o Nome
        else:
            print('\n--- Nome inválido ---')
            print('(O nome deve conter apenas letras e espaços.)')
            print('(Não pode ser vazio.)')
            input('Pressione Enter para tentar novamente...')

# Valida a Matrícula Funcional (MF)
def validar_e_obter_mf_professor():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite a Matrícula Funcional (MF)'.center(45) + '|')
        print('(Apenas números)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        mf_input = input('Matrícula Funcional (MF): ').strip().capitalize()

        if mf_input == 'Cancelar':
            return None

        try:
            mf = int(mf_input) # Tenta converter para inteiro
            return mf # Retorna a MF
        except ValueError:
            print('\n--- MF Inválida ---')
            print('(Insira apenas números para a Matrícula Funcional.)')
            input('Pressione Enter para tentar novamente...')

# Valida o CPF
def validar_e_obter_cpf_professor():
    while True:
        limpar_terminal()
        print(45*'-')
        print('Digite o CPF (11 dígitos, sem pontuação)'.center(45) + '|')
        print('(Digite "Cancelar" para voltar)'.center(45) + '|')
        print(45*'-')
        cpf = input('CPF (somente números): ').strip().capitalize()

        if cpf == 'Cancelar':
            return None

        # Verifica se tem 11 dígitos e se todos são numéricos
        if len(cpf) == 11 and cpf.isnumeric():
            # Verifica se todos os dígitos são iguais
            if cpf == cpf[0] * 11:
                 print('\n--- CPF Inválido ---')
                 print('(CPF com todos os dígitos iguais não é válido.)')
                 input('Pressione Enter para tentar novamente...')
            else:
                 return cpf # Retorna o CPF
        else:
            print('\n--- CPF Inválido ---')
            print('(O CPF deve conter exatamente 11 dígitos numéricos.)')
            print('(Não inclua pontos ou traços.)')
            input('Pressione Enter para tentar novamente...')


# --- Funções de Cadastramento de Professores ---

# Adiciona professores, validando Nome, MF e CPF
def incluir_professor():
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    while True:
        limpar_terminal()
        print('--- Cadastro de Novo Professor ---')

        nome = validar_e_obter_nome_professor()
        if nome is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Professor...')
            return

        mf = validar_e_obter_mf_professor()
        if mf is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Professor...')
            return

        cpf = validar_e_obter_cpf_professor()
        if cpf is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Professor...')
            return

        estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
        if any(e['cpf'] == cpf for e in estudantes):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado para um estudante! ---')
             input('Pressione Enter para tentar novamente...')
             continue

        if any(p['cpf'] == cpf for p in professores):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado para um professor! ---')
             input('Pressione Enter para tentar novamente...')
             continue

        if any(p['mf'] == mf for p in professores):
            print(f'\n--- Erro: MF < {mf} > já cadastrado! ---')
            input('Pressione Enter para tentar novamente...')
            continue

        professores.append({'nome': nome, 'mf': mf, 'cpf': cpf})
        salvar_dados(professores, CAMINHO_ARQUIVO_PROFESSOR)

        limpar_terminal()
        print('--- Professor Cadastrado com Sucesso! ---')
        print(f'Nome: {nome}')
        print(f'MF: {mf}')
        print(f'CPF: {cpf}')
        print('-----------------------------------------')

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

    return

# Mostra a lista de professores cadastrados
def listar_professores():
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    limpar_terminal()
    print('--- Lista de Professores Cadastrados ---')

    if not professores:
        print('\n< Nenhum professor cadastrado no momento >')
        # Input movido para o loop principal
    else:
        # Cabeçalho
        print('-' * 65)
        print(f'{'#':<3} | {'Nome':<25} | {'MF':<12} | {'CPF':<15} |')
        print('-' * 65)

        # Dados dos professores
        for indice, professor in enumerate(professores):
            nome_str = str(professor.get('nome', 'N/A'))
            mf_str = str(professor.get('mf', 'N/A'))
            cpf_str = str(professor.get('cpf', 'N/A'))
            print(f"{indice:<3} | {nome_str:<25} | {mf_str:<12} | {cpf_str:<15} |")

        print('-' * 65)

# Mostra a lista de professores cadastrados dando a opção de excluir
def excluir_professores():
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    listar_professores()

    if not professores:
        input('\nPressione Enter para voltar ao menu Professor...')
        return

    while True:
        print(59*'-')
        print('Digite o índice < # > do professor que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        indice_professor_input = input('Índice: ').strip().capitalize()

        if indice_professor_input == 'Cancelar':
            break

        try:
            indice_professor = int(indice_professor_input)
            if 0 <= indice_professor < len(professores):
                professor_excluido = professores.pop(indice_professor)
                salvar_dados(professores, CAMINHO_ARQUIVO_PROFESSOR)
                print(f'\nProfessor: {professor_excluido.get("nome", "N/A")} | Foi excluído')
                input('Pressione Enter para continuar...')
                # Removida recursão, retorna ao menu
                return
            else:
                raise IndexError

        except (ValueError, IndexError):
            print('\n--- Índice inválido ---\n'
                'O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(5)

# Atualiza cadastro de professor
def atualizar_cadastro_professor():
    professores = carregar_dados(CAMINHO_ARQUIVO_PROFESSOR)
    listar_professores()

    if not professores:
        input('\nPressione Enter para voltar ao menu Professor...')
        return

    while True:
        print(59*'-')
        print('Digite o índice < # > do professor que deseja atualizar'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        indice_professor_input = input('Índice: ').strip().capitalize()

        if indice_professor_input == 'Cancelar':
            break

        try:
            indice_professor = int(indice_professor_input)
            if 0 <= indice_professor < len(professores):
                professor_selecionado = professores[indice_professor]

                print('\n--- Professor Selecionado ---')
                print(f'Nome: {professor_selecionado['nome']}')
                print(f'MF: {professor_selecionado['mf']}')
                print(f'CPF: {professor_selecionado['cpf']}')
                print('-----------------------------')

                alteracao_feita = False
                while True:
                    print()
                    print(79 * '-')
                    print('Digite o número da ação desejada no campo abaixo'.center(80) + '|')
                    print('(1) Alterar Nome - (2) Alterar MF - (3) Alterar CPF - (4) Alterar tudo - (C) Cancelar Ação'.center(80) + '|')
                    print(79 * '-')
                    acao_usuario_atualizar = input('Ação: ').strip().upper()

                    if acao_usuario_atualizar == 'C':
                        print("Alteração cancelada.")
                        input("Pressione Enter para voltar...")
                        break

                    if acao_usuario_atualizar == '1':
                        novo_nome = validar_e_obter_nome_professor()
                        if novo_nome is not None:
                            professor_selecionado['nome'] = novo_nome
                            input('Nome alterado com sucesso!\nPressione Enter para continuar...')
                            alteracao_feita = True
                        break

                    if acao_usuario_atualizar == '2':
                        novo_mf = validar_e_obter_mf_professor()
                        if novo_mf is not None:
                            if any(p['mf'] == novo_mf for i, p in enumerate(professores) if i != indice_professor):
                                print(f'\n--- Erro: MF < {novo_mf} > já cadastrado para outro professor! ---')
                                input('Pressione Enter para tentar novamente...')
                            else:
                                professor_selecionado['mf'] = novo_mf
                                input('Matrícula Funcional alterada com sucesso!\nPressione Enter para continuar...')
                                alteracao_feita = True
                                break
                        break

                    if acao_usuario_atualizar == '3':
                        novo_cpf = validar_e_obter_cpf_professor()
                        if novo_cpf is not None:
                            estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
                            if any(e['cpf'] == novo_cpf for e in estudantes):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para um estudante! ---')
                                input('Pressione Enter para tentar novamente...')
                                break
                            if any(p['cpf'] == novo_cpf for i, p in enumerate(professores) if i != indice_professor):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para outro professor! ---')
                                input('Pressione Enter para tentar novamente...')
                            else:
                                professor_selecionado['cpf'] = novo_cpf
                                input('CPF alterado com sucesso!\nPressione Enter para continuar...')
                                alteracao_feita = True
                                break
                        break

                    if acao_usuario_atualizar == '4':
                        print("\n--- Alterando Nome ---")
                        novo_nome = validar_e_obter_nome_professor()
                        if novo_nome is None: break

                        print("\n--- Alterando MF ---")
                        novo_mf = validar_e_obter_mf_professor()
                        if novo_mf is None: break

                        if any(p['mf'] == novo_mf for i, p in enumerate(professores) if i != indice_professor):
                            print(f'\n--- Erro: MF < {novo_mf} > já pertence a outro professor! ---')
                            input('Pressione Enter para voltar...')
                            break

                        print("\n--- Alterando CPF ---")
                        novo_cpf = validar_e_obter_cpf_professor()
                        if novo_cpf is None: break

                        estudantes = carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE)
                        if any(e['cpf'] == novo_cpf for e in estudantes):
                            print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado para um estudante! ---')
                            input('Pressione Enter para voltar...')
                            break

                        if any(p['cpf'] == novo_cpf for i, p in enumerate(professores) if i != indice_professor):
                            print(f'\n--- Erro: CPF < {novo_cpf} > já pertence a outro professor! ---')
                            input('Pressione Enter para voltar...')
                            break

                        professor_selecionado['nome'] = novo_nome
                        professor_selecionado['mf'] = novo_mf
                        professor_selecionado['cpf'] = novo_cpf
                        input('Nome, Matrícula Funcional e CPF foram alterados com sucesso!\nPressione Enter para continuar...')
                        alteracao_feita = True
                        break

                    else:
                        print('--- Ação Inválida ---\n'
                            'Deve ser digitado apenas o número referente à ação\n'
                            'Ex: > 1 < para atualizar o nome')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(10)

                if alteracao_feita:
                    salvar_dados(professores, CAMINHO_ARQUIVO_PROFESSOR)
                    print("\nAlterações salvas.")
                    input("Pressione Enter para voltar ao menu Professor...")
                    return
                else:
                    limpar_terminal()
                    listar_professores()

            else:
                raise IndexError

        except (ValueError, IndexError):
            print('\n--- Índice inválido ---')
            print('O índice deve ser um número correspondente à coluna # da lista.')
            input('Pressione Enter para tentar novamente...')
            limpar_linha(6)

# --- Loop Principal ---
while True:
    MenuPrincipal()
    escolha_menu_principal = input('Insira o dígito correspondente à opção desejada: ').strip()

    if escolha_menu_principal not in opcoes_menu_principal:
        print('--- Opção inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Estudante')
        input('Pressione Enter para continuar...')
        continue

    # --- Loop do Menu Secundário ---
    while True:
        opcao_texto = opcoes_menu_principal[escolha_menu_principal]

        # --- Menu Sair ---
        if opcao_texto == 'Sair':
            escolha_sair = ''
            while escolha_sair not in ['S', 'V']:
                MenuSecundario(opcao_texto) # Mostra S ou V
                escolha_sair = input('Confirmar saída (S) ou voltar (V): ').strip().upper()
                if escolha_sair not in ['S', 'V']:
                    print('--- Opção inválida --- Digite S ou V.')
                    input('Pressione Enter para continuar...')
                    limpar_linha(3)

            if escolha_sair == 'S':
                limpar_terminal()
                print('Desligando o sistema...')
                sys.exit() # Encerra o programa
            else: # escolha_sair == 'V'
                break # Sai do menu secundário e volta para o principal

        # ---- Menu Estudante ----
        elif opcao_texto == 'Estudante':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1': # Incluir
                incluir_estudantes()
            elif escolha_menu_secundario == '2': # Listar
                listar_estudantes()
                # Adicionado input aqui SE a lista não estiver vazia
                if carregar_dados(CAMINHO_ARQUIVO_ESTUDANTE):
                    input('\nPressione Enter para voltar ao menu Estudante...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_estudante() # Note que esta função ainda tem recursão no seu código original
            elif escolha_menu_secundario == '4': # Atualizar
                atualizar_cadastro_estudante()
            elif escolha_menu_secundario == '5': # Voltar
                break # Sai do menu secundário e volta para o principal
            else:
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # ---- Menu Disciplina ----
        elif opcao_texto == 'Disciplina':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1': # Incluir
                incluir_disciplina()
            elif escolha_menu_secundario == '2': # Listar
                listar_disciplinas()
                # Adicionado input aqui SE a lista não estiver vazia
                if carregar_dados(CAMINHO_ARQUIVO_DISCIPLINA):
                    input('\nPressione Enter para voltar ao menu Disciplina...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_disciplina() # Note que esta função ainda tem recursão no seu código original
            elif escolha_menu_secundario == '4': # Atualizar
                atualizar_cadastro_disciplina() # Note que esta função ainda tem recursão no seu código original
            elif escolha_menu_secundario == '5': # Voltar
                break # Sai do menu secundário e volta para o principal
            else:
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # ---- Menu Professor ----
        elif opcao_texto == 'Professor':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1': # Incluir
                incluir_professor()
            elif escolha_menu_secundario == '2': # Listar
                listar_professores()
                # Adicionado input aqui SE a lista não estiver vazia
                if carregar_dados(CAMINHO_ARQUIVO_PROFESSOR):
                    input('\nPressione Enter para voltar ao menu Professor...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_professores() # Note que esta função ainda tem recursão no seu código original
            elif escolha_menu_secundario == '4': # Atualizar
                atualizar_cadastro_professor()
            elif escolha_menu_secundario == '5': # Voltar
                break # Sai do menu secundário e volta para o principal
            else:
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # ---- Menu Turma ----
        elif opcao_texto == 'Turma':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1': # Incluir
                ...
            elif escolha_menu_secundario == '2': # Listar
                ...
            elif escolha_menu_secundario == '3': # Excluir
                ...
            elif escolha_menu_secundario == '4': # Atualizar
                ...
            elif escolha_menu_secundario == '5': # Voltar
                break # Sai do menu secundário e volta para o principal
            else:
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # ---- Menu Matrícula ----
        elif opcao_texto == 'Matrícula':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1': # Incluir
                ...
            elif escolha_menu_secundario == '2': # Listar
                ...
            elif escolha_menu_secundario == '3': # Excluir
                ...
            elif escolha_menu_secundario == '4': # Atualizar
                ...
            elif escolha_menu_secundario == '5': # Voltar
                break # Sai do menu secundário e volta para o principal
            else:
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')
