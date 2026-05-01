print(" |---------------------|")
print(" |     Calculadora     |")
print(" |---------------------|")    
()
print("Essa calculadora, faz todas as operaçoes")    
print("a partir de dois numeros que você informar")
()
print("Digite o valor correspondete ao calculo")
print("que você deseja")
()
print("1 - As 4 operações")
print("2 - media de 3 valores")
print("3 - Fórmula de báskara")
()
opcao = float(input("digite uma das operações acima: "))
()

match opcao:
    case 1: 
        first_num = float(input("Digite o Primeiro numero: "))
        second_num = float(input("Digite o segundo número: "))

        adicao = first_num + second_num
        print("resultado da adição é:", adicao,)

        subtracao = first_num - second_num
        print("resultado da subtração:",subtracao)

        multiplicacao = first_num * second_num
        print(f"resultado da multiplicação: {multiplicacao}")

        if second_num != 0:
            divisao = first_num / second_num
            print(f"resultado da divisão: {divisao}")
        else:
            divisao = print("Não divisivel por zero")
        print()

    case 2:
        first_num = float(input("digite aqui a 1ª numero:"))
        second_num = float(input("digite aqui a 2ª numero:"))
        third_num = float(input("digite aqui a 3ª numero:"))

        soma = first_num + second_num + third_num
        media = soma/3

        print("A média é:",media)
    

    case 3:
        a = float(input("Digite o valor de a"))
        b = float(input("Digite o valor de b"))
        c = float(input("Digite o valor de c"))
        ()
        if a == 0:
            print("Isso não é uma equação do segundo grau (a deve ser diferente de 0).")
        else:
            delta = b**2 - 4*a*c
            
            if delta < 0:
                print("Não é possivel fazer raizes de números menores de 0")
            