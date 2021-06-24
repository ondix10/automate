import copy
import itertools


# from graphviz import Digraph, Source


def detecterDeterminisation(automateEnvoye, nombreEtat):
    detectionDet = False
    counterEtatInitial = 0
    for ligne in automateEnvoye:

        for colonne in ligne:
            if colonne == "etatInitial":
                if ligne[colonne] == True:
                    counterEtatInitial = counterEtatInitial + 1

            i = 1
            while i <= nombreEtat:

                if i == colonne:

                    for cellule in ligne[i]:

                        if len(cellule) > 1:
                            detectionDet = True
                        for element in cellule:

                            if element == "@":
                                detectionDet = True

                i = i + 1

    if counterEtatInitial > 1:
        detectionDet = True

    return detectionDet


def appliquerEFermetureEtatInitiaux(lesEtats, automate, indiceEFermeture):
    retourFinal = []

    for etat in lesEtats:

        for ligne in automate:

            for colonne in ligne:

                if colonne != 'etatInitial' and colonne != 'etatFinal':
                    if type(int(colonne)) is int:

                        if str(colonne) == etat:

                            for etatTransition in ligne[colonne][indiceEFermeture]:

                                if etatTransition != '-':
                                    if etat not in retourFinal:
                                        retourFinal.append(etat)
                                    if etatTransition not in retourFinal:
                                        retourFinal.append(etatTransition)
                                else:
                                    if etat not in retourFinal:
                                        retourFinal.append(etat)
    if not retourFinal:
        retourFinal.append('-')

    return retourFinal


def mesTransitions(nombreTransition, lesEtats, automate):
    retourFinal = {}

    for etat in lesEtats:

        for ligne in automate:
            ligneTrouve = False

            for colonne in ligne:
                if colonne == int(etat):
                    ligneTrouve = True

            if ligneTrouve == True:

                i = 0

                for element in ligne[int(etat)]:

                    j = 0
                    while j < nombreTransition:

                        if i == j:

                            if i in retourFinal:

                                retourFinal[i] = retourFinal[i] + element

                            else:
                                retourFinal[i] = element

                        j = j + 1

                    i = i + 1

    # Effacer doublons

    for cle in retourFinal:
        retourFinal[cle] = list(set(retourFinal[cle]))

    # suppression - au cas ou d'autres etat existe

    for cle in retourFinal:

        if len(retourFinal[cle]) != 1 and '-' in retourFinal[cle]:
            retourFinal[cle].remove('-')

    # triage du plus petit au plus grand

    for cle in retourFinal:
        newElement = []
        elementMieux = []
        if '-' not in retourFinal[cle]:
            for element in retourFinal[cle]:
                newElement.append(int(element))

            for element in sorted(newElement):
                elementMieux.append(str(element))

            retourFinal[cle] = elementMieux

    return retourFinal


def appliquerEfermeture(lesEtats, automate, indiceEFermeture):
    retourFinal = {}

    for etat in lesEtats:

        for info in lesEtats[etat]:

            for ligne in automate:

                for colonne in ligne:

                    if colonne != 'etatInitial' and colonne != 'etatFinal':
                        if type(int(colonne)) is int:

                            if str(colonne) == info:

                                # print(ligne[colonne][indiceEFermeture])

                                for etatTransition in ligne[colonne][indiceEFermeture]:

                                    if etatTransition != '-':

                                        if etat in retourFinal:

                                            # print(etatTransition)
                                            retourFinal[etat] = retourFinal[etat] + info
                                            retourFinal[etat] = retourFinal[etat] + etatTransition

                                            print(retourFinal)



                                        else:
                                            retourFinal[etat] = etatTransition

                                            # print(retourFinal[etat])



                                    else:
                                        retourFinal[etat] = info

    # Effacer doublons

    for cle in retourFinal:
        retourFinal[cle] = list(set(retourFinal[cle]))

    # suppression - au cas ou d'autres etat existe

    for cle in retourFinal:

        if len(retourFinal[cle]) != 1 and '-' in retourFinal[cle]:
            retourFinal[cle].remove('-')

    # triage du plus petit au plus grand

    for cle in retourFinal:
        newElement = []
        elementMieux = []
        if '-' not in retourFinal[cle]:
            for element in retourFinal[cle]:
                newElement.append(int(element))

            for element in sorted(newElement):
                elementMieux.append(str(element))

            retourFinal[cle] = elementMieux

    for etat in lesEtats:

        for info in retourFinal:

            if etat == info:
                retourFinal[info] = retourFinal[info] + lesEtats[etat]

    return retourFinal


