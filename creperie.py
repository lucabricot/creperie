import sys


#toute les crêpes disponible à la carte
crepe_menu = [
    {
        'nom': 'Confiture',
        'prix': 4.50,
        'gout': 'Salée',
        'ingredients': ['Sucre Glace', 'Confiture Fraise', 'Chantilly']
    },
    {
        'nom': 'Nutela',
        'prix': 4.00,
        'gout': 'Salée',
        'ingredients': ['Nutela', 'Bananes', 'Chantilly']
    },
    {
        'nom': 'Cidres',
        'prix': 9.00,
        'gout': 'Salée',
        'ingredients': ['Cidres', 'Pommes', 'Vanille']
    },
    {
        'nom': 'Frobon',
        'prix': 8.00,
        'gout': 'Sucrée',
        'ingredients': ['Fromage', 'Jambon', 'Ananas']
    },
    {
        'nom': 'TroisViandes',
        'prix': 12.00,
        'gout': 'Sucrée',
        'ingredients': ['Kebab', 'Poulet', 'Steak']
    },
    {
        'nom': 'Verdure',
        'prix': 7.50,
        'gout': 'Salée',
        'ingredients': ['Salade', 'Framboises', 'Haricots']
    }
    ]




#la page d'accueil pour réaliser une action
def home_page():
    print("---------------------------------------------------------------")
    print("1. Afficher la liste de crêpes par ordre alphabétique.")
    print("2. Afficher la liste de crêpes par prix croissant.")
    print("3. Crêpe la plus chère.")
    print("4. Crêpe la moins chère.")
    print("5. Choisir sa crêpe du menu")
    print("6. Creer sa propre crêpe.")
    print("7. Afficher le panier")
    print("8. Quitter le programme.")
    print("---------------------------------------------------------------")
    action = int(input("Veuillez choisir un chiffre pour réaliser l'action souhaitée. "))
    
    if action == 1:
        alphabetique_selec(length)

    elif action == 2:
        prix_croissant(length)

    elif action == 3:
        maxi()

    elif action == 4:
        mini()
        
    elif action == 5:
        menu()
            
    elif action == 6:
        custom()

    elif action == 7:
        print("\nVotre Panier: \n")
        for i in panier:
            print(i)
        home_page()

    elif action == 8:
        sys.exit()

    else:
        print("Veuillez écrire un chiffre valide!")

        
length = len(crepe_menu)
panier = []

#1: fonction pour afficher la liste de crepres par ordre alphabétique avec tri par selection    


def alphabetique_selec(length): 
    for i in range(length):
        min = i

        for j in range(i+1, length):
            if (crepe_menu[min]['nom'] > crepe_menu[j]['nom']):
                min = j
        
        temp = crepe_menu[i]
        crepe_menu[i] = crepe_menu[min]
        crepe_menu[min] = temp

    print ("\n La liste des crêpes par ordre alphabétique: \n")
    for i in range(length):
        print("Nom de la crêpe:",crepe_menu[i]['nom'],"║ prix:",crepe_menu[i]['prix'],"║ ingrédients dans la crêpe:",crepe_menu[i]['gout'],crepe_menu[i]['ingredients'])
    home_page()


    

#2: fonction pour afficher la liste de crepes par prix croissant avec tri par bulles        
def prix_croissant(length):     
    for i in range(length):
        for j in range(length-1-i):
            if (crepe_menu[j]['prix'] > crepe_menu[j+1]['prix']):
                crepe_menu[j], crepe_menu[j+1] = crepe_menu[j+1], crepe_menu[j]
                
    print ("\n La liste des crêpes par prix croissant: \n")
    for i in range(length):
        print("Nom de la crêpe:",crepe_menu[i]['nom'],"║ prix:",crepe_menu[i]['prix'],"║ ingrédients dans la crêpe:",crepe_menu[i]['gout'],crepe_menu[i]['ingredients'])
    home_page()

    

