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

# --- Funções JSON - Estudantes
def carregar_dados_estudantes():
    try:
        with open(CAMINHO_ARQUIVO_ESTUDANTE, 'r') as a:
            return json.load(a)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_estudantes(estudantes):
    with open(CAMINHO_ARQUIVO_ESTUDANTE, 'w', encoding='utf8') as a:
        json.dump(estudantes, a, indent=2)

# --- Funções JSON - Disciplinas
def carregar_dados_disciplinas():
    try:
        with open(CAMINHO_ARQUIVO_DISCIPLINA, 'r') as a:
            return json.load(a)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_disciplinas(estudantes):
    with open(CAMINHO_ARQUIVO_DISCIPLINA, 'w', encoding='utf8') as a:
        json.dump(estudantes, a, indent=2)

# --- Funções JSON - Professores
def carregar_dados_professores():
    try:
        with open(CAMINHO_ARQUIVO_PROFESSOR, 'r') as a:
            return json.load(a)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_professores(estudantes):
    with open(CAMINHO_ARQUIVO_PROFESSOR, 'w', encoding='utf8') as a:
        json.dump(estudantes, a, indent=2)

# --- Funções JSON - Turma
def carregar_dados_turma():
    try:
        with open(CAMINHO_ARQUIVO_TURMA, 'r') as a:
            return json.load(a)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_turma(estudantes):
    with open(CAMINHO_ARQUIVO_TURMA, 'w', encoding='utf8') as a:
        json.dump(estudantes, a, indent=2)

# --- Funções JSON - Matrícula
def carregar_dados_matricula():
    try:
        with open(CAMINHO_ARQUIVO_MATRICULA, 'r') as a:
            return json.load(a)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_matricula(estudantes):
    with open(CAMINHO_ARQUIVO_MATRICULA, 'w', encoding='utf8') as a:
        json.dump(estudantes, a, indent=2)

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

# Adiciona estudantes à lista, validando Nome, RA e CPF
def incluir_estudantes():
    estudantes = carregar_dados_estudantes()
    while True:
        limpar_terminal()
        print('--- Cadastro de Novo Estudante ---')

        # Obter Nome
        nome = validar_e_obter_nome()
        if nome is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        # Obter RA (Registro Acadêmico)
        ra = validar_e_obter_ra()
        if ra is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        # Obter CPF
        cpf = validar_e_obter_cpf()
        if cpf is None:
            print('Operação cancelada.')
            input('Pressione Enter para voltar ao menu Estudante...')
            return

        if any(e['ra'] == ra for e in estudantes):
            print(f'\n--- Erro: RA < {ra} > já cadastrado! ---')
            input('Pressione Enter para tentar novamente...')
            continue

        if any(e['cpf'] == cpf for e in estudantes):
             print(f'\n--- Erro: CPF < {cpf} > já cadastrado! ---')
             input('Pressione Enter para tentar novamente...')
             continue # Volta para o início de incluir_estudante

        # Criar dicionário do estudante e adicionar ao arquivo
        estudantes.append({'nome': nome, 'ra': ra, 'cpf': cpf})
        salvar_estudantes(estudantes)

        limpar_terminal()
        print('--- Estudante Cadastrado com Sucesso! ---')
        print(f'Nome: {nome}')
        print(f'RA: {ra}')
        print(f'CPF: {cpf}')
        print('-----------------------------------------')

        # Perguntar se deseja continuar a cadastrar estudantes
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
             break # Sai do loop incluir_estudante e volta ao menu secundário

    return # Volta ao Menu Secundário

