# isso é um comentario

# agora, nós escreveremos na tela usando o comando print!
# O comando print, serve para escrevermos alguma coisa na tela
print ("hello, world!")
print ("Olá, mundo!, esse é o curso de lógica de programação")

# O comando input serve para receber uma entrada do teclado, sendo que o usuario irá digitar
# a sintaxe do comando input é: input("mensagem")

nome =  input("Digite seu nome: ")
idade = int(input("Qual sua idade: "))

# input guarda a informação variavel
# o comando input SEMPRE vai converter como str (letras)
#para converter é so colocar int(input("xxxxx")), assim o valor é convertido para numeros inteiros

print("Olá,", nome, "você tem", idade, "anos, que velho ;D")

# consigo saber qual a variavel usando o seguinte codigo
# tipos de variedades 
# -int = numeros inteiros Ex: 1, 10, 1000
# -float = numeros com vírgula ex: 3.14, 1.68

print("o tipo da variavel nome é", type(nome))
print("o tipo de variedade idade é", type(idade))
# esse codigo acima é linear.