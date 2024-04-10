import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('imported_image_2.png',cv2.IMREAD_GRAYSCALE)

# Show the image
plt.imshow(image, cmap = 'gray')
plt.title('Grayscale Image Before Bit Plane Slicing')
plt.axis('off')
plt.show()

# Create a Matplotlib figure to display the bit planes
plt.figure(figsize = (12, 8))

# Perform bit plane slicing and display each bit plane
modified_image = 0

for i in range(8):

    # Create subplots for each bit plane
    plt.subplot(2, 4, i + 1)
    plt.title(f'Bit Plane {i}')
    plt.imshow((image >> i) & 1, cmap = 'gray')
    plt.axis('off')

plt.suptitle('Bit Plane Slicing', fontsize = 16)
plt.tight_layout()
plt.show()

# The bit plane you want to replace (0-based index)
bit_plane_to_replace = int(input('Enter the bit plane you want to replace (0-based index): '))

# The bit plane you want to insert (0-based index)
bit_plane_to_insert = int(input('Enter the bit plane you want to insert (0-based index): '))

for i in range(8):
    if i == bit_plane_to_replace:
        # Replace the specified bit plane with the new bit plane
        bit_plane = (image >> bit_plane_to_insert) & 1
    else:
        bit_plane = (image >> i) & 1
    # Combine the modified bit plane with the rest of the image
    modified_image += (bit_plane << i)

# Show the modified image
plt.imshow(modified_image, cmap = 'gray')
plt.title('Grayscale Image After Bit Plane Slicing')
plt.axis('off')
plt.show()