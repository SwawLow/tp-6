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
    print(f"{question}({explanation if explanation else f"{answer_pos} ou {answer_neg}"}):")
    answer = input("> ").upper()
    answer_pos = answer_pos.upper()
    answer_neg = answer_neg.upper()

    if answer == answer_pos:
        bool_answer = True
    elif answer == answer_neg:
        bool_answer = False
    else:
        bool_answer = give_question(question, answer_pos.lower(), answer_neg.lower(), explanation)

    return bool_answer

def word_approximation(input: str, word_list: list) -> str:
        
    """
        pre: input peut etre tout les str possible
            word_list est la list qui est comparer a input
        post: retourn une un str le plus proche d'input
    """

    #["AVG", "EXIT", "FILE", "HELP", "INFO", "LANGUAGE", "SEARCH", "SUM", "WORDS"]

    first = 0
    last = len(word_list)-1
    found = False

    length = len(input)
    if length == 0:
        return None

    while first<=last and not found:
        middle = (first + last)//2
        count_last = 0
        count_first = 0
        count = 0
        for q in range(length):
            count += 1 if word_list[middle][q] == input[q] else 0
        if count == length:
            found = True
        else:
            for n in range(length):
                if input[n] < word_list[middle][n]:
                    count_last+=1
                else:
                    count_first+=1

            if count_last > count_first:
                last = middle-1
            else:
                first = middle+1

    if found == True:
        return word_list[middle]
    
assert not word_approximation(str, []), "word_list should have a length of atleast 1"
    
def language() -> str:
    """
        post: retourn "en" ou "fr"
    """
    return "en" if give_question("\"en\" for English\n\"fr\" pour Français", "en", "fr") else "fr"

def file_get(lang: str) -> str:
    """
        pre: lang est soit "en" ou "fr"
        post: retourn le fichier qui va etre utiliser
    """
    contin_u = True
    while contin_u == True:
        print("Write file name that is contained within the same folder as tp6") if lang == "en" else print("Saisissez le nom du fichier qui se trouve dans le même dossier que tp6")
        file_name = input("> ")
        full_name = f"tp6\{file_name}"
        try:
            f = open(full_name, 'r')
            f.close()
            print("Loaded " + file_name)
            return full_name
        except:
            print("Error: file not found" if lang == "en" else "Erreur: fichier introuvable")
            contin_u = True if give_question("Do you want to continue?" if lang == "en" else "Voulez vous continuer?","yes" if lang == "en" else "oui", "no" if lang == "en" else "non") else False    

assert not file_get(not "en" or "fr"), "lang should be either en or fr"

def info(input_file: str, lang: str):
    """
        pre: input_file est un chemin de fichier
            lang est soit "en" ou "fr"
        post: print le nombre de ligne et de caracter
    """
    if not input_file:
        print("Error: no file loaded" if lang == "en" else "Erreur: aucun fichier chargé")
        return
    
    try:
        f = open(input_file, 'r')
        contenu = f.readlines()
        f.close()
    except:
        print("Error: file does not exist" if lang == "en" else "Erreur: fichier n'existe pas")
        return

    lignes = contenu.split('\n')
    nb_lignes = len(lignes)
    nb_char = len(contenu)
    
    print(f"{nb_lignes} lines" if lang == "en" else f"{nb_lignes} lignes")
    print(f"{nb_char} characters" if lang == "en" else f"{nb_char} caracters")

assert not info(not "en" or "fr"), "lang should be either en or fr"

def words(input_file: str, lang: str) -> list:
    """
        pre: input_file est un chemin de fichier
            lang est soit "en" ou "fr"
        post: retourn tout les mot d'un fichier dans une list
    """
    if not input_file:
        print("Error: no file loaded" if lang == "en" else "Erreur: aucun fichier chargé")
        return
    
    try:
        f = open(input_file, 'r')
        lignes = f.readlines()
        f.close()
    except:
        print("Error: file does not exist" if lang == "en" else "Erreur: fichier n'existe pas")
        return
    
    list_mots = []
    i = 0

    for k in range(len(lignes)):
            lignes[k] = lignes[k].split()

    for p in range(len(lignes)):
        for n in range(len(lignes[p])):
            list_mots.append(lignes[p][n])

    print("Read file as list of words" if lang == "en" else "Lire le fichier comme une liste de mots")
    return list_mots

assert not words(not "en" or "fr"), "lang should be either en or fr"

def search(list_mots: list, lang: str):
    """
        pre: input_file est le chemin d'un fichier
        post: print du text en fonction de si l'input de l'utilisateur est dans un doc,
    """
    search = None
    contin_u = True if list_mots else False
    while contin_u == True:
        print("Write the word you want to find" if lang == "en" else "Écrivez le mot que vous souhaitez trouver.")
        search = input("> ").upper().strip()
        count = 0
        for n in range(len(list_mots)):
            if search == list_mots[n].upper():
                count += 1
                break
        print(f"{search.lower()} est dans le document") if count != 0 else print(f"{search.lower()} est pas dans le document")
        contin_u = True if give_question("Do you want to continue?" if lang == "en" else "Voulez vous continuer?","yes" if lang == "en" else "oui", "no" if lang == "en" else "non", "The answer must be either yes or no; no other answer will be tolerated" if lang == "en" else "soit oui ou non, aucune autre reponse sera tolerer") and search else False    

    print("The word list was not defined (tip: use \"words\" command)" if lang == "en" else "Le liste de mot n'a pas été défini (Conseil : utilisez la commande \"words\")") if not search else ""

