import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('imported_image.png',cv2.IMREAD_GRAYSCALE)

# Enter original and enhanced dynamic ranges
r1, r2 = map(int, input('Enter original dynamic ranges: ').split())
s1, s2 = map(int, input('Enter enhanced dynamic ranges: ').split())

# Plot the histogram of grayscale pixel values before contrast change
hist = [0] * 256
for row in image:
    for pixel in row:
        hist[pixel] += 1

plt.plot(range(256), hist, color = 'gray')
plt.title('Histogram Before Contrast Change')
plt.xlabel('Gray Level')
plt.ylabel('No. of Pixels')
plt.show()

# Contrast Stretching
if s1 < r1 and s2 > r2:
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if pixel < r1:
                image[i][j] = image[i][j] * (s1 / r1)
            elif pixel > r2:
                image[i][j] = image[i][j] * ((255 - s2) / (255 - r2)) + 255 - 255 * ((255 - s2) / (255 - r2))
            else:
                image[i][j] = image[i][j] * ((s2 - s1) / (r2 - r1)) + s1 - r1 * ((s2 - s1) / (r2 - r1))

# Contrast Contraction
if s1 > r1 and s2 < r2:
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if pixel < r1:
                image[i][j] = image[i][j] * (s1 / r1)
            elif pixel > r2:
                image[i][j] = image[i][j] * ((255 - s2) / (255 - r2)) + 255 - 255 * ((255 - s2) / (255 - r2))
            else:
                image[i][j] = image[i][j] * ((s2 - s1) / (r2 - r1)) + s1 - r1 * ((s2 - s1) / (r2 - r1))

# Plot the histogram of grayscale pixel values after contrast change
hist = [0] * 256
for row in image:
    for pixel in row:
        hist[pixel] += 1

plt.plot(range(256), hist, color = 'gray')
plt.title('Histogram After Contrast Change')
plt.xlabel('Gray Level')
plt.ylabel('No. of Pixels')
plt.show()