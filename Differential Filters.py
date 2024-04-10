import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('imported_image.png', cv2.IMREAD_GRAYSCALE)

rows = len(image)
columns = len(image[0])

result = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(0)
    result.append(row)

padded3 = []
for i in range(rows + 2):
    row = []
    for j in range(columns + 2):
        row.append(0)
    padded3.append(row)

padded5 = []
for i in range(rows + 4):
    row = []
    for j in range(columns + 4):
        row.append(0)
    padded5.append(row)

# Show the image before filtering
plt.imshow(image, cmap = 'gray')
plt.title('Image Before Filtering')
plt.axis('off')
plt.show()

# Ask whether you want to perform 8-neighbor laplacian filtering, 4-neighbor laplacian filtering,
# corners laplacian filtering, main-diagonal robert filtering, anti-diagonal robert filtering,
# x prewitt filtering, y prewitt filtering, main-diagonal prewitt filtering, anti-diagonal prewitt filtering,
# x sobel filtering, y sobel filtering, main-diagonal sobel filtering or anti-diagonal sobel filtering
print('1. 8-neighbor Laplacian Filtering')
print('2. 4-neighbor Laplacian Filtering')
print('3. Corners Laplacian Filtering')
print('4. Main-Diagonal Robert Filtering')
print('5. Anti-Diagonal Robert Filtering')
print('6. X Prewitt Filtering')
print('7. Y Prewitt Filtering')
print('8. Main-Diagonal Prewitt Filtering')
print('9. Anti-Diagonal Prewitt Filtering')
print('10. X Sobel Filtering')
print('11. Y Sobel Filtering')
print('12. Main-Diagonal Sobel Filtering')
print('13. Anti-Diagonal Sobel Filtering')
choice = int(input('Enter your choice: '))

# Ask whether you want to ignore, repeat or reflect the border pixels
print('1. Ignore the border pixels')
print('2. Repeat the border pixels')
print('3. Reflect the border pixels')
border_choice = int(input('Enter your choice: '))

# Ignore the border pixels
if border_choice == 1:
    for i in range(rows):
        for j in range(columns):
            if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
                result[i][j] = image[i][j]

# Repeat the border pixels
if border_choice == 2:
    for i in range(rows):
        for j in range(columns):
            if i == 0 and j == 0:
                padded3[i][j] = padded5[i][j] = image[i][j]
                padded3[i][j + 1] = padded5[i][j + 1] = image[i][j]
                padded5[i][j + 2] = image[i][j]
                padded3[i + 1][j] = padded5[i + 1][j] = image[i][j]
                padded3[i + 1][j + 1] = padded5[i + 1][j + 1] = image[i][j]
                padded5[i + 1][j + 2] = image[i][j]
                padded5[i + 2][j] = image[i][j]
                padded5[i + 2][j + 1] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
            elif i == rows - 1 and j == columns - 1:
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 1][j + 2] = image[i][j]
                padded3[i + 2][j + 1] = image[i][j]
                padded3[i + 2][j + 2] = padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 2][j + 3] = image[i][j]
                padded5[i + 2][j + 4] = image[i][j]
                padded5[i + 3][j + 2] = image[i][j]
                padded5[i + 3][j + 3] = image[i][j]
                padded5[i + 3][j + 4] = image[i][j]
                padded5[i + 4][j + 2] = image[i][j]
                padded5[i + 4][j + 3] = image[i][j]
                padded5[i + 4][j + 4] = image[i][j]
            elif i == 0 and j == columns - 1:
                padded3[i][j + 1] = image[i][j]
                padded3[i][j + 2] = padded5[i][j + 2] = image[i][j]
                padded5[i][j + 3] = image[i][j]
                padded5[i][j + 4] = image[i][j]
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 1][j + 2] = padded5[i + 1][j + 2] = image[i][j]
                padded5[i + 1][j + 3] = image[i][j]
                padded5[i + 1][j + 4] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 2][j + 3] = image[i][j]
                padded5[i + 2][j + 4] = image[i][j]
            elif i == rows - 1 and j == 0:
                padded3[i + 1][j] = image[i][j]
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 2][j] = padded5[i + 2][j] = image[i][j]
                padded3[i + 2][j + 1] = padded5[i + 2][j + 1] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 3][j] = image[i][j]
                padded5[i + 3][j + 1] = image[i][j]
                padded5[i + 3][j + 2] = image[i][j]
                padded5[i + 4][j] = image[i][j]
                padded5[i + 4][j + 1] = image[i][j]
                padded5[i + 4][j + 2] = image[i][j]
            elif i == 0:
                padded3[i][j + 1] = padded5[i][j + 2] = image[i][j]
                padded3[i + 1][j + 1] = padded5[i + 1][j + 2] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
            elif j == 0:
                padded3[i + 1][j] = padded5[i + 2][j] = image[i][j]
                padded3[i + 1][j + 1] = padded5[i + 2][j + 1] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
            elif i == rows - 1:
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 2][j + 1] = padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 3][j + 2] = image[i][j]
                padded5[i + 4][j + 2] = image[i][j]
            elif j == columns - 1:
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 1][j + 2] = padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 2][j + 3] = image[i][j]
                padded5[i + 2][j + 4] = image[i][j]
            else:
                padded3[i + 1][j + 1] = padded5[i + 2][j + 2] = image[i][j]

