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

# Ask whether you want 3x3 average filtering, 5x5 average filtering, circular filtering,
# pyramidal filtering, cone filtering,  3x3 gaussian filtering, 5x5 gaussian filtering
print('1. 3x3 Average Filtering')
print('2. 5x5 Average Filtering')
print('3. Circular Filtering')
print('4. Pyramidal Filtering')
print('5. Cone Filtering')
print('6. 3x3 Gaussian Filtering')
print('7. 5x5 Gaussian Filtering')
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

# Perform the specified filtering operation with the specified border choice
# 3x3 average filtering
if choice == 1:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i != 0 and j != 0 and i != rows - 1 and j != columns - 1:
                    neighbor_sum = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            neighbor_sum += image[i + x][j + y]
                    result[i][j] = round(neighbor_sum / 9)
            elif border_choice == 2 or border_choice == 3:
                neighbor_sum = 0
                for x in range(3):
                    for y in range(3):
                        neighbor_sum += padded3[i + x][j + y]
                result[i][j] = round(neighbor_sum / 9)

# 5x5 average filtering
if choice == 2:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i > 1 and j > 1 and i < rows - 2 and j < columns - 2:
                    neighbor_sum = 0
                    for x in range(-2, 3):
                        for y in range(-2, 3):
                            neighbor_sum += image[i + x][j + y]
                    result[i][j] = round(neighbor_sum / 25)
                elif i == 1 or j == 1 or i == rows - 2 or j == columns - 2:
                    result[i][j] = image[i][j]
            elif border_choice == 2 or border_choice == 3:
                neighbor_sum = 0
                for x in range(5):
                    for y in range(5):
                        neighbor_sum += padded5[i + x][j + y]
                result[i][j] = round(neighbor_sum / 25)

# Circular filtering
if choice == 3:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i > 1 and j > 1 and i < rows - 2 and j < columns - 2:
                    neighbor_sum = 0
                    for y in range(-1, 2):
                        neighbor_sum += image[i - 2][j + y]
                    for x in range(-1, 2):
                        for y in range(-2, 3):
                            neighbor_sum += image[i + x][j + y]
                    for y in range(-1, 2):
                        neighbor_sum += image[i + 2][j + y]
                    result[i][j] = round(neighbor_sum / 21)
                elif i == 1 or j == 1 or i == rows - 2 or j == columns - 2:
                    result[i][j] = image[i][j]
            elif border_choice == 2 or border_choice == 3:
                neighbor_sum = 0
                for y in range(1, 4):
                    neighbor_sum += padded5[i][j + y]
                for x in range(1, 4):
                    for y in range(5):
                        neighbor_sum += padded5[i + x][j + y]
                for y in range(1, 4):
                    neighbor_sum += padded5[i + 4][j + y]
                result[i][j] = round(neighbor_sum / 21)

# Pyramidal filtering
if choice == 4:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i > 1 and j > 1 and i < rows - 2 and j < columns - 2:
                    neighbor_sum = 0
                    neighbor_sum = image[i - 2][j - 2] * 1 + image[i - 2][j - 1] * 2 + image[i - 2][j] * 3 + image[i - 2][j + 1] * 2 + image[i - 2][j + 2] * 1
                    neighbor_sum += (image[i - 1][j - 2] * 2 + image[i - 1][j - 1] * 4 + image[i - 1][j] * 6 + image[i - 1][j + 1] * 4 + image[i - 1][j + 2] * 2)
                    neighbor_sum += (image[i][j - 2] * 3 + image[i][j - 1] * 6 + image[i][j] * 9 + image[i][j + 1] * 6 + image[i][j + 2] * 3)
                    neighbor_sum += (image[i + 1][j - 2] * 2 + image[i + 1][j - 1] * 4 + image[i + 1][j] * 6 + image[i + 1][j + 1] * 4 + image[i + 1][j + 2] * 2)
                    neighbor_sum += (image[i + 2][j - 2] * 1 + image[i + 2][j - 1] * 2 + image[i + 2][j] * 3 + image[i + 2][j + 1] * 2 + image[i + 2][j + 2] * 1)
                    result[i][j] = round(neighbor_sum / 81)
                elif i == 1 or j == 1 or i == rows - 2 or j == columns - 2:
                    result[i][j] = image[i][j]
            elif border_choice == 2 or border_choice == 3:
                neighbor_sum = 0
                neighbor_sum = padded5[i][j] * 1 + padded5[i][j + 1] * 2 + padded5[i][j + 2] * 3 + padded5[i][j + 3] * 2 + padded5[i][j + 4] * 1
                neighbor_sum += (padded5[i + 1][j] * 2 + padded5[i + 1][j + 1] * 4 + padded5[i + 1][j + 2] * 6 + padded5[i + 1][j + 3] * 4 + padded5[i + 1][j + 4] * 2)
                neighbor_sum += (padded5[i + 2][j] * 3 + padded5[i + 2][j + 1] * 6 + padded5[i + 2][j + 2] * 9 + padded5[i + 2][j + 3] * 6 + padded5[i + 2][j + 4] * 3)
                neighbor_sum += (padded5[i + 3][j] * 2 + padded5[i + 3][j + 1] * 4 + padded5[i + 3][j + 2] * 6 + padded5[i + 3][j + 3] * 4 + padded5[i + 3][j + 4] * 2)
                neighbor_sum += (padded5[i + 4][j] * 1 + padded5[i + 4][j + 1] * 2 + padded5[i + 4][j + 2] * 3 + padded5[i + 4][j + 3] * 2 + padded5[i + 4][j + 4] * 1)
                result[i][j] = round(neighbor_sum / 81)

