import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('imported_image.png',cv2.IMREAD_GRAYSCALE)

# Ask whether you want in range or full range histogram equalization
choice = input('Enter 1 for full range histogram equalization and 2 for in range histogram equalization: ')

# Frequency of each pixel value
min_val = max_val = image[0, 0]
count = [0] * 256
counter = 0
numbers = []
for row in image:
    for pixel in row:
        if pixel < min_val:
            min_val = pixel
        if pixel > max_val:
            max_val = pixel
        count[pixel] += 1
        counter += 1

for number in range(256):
    if count[number] != 0:
        numbers.append(number)

# Calculate probability of each pixel value to the total number of pixels
probability = []
for number in numbers:
    probability.append(count[number] / counter)

# Calculate cumulative probability
cumulative_probability = []
cumulative_probability.append(probability[0])
for prob in probability[1:]:
    cumulative_probability.append(cumulative_probability[-1] + prob)

# Calculate the new pixel values
new_pixel_values = []
for prob in cumulative_probability:
    new_pixel_values.append(round(prob * 255))

# In range
if choice == 2:
    ranger = max_val - min_val
    mini = min_val
# Full range
else:
    ranger = 255
    mini = 0

# Calculate the new pixel values
final_pixel_values = []
for prob in cumulative_probability:
    final_pixel_values.append(round(prob * ranger + mini))

# Create the new image
new_image = []
for row in image:
    new_row = []
    for pixel in row:
        new_row.append(final_pixel_values[numbers.index(pixel)])
    new_image.append(new_row)

# Show the image before histogram equalization
plt.imshow(image, cmap = 'gray')
plt.title('Grayscale Image Before Histogram Equalization')
plt.axis('off')
plt.show()

# Show the image after histogram equalization
plt.imshow(new_image, cmap = 'gray')
plt.title('Grayscale Image After Histogram Equalization')
plt.axis('off')
plt.show()

# Plot the histogram of grayscale pixel values before equalization
plt.plot(range(256), count, color = 'gray')
plt.title('Histogram Before Equalization')
plt.xlabel('Gray Level')
plt.ylabel('No. of Pixels')
plt.show()

# Plot the histogram of grayscale pixel values after equalization
new_hist = [0] * 256
for row in new_image:
    for pixel in row:
        new_hist[pixel] += 1

plt.plot(range(256), new_hist, color = 'gray')
plt.title('Histogram After Equalization')
plt.xlabel('Gray Level')
plt.ylabel('No. of Pixels')
plt.show()