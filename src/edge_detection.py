import numpy as np
import matplotlib.pyplot as plt

from skimage import filters
from skimage.data import camera, astronaut
from skimage.util import compare_images


image = camera()
edge_roberts = filters.roberts(image)
edge_sobel = filters.sobel(image)

fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

axes[0].imshow(edge_roberts, cmap=plt.cm.gray)
axes[0].set_title("Roberts Edge Detection")

axes[1].imshow(edge_sobel, cmap=plt.cm.gray)
axes[1].set_title("Sobel Edge Detection")

for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.show()