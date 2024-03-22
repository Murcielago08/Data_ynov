import numpy as np

# Exercice 1

np.random.seed(0)
ventes = np.random.randint(0, 1001, (12, 5))
print(ventes)

# Exercice 2

moyenne_ventes = np.mean(ventes, axis=0).astype(int)
# Average ?
# moyenne_ventes = np.average(ventes, axis=0).astype(int)
print(moyenne_ventes)

# Exercice 3

print(ventes[:, 0] > moyenne_ventes[0])
print(np.where(ventes[:, 0] > moyenne_ventes[0]))
print(np.where(ventes[:, 0] > moyenne_ventes[0])[0] + 1)

# Exercice 4

print(np.where(ventes[:, 1] > ventes[:, 2])[0] + 1)

# Exercice 5

total_ventes_par_produit = np.sum(ventes, axis=0)
print(total_ventes_par_produit)
print(np.argmax(total_ventes_par_produit))

# Exerice 6

mois_ventes_faibles = np.where(np.all(ventes < 500, axis=1))[0] + 1
print(mois_ventes_faibles)

# Exercice 7

augmentation_ventes = np.diff(ventes, axis=0) > 0
print(augmentation_ventes)

delta_ventes = np.diff(ventes, axis=0)
print(delta_ventes)

for i in range(delta_ventes.shape[1]):
    print(delta_ventes[:, i] > 0)
    mois_augmentation = np.where(delta_ventes[:, i] > 0)[0] + 2
    print(mois_augmentation)

# Exercice 8
    
variations_ventes = np.diff(ventes, axis=0) / ventes[:-1] * 100
print(variations_ventes)
tendance_moyenne = np.mean(variations_ventes, axis=0)
print(np.argmax(tendance_moyenne) + 1)
print(np.argmin(tendance_moyenne) + 1)

# Exercices 9
# DONNER LA CORRECTION


# BONUS

moyenne_mensuelle = np.mean(ventes, axis=1)

mois = np.arange(1, 13)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(mois, moyenne_mensuelle, marker="s", linestyle="--", color="blue", label="Moyenne des ventes")
plt.title("Moyenne des ventes mensuelles pour l'ensemble des produits")
plt.xlabel("Mois")
plt.ylabel("Moyenne des ventes")
plt.xticks(mois)
plt.legend()
plt.grid(True)
plt.show()