def mesTransitionsAvecEFermeture(nombreTransition, lesEtats, automate):
    retourFinal = {}

    for etat in lesEtats:

        for ligne in automate:
            ligneTrouve = False

            for colonne in ligne:
                if colonne == int(etat):
                    ligneTrouve = True

            if ligneTrouve == True:

                i = 0

                for element in ligne[int(etat)]:

                    j = 0
                    while j < nombreTransition:

                        if i == j:

                            if i in retourFinal:

                                retourFinal[i] = retourFinal[i] + element

                            else:
                                retourFinal[i] = element

                        j = j + 1

                    i = i + 1

    # Effacer doublons

    for cle in retourFinal:
        retourFinal[cle] = list(set(retourFinal[cle]))

    # suppression - au cas ou d'autres etat existe

    for cle in retourFinal:

        test = False
        if len(retourFinal[cle]) != 1 and '-' in retourFinal[cle]:
            retourFinal[cle].remove('-')

    # triage du plus petit au plus grand

    # print(retourFinal)
    # print('avant')

    # print(retourFinal)

    for transition in retourFinal:
        retourFinal[transition] = appliquerEFermetureEtatInitiaux(retourFinal[transition], automate, nombreTransition)

    # Effacer doublons

    for cle in retourFinal:
        retourFinal[cle] = list(set(retourFinal[cle]))

    for cle in retourFinal:
        newElement = []
        elementMieux = []

        if '-' not in retourFinal[cle]:
            for element in retourFinal[cle]:
                newElement.append(int(element))

            for element in sorted(newElement):
                elementMieux.append(str(element))

            retourFinal[cle] = elementMieux

    # suppression - au cas ou d'autres etat existe

    try:
        for cle in retourFinal:

            if len(retourFinal[cle]) != 1 and '-' in retourFinal[cle]:

                for ceci in retourFinal[cle]:
                    retourFinal.remove('-')
    except:
        pass

    return retourFinal


