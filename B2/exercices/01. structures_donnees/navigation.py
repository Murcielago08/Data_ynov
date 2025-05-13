historique = []
pagesRetour = []

def visiter(url):
    global historique, pagesRetour
    print(f"Visite: {url}")
    historique.append(url)
    pagesRetour.clear()

def retour():
    if len(historique) > 1:
        pagesRetour.append(historique.pop())
    else:
        print("Pas de page précédente")

def avant():
    if pagesRetour:
        historique.append(pagesRetour.pop())
        print(f"Aller à {historique[-1]}")
    else:
        print("Pas de page suivante")

def afficher_historique():
    print(f"  - Historique: {historique}")
    print(f"  - Pages dispo pour un retour en avant: {pagesRetour}")

visiter("page1.com")
visiter("page2.com")
visiter("page3.com")
afficher_historique()
retour()
retour()
afficher_historique()
avant()
afficher_historique()
visiter("page4.com")
afficher_historique()