# Mostra a lista de estudantes cadastrados
def listar_estudantes():
    estudantes = carregar_dados_estudantes()
    limpar_terminal()
    print('--- Lista de Estudantes Cadastrados ---')

    if not estudantes:
        print('\n< Nenhum estudante cadastrado no momento >')
        input('\nPressione Enter para voltar ao menu Estudante...')
    else:
        # Cabeçalho
        # Define larguras mínimas
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
    estudantes = carregar_dados_estudantes()
    listar_estudantes()
    while estudantes:
        print(59*'-')
        print('Digite o índice < # > do estudante que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        indice_estudante = input('Índice: ').strip().capitalize()

        if indice_estudante == 'Cancelar':
            break

        try: # Valida e Exclui o estudante da lista
            indice_estudante = int(indice_estudante)
            if indice_estudante >= 0: # Bloqueia a entrada de números < 0 para excluir estudantes
                estudante_excluido = estudantes[indice_estudante]
                estudantes.pop(indice_estudante)
                salvar_estudantes(estudantes)
                print(f'Estudante: {estudante_excluido['nome']} | Foi excluído')
                input('Pressione Enter para continuar...')
                return excluir_estudante()
            else:
                raise ValueError

        except Exception:
            print('--- Índice inválido ---\n'
                'O índice do aluno é o numero da coluna | # | do mesmo.\n'
                'Ex: > 0 <  para o estudante: | Thiago Zanuz | 1234567890 | 32112332112'
                )
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)

