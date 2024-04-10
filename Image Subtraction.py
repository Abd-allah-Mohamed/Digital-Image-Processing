import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('imported_image.tiff', cv2.IMREAD_GRAYSCALE)
image_people = cv2.imread('imported_image_with_people.tiff', cv2.IMREAD_GRAYSCALE)

rows = len(image)
columns = len(image[0])
image_subtraction = []

# Calculate the difference between the two images
for i in range(rows):
    row_subtraction = []
    for j in range(columns):
        pixel_diff = abs(int(image[i, j]) - int(image_people[i, j]))
        row_subtraction.append(pixel_diff)
    image_subtraction.append(row_subtraction)

# Show the images
fig = plt.figure(figsize = (10, 7))
rows = 2
columns = 2

fig.add_subplot(2, 2, 1)
plt.imshow(image_people, cmap = 'gray')
plt.axis('off')
plt.title("Image With People")

fig.add_subplot(2, 2, 2)
plt.imshow(image, cmap = 'gray')
plt.axis('off')
plt.title("Image Without People")

fig.add_subplot(2, 2, 3)
plt.imshow(image_subtraction, cmap = 'gray')
plt.axis('off')
plt.title("Image Subtraction")
plt.show()