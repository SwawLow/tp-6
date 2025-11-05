def give_question(question: str, answer_pos: str, answer_neg: str, explanation=None) -> bool:
    """
        pre: question, answer_pos et answer_neg son obligatoir mais explanation est optionel
            question: la question demander
            answer_pos: le text qui afficher pour la reponse positive
            answer_neg: le text qui afficher pour la reponse negative
            explanation: la specification pour l'utilisateur, ex: "yes or no"
            si explanation est pas specifier, par defaut "answer_pos ou answer_neg" sera afficher

        post: retourn une valeur bool en fonction de la reponse fourni
    """
    answer = input(f"{question}({explanation if explanation else f"{answer_pos} ou {answer_neg}"}): ").upper()
    answer_pos = answer_pos.upper()
    answer_neg = answer_neg.upper()

    if answer == answer_pos:
        bool_answer = True
    elif answer == answer_neg:
        bool_answer = False
    else:
        bool_answer = give_question(question, answer_pos.lower(), answer_neg.lower(), explanation)

    return bool_answer

def file_get() -> str:
    file = "tp6\README.txt"
    return file

def info():
    pass

def words():
    pass

def search(input_file: str):
    """
        pre: input_file est le chemin d'un fichier
        post: print du text en fonction de si l'input de l'utilisateur est dans un doc,
    """
    search = None
    conti_u = True if input_file else False
    while conti_u == True:
        file = open(input_file, "r")
        search = input("le mot a rechercher: ").upper().strip()
        count = 0
        l1 = []
        for line in file.readlines():
            l1.append(line.strip(" \n"))
        
        for k in range(len(l1)):
            l1[k] = l1[k].split()
            for n in range(len(l1[k])):
                if search == l1[k][n].upper():
                    count += 1
                    break

        print(f"{search.lower()} est dans le document") if count != 0 else print(f"{search.lower()} est pas dans le document")
        conti_u = True if give_question("Voulez vous continuer?", "oui", "non", "soit oui ou non aucune, autre reponse sera tolerer") else False    
        file.close()
    print("aucune fichier n'a été sélectionner\nOrienter vous ver la command \"file\"") if not search else ""

def sum():
    """
        pre: nb1 et nb2 doit etre float ou int
        post: print la somme des termes saisie,
            si le chiffre est entier, il devien int avant le print
    """
    conti_u = True
    while conti_u == True:
        try:
            n_sum = int(input("le nombre de chiffre dans la somme (pas de decimal): "))
            sum = 0
            for n in range(n_sum):
                sum += float(input(f"Terme n°{n+1}: "))
        except:
            print("Une erreur s'est produite.\n" \
            "Aucune lettre peux se trouver dans une moyenne.\n" \
            "Le nombre de chiffre dans la moyenne paux pas etre decimal\n")

        if sum:
            if str(sum) == str(sum//1):
                print(f"\nLa somme: {str(int(sum))}\n")
            else:
                print(f"\nLa somme: {str(sum)}\n")
        conti_u = True if give_question("Voulez vous continuer?", "oui", "non", "soit oui ou non, aucune autre reponse sera tolerer") else False    

def avg():
    """
        pre: n_avg doit etre un int. nb doit etre float ou int
        post: print la moyene des chiffre saisie, 
            si le chiffre est entier, il devien int avant le print
    """
    conti_u = True
    while conti_u == True:
        try:
            n_avg = int(input("le nombre de chiffre dans la moyenne (pas de decimal): "))
            sum = 0
            for n in range(n_avg):
                sum += float(input(f"Chiffre n°{n+1}: "))
        except:
            print("Une erreur s'est produite.\n" \
            "Aucune lettre peux se trouver dans une moyenne.\n" \
            "Le nombre de chiffre dans la moyenne paux pas etre decimal\n")

        if sum:
            average = sum/n_avg
            if str(average) == str(average//1):
                print(f"\nLa moyenne: {(int(average))}\n")
            else:
                print(f"\nLa moyenne: {str(average)}\n")
        conti_u = True if give_question("Voulez vous continuer?", "oui", "non", "soit oui ou non, aucune autre reponse sera tolerer") else False    


def help():
    print("\n" \
    "file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment\n" \
    "info: montre le nombre de lignes et de caractères du fichier\n" \
    "words: utilise le fichier comme liste de mots à partir de maintenant\n" \
    "search <word>: détermine si le mot est dans la liste de mots\n" \
    "sum <number1> ... <numbern>: calcule la somme des nombres spécifiés\n" \
    "avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés\n" \
    "exit: arrête l'outil\n")

def main():
    answer = None
    input_file = ""
    while True:    
        answer = input("Ecriver une commande (écrivez \"help\" pour afficher toutes les commandes):\n").upper()
        if answer == "HELP":
        #help: montre des instructions à l'utilisateur
            help()
        elif answer == "FILE":
        #file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment
            input_file = file_get()
        elif answer == "INFO":
        #info: montre le nombre de lignes et de caractères du fichier
            info()
        elif answer == "WORDS":
        #words: utilise le fichier comme liste de mots à partir de maintenant
            words()
        elif answer == "SEARCH":
        #search <word>: détermine si le mot est dans la liste de mots
            print(input_file)
            search(input_file)
        elif answer == "SUM":
        #sum <number1> ... <numbern>: calcule la somme des nombres spécifiés
            sum()
        elif answer == "AVG":
        #avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés
            avg()
        elif answer == "EXIT":
            break
        else:
            print("ce n'est pas une commande, écrivez \"help\" pour la liste complète\n")
    answer = None

main()