assert not search(not "en" or "fr"), "lang should be either en or fr"

def sum(lang: str):
    """
        pre: nb1 et nb2 doit etre float ou int
        post: print la somme des termes saisie,
            si le chiffre est entier, il devien int avant le print
    """
    contin_u = True
    while contin_u == True:
        try:
            print("the number of digits in the sum (no decimals)" if lang == "en" else "le nombre de chiffre dans la somme (pas de decimal)")
            n_sum = int(input("> "))
            while n_sum == 1:
                print("A sum cannot have 1 term" if lang == "en" else "Une somme ne peut pas avoir 1 term")
                n_sum = int(input("> "))
            sum = 0
            for n in range(abs(n_sum)):
                sum += float(input(f"Terme n°{n+1}: "))
        except:
            print("An error has occurred.\n"
            "No letters can be present in a sum.\n"
            "The number of digits in the average cannot be a decimal.\n" if lang == "en" else "Une erreur s'est produite.\n" \
            "Aucune lettre peux se trouver dans une somme.\n" \
            "Le nombre de chiffre dans la moyenne paux pas etre decimal\n")
        if sum:
            if str(sum) == str(sum//1):
                print(f"The sum: {int(sum)}\n" if lang == "en" else f"\nLa somme: {int(sum)}\n")
            else:
                print(f"The sum: {sum}\n" if lang == "en" else f"\nLa somme: {sum}\n")
        contin_u = True if give_question("Do you want to continue?" if lang == "en" else "Voulez vous continuer?","yes" if lang == "en" else "oui", "no" if lang == "en" else "non", "The answer must be either yes or no; no other answer will be tolerated." if lang == "en" else "soit oui ou non, aucune autre reponse sera tolerer") else False    

assert not sum(not "en" or "fr"), "lang should be either en or fr"

def avg(lang: str):
    """
        pre: n_avg doit etre un int. nb doit etre float ou int
        post: print la moyene des chiffre saisie, 
            si le chiffre est entier, il devien int avant le print
    """
    contin_u = True
    while contin_u == True:
        try:
            print("the number of digits in the average" if lang == "en" else "le nombre de chiffre dans la moyenne (pas de decimal)")
            n_avg = int(input("> "))
            while n_avg < 1:
                print(f"An average cannot have {n_avg} interger" if lang == "en" else f"Une moyenne ne peut pas avoir {n_avg} chiffre")
                n_avg = int(input("> "))
            sum = 0
            for n in range(abs(n_avg)):
                sum += float(input(f"Chiffre n°{n+1}: "))
        except:
            print("An error has occurred.\n" \
            "No letters can be included in an average.\n" \
            "The number of digits in the average cannot be a decimal.\n" if lang == "en" else "Une erreur s'est produite.\n" \
            "Aucune lettre peux se trouver dans une moyenne.\n" \
            "Le nombre de chiffre dans la moyenne paux pas etre decimal\n")


        average = sum/n_avg
        if str(average) == str(average//1):
            print(f"The Average: {int(average)}\n" if lang == "en" else f"\nLa moyenne: {int(average)}\n")
        else:
            print(f"The Average: {average}\n" if lang == "en" else f"\nLa moyenne: {average}\n")
        contin_u = True if give_question("Do you want to continue?" if lang == "en" else "Voulez vous continuer?","yes" if lang == "en" else "oui", "no" if lang == "en" else "non", "The answer must be either yes or no; no other answer will be tolerated." if lang == "en" else "soit oui ou non, aucune autre reponse sera tolerer") else False    

assert not avg(not "en" or "fr"), "lang should be either en or fr"

def help(lang: str):
    """
        pre: lang est soit "en" ou "fr"
        post: print des info
    """
     
    print("\n" \
    "file <name>: specifies the name of a file that the tool should work with from now on\n" \
    "info: displays the number of lines and characters in the file\n" \
    "words: uses the file as a word list from now on\n" \
    "search <word>: determines if the word is present in the word list\n" \
    "sum <number1> ... <numbern>: calculates the sum of the specified numbers\n" \
    "avg <number1> ... <numbern>: calculates the average of the specified numbers\n" \
    "language: switches the language between French and English\n" \
    "exit: stops the tool\n" if lang == "en" else "\n" \
    "file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment\n" \
    "info: montre le nombre de lignes et de caractères du fichier\n" \
    "words: utilise le fichier comme liste de mots à partir de maintenant\n" \
    "search <word>: détermine si le mot est dans la liste de mots\n" \
    "sum <number1> ... <numbern>: calcule la somme des nombres spécifiés\n" \
    "avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés\n" \
    "language change langue entre français et anglais" \
    "exit: arrête l'outil\n")

assert not help(not "en" or "fr"), "lang should be either en or fr"