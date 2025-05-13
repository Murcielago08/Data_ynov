def fonction_hachage(chaine):
    return sum(ord(caractere) for caractere in chaine)

if __name__ == "__main__":

    # index 0, 1, 2 ...
    pays = ["Afghanistan", "Afrique du Sud", "Allemagne", "Belgique", "Estonie"]
    code = ["AF", "AZ"]


    # AF Afghanistan
    # AZ Afrique du Sud
    # DE Allemagne
    # BE Belgique
    # EE Estonie

    # Fonction de hachage
        # Hashcode

    print(fonction_hachage("NOEL"))
    print(fonction_hachage("LEON"))

    # Exercice
        # Classe Student
            # prenom
            # nom
            # date de naissance "dd/mm/yyyy" 26/07/1985
        # méthode hash
            # hashcode -> entier

    class Student:
        def __init__(self, prenom, nom, dn) -> None:
            self.prenom = prenom
            self.nom = nom
            self.dn = dn

        def hash(self):
            hash = 0
            hash += fonction_hachage(self.prenom)
            hash += fonction_hachage(self.nom)
            hash += sum(int(chiffre) for chiffre in self.dn.replace("/", ""))
            return hash

    student1 = Student("Leon", "Duval", "12/06/1998")
    student2 = Student("Leon", "Duval", "12/06/1998")
    print(student1.hash())
    print(student2.hash())

    student3 = Student("Noel", "Valud", "19/08/1962")
    print(student3.hash())
    student4 = Student("Amy", "Doning", "29/12/1997")
    print(student4.hash())

    # print(hash(student3))
    # print(hash(student4))

    from hashlib import md5

    print(md5("ZEKREZLKREZMLKREZMRKLEZRKM".encode()).hexdigest())
    print(md5("MSQLDKQSLKDQSLKQSDKLK".encode()).hexdigest())
