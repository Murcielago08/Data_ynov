from collections import deque
# from queue import PriorityQueue

# file_attente = {
#     1: deque(),
#     2: deque(),
#     3: deque(),
# }

def ajouter_demande(file_attente: deque, client, demande) -> None:
    file_attente.append((client, demande))
    return  file_attente

def traiter_demande(file_attente: deque) -> deque:
    if file_attente:
        demande_traitee = file_attente.popleft()
        # demande_traitee = file_attente[1:]
        print(f"Traitment de la demande de {demande_traitee[0]}: {demande_traitee[1]}")
        return file_attente
    else:
        print("La file d'attente est vide")
        return file_attente
    
def afficher_file_attente(file_attente: deque) -> None:
    if file_attente:
        print("Fille d'attente:")
        for i, (client, demande) in enumerate(file_attente, start=1):
            print(f"{i}. {client}: {demande}")
        else:
            print("La file d'attente est vide.")

file_attente = deque()
# file_attente = list()
file_attente = ajouter_demande(file_attente, "Alice", "Problème de connexion")
file_attente = ajouter_demande(file_attente, "Bob", "Mot de passe oublié")
file_attente = ajouter_demande(file_attente, "Charlie", "Problème de facturation")

afficher_file_attente(file_attente)
traiter_demande(file_attente)

file_attente = ajouter_demande(file_attente, "Jane", "Clavier QWERTY ????")

traiter_demande(file_attente)
afficher_file_attente(file_attente)