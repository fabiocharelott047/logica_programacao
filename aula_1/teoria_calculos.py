nome =  input("Digite seu nome: ")
idade = int(input("Qual sua idade: "))
turma = int(input("Qual sua turma"))

if idade >=18:
    input("Está estudando?")
# terminar para maios e menor de 18 para depois pedir turma

print("qual nota você tirou nas ultimas três provas?")

nota1 = float(input("digite aqui a 1ª nota:"))
nota2 = float(input("digite aqui a 2ª nota:"))
nota3 = float(input("digite aqui a 3ª nota:"))

soma = nota1+nota2+nota3
media = soma/3

print("A sua média nessas três provas é:",media)
if media >= 7:
    print("Você foi aprovado!")
    if media >=9.5:
        print("Parabéns conseguistes um premio por ter uma nota acima da média!")
elif media <= 4:
    print("Você está de recuperação")
else:
    print("Fostes reprovado!")
    
