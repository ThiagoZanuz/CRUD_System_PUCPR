import os
import sys
import json

CAMINHO_ARQUIVO = 'arquivo.json'

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

# --- Funções Json ---
def carregar_dados():
    try:
        with open(CAMINHO_ARQUIVO, 'r') as a:
            return json.load(a)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_estudantes(estudantes):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as a:
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
def incluir_estudante():
    estudantes = carregar_dados()
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
    estudantes = carregar_dados()
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
    estudantes = carregar_dados()
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
    estudantes = carregar_dados()
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
                print(f'Nome: {estudante_selecionado["nome"]}')
                print(f'RA: {estudante_selecionado["ra"]}')
                print(f'CPF: {estudante_selecionado["cpf"]}')
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
                incluir_estudante()
            elif escolha_menu_secundario == '2': # Listar
                listar_estudantes()
                if carregar_dados():
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

        # ---- Outros Menus (Em desenvolvimento) ----
        else:
            limpar_terminal()
            print(f'--- Menu "{opcao_texto}" em desenvolvimento ---')
            input('Pressione Enter para voltar ao Menu Principal...')
            break # Sai do menu secundário e volta para o principal
