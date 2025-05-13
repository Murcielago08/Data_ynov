# Générer une série (1d) qui représente un nombre aléatoire de ventes de livres (entre 50 et 100 ventes) sur la semaine passée.
    # Les prix situés entre 7€ et 35€
    # Ils se terminent toujours par 0ct ou 50ct

# Calculer la moyenne des ventes
# Calculer la médiane des ventes
# Calculer l'écart-type des ventes

import numpy as np

np.random.seed(0)

ventes = np.random.choice(np.arange(7, 35.5, 0.5), size=np.random.randint(50, 100))

print(ventes)
print(ventes.shape)

print(np.sum(ventes))
print(np.mean(ventes).round(2))
print(np.median(ventes).round(2))
print(np.std(ventes).round(2))