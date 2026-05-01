import math

def bhaskara(a: float, b: float, c: float):
    """
    Calcula as raízes de uma equação do segundo grau: ax² + bx + c = 0
    Retorna uma tupla com as raízes ou uma mensagem de erro.
    """
    # Validação: 'a' não pode ser zero
    if a == 0:
        raise ValueError("O coeficiente 'a' deve ser diferente de zero para ser uma equação do 2º grau.")

    # Calcula o discriminante (delta)
    delta = b**2 - 4*a*c

    if delta > 0:
        # Duas raízes reais distintas
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        # Uma raiz real (repetida)
        x = -b / (2*a)
        return x,
    else:
        # Raízes complexas
        real = -b / (2*a)
        imag = math.sqrt(-delta) / (2*a)
        return complex(real, imag), complex(real, -imag)

def main():
    try:
        # Entrada de dados
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        # Cálculo das raízes
        raizes = bhaskara(a, b, c)

        # Exibição do resultado
        if len(raizes) == 1:
            print(f"Raiz única: {raizes[0]}")
        else:
            print(f"Raízes: {raizes[0]} e {raizes[1]}")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
