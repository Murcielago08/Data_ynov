pays = [None] * 100
print(pays)

from hash import fonction_hachage

pays[fonction_hachage("FR") % len(pays)] = "France"
print(pays)
print(pays[fonction_hachage("FR") % len(pays)])

pays[fonction_hachage("AZ") % len(pays)] = "Afrique du Sud"
print(pays)
print(pays[fonction_hachage("AZ") % len(pays)])

pays[fonction_hachage("BE") % len(pays)] = "Belgique"
print(pays)
print(pays[fonction_hachage("AZ") % len(pays)])