# Cone filtering
if choice == 5:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i > 1 and j > 1 and i < rows - 2 and j < columns - 2:
                    neighbor_sum = 0
                    neighbor_sum = image[i - 2][j] * 1
                    neighbor_sum += (image[i - 1][j - 1] * 2 + image[i - 1][j] * 2 + image[i - 1][j + 1] * 2)
                    neighbor_sum += (image[i][j - 2] * 1 + image[i][j - 1] * 2 + image[i][j] * 5 + image[i][j + 1] * 2 + image[i][j + 2] * 1)
                    neighbor_sum += (image[i + 1][j - 1] * 2 + image[i + 1][j] * 2 + image[i + 1][j + 1] * 2)
                    neighbor_sum += (image[i + 2][j] * 1)
                    result[i][j] = round(neighbor_sum / 25)
                elif i == 1 or j == 1 or i == rows - 2 or j == columns - 2:
                    result[i][j] = image[i][j]
            elif border_choice == 2 or border_choice == 3:
                neighbor_sum = 0
                neighbor_sum = padded5[i][j + 2] * 1
                neighbor_sum += (padded5[i + 1][j + 1] * 2 + padded5[i + 1][j + 2] * 2 + padded5[i + 1][j + 3] * 2)
                neighbor_sum += (padded5[i + 2][j] * 1 + padded5[i + 2][j + 1] * 2 + padded5[i + 2][j + 2] * 5 + padded5[i + 2][j + 3] * 2 + padded5[i + 2][j + 4] * 1)
                neighbor_sum += (padded5[i + 3][j + 1] * 2 + padded5[i + 3][j + 2] * 2 + padded5[i + 3][j + 3] * 2)
                neighbor_sum += (padded5[i + 4][j + 2] * 1)
                result[i][j] = round(neighbor_sum / 25)
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

# 3x3 gaussian filtering
if choice == 6:
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

# 5x5 gaussian filtering
if choice == 7:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i > 1 and j > 1 and i < rows - 2 and j < columns - 2:
                    neighbor_sum = 0
                    neighbor_sum = image[i - 2][j - 2] * 1 + image[i - 2][j - 1] * 4 + image[i - 2][j] * 7 + image[i - 2][j + 1] * 4 + image[i - 2][j + 2] * 1
                    neighbor_sum += (image[i - 1][j - 2] * 4 + image[i - 1][j - 1] * 16 + image[i - 1][j] * 26 + image[i - 1][j + 1] * 16 + image[i - 1][j + 2] * 4)
                    neighbor_sum += (image[i][j - 2] * 7 + image[i][j - 1] * 26 + image[i][j] * 41 + image[i][j + 1] * 26 + image[i][j + 2] * 7)
                    neighbor_sum += (image[i + 1][j - 2] * 4 + image[i + 1][j - 1] * 16 + image[i + 1][j] * 26 + image[i + 1][j + 1] * 16 + image[i + 1][j + 2] * 4)
                    neighbor_sum += (image[i + 2][j - 2] * 1 + image[i + 2][j - 1] * 4 + image[i + 2][j] * 7 + image[i + 2][j + 1] * 4 + image[i + 2][j + 2] * 1)
                    result[i][j] = round(neighbor_sum / 273)
                elif i == 1 or j == 1 or i == rows - 2 or j == columns - 2:
                    result[i][j] = image[i][j]
            elif border_choice == 2 or border_choice == 3:
                neighbor_sum = 0
                neighbor_sum = padded5[i][j] * 1 + padded5[i][j + 1] * 4 + padded5[i][j + 2] * 7 + padded5[i][j + 3] * 4 + padded5[i][j + 4] * 1
                neighbor_sum += (padded5[i + 1][j] * 4 + padded5[i + 1][j + 1] * 16 + padded5[i + 1][j + 2] * 26 + padded5[i + 1][j + 3] * 16 + padded5[i + 1][j + 4] * 4)
                neighbor_sum += (padded5[i + 2][j] * 7 + padded5[i + 2][j + 1] * 26 + padded5[i + 2][j + 2] * 41 + padded5[i + 2][j + 3] * 26 + padded5[i + 2][j + 4] * 7)
                neighbor_sum += (padded5[i + 3][j] * 4 + padded5[i + 3][j + 1] * 16 + padded5[i + 3][j + 2] * 26 + padded5[i + 3][j + 3] * 16 + padded5[i + 3][j + 4] * 4)
                neighbor_sum += (padded5[i + 4][j] * 1 + padded5[i + 4][j + 1] * 4 + padded5[i + 4][j + 2] * 7 + padded5[i + 4][j + 3] * 4 + padded5[i + 4][j + 4] * 1)
                result[i][j] = round(neighbor_sum / 273)

# Show the result image after filtering
plt.imshow(result, cmap = 'gray')
plt.title('Image After Filtering')
plt.axis('off')
plt.show()