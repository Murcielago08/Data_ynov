import numpy as np

# tab_A = np.array([[1, 2], [3, 4]])
# print(tab_A)

# print(tab_A == 2)
# print(tab_A > np.mean(tab_A))

# print(np.logical_or(tab_A == 2, tab_A == 3))
# print(np.logical_and(tab_A > 1, tab_A < 4))

# filtre = [[True, False], [False, True]]

# print(tab_A[filtre])

rnd_A = np.random.randint(0, 100, (10, 10))
print(rnd_A)

print(rnd_A[np.logical_and(rnd_A > 45, rnd_A < 50)])

indices = np.where(np.logical_and(rnd_A > 45, rnd_A < 50))
print(indices)

# print(rnd_A[indices[0][2]][indices[1][2]])

data = np.array([[1, 1, 1],
                 [1, 1, 1],
                 [1, 0, 1]])
print(data)
print(np.all(data == 1))
print(np.any(data == 0))

ventes = np.random.randint(1, 200, 7)
print(ventes)
print(np.diff(ventes))