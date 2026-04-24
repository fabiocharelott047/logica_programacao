#nesse codigo, analisaremos a idade do usuario e falaremos se é maior de idade ou não

nome =  input("Digite seu nome: ")
idade = int(input("Qual sua idade: "))
print("Olá,", nome, "!, você tem", idade, "anos, que velho ;D")

# a estrutura de decisão analisa uma comparacção e executa o codigo com base na resposta. 
# Para utilizarmos a estrutura de decisão, precisamos de comparadores que são:
#
# - > maior 
# - < menor
# - == igual
# - != diferente
# - >= maior ou igual
# - <= menor ou igual
# - ! não

#no pyton se true é colocado com um "tab" para dentro como o inicio de um paragrafo

if idade >= 18:
    print("Voce é maior de idade!")
    if idade >= 60:
        print("És idoso!")
        print("Você ja pode pegar sua carteirinha de estacionamento")
else:
    print("És menor de idade!")
    print("Oque estas a fazer aqui?")
    print ("no puedes comprar los cigarretes")

#if = true
# eslse = false
#if idade <= 18:
#    print("Oque voce esta fazendo aqui?")