cadastro = [{'nome':'joao','email': 'manteiga.com', 'senha' : 'manteiga delas'}]

escolher_usuario = str(input('digite o nome do usuario que deseja alterar: '))
for usuario in cadastro:
    if escolher_usuario == usuario['nome']:
        novo_nome = str(input('digite o um novo nome de usuário: '))
        novo_email = str(input('digite o novo email do usuário: '))
        nova_senha = str(input('digite a nova senha do usuário: '))
        if novo_nome:
            usuario['nome'] = novo_nome
        if novo_email:    
            usuario['email'] = novo_email
        if nova_senha:    
            usuario['senha'] = nova_senha

print(cadastro)