def atualizar_cadastro_estudante():
    estudantes = carregar_dados_estudantes()
    listar_estudantes()
    while estudantes:
        print(59*'-')
        print('Digite o índice < # > do estudante que deseja atualizar'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        indice_estudante = input('Índice: ').strip().capitalize()

        if indice_estudante == 'Cancelar':
            break

        try:
            indice_estudante = int(indice_estudante)
            if indice_estudante >= 0:  # Bloqueia números negativos
                estudante_selecionado = estudantes[indice_estudante]

                print('\n--- Estudante Selecionado ---')
                print(f'Nome: {estudante_selecionado['nome']}')
                print(f'RA: {estudante_selecionado['ra']}')
                print(f'CPF: {estudante_selecionado['cpf']}')
                print('-----------------------------')

                while True:
                    print()
                    print(79 * '-')
                    print('Digite o número da ação desejada no campo abaixo'.center(80) + '|')
                    print('(1) Alterar Nome - (2) Alterar RA - (3) Alterar CPF - (4) Alterar tudo'.center(80) + '|')
                    print(79 * '-')
                    acao_usuario_atualizar = input('Ação: ')

                    if acao_usuario_atualizar == '1':  # Alterar Nome
                        novo_nome = validar_e_obter_nome()
                        if novo_nome is not None:
                            estudante_selecionado['nome'] = novo_nome
                            input('Nome alterado com sucesso!\nPressione Enter para continuar...')
                        break

                    if acao_usuario_atualizar == '2':  # Alterar RA
                        novo_ra = validar_e_obter_ra()
                        if novo_ra is not None:
                            # --- Verificação de duplicidade para RA ---
                            if any(e['ra'] == novo_ra for e in estudantes):
                                print(f'\n--- Erro: RA < {novo_ra} > já cadastrado! ---')
                                input('Pressione Enter para tentar novamente...')
                                break
                            else:
                                estudante_selecionado['ra'] = novo_ra
                                input('Registro Acadêmico alterado com sucesso!\nPressione Enter para continuar...')
                        break

                    if acao_usuario_atualizar == '3':  # Alterar CPF
                        novo_cpf = validar_e_obter_cpf()
                        if novo_cpf is not None:
                            # --- Verificação de duplicidade para CPF ---
                            if any(e['cpf'] == novo_cpf for e in estudantes):
                                print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado! ---')
                                input('Pressione Enter para tentar novamente...')
                                break
                            else:
                                estudante_selecionado['cpf'] = novo_cpf
                                input('CPF alterado com sucesso!\nPressione Enter para continuar...')
                        break

                    if acao_usuario_atualizar == '4':  # Alterar Nome, RA e CPF ao mesmo tempo
                        novo_nome = validar_e_obter_nome()
                        if novo_nome is not None:
                            novo_ra = validar_e_obter_ra()
                            if novo_ra is not None:
                                # --- Verificação de duplicidade para RA ---
                                if any(e['ra'] == novo_ra for e in estudantes):
                                    print(f'\n--- Erro: RA < {novo_ra} > já cadastrado! ---')
                                    input('Pressione Enter para tentar novamente...')
                                    break
                                else:
                                    estudante_selecionado['ra'] = novo_ra
                                    input('Registro Acadêmico alterado com sucesso!\nPressione Enter para continuar...')

                                novo_cpf = validar_e_obter_cpf()
                                if novo_cpf is not None:
                                    # --- Verificação de duplicidade para CPF ---
                                    if any(e['cpf'] == novo_cpf for e in estudantes):
                                        print(f'\n--- Erro: CPF < {novo_cpf} > já cadastrado! ---')
                                        input('Pressione Enter para tentar novamente...')
                                        break
                                    else:
                                        estudante_selecionado['cpf'] = novo_cpf
                                        input('CPF alterado com sucesso!\nPressione Enter para continuar...')

                                    # Se tudo estiver certo, atualiza os dados do estudante
                                    estudante_selecionado['nome'] = novo_nome
                                    estudante_selecionado['ra'] = novo_ra
                                    estudante_selecionado['cpf'] = novo_cpf
                                    input('Nome, Registro Acadêmico e CPF foram alterados com sucesso!\nPressione Enter para continuar...')
                                    break
                                else:
                                    break
                            else:
                                break
                        else:
                            break

                    else:
                        print('--- Ação Inválida ---\n'
                            'Deve ser digitado apenas o número referente à ação\n'
                            'Ex: > 1 < para atualizar o nome')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(10)
                
                salvar_estudantes(estudantes)
                return atualizar_cadastro_estudante()
            else:
                raise ValueError
        except Exception:
            print('--- Índice inválido ---\n'
                'O índice do aluno é o numero da coluna | # | do mesmo.\n'
                'Ex: > 0 <  para o estudante: | Thiago Zanuz | 1234567890 | 32112332112'
                )
            input('Pressione Enter para tentar novamente...')
            return atualizar_cadastro_estudante()
# ----------------------------------------------------------------------------------------------------------
# --- Funções Disciplinas ---

def incluir_disciplina():
    disciplinas = carregar_dados_disciplinas()
    limpar_terminal()
    print(40*'-')
    print('Cadastramento de Disciplinas'.center(40) + '|')
    print('(Digite "Cancelar" para voltar)')
    print(40*'-')
    print()


    while True:
        nome = input('Nome da disciplina: ').capitalize().strip()
        if nome.isnumeric() or nome == '':
            input('--- Nome Inválido ---\n'
                'O nome da disciplina deve conter letras\n'
                'Pressione Enter para tentar novamente...'
                )
            limpar_linha(4)
            continue
        break

    while nome != 'Cancelar':
        abertura = input('Insira a data de abertura (dd/mm/aaaa): ').strip()
        try:
            dia1 = int(abertura[:2])
            mes1 = int(abertura[3:5])
            ano1 = int(abertura[6:10])
            if len(abertura) == 10:
                if 0 < dia1 <= 31:
                    if abertura[2] == '/':
                        if 0 < mes1 <= 12:
                            if abertura[5] == '/':
                                if 2025 <= ano1:
                                    break
                                else:
                                    raise Exception
                            else:
                                raise Exception
                        else:
                            raise Exception
                    else:
                        raise Exception
                else:
                    raise Exception
            else:
                raise Exception
        except Exception:
            input('\n--- Data Inválida ---\n'
                'A data deve ser inserida no seguinte formato:\n'
                '-> 2 Dígitos para dia\n'
                '-> 2 Dígitos para mês\n'
                '-> 4 Dígitos para ano\n'
                'Todos separados por uma barra "/"\n'
                'O formato final deverá se parecer com "24/10/2025"\n'
                'Pressione Enter para tentar novamente...'
                )
            limpar_linha(10)
            continue

    while nome != 'Cancelar':
        fechamento = input('Insira a data de fechamento (dd/mm/aaaa): ').strip()
        try:
            dia2 = int(fechamento[:2])
            mes2 = int(fechamento[3:5])
            ano2 = int(fechamento[6:10])
            if len(fechamento) == 10:
                if 0 < dia2 <= 31:
                    if fechamento[2] == '/':
                        if 0 < mes2 <= 12:
                            if fechamento[5] == '/':
                                if 2025 <= ano2:
                                    if (ano2, mes2, dia2) >= (ano1, mes1, dia1):
                                        break
                                    else:
                                        raise Exception
                                else:
                                    raise Exception
                            else:
                                raise Exception
                        else:
                            raise Exception
                    else:
                        raise Exception
                else:
                    raise Exception
            else:
                raise Exception
        except Exception:
            input('\n--- Data Inválida ---\n'
                '- Obs: A data não pode ser anterior a data de abertura -\n\n'
                'A data deve ser inserida no seguinte formato:\n'
                '-> 2 Dígitos para dia\n'
                '-> 2 Dígitos para mês\n'
                '-> 4 Dígitos para ano\n'
                'Todos separados por uma barra "/"\n'
                'O formato final deverá se parecer com "27/11/2025"\n'
                'Pressione Enter para tentar novamente...'
                )
            limpar_linha(12)
            continue

    while nome != 'Cancelar':
        try:
            carga_horaria = int(input('Carga horária (Apenas números): ').strip())
            if carga_horaria >= 0:
                break
            else:
                raise Exception

        except Exception:
            input('--- Carga horária Inválida ---\n'
                    'Insira apenas dígitos, como: 90\n'
                    'Pressione Enter para tentar novamente...'
                    )
            limpar_linha(4)
            continue

    disciplinas.append({'disciplina': nome, 'abertura': abertura, 'fechamento': fechamento, 'carga_horaria': carga_horaria})
    salvar_disciplinas(disciplinas)
    input(f'Disciplina: ({nome}) cadastrada com sucesso!\n'
          'Pressione Enter para continuar...'
          )

def listar_disciplinas():
    disciplinas = carregar_dados_disciplinas()
    limpar_terminal()
    print('--- Lista de Disciplinas Cadastradas ---')

    if not disciplinas:
        print('\n< Nenhuma disciplina cadastrada no momento >')
        input('\nPressione Enter para voltar ao menu Disciplina...')
    else:
        # Cabeçalho
        # Define larguras mínimas
        print('-' * 84)
        print(f'{'#':<3} | {'Disciplina':<35} | {'Abertura':<10} | {'Fechamento':<10} | {'Carga Horária':<12} |')
        print('-' * 84)

        # Dados dos estudantes
        for indice, disciplina in enumerate(disciplinas):
            disciplina_nome = disciplina['disciplina']
            disciplina_abertura = disciplina['abertura']
            disciplina_fechamento = disciplina['fechamento']
            disciplina_carga_horaria = str(disciplina['carga_horaria'])
            print(f'{indice:<3} | {disciplina_nome:<35} | {disciplina_abertura:<9} | {disciplina_fechamento:<10} | {disciplina_carga_horaria:<13} |')

        print('-' * 84)

def excluir_disciplina():
    disciplinas = carregar_dados_disciplinas()
    listar_disciplinas()
    while disciplinas:
        print(59*'-')
        print('Digite o índice < # > da disciplina que deseja excluir'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(59*'-')
        indice_disciplina = input('Índice: ').strip().capitalize()

        if indice_disciplina == 'Cancelar':
            break

        try: # Valida e Exclui a disciplina da lista
            indice_disciplina = int(indice_disciplina)
            if indice_disciplina >= 0: # Bloqueia a entrada de números < 0 para excluir disciplinas
                disciplina_excluida = disciplinas[indice_disciplina]
                disciplinas.pop(indice_disciplina)
                salvar_disciplinas(disciplinas)
                print(f'Disciplina: {disciplina_excluida['disciplina']} | Foi excluída')
                input('Pressione Enter para continuar...')
                return excluir_disciplina()
            else:
                raise ValueError

        except Exception:
            print('--- Índice inválido ---\n'
                'O índice da disciplina é o numero da coluna | # | da mesma.\n'
                'Ex: > 0 <  para a disciplina: | Matemática | 12/02/2025 | 15/04/2025 | 90 |'
                )
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)

def atualizar_cadastro_disciplina():
    disciplinas = carregar_dados_disciplinas()

    if not disciplinas:
        print('--- Nenhuma disciplina cadastrada ---')
        input('Pressione Enter para voltar ao menu...')
        return

    listar_disciplinas()
    while True:
        print(60*'-')
        print('Digite o índice < # > da disciplina que deseja atualizar'.ljust(60) + '|')
        print('Digite "Cancelar" no campo abaixo para cancelar a operação'.ljust(60) + '|')
        print(60*'-')
        indice_disciplina = input('Índice: ').strip().capitalize()

        if indice_disciplina == 'Cancelar':
            break

        try:
            indice_disciplina = int(indice_disciplina)
            if indice_disciplina >= 0 and indice_disciplina < len(disciplinas):  # Garante que o índice existe
                disciplina_selecionada = disciplinas[indice_disciplina]

                print('\n--- Disciplina Selecionada ---')
                print(f'Disciplina: {disciplina_selecionada["disciplina"]}')
                print(f'Abertura: {disciplina_selecionada["abertura"]}')
                print(f'Fechamento: {disciplina_selecionada["fechamento"]}')
                print(f'Carga Horária: {disciplina_selecionada["carga_horaria"]}')
                print()

                while True:
                    print(100 * '-')
                    print('Digite o número da ação desejada no campo abaixo'.center(100) + '|')
                    print('(1) Alterar Nome - (2) Alterar Abertura - (3) Alterar Fechamento - (4) Alterar Carga Horária'.center(100) + '|')
                    print(100 * '-')
                    acao_usuario_atualizar = input('Ação: ')

                    if acao_usuario_atualizar == '1':  # Alterar Nome
                        while True:
                            novo_nome = input('Nome atualizado da disciplina: ').capitalize().strip()
                            if novo_nome.isnumeric() or novo_nome == '':
                                input('--- Nome Inválido ---\n'
                                    'O nome da disciplina deve conter letras\n'
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(4)
                            else:
                                disciplina_selecionada['disciplina'] = novo_nome
                                input('Nome atualizado com sucesso!!!\n'
                                      'Pressione Enter para continuar...'
                                      )
                                break

                    elif acao_usuario_atualizar == '2':  # Alterar Abertura
                        while True:
                            dia2 = int(disciplina_selecionada['fechamento'][:2])
                            mes2 = int(disciplina_selecionada['fechamento'][3:5])
                            ano2 = int(disciplina_selecionada['fechamento'][6:10])

                            abertura = input('Insira a data atualizada de abertura (dd/mm/aaaa): ').strip()
                            try:
                                dia1 = int(abertura[:2])
                                mes1 = int(abertura[3:5])
                                ano1 = int(abertura[6:10])
                                if len(abertura) == 10:
                                    if 0 < dia1 <= 31:
                                        if abertura[2] == '/':
                                            if 0 < mes1 <= 12:
                                                if abertura[5] == '/':
                                                    if 2025 <= ano1:
                                                        if (ano2, mes2, dia2) >= (ano1, mes1, dia1):
                                                            disciplina_selecionada['abertura'] = abertura
                                                            input('Data de abertura atualizada com sucesso!!!\n'
                                                                  'Pressione Enter para continuar...'
                                                                  )
                                                            break
                                                        else:
                                                            raise Exception
                                                    else:
                                                        raise Exception
                                                else:
                                                    raise Exception
                                            else:
                                                raise Exception
                                        else:
                                            raise Exception
                                    else:
                                        raise Exception
                                else:
                                    raise Exception
                            except Exception:
                                input('\n--- Data Inválida ---\n'
                                    '- Obs: A data não pode ser sucessora a data de fechamento -\n\n'
                                    'A data deve ser inserida no seguinte formato:\n'
                                    '-> 2 Dígitos para dia\n'
                                    '-> 2 Dígitos para mês\n'
                                    '-> 4 Dígitos para ano\n'
                                    'Todos separados por uma barra "/"\n'
                                    'O formato final deverá se parecer com "24/10/2025"\n'
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(12)
                                continue

                    elif acao_usuario_atualizar == '3':  # Alterar Fechamento
                        while True:
                            dia1 = int(disciplina_selecionada['abertura'][:2])
                            mes1 = int(disciplina_selecionada['abertura'][3:5])
                            ano1 = int(disciplina_selecionada['abertura'][6:10])

                            fechamento = input('Insira a data atualizada de fechamento (dd/mm/aaaa): ').strip()
                            try:
                                dia2 = int(fechamento[:2])
                                mes2 = int(fechamento[3:5])
                                ano2 = int(fechamento[6:10])
                                if len(fechamento) == 10:
                                    if 0 < dia2 <= 31:
                                        if fechamento[2] == '/':
                                            if 0 < mes2 <= 12:
                                                if fechamento[5] == '/':
                                                    if 2025 <= ano2:
                                                        if (ano2, mes2, dia2) >= (ano1, mes1, dia1):
                                                            disciplina_selecionada['fechamento'] = fechamento
                                                            input('Data de fechamento atualizada com sucesso!!!\n'
                                                                  'Pressione Enter para continuar...'
                                                                  )
                                                            break
                                                        else:
                                                            raise Exception
                                                    else:
                                                        raise Exception
                                                else:
                                                    raise Exception
                                            else:
                                                raise Exception
                                        else:
                                            raise Exception
                                    else:
                                        raise Exception
                                else:
                                    raise Exception
                            except Exception:
                                input('\n--- Data Inválida ---\n'
                                    '- Obs: A data não pode ser anterior a data de abertura -\n\n'
                                    'A data deve ser inserida no seguinte formato:\n'
                                    '-> 2 Dígitos para dia\n'
                                    '-> 2 Dígitos para mês\n'
                                    '-> 4 Dígitos para ano\n'
                                    'Todos separados por uma barra "/"\n'
                                    'O formato final deverá se parecer com "27/11/2025"\n'
                                    'Pressione Enter para tentar novamente...'
                                    )
                                limpar_linha(12)
                                continue
                    elif acao_usuario_atualizar == '4':  # Alterar Carga Horária
                        while True:
                            try:
                                carga_horaria = int(input('Carga horária atualizada (Apenas números): ').strip())
                                if carga_horaria >= 0:
                                    disciplina_selecionada['carga_horaria'] = carga_horaria
                                    input('Carga horária atualizada com sucesso!!!\n'
                                        'Pressione Enter para continuar...'
                                        )
                                    break
                                else:
                                    raise Exception

                            except Exception:
                                input('--- Carga Horária Inválida ---\n'
                                        'Insira apenas dígitos, como: 90\n'
                                        'Pressione Enter para tentar novamente...'
                                        )
                                limpar_linha(4)
                                continue

                    else:
                        print('--- Ação Inválida ---\n'
                              'Deve ser digitado apenas o número referente à ação\n'
                              'Ex: > 1 < para atualizar o nome da disciplina')
                        input('Pressione Enter para tentar novamente...')
                        limpar_linha(9)
                    
                    break
                salvar_disciplinas(disciplinas)
                return atualizar_cadastro_disciplina()
            else:
                raise ValueError
        except Exception:
            print('--- Índice inválido ---\n'
                  'O índice da disciplina é o numero da coluna | # | da mesma.\n'
                  'Ex: > 0 <  para a disciplina: | Matemática | 12/04/2025 | 15/06/2025 | 56 |'
                  )
            input('Pressione Enter para tentar novamente...')
            limpar_linha(9)
            continue  # Volta para pedir o índice novamente

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
                if carregar_dados_estudantes():
                    input('\nPressione Enter para voltar ao menu Estudante...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_estudante()
            elif escolha_menu_secundario == '4': # Atualizar
                atualizar_cadastro_estudante()
            elif escolha_menu_secundario == '5': # Voltar
                break # Sai do menu secundário e volta para o principal
            else:
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # ---- Menu Estudante ----
        elif opcao_texto == 'Disciplina':
            MenuSecundario(opcao_texto)
            escolha_menu_secundario = input('Insira o dígito correspondente à função desejada: ').strip()

            if escolha_menu_secundario == '1': # Incluir
                incluir_disciplina()
            elif escolha_menu_secundario == '2': # Listar
                listar_disciplinas()
                if carregar_dados_disciplinas():
                    input('\nPressione Enter para voltar ao menu Disciplina...')
            elif escolha_menu_secundario == '3': # Excluir
                excluir_disciplina()
            elif escolha_menu_secundario == '4': # Atualizar
                atualizar_cadastro_disciplina()
            elif escolha_menu_secundario == '5': # Voltar
                break # Sai do menu secundário e volta para o principal
            else:
                print('--- Função Inválida ---\nDigite apenas o número correspondente.\nEx: "1" | Incluir')
                input('Pressione Enter para continuar...')

        # ---- Menu Estudante ----
        elif opcao_texto == 'Professor':
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

        # ---- Menu Estudante ----
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

        # ---- Menu Estudante ----
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
