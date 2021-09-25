import time

score=0

while 1:
    print('Vous avez utilisé ce programme : %s' % (score))
    
    on = 0
    anneeBisextile = False 

    annee = input("Entrez une année pour savoir si elle est bisextile : ")
    annee = int(annee)
    
    print(annee)
    time.sleep(1.2)
    print('Faissons le calcul')
    time.sleep(2)

    if annee % 400 == 0:
        anneeBisextile = True
    elif annee % 100 == 0:
        anneeBisextile = False
    elif annee % 4 == 0:
        anneeBisextile = True
    else:
        anneeBisextile = False

    if anneeBisextile: # Si l'année est bissextile
        print("L'année saisie est bissextile.")
        time.sleep(2.2)
    else:
        print("L'année saisie n'est pas bissextile.")
        time.sleep(2.2)

    on = input("Voulez vous recommencer le programme ? 1: Oui 0:Non")
    on = int(on)

    time.sleep(0.5)

    if on == 0:
        print('it Was a Pleasure to greet you here ! Have a good day ')
        print('Author : Hugo Abric')
        break
    if on == 1:
        score += 1
        time.sleep(0.1)
        continue
        

  