#3 : fonction pour afficher la crepe la plus cher
def maxi():                  
    for i in range(length):
        for j in range(length-1-i):
            if (crepe_menu[j]['prix'] < crepe_menu[j+1]['prix']):
               crepe_menu[j], crepe_menu[j+1] = crepe_menu[j+1], crepe_menu[j]
    print(crepe_menu[j])
    home_page()

    

#4: fonction pour afficher la crepe la moins cher
def mini():                     
    for i in range(length):
        for j in range(length-1-i):
            if (crepe_menu[j]['prix'] > crepe_menu[j+1]['prix']):
                crepe_menu[j], crepe_menu[j+1] = crepe_menu[j+1], crepe_menu[j]
    print(crepe_menu[j])
    home_page()

    
#5: Fonction pour chosir une crêpe au menu
def menu():
    L = []
    choix = 0
    while choix < 1:
        for i in range(length):
            print("Nom de la crêpe:",crepe_menu[i]['nom'],"║ prix:",crepe_menu[i]['prix'],"║ ingrédients dans la crêpe:",crepe_menu[i]['gout'],crepe_menu[i]['ingredients'])

        elt = str((input("\n Veuillez choisir une crêpe du menu: \n")))
        temp = []
        for i in range(length):
            temp.append(crepe_menu[i]['nom'])
        if elt not in temp:
            print("\nCette crêpe n'existe pas! \n")
            choix -= 1
        else:
            L.append(elt)
            panier.append(L)
            txt = open('panier.txt' , 'w')
            txt.write("Panier:" + "\n\n")
            for i in panier:
                txt.write( "\n----------------------------------\n")
                for j in i: 
                    txt.write(j + " ")    
            print("Vous avez choisi la crêpe:",panier) 
        choix += 1
    home_page() 

#les ingredients disponible 
ingredients = ['Sucre Glace', 'Confiture Fraise', 'Chantilly', 'Nutela', 'Bananes', 'Cidres', 'Pommes', 'Vanille', 'Fromage', 'Jambon', 'Ananas', 'Kebab', 'Poulet', 'Steak', 'Salade', 'Framboises', 'Haricots']

#le prix de chaque ingrédient
ingredients = {
        'Sucre Glace': 0.20,
        'Confiture Fraise': 0.30,
        'Chantilly': 0.40,
        'Nutela': 0.50,
        'Bananes': 0.60,
        'Cidres': 0.90,
        'Pommes': 0.60,
        'Vanille': 0.70,
        'Fromage': 0.90,
        'Jambon': 0.80,
        'Ananas': 0.80,
        'Kebab': 0.90,
        'Poulet': 0.80,
        'Steak': 0.80,
        'Salade': 0.50,
        'Framboises': 0.60,
        'Haricots': 0.60
    }


#6: fonction pour faire sa propre crepe
    
def custom():
    somme = 0
    choix = 1
    ingredient = []
    prix_crepe = 5
    while choix <= 3:
        print("\n Nos ingrédients:")
        for elt,key in ingredients.items():
            print("-" + elt,":",key, "€")

        elt = (input("\n Veuillez choisir un ingrédient à mettre dans votre crêpe \n"))
        
        if elt not in ingredients:
            print("\n cet ingrédient n'est pas disponible! \n")
            choix -= 1
            
        else :
            ingredient.append(elt)
            print("\n Ingrédient ajouté avec succès \n")

            if somme == 0:
                somme = prix_crepe + ingredients[elt]
            else:
                somme += ingredients[elt]
                    
            print("Votre crêpe à comme prix:",somme,"€","\n")
            
        choix += 1
    print("Votre crêpe contient ces ingredients:",ingredient)
    
    reponse = input("\n Voulez vous ajouter cette crêpe au panier ? (oui ou non) \n")
    if reponse == "oui":
        panier.append(ingredient)
        txt = open('panier.txt' , 'w')
        txt.write("Panier:" + "\n\n")
        for i in panier:
            txt.write( "\n----------------------------------\n")
            for j in i: 
                txt.write(j + " ")      

        print("Ta crêpe est ajouté au panier! \n")
        home_page()
        
    if reponse == "non":
        home_page()

home_page()    
    
                
