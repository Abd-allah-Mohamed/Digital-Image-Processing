import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('imported_image.png',cv2.IMREAD_GRAYSCALE)

# Show the image
plt.imshow(image, cmap = 'gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

# Convert the image to negative
negative_image = 255 - image

# Show the image
plt.imshow(negative_image, cmap = 'gray')
plt.title('Negative Image')
plt.axis('off')
plt.show()