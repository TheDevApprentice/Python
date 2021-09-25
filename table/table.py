def table(nb, max):
    nb = int(nb)
    max = int(max)
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i +1) * nb)
        i += 1

x = input('entrez un nombre : ')

y = input("entre un nombre : ")

table(x,y)