# Reflect the border pixels
if border_choice == 3:
    for i in range(rows):
        for j in range(columns):
            if i == 0 and j == 0:
                padded3[i][j] = image[i][j]
                padded5[i][j] = image[i + 1][j + 1]
                padded3[i][j + 1] = image[i][j]
                padded5[i][j + 1] = image[i + 1][j]
                padded5[i][j + 2] = image[i + 1][j]
                padded3[i + 1][j] = image[i][j]
                padded5[i + 1][j] = image[i][j + 1]
                padded3[i + 1][j + 1] = padded5[i + 1][j + 1] = image[i][j]
                padded5[i + 1][j + 2] = image[i][j]
                padded5[i + 2][j] = image[i][j + 1]
                padded5[i + 2][j + 1] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
            elif i == rows - 1 and j == columns - 1:
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 1][j + 2] = image[i][j]
                padded3[i + 2][j + 1] = image[i][j]
                padded3[i + 2][j + 2] = padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 2][j + 3] = image[i][j]
                padded5[i + 2][j + 4] = image[i][j - 1]
                padded5[i + 3][j + 2] = image[i][j]
                padded5[i + 3][j + 3] = image[i][j]
                padded5[i + 3][j + 4] = image[i][j - 1]
                padded5[i + 4][j + 2] = image[i - 1][j]
                padded5[i + 4][j + 3] = image[i - 1][j]
                padded5[i + 4][j + 4] = image[i - 1][j - 1]
            elif i == 0 and j == columns - 1:
                padded3[i][j + 1] = image[i][j]
                padded3[i][j + 2] = image[i][j]
                padded5[i][j + 2] = image[i + 1][j]
                padded5[i][j + 3] = image[i + 1][j]
                padded5[i][j + 4] = image[i + 1][j - 1]
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 1][j + 2] = padded5[i + 1][j + 2] = image[i][j]
                padded5[i + 1][j + 3] = image[i][j]
                padded5[i + 1][j + 4] = image[i][j - 1]
                padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 2][j + 3] = image[i][j]
                padded5[i + 2][j + 4] = image[i][j - 1]
            elif i == rows - 1 and j == 0:
                padded3[i + 1][j] = image[i][j]
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 2][j] = image[i][j]
                padded5[i + 2][j] = image[i][j + 1]
                padded3[i + 2][j + 1] = padded5[i + 2][j + 1] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 3][j] = image[i][j + 1]
                padded5[i + 3][j + 1] = image[i][j]
                padded5[i + 3][j + 2] = image[i][j]
                padded5[i + 4][j] = image[i - 1][j + 1]
                padded5[i + 4][j + 1] = image[i - 1][j]
                padded5[i + 4][j + 2] = image[i - 1][j]
            elif i == 0:
                padded3[i][j + 1] = image[i][j]
                padded5[i][j + 2] = image[i + 1][j]
                padded3[i + 1][j + 1] = padded5[i + 1][j + 2] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
            elif j == 0:
                padded3[i + 1][j] = image[i][j]
                padded5[i + 2][j] = image[i][j + 1]
                padded3[i + 1][j + 1] = padded5[i + 2][j + 1] = image[i][j]
                padded5[i + 2][j + 2] = image[i][j]
            elif i == rows - 1:
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 2][j + 1] = padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 3][j + 2] = image[i][j]
                padded5[i + 4][j + 2] = image[i - 1][j]
            elif j == columns - 1:
                padded3[i + 1][j + 1] = image[i][j]
                padded3[i + 1][j + 2] = padded5[i + 2][j + 2] = image[i][j]
                padded5[i + 2][j + 3] = image[i][j]
                padded5[i + 2][j + 4] = image[i][j - 1]
            else:
                padded3[i + 1][j + 1] = padded5[i + 2][j + 2] = image[i][j]

