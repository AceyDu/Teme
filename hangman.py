import random


hangman=[["________",
   " |     |",
   " |",
   " |",
   " |",
   " |",
   " |",
   "___"],
   ["________",
    " |     |",
    " |     o",
    " |",
    " |",
    " |",
    " |",
    "___"],
["________",
    " |     |",
    " |     o",
    " |     |",
    " |",
    " |",
    " |",
    "___"],
["________",
    " |     |",
    " |     o",
    " |   / |",
    " |",
    " |",
    " |",
    "___"],
["________",
    " |     |",
    " |     o",
    " |   / | \\",
    " |",
    " |",
    " |",
    "___"],
["________",
    " |     |",
    " |     o",
    " |   / | \\",
    " |    /",
    " |",
    " |",
    "___"],
   ["________",
    " |     |",
    " |     o",
    " |   / | \\",
    " |    / \\",
    " |",
    " |",
    "___"],
     ["________",
      " |     |",
      " |     o",
      " |   / | \\",
      " |    / \\",
      " |   *****",
      " |",
      "___"]
         ]


cuvinte = ["pantofi", "frigider", "carte", "pantaloni"]

cuvant = random.choice(cuvinte)

lista = list(cuvant)
copie = list(cuvant)
prima = lista[0]
ultima = lista[-1]
for i in range(len(lista)):
    if lista[i] != prima and lista[i] != ultima:
        lista[i] = '_'


for i in hangman[0]:
    print(i)

print(lista)

vieti = 7
litere = list()
litere.append(prima)
litere.append(ultima)

while vieti !=0:

    ok = False
    litera = input("Alege o litera: ").lower()
    if litera.isalpha() and len(litera) == 1:
        if litera in litere:
            print("Ai folosit deja litera: ", litera)
            print("Literele folosite pana acum:")
            print(litere)
            continue
        litere.append(litera)
        for i in range(len(copie)):
            if copie[i] == litera:
                lista[i] = litera
                ok = True
        if ok is False:
            vieti -= 1
            print("Litera: ", litera, " nu se afla in cuvant.")
            if vieti > 0:
                for i in hangman[7-vieti]:
                    print(i)
                print("Mai ai ", vieti, " vieti.")
        else:
            print(lista)
        if "_" not in lista:
            print("Ai castigat!")
            break
    else:
        print("Introduceti doar litere!")

if vieti == 0:
    for i in hangman[-1]:
        print(i)
    print("Ai pierdut!")
    print("Cuvantul era: ", cuvant)