def determinisationSansEfermeture(automateNonDeterministe, nombreTransition, nombreEtat):
    nouveauAutomate = {}

    etatInitiaux = []
    etatFinaux = []

    for ligne in automateNonDeterministe:
        validationInitial = validationInitial2 = False
        for colonne in ligne:
            if colonne == "etatInitial":

                if ligne[colonne] == True:
                    validationInitial = True

            if colonne == "etatFinal":
                if ligne[colonne] == True:
                    validationInitial2 = True

        if validationInitial:
            for colonne in ligne:
                if type(colonne) is int:
                    etatInitiaux.append(str(colonne))
        if validationInitial2:
            for colonne in ligne:
                if type(colonne) is int:
                    etatFinaux.append(str(colonne))

    nouveauAutomate["".join(etatInitiaux)] = mesTransitions(nombreTransition, etatInitiaux, automateNonDeterministe)

    lesNewEtat = []

    lesEtat = []

    i = 1
    while i <= nombreEtat:
        lesEtat.append(str(i))
        i = i + 1

    for l in range(1, len(lesEtat) + 1):
        for element in itertools.combinations(lesEtat, l):
            lesNewEtat.append("".join(element))

    for nouveauEtat in lesNewEtat:

        if nouveauEtat not in nouveauAutomate:
            nouveauAutomate[nouveauEtat] = mesTransitions(nombreTransition, transformerEnListe(nouveauEtat),
                                                          automateNonDeterministe)

    for element in nouveauAutomate:
        nouveauAutomate[element]['etatInitial'] = False
        nouveauAutomate[element]['etatFinal'] = False

    # nouveauEtat

    for element in nouveauAutomate:

        if element == "".join(etatInitiaux):
            nouveauAutomate[element]['etatInitial'] = True

    # trouve les nouveaux etat finaux
    nouveauEtatFinaux = []
    for etat in etatFinaux:

        for element in nouveauAutomate:

            if etat in transformerEnListe(element):
                nouveauAutomate[element]['etatFinal'] = True
                nouveauEtatFinaux.append(element)

    listeEtatRetenu = []
    listeEtatRetenu.append("".join(etatInitiaux))
    etatRetour = []
    etatTraite = ("".join(etatInitiaux)).split()

    i = 0
    while etatTraite:

        etatRetour = mesNouveauxAlies(etatTraite, nouveauAutomate, nombreTransition, listeEtatRetenu)

        for etatRecu in etatRetour:
            listeEtatRetenu.append(etatRecu)

        etatTraite = etatRetour
        i = i + 1
    #listeEtatRetenu.remove('-')

    automateFinal = {}

    for etat in nouveauAutomate:

        if etat in listeEtatRetenu:
            automateFinal[etat] = nouveauAutomate[etat]

    # La forme comme celui d'avant

    automateFinalMaxProLoL = []

    for etat in listeEtatRetenu:

        uneLigne = {}

        for ligneAncien in automateFinal:

            if etat == ligneAncien:
                transition = []
                initial = False
                final = False
                i = 0
                while i < nombreTransition:
                    transition.append("".join(automateFinal[ligneAncien][i]))
                    i = i + 1
                initial = automateFinal[ligneAncien]["etatInitial"]
                final = automateFinal[ligneAncien]["etatFinal"]
        uneLigne[etat] = transition
        uneLigne['initial'] = initial
        uneLigne['final'] = final

        automateFinalMaxProLoL.append(uneLigne)

        # automateFinalMaxProAmeliorer=[]

        # i=j=0

    #print(automateFinalMaxProLoL)

    return automateFinalMaxProLoL


