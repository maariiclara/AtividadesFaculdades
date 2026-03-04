'''
leia um nome de usuario e sua senha 
nao aceita a senha igual ao nome de usuario
mensagem de erro + volta a pedir informacoes
'''


while (usuario == senha):
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    if (usuario == senha):
        print("As senhas nao podem ")
    else:
        print("Digite um número válido!")