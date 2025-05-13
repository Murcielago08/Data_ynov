import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# image_rgb = np.random.rand(100, 100, 3).round(2)
# print(image_rgb)


# image_rgb_2 = image_rgb.copy()
# image_rgb_2[0, 2, :] = 0

# # print(image_rgb == image_rgb_2)
# # print(np.where(image_rgb != image_rgb_2))
# # indices = np.where(image_rgb != image_rgb_2)

# # print(f"Pixel différent détecté : ligne: {indices[0]}")

img = mpimg.imread("./img1.png")
print(img)

# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         if (i + j) % 2 == 0:
#             img[i, j] = 0

r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
img_gray = r * 0.2989 + g * 0.5870 + b * 0.1140

# plt.imshow(img)
# plt.title("Image aléatoire en couleurs")
# plt.axis(False)
# plt.show()

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Image originale")

plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap="gray")
plt.title("Niveaux de gris")

plt.show()