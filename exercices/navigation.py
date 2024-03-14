# pile -> stack
    # LIFO

    # push : Ajouter sur la pile
    # pop : Retirer et renvoyer
    # peek : lire le dernier

# def valider_parentheses(chaine):
#     stack = []
#     for char in chaine:
#         if char == "(":
#             stack.append(chaine)
#         elif char == ")":
#             if not stack or stack[-1] != "(":
#                     return False
#             stack.pop()
#     return len(stack) == 1

historique = []
pagesRetour = []

def visiter(url):
    print(f"Visite : {url}")
    historique.append(url)
    pagesRetour.clear()

def retour() -> str:
    if len(historique) > 1:
        pagesRetour.append(historique.pop())
        return historique[-1]
    else:
        return None

def avant() -> str:
    if pagesRetour:
        historique.append(pagesRetour.pop())
    else:
        return None

def afficher_historique() -> None:
    print(f" -> Historique de navigation : {historique}")
    print(f" -> Pages disponibles pour un retour en avant : {pagesRetour}")


visiter("page1.com")
visiter("page2.com")
visiter("page3.com")
afficher_historique()
retour()
retour()
afficher_historique()
visiter("page4.com")
afficher_historique()