import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('imported_image.png',cv2.IMREAD_GRAYSCALE)

# Enter the range of gray levels to be enhanced
r1, r2 = map(int, input('Enter the range of gray levels to be enhanced: ').split())

# Show the image
plt.imshow(image, cmap = 'gray')
plt.title('Grayscale Image Before Gray Level Slicing')
plt.axis('off')
plt.show()

# Perform gray level slicing
for i, row in enumerate(image):
    for j, pixel in enumerate(row):
        if pixel >= r1 and pixel <= r2:
            image[i][j] = 255

# Show the image
plt.imshow(image, cmap = 'gray')
plt.title('Grayscale Image After Gray Level Slicing')
plt.axis('off')
plt.show()