def determinisationAvecEfermeture(automateNonDeterministe, indiceETransition, nombreEtat):
    """

    initialisation des variables
    Notre Automate Non deterministe:param automateNonDeterministe:
    Nombre d'etiquete sans epsilon:param indiceETransition:
    Automate determiniser:return:
    """
    nouveauAutomate = {}

    nombreEtiquette = indiceETransition
    etatInitiaux = []
    etatFinaux = []

    """
    Recuperation des etat initiaux et finaux
    """

    for ligne in automateNonDeterministe:
        validationInitial = validationInitial2 = False
        for colonne in ligne:
            if colonne == "etatInitial":

                if ligne[colonne] == True:
                    validationInitial = True

            if colonne == "etatFinal":
                if ligne[colonne] == True:
                    validationInitial2 = True

        if validationInitial:
            for colonne in ligne:
                if type(colonne) is int:
                    etatInitiaux.append(str(colonne))
        if validationInitial2:
            for colonne in ligne:
                if type(colonne) is int:
                    etatFinaux.append(str(colonne))
    """
    Application de la E Fermeture pour avoir, un nouveau Etat initial
   
    """
    etatInitiaux = appliquerEFermetureEtatInitiaux(etatInitiaux, automateNonDeterministe, nombreEtiquette)
    nouveauAutomate["".join(etatInitiaux)] = mesTransitionsAvecEFermeture(nombreEtiquette, etatInitiaux,
                                                                          automateNonDeterministe)

    lesNewEtat = []

    lesEtat = []

    i = 1
    while i <= nombreEtat:
        lesEtat.append(str(i))
        i = i + 1

    for l in range(1, len(lesEtat) + 1):
        for element in itertools.combinations(lesEtat, l):
            lesNewEtat.append("".join(element))

    for nouveauEtat in lesNewEtat:

        if nouveauEtat not in nouveauAutomate:
            nouveauAutomate[nouveauEtat] = mesTransitionsAvecEFermeture(nombreEtiquette,
                                                                        transformerEnListe(nouveauEtat),
                                                                        automateNonDeterministe)

    for element in nouveauAutomate:
        nouveauAutomate[element]['etatInitial'] = False
        nouveauAutomate[element]['etatFinal'] = False

    # nouveauEtat

    for element in nouveauAutomate:
        # print(nouveauAutomate[element])

        if element == "".join(etatInitiaux):
            nouveauAutomate[element]['etatInitial'] = True

    # trouve les nouveaux etat finaux
    nouveauEtatFinaux = []
    for etat in etatFinaux:

        for element in nouveauAutomate:

            if etat in transformerEnListe(element):
                nouveauAutomate[element]['etatFinal'] = True
                nouveauEtatFinaux.append(element)

    listeEtatRetenu = []
    listeEtatRetenu.append("".join(etatInitiaux))
    etatRetour = []
    etatTraite = ("".join(etatInitiaux)).split()
    # print(etatTraite)

    # i = 0
    while etatTraite:

        # print(etatTraite)
        etatRetour = mesNouveauxAlies(etatTraite, nouveauAutomate, nombreEtiquette, listeEtatRetenu)

        for etatRecu in etatRetour:
            # print(etatRecu)
            listeEtatRetenu.append(etatRecu)

        etatTraite = etatRetour
        # i = i + 1

    # listeEtatRetenu.remove('-')
    # print(listeEtatRetenu)

    # print(nouveauAutomate)

    automateFinal = {}

    for etat in nouveauAutomate:

        if etat in listeEtatRetenu:
            automateFinal[etat] = nouveauAutomate[etat]

    # La forme comme celui d'avant

    automateFinalMaxProLoL = []
    # print(automateFinal)
    # print(listeEtatRetenu)
    for etat in listeEtatRetenu:

        uneLigne = {}

        for ligneAncien in automateFinal:

            # print(ligneAncien)
            if etat == ligneAncien:

                transition = []
                initial = False
                final = False
                i = 0
                while i < nombreEtiquette:
                    try:
                        transition.append("".join(automateFinal[ligneAncien][i]))
                    except:
                        pass
                    i = i + 1
                initial = automateFinal[ligneAncien]["etatInitial"]
                final = automateFinal[ligneAncien]["etatFinal"]
        # print(etat)
        uneLigne[etat] = transition
        uneLigne['initial'] = initial
        uneLigne['final'] = final

        automateFinalMaxProLoL.append(uneLigne)

    """
    i= 0
    for ligne in automateFinalMaxProLoL:
        supprimer =False
        for element in ligne:
            if element=='-':
                supprimer =True

        if supprimer:
            del (automateFinalMaxProLoL[i])
        i=i+1
    """
    return automateFinalMaxProLoL


def transformerEnListe(mot):
    listeRetour = []
    for i in mot:
        listeRetour.append(i)
    return listeRetour


def mesNouveauxAlies(etatTraite, automate, nombreTransition, listeEtatRetenu):
    resultat = []

    # print(etatTraite)
    for etatPresent in etatTraite:
        # print(etatPresent)

        for etat in automate:

            if etat == etatPresent:

                i = 0
                while i < nombreTransition:

                    for info in automate[etat]:
                        # print(automate[etat])

                        if info == i:
                            # print(info)
                            if "-" not in automate[etat][info]:
                                if "".join(automate[etat][info]) not in listeEtatRetenu:
                                    # print("".join(automate[etat][info]))
                                    resultat.append("".join(automate[etat][info]))
                    i = i + 1

    return resultat