# 3x3 Gaussian Filtering
for i in range(rows):
    for j in range(columns):
        if border_choice == 1:
            if i != 0 and j != 0 and i != rows - 1 and j != columns - 1:
                neighbor_sum = 0
                neighbor_sum = image[i - 1][j - 1] * 1 + image[i - 1][j] * 2 + image[i - 1][j + 1] * 1
                neighbor_sum += (image[i][j - 1] * 2 + image[i][j] * 4 + image[i][j + 1] * 2)
                neighbor_sum += (image[i + 1][j - 1] * 1 + image[i + 1][j] * 2 + image[i + 1][j + 1] * 1)
                result[i][j] = round(neighbor_sum / 16)
        elif border_choice == 2 or border_choice == 3:
            neighbor_sum = 0
            neighbor_sum = padded3[i][j] * 1 + padded3[i][j + 1] * 2 + padded3[i][j + 2] * 1
            neighbor_sum += (padded3[i + 1][j] * 2 + padded3[i + 1][j + 1] * 4 + padded3[i + 1][j + 2] * 2)
            neighbor_sum += (padded3[i + 2][j] * 1 + padded3[i + 2][j + 1] * 2 + padded3[i + 2][j + 2] * 1)
            result[i][j] = round(neighbor_sum / 16)

rows2 = len(result)
columns2 = len(result[0])
result2 = []
for i in range(rows2):
    row2 = []
    for j in range(columns2):
        row2.append(0)
    result2.append(row2)

# Perform the specified filtering operation with the specified border choice
# 8-neighbor laplacian filtering
if choice == 1:
    kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
# 4-neighbor laplacian filtering
elif choice == 2:
    kernel = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
# Corners laplacian filtering
elif choice == 3:
    kernel = [[2, -1, 2], [-1, -4, -1], [2, -1, 2]]
# Main-diagonal robert filtering
elif choice == 4:
    kernel = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
# Anti-diagonal robert filtering
elif choice == 5:
    kernel = [[0, 1, 0], [-1, 0, 0], [0, 0, 0]]
# X prewitt filtering
elif choice == 6:
    kernel = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
# Y prewitt filtering
elif choice == 7:
    kernel = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
# Main-diagonal prewitt filtering
elif choice == 8:
    kernel = [[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]
# Anti-diagonal prewitt filtering
elif choice == 9:
    kernel = [[1, 1, 0], [1, 0, -1], [0, -1, -1]]
# X sobel filtering
elif choice == 10:
    kernel = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
# Y sobel filtering
elif choice == 11:
    kernel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
# Main-diagonal sobel filtering
elif choice == 12:
    kernel = [[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]
# Anti-diagonal sobel filtering
elif choice == 13:
    kernel = [[2, 1, 0], [1, 0, -1], [0, -1, -2]]

maxo = 0
mino = 0

# Applying filter
for i in range(1, rows2 - 1):
    for j in range(1, columns2 - 1):
        convolution = 0
        for m in range(3):
            for n in range(3):
                convolution += result[i + m - 1][j + n - 1] * kernel[m][n]
        result2[i][j] = convolution
        if i == 1 and j == 1:
            maxo = mino = result2[i][j]
        if maxo < result2[i][j]:
            maxo = result2[i][j]
        if mino > result2[i][j]:
            mino = result2[i][j]

# Scale values between 0 and 255 and make these values positive
for i in range(rows2):
    for j in range(columns2):
        result2[i][j] = abs((result2[i][j]/(maxo - mino)) * 255)

# Show the image after filtering
plt.imshow(result2, cmap = 'gray')
plt.title('Image After Filtering')
plt.axis('off')
plt.show()