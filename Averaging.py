import cv2
import matplotlib.pyplot as plt

# Generate array of noisy images
noisy_images = []
for i in range(3):
    image = cv2.imread('image (' + str(i) + ').png',cv2.IMREAD_GRAYSCALE)
    noisy_images.append(image)

# Calculate the mean of the noisy images
mean_image = []
for i in range(len(image)):
    row_mean = []
    for j in range(len(image[0])):
        pixel_sum = 0
        for noisy_image in noisy_images:
            pixel_sum += noisy_image[i, j]
        row_mean.append(round(pixel_sum / 3))
    mean_image.append(row_mean)

# Show the image after averaging
plt.imshow(mean_image, cmap = 'gray')
plt.title('Image After Averaging')
plt.axis('off')
plt.show()