"""
def afficherAutomate(automate):
    listeTransition = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
        "v",
        "w", "x", "y", "z")

    graphe2 = Digraph(comment='L\'automate deterministe')

    for ligne in automate:

        for etat in ligne:

            try:

                if type(int(etat)) is int:

                    if ligne['final']:
                        graphe2.attr('node', shape='doublecircle')
                        graphe2.node(etat, etat)
                    else:
                        graphe2.attr('node', shape='circle')
                        graphe2.node(etat, etat)



            except:
                continue
    dejaAfficher = []
    for ligne in automate:

        for etat in ligne:
            final = False
            try:

                if type(int(etat)) is int:

                    i = 0
                    for element in ligne[etat]:
                        if element != '-':

                            if str(etat) + str(listeTransition[i]) + str(element) not in dejaAfficher:
                                graphe2.edge(etat, str(element), label=str(listeTransition[i]))
                                dejaAfficher.append(str(etat) + str(listeTransition[i]) + str(element))

                        i = i + 1


            except:
                continue

    s = Source((graphe2.source), filename="meka.gv", format="png")
    s.view()


def afficherAutomate2(automate):
    listeTransition = [
        "o", "n", "d", "i", "y", "b", "t", "a", "ε"]

    graphe2 = Digraph(comment='L\'automate deterministe')

    for ligne in automate:

        for etat in ligne:

            try:

                if type(int(etat)) is int:

                    if ligne['etatFinal']:
                        graphe2.attr('node', shape='doublecircle', color='red')
                        graphe2.node(str(etat), str(etat))

                    if ligne['etatInitial']:
                        graphe2.attr('node', shape='Mdiamond', color='green')
                        graphe2.node(str(etat), str(etat))

                    if ligne['etatInitial'] == True and ligne['etatFinal'] == True:
                        graphe2.attr('node', shape='doublecircle', color='green')
                        graphe2.node(str(etat), str(etat))

                    if ligne['etatFinal'] == False and ligne['etatInitial'] == False:
                        graphe2.attr('node', shape='circle', color='gray')
                        graphe2.node(str(etat), str(etat))




            except:
                continue
    dejaAfficher = []
    for ligne in automate:

        for etat in ligne:
            final = False
            try:

                if type(int(etat)) is int:

                    for element in ligne[etat]:

                        for info in element:

                            if info != '-':
                                graphe2.edge(str(etat), str(info),
                                             label=str(listeTransition[ligne[etat].index(element)]))



            except:
                continue

        # print('_____________')
    s = Source((graphe2.source), filename="meka.gv", format="png")
    s.view()


def afficherAutomate3(automate):
    listeTransition = [
        "o", "n", "d", "i", "y", "b", "t", "a", "ε"]

    graphe2 = Digraph(comment='L\'automate deterministe')

    for ligne in automate:

        for etat in ligne:

            try:

                if type(int(etat)) is int:

                    if ligne['final']:
                        graphe2.attr('node', shape='doublecircle')
                        graphe2.node(etat, etat)
                    else:
                        graphe2.attr('node', shape='circle')
                        graphe2.node(etat, etat)



            except:
                continue
    dejaAfficher = []
    for ligne in automate:

        for etat in ligne:
            final = False
            try:

                if type(int(etat)) is int:

                    i = 0
                    for element in ligne[etat]:
                        if element != '-':

                            if str(etat) + str(listeTransition[i]) + str(element) not in dejaAfficher:
                                graphe2.edge(etat, str(element), label=str(listeTransition[i]))
                                dejaAfficher.append(str(etat) + str(listeTransition[i]) + str(element))

                        i = i + 1


            except:
                continue
 
    s = Source((graphe2.source), filename="meka.gv", format="png")
    s.view()

"""


def minimiserAutomate(automate):
    automateMinimal = []

    automate = [{'1': ['2', '7'], "initial": True, "final": False},
                {'2': ['4', '2'], "initial": False, "final": False},
                {'3': ['1', '4'], "initial": False, "final": False},
                {'4': ['7', '6'], "initial": False, "final": False},
                {'5': ['3', '11'], "initial": False, "final": False},
                {'6': ['4', '-'], "initial": False, "final": True},
                {'7': ['5', '10'], "initial": False, "final": False},
                {'8': ['10', '8'], "initial": False, "final": True},
                {'9': ['8', '4'], "initial": False, "final": False},
                {'10': ['11', '-'], "initial": False, "final": True},
                {'11': ['9', '4'], "initial": False, "final": False},
                {'12': ['2', '-'], "initial": False, "final": True},
                ]

    etatTerminaux = []
    etatNonTerminaux = []

    # etatTerminaux

    for ligne in automate:

        for info in ligne:

            try:
                if type(int(info)) is int:

                    if ligne['final'] == True:
                        etatTerminaux.append(info)

            except:
                continue

    # etatNonTerminaux

    for ligne in automate:

        for info in ligne:

            try:
                if type(int(info)) is int:

                    if info not in etatTerminaux:
                        etatNonTerminaux.append(info)

            except:
                continue

    #print(etatTerminaux)

    #print(etatNonTerminaux)

    # division successive des terminaux
    groupeATraiter = etatTerminaux

    divisionGroupeEnSousGroupe(groupeATraiter, automate, etatTerminaux, etatNonTerminaux)

    # division successive de non terminaux

    return automateMinimal


