import numpy as np

# ndarray

# tableau_1d = np.array([1, 2, 3, 4, 5])
# print(tableau_1d)

# print(tableau_1d.ndim)

# tableau_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(tableau_2d)
# print(tableau_2d[1, 2])
# print(tableau_2d[1, -1])

# print(tableau_2d.shape)
# # >= 3 dimensions
#     # Tenseur

# for ligne in tableau_2d:
#     for el in ligne:
#         print(el)

# arr = np.zeros(10).astype(int)
# print(arr)

# arr2 = np.zeros(10).astype(int).astype(str)
# print(arr2)

# arr1 = np.ones(10)
# print(arr1)

# arr_full = np.zeros(shape=(10, 10))
# arr_full[3, 8] = 1
# print(arr_full)

# np.random.seed(99)

# arr_rnd = np.random.randint(10, 1000000, (1000, 1000000))
# print(arr_rnd[3, 99999])

np.random.seed(0)

arr_rnd = np.random.randint(0, 100, (10, 10))
print(arr_rnd)

# print(arr_rnd[-2: , -2:])

print(arr_rnd + 10)

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
print(arr.T)

print(np.min(arr_rnd))
print(np.max(arr_rnd))
print(np.sum(arr_rnd))
print(np.mean(arr_rnd))
print(np.median(arr_rnd))
print(np.std(arr_rnd))

