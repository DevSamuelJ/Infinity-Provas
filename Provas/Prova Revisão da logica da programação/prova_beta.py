#Crie um programa em Python que simule um sistema de login. 
# 1 - O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# 2 - Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# 3 - Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
# 4 - Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.


# nome_usuario = "samuel"
# senha = 123

# tentativa_usuario = 0 

# while True: #melhor fazer com o while mesmo usando o numero de tentativas.
#   qual_usuario = input("Informe o nome do usuario para login: ")
#   if qual_usuario == nome_usuario:
#     print("Usuario correto!")
#     break
#   tentativa_usuario += 1
#   if tentativa_usuario == 1:
#     print(f"Usuario incorreto, tentativa {tentativa_usuario}/3 ")
#   elif tentativa_usuario == 2:
#     print(f"Usuario incorreto, tentativa {tentativa_usuario}/3 ")
#   elif tentativa_usuario ==3:
#     print(f"Usuario incorreto, tentativa {tentativa_usuario}/3 ")
#   else: 
#     for bloqueio in range(3):
#       print("Acesso bloqueado.")
#     break
# tentativa_senha = 0
# while True:
#   qual_senha = int(input("Informe a senha para login: "))
#   tentativa_senha += 1
#   if qual_senha == senha:
#       print("Senha correta!")
#       break
#   tentativa_senha += 1
#   if tentativa_senha == 1:
#     print(f"Senha incorreta, tentativa {tentativa_senha}/3 ")
#   elif tentativa_senha == 2:
#     print(f"Senha incorreta, tentativa {tentativa_senha}/3 ")
#   elif tentativa_senha ==3:
#     print(f"Senha incorreta, tentativa {tentativa_senha}/3 ")
#   else: 
#     for bloqueio in range(3):
#       print("Acesso bloqueado.")
#     break


#============== na de cima eu fiz usuario e senha separados porem tem que ser juntos

nome = "samuel"
senha = "123"

tentativa = 0

while True:
  qual_nome = input("Informe o usuario para login: ")
  qual_senha = input("Informe a senha para login: ")

  if qual_nome == nome and qual_senha == senha:
    print(f"Bem-vindo, {nome.upper()}!")
    break 
  tentativa += 1
  if tentativa == 0 or tentativa == 1 or tentativa == 2:
    print(f"Usuario e senha incorretos, tentativa {tentativa}/3")

  # tentativa += 1
  # if tentativa == 0:
  #   print(f"Usuario e senha incorretos, tentativa {tentativa}/3")
  # elif tentativa == 1:
  #   print(f"Usuario e senha incorretos, tentativa {tentativa}/3")
  # elif tentativa == 2:
  #   print(f"Usuario e senha incorretos, tentativa {tentativa}/3")
  else:
     print(f"Usuario e senha incorretos, tentativa {tentativa}/3")
     for i in range(3):
       print("Acesso bloquedo.")
     break