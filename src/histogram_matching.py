import matplotlib.pyplot as plt

from skimage import data, io
from skimage import exposure
from skimage.exposure import match_histograms

reference = io.imread("./images/city.jpg")
image = io.imread("./images/landscape.jpg")

matched = match_histograms(image, reference, multichannel=True)

fig, (ax1, ax2, ax3) = plt.subplots(
    nrows=1, ncols=3, figsize=(8, 3), sharex=True, sharey=True
)
for aa in (ax1, ax2, ax3):
    aa.set_axis_off()

ax1.imshow(image)
ax1.set_title("Source")
ax2.imshow(reference)
ax2.set_title("Reference")
ax3.imshow(matched)
ax3.set_title("Matched")

plt.tight_layout()
plt.show()