def divisionGroupeEnSousGroupe(groupeElement, automate, terminaux, nonTerminaux):
    groupeRetour = []

    # for element in groupeElement:

    # for ligne in automate:

    return groupeRetour


def sonEtaSorti(avant, caractere, automate, mot):
    etatSorti = None
    listeTransition = ["o", "n", "d", "i", "y", "b", "t", "a", "ε"]
    if mot[caractere] not in listeTransition:
        etatSorti = None

    else:

        position = listeTransition.index(mot[caractere])

        for ligne in automate:

            for element in ligne:

                try:
                    if element == avant:
                        if ligne[element][int(position)] != '-':
                            etatSorti = ligne[element][int(position)]

                except:
                    continue

    return etatSorti


def reconnaitreMot(etatAvant, caractere, automate, mot, listeEtatSorti):
    decision = False

    if caractere + 1 == len(mot):

        if sonEtaSorti(etatAvant, caractere, automate, mot) in listeEtatSorti:

            decision = True

        else:
            decision = False

    else:

        prochainEtatAvant = sonEtaSorti(etatAvant, caractere, automate, mot)
        if reconnaitreMot(prochainEtatAvant, caractere + 1, automate, mot, listeEtatSorti):
            decision = True

    return decision


def transformerEnEntier(automate):
    automateRetour = []

    i = 1
    listeEtat = []
    for ligne in automate:

        for element in ligne:

            try:

                if type(int(element)) is int:
                    listeEtat.append(element)

            except:
                continue

    for etat in listeEtat:

        for ligne in automate:

            for element in ligne:

                try:
                    if type(int(element)) is int:

                        for info in ligne[element]:
                            if info == etat:
                                ligne[element][ligne[element].index(info)] = str(listeEtat.index(etat) + 1)


                except:
                    continue

    i = 1
    for ligne in automate:
        uneLigne = {}

        for element in ligne:

            try:
                if type(int(element)) is int:

                    transition = []
                    for info in ligne[element]:
                        transition.append(info.split())

                    uneLigne[i] = transition

            except:
                pass
            if element == "initial":
                uneLigne['etatInitial'] = ligne[element]
            if element == "final":
                uneLigne['etatFinal'] = ligne[element]
        i = i + 1

        automateRetour.append(uneLigne)

    return automateRetour


def inverserAutomate(automate,nombreEtiquette):
    automateRetour = []

    listeEtats=[]
    for ligne in automate:

        for element in ligne:

            try:

                if type(int(element)) is int:
                    listeEtats.append(element)

            except:
                continue





    for etat in listeEtats:
        i = 0
        uneLigne = {}
        inversion=[]
        while i < nombreEtiquette:

            inversion.append(['-'])
            i=i+1

        for ligne in automate:


            for element in ligne:

                try:

                    if type(int(element)) is int:

                        for info in ligne[element]:
                            if '-' not in info:

                                if str(etat) in info:


                                    inversion[ligne[element].index(info)].append(str(element))


                except:
                    continue

        uneLigne[etat] = inversion

        for ligne in automate:


            for element in ligne:

                if etat == element:

                    uneLigne['etatInitial']=False

                    uneLigne['etatFinal']=False

        for ligne in automate:


            for element in ligne:

                if etat == element:
                    if ligne['etatInitial']:
                        uneLigne['etatInitial']=False
                        uneLigne['etatFinal'] = True

                    if ligne['etatFinal']:
                        uneLigne['etatFinal']=False
                        uneLigne['etatInitial'] = True






        automateRetour.append(uneLigne)



    for cle in automateRetour:
        #print(cle)

        for element in cle:

            try:
                if type(element) is int:
                    for info in cle[element]:

                        if len(info) != 1 and '-' in info:
                            info.remove('-')
            except:
                continue





    return automateRetour
