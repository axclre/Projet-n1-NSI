## Jeu du plus ou moins askip
import random

print('Je choisis un nombre entre 1 et 100')


nbr_a_deviner = random.randint(1, 100) ## L'ordinateur choisit un nombre entre 1 et 100
print(nbr_a_deviner)
tries = 1

while tries < 4 :
    reponse = input('Essaie de deviner mon nombre ! Tu as 3 essais au total ! : ') ## On demande à l'user de choisir un nombre et on la stocke dans la variable réponse
    if reponse == "donne la reponse stp" : ## Cheat code 
        print('La réponse est : ',nbr_a_deviner)
        print("Petit chenapan !")
        continue
    reponse = int(reponse) ## On convertit la réponse en entier
    if reponse < nbr_a_deviner :
        tries += 1 ## On rajoute 1 au nombre d'essais de l'user
        print("C'est plus ! Essayez encore !")
        print('Il vous reste', 4-tries, 'essais.')
    elif reponse > nbr_a_deviner : 
        tries += 1
        print("C'est moins ! Essayez encore !")
        print('Il vous reste', 4-tries,'essais.')
    elif reponse == nbr_a_deviner :
        print("C'est correct ! Bravo !")
        print("Vous avez réussi en ", tries,"essais.")
        break ## On arrête la boucle while quand l'user a trouvé la bonne réponse
if tries == 4 :
    print("Perdu, vous n'avez plus d'essais!")

if tries != 4 :
    hardmode = input('Voulez vous essayer le mode difficile ?(Y/N) : ')

tries_hard = 1

if hardmode == "Y" or hardmode == "y" :
    print('Voici le mode difficile !')
    print('Je choisis un nombre entre 67 et 4141.')
    nbr_a_deviner_hard = random.randint(67,4141)
    print(nbr_a_deviner_hard)
    while tries_hard < 11 :
        reponse_hard = input('Essaie de deviner mon nombre ! Tu as 10 essais au total ! : ')
        if reponse_hard == "donne la reponse stp" : ## Faux cheat code
            print('Tu pensais vraiment pouvoir tricher en mode difficile petit filou ?')
            print('Juste pour la peine je te retire 2 essais :)')
            tries_hard += 2
            print('Il te reste maintenant', 11-tries_hard, 'essais.')
            continue
        reponse_hard = int(reponse_hard)
        if reponse_hard < nbr_a_deviner_hard :
            tries_hard += 1
            print("C'est plus ! Essayez encore !")
            print("Il vous reste", 11-tries_hard,"essais.")
            nbr_a_deviner_hard = random.randint(reponse_hard,4141)
            print(nbr_a_deviner_hard)
        elif reponse_hard > nbr_a_deviner_hard :
            tries_hard += 1
            print("C'est moins ! Essayez encore !")
            print("Il vous reste", 11-tries_hard,"essais")
            nbr_a_deviner_hard = random.randint(67,reponse_hard)
            print(nbr_a_deviner_hard)
        elif reponse_hard == nbr_a_deviner_hard :
            print("C'est correct ! Bravo !")
            print("Vous avez réussi le mode difficile en", tries_hard, "essais !")
            break
if tries_hard == 11 :
    print("Plus d'essais ! Vous avez échoué au mode difficile !")

if hardmode == "N" or hardmode == "n" :
    print("Merci d'avoir joué quand même !")