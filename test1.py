# -*- coding: utf-8 -*-


def nbr_choix (N):
    nbr_choisit = N+1

    while nbr_choisit < 1 or nbr_choisit > N:
        try:
            nbr_choisit = int(input("selection : "))
        except ValueError:
            print("rentre un nombre entier")
        else:
            print(nbr_choisit)
        #    newnbr = nbr_choisit
           # break
    #return #nbr_choisit
    print(nbr_choisit)
    return nbr_choisit
#main

nbr_choix(4)

print(nbr_choisit)
#print(newnbr)
if nbr_choisit == 1:
    print("premier choix")
elif nbr_choisit == 2:
    print("second choix")
elif nbr_choisit == 3:
    print("3eme choix")
elif nbr_choisit == 4:
    print("4eme choix")
