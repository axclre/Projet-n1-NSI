## Jeu du plus ou moins askip
import random

print('Je choisis un nombre entre 1 et 67')


nbr_a_deviner = random.randint(1, 67) ## L'ordinateur choisit un nombre entre 1 et 67
print(nbr_a_deviner)
tries = 0

while tries < 3 :
    reponse = int(input('Essaie de deviner mon nombre ! Tu as 3 essais !')) ## On demande à l'user de choisir un nombre et on la stocke dans la variable réponse
    if reponse < nbr_a_deviner :
        tries += 1 ## On rajoute 1 au nombre d'essais de l'user
        print("C'est moins ! Essayez encore !")
        print('Il vous reste', 3-tries, 'essais.')
    elif reponse > nbr_a_deviner : 
        tries += 1
        print("C'est plus ! Essayez encore !")
        print('Il vous reste', 3-tries,'essais.')
    elif reponse == nbr_a_deviner :
        print("C'est correct ! Bravo !")
        print("Vous avez réussi en ", tries,"essais.")
        break ## On arrête la boucle while quand l'user a trouvé la bonne réponse
if tries == 3 :
    print("Perdu, vous n'avez plus d'essais!")

if tries != 3 :
    hardmode = input('Voulez vous essayer le mode difficile ?(Y/N)')

if hardmode == Y :
    print('Voici le mode difficile !')
    print('Je choisis un nombre entre 67 et 4141.')
    nbr_a_deviner_hard = random.randint(67,4141)
    print(nbr_a_deviner_hard)
    tries_hard = 0
    while tries_hard < 10 :
        reponse_hard = int(input('Essaie de deviner mon nombre ! Tu as 10 essais !'))
        if reponse_hard < nbr_a_deviner_hard :
            print("C'est moins ! Essayez encore !")
            print("Il vous reste", 10-tries_hard,"essais.")
            nbr_a_deviner_hard = random.randint(reponse_hard,4141)
            print(nbr_a_deviner_hard)
        elif reponse_hard > nbr_a_deviner_hard :
            print("C'est plus ! Essayez encore !")
            print("Il vous reste", 10-tries_hard,"essais")
            nbr_a_deviner_hard = random.randint(67,reponse_hard)
            print(nbr_a_deviner_hard)
        elif reponse_hard == nbr_a_deviner_hard :
            print("C'est correct ! Bravo !")
            print("Vous avez réussi le mode difficile en", tries_hard, "essais")
            break
if tries_hard == 10 :
    print("Plus d'essais ! Vous avez échoué au mode difficile !")