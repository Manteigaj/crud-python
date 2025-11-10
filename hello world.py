import os
from time import sleep

cadastro = []

def mostrar_menu():
    print('escolha a opção: ')
    print('1- cadastrar usuário')
    print('2- listar usuários')
    print('3- atualizar cadastro')
    print('4- deletar usuário')
    print('5- encerrar programa')
    escolher_opcao()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('digite a opção escolhida '))
        if opcao_escolhida == 1:
            cadastrar_usuario()
        elif opcao_escolhida == 2:
            listar_usuarios()
        elif opcao_escolhida == 3:
            atualizar_usuario()
        elif opcao_escolhida == 4:
            deletar_usuario()
        elif opcao_escolhida == 5:
            print('encerrando programa')
        else:
            print('opção invalida')
            voltar_ao_menu()
    except:
        print('opção invalida!/n')
        voltar_ao_menu()

def voltar_ao_menu():
    input('pressione uma tecla para voltar ao menu principal')
    main()

def cadastrar_usuario():
    os.system('cls')
    nome_usuario = str(input('digite o nome do usuario: '))
    email_usuario = str(input('digite o email do usuario: '))
    senha_usuario = str(input('digite a senha do usuario: '))
    usuario = {'nome':nome_usuario, 'email':email_usuario, 'senha':senha_usuario}
    cadastro.append(usuario)
    voltar_ao_menu()

def listar_usuarios():
    os.system('cls')
    if not cadastro:
        print('nenhum usuário encontrado')
    else:
        for usuario in cadastro:
            nome_usuario = usuario['nome']
            email_usuario = usuario['email']
            senha_usuario = usuario['senha']
            print(f'nome : {nome_usuario} | email : {email_usuario} | senha : {senha_usuario}')
    voltar_ao_menu()

def atualizar_usuario():
    os.system('cls')
    escolher_usuario = str(input('digite o nome do usuario que deseja alterar: '))
    for usuario in cadastro:
        if escolher_usuario == usuario['nome']:
            novo_nome = str(input('digite o um novo nome de usuário (deixe em branco para manter): '))
            novo_email = str(input('digite o novo email do usuário (deixe em branco para manter): '))
            nova_senha = str(input('digite a nova senha do usuário (deixe em branco para manter): '))
            if novo_nome:
                usuario['nome'] = novo_nome
            if novo_email:    
                usuario['email'] = novo_email
            if nova_senha:    
                usuario['senha'] = nova_senha
        else:
            print('usuário não encontrado')   
    voltar_ao_menu()

def deletar_usuario():
    os.system('cls')
    escolher_usuario = str(input('digite o nome do usuário que deseja deletar: '))
    for usuario in cadastro:
        if escolher_usuario == usuario['nome']:
            cadastro.remove(usuario)
        else:
            print('usuário não encontrado')
    voltar_ao_menu()

def main():
    os.system('cls')
    mostrar_menu()
    
if __name__ == '__main__':
    main()