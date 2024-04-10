import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('imported_image.png',cv2.IMREAD_GRAYSCALE)

# Show the image
plt.imshow(image, cmap = 'gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

# Calculate the minimum, maximum, standard deviation, and mean of the image
min_val = max_val = image[0, 0]
mean_val = 0
pixel_count = 0
sum_squared_diff = 0

for row in image:
    for pixel in row:
        if pixel < min_val:
            min_val = pixel
        if pixel > max_val:
            max_val = pixel
        mean_val += pixel
        pixel_count += 1

mean_val /= pixel_count

for row in image:
    for pixel in row:
        diff = pixel - mean_val
        sum_squared_diff += diff * diff

std_val = (sum_squared_diff / pixel_count) ** 0.5

print('Max =', max_val)
print('Min =', min_val)
print('Mean =', mean_val)
print('Standard Deviation =', std_val)

# Plot the histogram of grayscale pixel values
hist = [0] * 256
for row in image:
    for pixel in row:
        hist[pixel] += 1

plt.plot(range(256), hist, color = 'gray')
plt.title('Histogram')
plt.xlabel('Gray Level')
plt.ylabel('No. of Pixels')
plt.show()