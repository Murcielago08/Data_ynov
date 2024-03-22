# ICI FO CODé
import numpy as np

#Ex 1
np.random.seed(0)
ventes = np.random.randint(0, 1000, (12, 5))
print(ventes, "\n")

#Ex 2
moyenne_ventes = np.mean(ventes, axis=0).round(2)
print(moyenne_ventes, "\n")

#Ex 3
print(ventes[:, 0] > moyenne_ventes[0])
print(np.where(ventes[:, 0] > moyenne_ventes[0]))
print(np.where(ventes[:, 0] > moyenne_ventes[0])[0] + 1, "\n")

#Ex 4
print(np.where(ventes[:, 1] > ventes[:, 2])[0] + 1, "\n")

#Ex 5
tot = np.sum(ventes, axis=0)
print(tot)
print(np.argmax(tot), "\n")

#Ex 6
mois_ventes_faible = np.where(np.all(ventes < 500, axis=1))[0]+1
print(mois_ventes_faible, "\n")

#Ex 7
augmentation_ventes = np.diff(ventes, axis=0) > 0
print(augmentation_ventes)

deltas_ventes = np.diff(ventes, axis=0)
print(deltas_ventes)

for i in range(deltas_ventes.shape[1]):
    print(deltas_ventes[:, i] > 0)
    mois_aug = np.where(deltas_ventes[:, i] > 0)[0] + 2
    print(mois_aug)

#Ex 8

#Ex 9

# Bonus

moyenne_mensuelle = np.mean(ventes, axis=1)

mois = np.arange(1, 13)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(mois, moyenne_mensuelle, marker="s", linestyle="--", color="blue", label="Moyenne des ventes")
plt.title("Moyenne des ventes mensuelle pour l'ensemble des produits")
plt.xlabel("Mois")
plt.ylabel("Moyenne des ventes")
plt.xticks(mois)
plt.legend()
plt.grid(True)
plt.show()