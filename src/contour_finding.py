import numpy as np
import matplotlib.pyplot as plt

from skimage import measure, io
from skimage.color import rgb2gray


image = io.imread("./images/geometry.png")

image_in_greyscale = rgb2gray(image)

# Find contours at a constant value of 0.8
contours = measure.find_contours(image_in_greyscale, 0.55)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(image_in_greyscale, cmap=plt.cm.gray)

for contour in contours:
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis("image")
ax.set_xticks([])
ax.set_yticks([])
plt.show()