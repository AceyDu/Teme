import sys

def enter_number():
    """

    :return: returneaza valoarea introdusa de la tastura
    """
    try:
        n = input("Variabila: ")
        n = float(n)
    except ValueError:
        print("Eroare la valoare")
        sys.exit(0)
    else:
        return n

def operator_valid():
    """

    :return: returneaza operatorul daca este valid
    """
    op = input("Operatorul dorit este: ")
    if op not in "+-/*^V":
        print("Nu este un operator valid")
        sys.exit(0)
    return op

def main():
    no1 = enter_number()
    print("Primul nr introdus este", no1)
    op = operator_valid()
    print("Operatorul introdus este", op)
    no2 = enter_number()
    print("Al doilea nr introdus este", no2)

    if op == '+':
        print("Rezultatul este", no1 + no2)
    elif op == "-":
        print("Rezultatul este", no1 - no2)
    elif op == "*":
        print("Rezultatul este", no1 * no2)
    elif op == "^":
        print("Rezultatul este", pow(no1, no2))
    elif op == "/":
        try:
            division = no1 / no2
        except ZeroDivisionError as e:
            print("Impartirea la zero nu este permisa", e)
        else:
            print("Rezultatul este", division)
    elif op == "V":
        if no1 < 0:
            print("Eroare matematica")
        else:
            print("Rezultatul este", pow(no1, 1 / no2))
    return


main()