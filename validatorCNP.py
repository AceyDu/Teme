import sys


def verify_cnp():
    cnp = input("Insert your CNP")
    list_cnp = list(cnp)
    verify_code = "279146358279"
    list_verify_code = list(verify_code)
    total = 0
    for i in range(0, 12):
        total += int(list_cnp[i]) * int(list_verify_code[i])
    c = total % 11
    if c == 10:
        c = 1
    if int(list_cnp[12]) == c:
        print("CNP is valid")
        sys.exit(1)
    else:
        print("CNP is not valid, please insert a valid one")
        verify_cnp()


verify_cnp()
