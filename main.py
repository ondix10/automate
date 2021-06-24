# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import function

#from graphviz import Digraph, Source

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    print('Bienvenue dans Auto BERESA\n')
    print('Nous vous offrons plusieurs possibilités\n')
    print('1. Voir notre automate.')
    print('2. Voir notre automate deterministe.')
    print('3. Voir notre automate minimiser.')
    print('4. Tester reconnaissance mot.')
    print('5. Proposer son automate pour determinisation et minimisation.')

    decision = input()

    if int(decision) == 5:



        print('Entrer le nombre d\'etat que vous avez ?')
        print('NB:- Les etats sont en Chiffre.')
        nombreEtat = int(input())

        print('Entrer le nombre de transitions que vous avez ? sans le vide ')
        print('NB:- Les transitions en lettre minuscule \n')
        nombreTransition = int(input())

        print('Votre automate contient t-il le vide ε ?, repondez par oui ou non ')

        contientVide = input()

        i = 1

        listeTransition = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v",
            "w", "x", "y", "z"]
        if contientVide == "oui":
            listeTransition[nombreTransition] = "@"

        tableauAutomate = []
        while i <= nombreEtat:

            #graphe.node(str(i), str(i))

            j = 0
            tableauTransition = []

            if contientVide == "oui":
                while j <= nombreTransition:

                    stopBoucle = False
                    listeEtatRetenu = []
                    while stopBoucle == False:

                        print('Entrer l\'etat qui fini la transition ' + str(listeTransition[j]) + ' de l\'etat ' + str(
                            i))
                        print('Pour passer au suivant taper " - "')
                        reponseEtat = input()

                        if reponseEtat == "-":
                            if len(listeEtatRetenu) == 0:
                                listeEtatRetenu.append("-")

                            else:
                                print("go")

                            stopBoucle = True

                        elif (0 < int(reponseEtat) <= nombreEtat) or (reponseEtat == "0"):

                            if reponseEtat not in listeEtatRetenu:
                                listeEtatRetenu.append(reponseEtat)
                                #graphe.edge(str(i), str(reponseEtat), label=str(listeTransition[j]))

                            else:
                                print("Vous avez deja mis " + reponseEtat)


                        else:
                            print('Mauvais caractère choisis')
                    j = j + 1
                    tableauTransition.append(listeEtatRetenu)

            else:
                while j < nombreTransition:

                    stopBoucle = False
                    listeEtatRetenu = []
                    while stopBoucle == False:

                        print('Entrer l\'etat qui fini la transition ' + str(listeTransition[j]) + ' de l\'etat ' + str(
                            i))
                        print('Pour passer au suivant taper " - "')
                        reponseEtat = input()

                        if reponseEtat == "-":
                            if len(listeEtatRetenu) == 0:
                                listeEtatRetenu.append("-")

                            else:
                                print("go")

                            stopBoucle = True

                        elif (0 < int(reponseEtat) <= nombreEtat) or (reponseEtat == "0"):

                            if reponseEtat not in listeEtatRetenu:
                                listeEtatRetenu.append(reponseEtat)
                                #graphe.edge(str(i), str(reponseEtat), label=str(listeTransition[j]))

                            else:
                                print("Vous avez deja mis " + reponseEtat)


                        else:
                            print('Mauvais caractère choisis')
                    j = j + 1
                    tableauTransition.append(listeEtatRetenu)

            reponseInitial = False
            while reponseInitial == False:
                print('L\'etat ' + str(i) + ' est-il initial ?')
                print('Repondez par oui ou non ')
                reponseSurInitial = input()

                if reponseSurInitial == "oui":
                    decisionInitial = True
                    reponseInitial = True



                elif reponseSurInitial == "non":
                    decisionInitial = False
                    reponseInitial = True

                else:
                    print('Repondez uniquement par oui ou non ')

            reponseFinal = False

            while reponseFinal == False:
                print('L\'etat ' + str(i) + ' est-il Final ?')
                print('Repondez par oui ou non !')
                reponseSurFinal = input()

                if reponseSurFinal == "oui":
                    decisionFinal = True
                    reponseFinal = True

                elif reponseSurFinal == "non":
                    decisionFinal = False
                    reponseFinal = True

                else:
                    print('Repondez uniquement par oui ou non ')

            tableauAutomate.append({i: tableauTransition, "etatInitial": decisionInitial, "etatFinal": decisionFinal})

            i = i + 1

        print(tableauAutomate)
        # function.afficherAutomate2(tableauAutomate)

        #s = Source((graphe.source), filename="meka.gv", format="png")
        #s.view()
        print('L\'automate que vous avez entré vient de s\'afficher !')
        input("Appuyez sur entrée pour determiniser .\n")

        if function.detecterDeterminisation(tableauAutomate,nombreEtat):

            if contientVide == "oui":

                automateDeterminise = function.determinisationAvecEfermeture(tableauAutomate, int(nombreTransition))

                function.afficherAutomate(automateDeterminise)

            else:
                automateDeterminise = function.determinisationSansEfermeture(tableauAutomate, int(nombreTransition),
                                                                             int(nombreEtat))
                function.afficherAutomate(automateDeterminise)


        else:

            print('votre automate est deja deterministe')

    if int(decision) == 3:
        listeTransition = [
            "o", "n", "d", "i", "y", "b", "t", "a", "ε"]

        beresa = [

            {1: [['2'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': True, 'etatFinal': False},
            {2: [['-'], ['3'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['5']],
             'etatInitial': False, 'etatFinal': True},
            {3: [['-'], ['-'], ['4'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {4: [['-'], ['-'], ['-'], ['5'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {5: [['-'], ['-'], ['-'], ['-'], ['6'], ['-'], ['8'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {6: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['1']],
             'etatInitial': False, 'etatFinal': False},
            {7: [['-'], ['-'], ['-'], ['-'], ['-'], ['4'], ['-'], ['-'], ['-']],
             'etatInitial': True, 'etatFinal': False},
            {8: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['9'], ['1']],
             'etatInitial': False, 'etatFinal': False},
            {9: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': True},

        ]
        beresaMix = function.determinisationAvecEfermeture(beresa, 8,9)


        beresaMix2=function.transformerEnEntier(beresaMix)
        print(beresaMix2)
        """
        beresaMix3=function.inverserAutomate(beresaMix2,8)
        print(beresaMix3)
        beresaMix4 = function.determinisationSansEfermeture(beresaMix3, 8,9)
        beresaMix5=function.transformerEnEntier(beresaMix4)
        print(beresaMix5)
        beresaMix6 = function.inverserAutomate(beresaMix5, 8)
        print(beresaMix6)
        beresaMix7 = function.determinisationSansEfermeture(beresaMix6, 8, 9)

        beresaMix8 = function.transformerEnEntier(beresaMix7)
        print(beresaMix8)
        """


    if int(decision) == 2:
        listeTransition = [
            "o", "n", "d", "i", "y", "b", "t", "a", "ε"]

        beresa = [

            {1: [['2'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': True, 'etatFinal': False},
            {2: [['-'], ['3'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['5']],
             'etatInitial': False, 'etatFinal': True},
            {3: [['-'], ['-'], ['4'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': True},
            {4: [['-'], ['-'], ['-'], ['5'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {5: [['-'], ['-'], ['-'], ['-'], ['6'], ['-'], ['8'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {6: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['1']],
             'etatInitial': False, 'etatFinal': False},
            {7: [['-'], ['-'], ['-'], ['-'], ['-'], ['4'], ['-'], ['-'], ['-']],
             'etatInitial': True, 'etatFinal': False},
            {8: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['9'], ['1']],
             'etatInitial': False, 'etatFinal': False},
            {9: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': True},

        ]
        beresaMix = function.determinisationAvecEfermeture(beresa, 8,9)


        beresaMix2=function.transformerEnEntier(beresaMix)
        print(beresaMix2)
        beresaMix3=function.inverserAutomate(beresaMix2,8)
        print(beresaMix3)


    if int(decision) == 4:


        print("Entrer mot à reconnaitre")
        mot = input()
        listeTransitionModifie = [
            "o", "n", "d", "i", "y", "b", "t", "a", "ε"]

        beresa = [

            {1: [['2'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': True, 'etatFinal': False},
            {2: [['-'], ['3'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['5']],
             'etatInitial': False, 'etatFinal': True},
            {3: [['-'], ['-'], ['4'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': True},
            {4: [['-'], ['-'], ['-'], ['5'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {5: [['-'], ['-'], ['-'], ['-'], ['6'], ['-'], ['8'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {6: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['1']],
             'etatInitial': False, 'etatFinal': False},
            {7: [['-'], ['-'], ['-'], ['-'], ['-'], ['4'], ['-'], ['-'], ['-']],
             'etatInitial': True, 'etatFinal': False},
            {8: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['9'], ['1']],
             'etatInitial': False, 'etatFinal': False},
            {9: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': True},

        ]
        autoMate = function.determinisationAvecEfermeture(beresa, 8,9)


        listeEtatSorti=[]
        for ligne in autoMate:

            for etat in ligne:

                try:

                    if type(int(etat)) is int:

                        if ligne['final']:
                            listeEtatSorti.append(etat)

                        if ligne['initial']:
                            etatAvant=etat
                except:
                    continue

        caractere=0

        #print(function.reconnaitreMot(etatAvant, caractere, autoMate, mot, listeEtatSorti))
        if function.reconnaitreMot(etatAvant, caractere, autoMate, mot, listeEtatSorti):

            print('mot reconnu')
        else:
            print('mot non reconnu')

    if int(decision) == 1:
        listeTransition = [
            "o", "n", "d", "i", "y", "b", "t", "a", "ε"]

        beresa = [

            {1: [['2'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': True, 'etatFinal': False},
            {2: [['-'], ['3'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['5']],
             'etatInitial': False, 'etatFinal': True},
            {3: [['-'], ['-'], ['4'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': True},
            {4: [['-'], ['-'], ['-'], ['5'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {5: [['-'], ['-'], ['-'], ['-'], ['6'], ['-'], ['8'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': False},
            {6: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['1']],
             'etatInitial': False, 'etatFinal': False},
            {7: [['-'], ['-'], ['-'], ['-'], ['-'], ['4'], ['-'], ['-'], ['-']],
             'etatInitial': True, 'etatFinal': False},
            {8: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['9'], ['1']],
             'etatInitial': False, 'etatFinal': False},
            {9: [['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-']],
             'etatInitial': False, 'etatFinal': True},

        ]
        function.afficherAutomate2(beresa)


