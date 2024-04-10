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
print('1. 3x3 Median Filtering')
print('2. 5x5 Median Filtering')
print('3. Kuwhara Filtering')
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

# 3x3 Median Filtering
if choice == 1:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
                    result[i][j] = image[i][j]
                else:
                    pixels = []
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            pixels.append(image[i + k][j + l])
                    pixels.sort()
                    result[i][j] = pixels[4]
            else:
                pixels = []
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        pixels.append(padded3[i + k][j + l])
                pixels.sort()
                result[i][j] = pixels[4]

# 5x5 Median Filtering
if choice == 2:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i == 0 or j == 0 or i == rows - 1 or j == columns - 1 or i == 1 or j == 1 or i == rows - 2 or j == columns - 2:
                    result[i][j] = image[i][j]
                else:
                    pixels = []
                    for k in range(-2, 3):
                        for l in range(-2, 3):
                            pixels.append(image[i + k][j + l])
                    pixels.sort()
                    result[i][j] = pixels[12]
            else:
                pixels = []
                for k in range(-2, 3):
                    for l in range(-2, 3):
                        pixels.append(padded5[i + k][j + l])
                pixels.sort()
                result[i][j] = pixels[12]

# Kuwhara Filtering
if choice == 3:
    for i in range(rows):
        for j in range(columns):
            if border_choice == 1:
                if i == 0 or j == 0 or i == rows - 1 or j == columns - 1 or i == 1 or j == 1 or i == rows - 2 or j == columns - 2:
                    result[i][j] = image[i][j]
                else:
                    r1_sum = r2_sum = r3_sum = r4_sum = 0
                    for k in range(-2, 0):
                        for l in range(0, 3):
                            r1_sum += image[i + k][j + l]
                    for k in range(0, 3):
                        for l in range(1, 3):
                            r2_sum += image[i + k][j + l]
                    for k in range(1, 3):
                        for l in range(-2, 1):
                            r3_sum += image[i + k][j + l]
                    for k in range(-2, 1):
                        for l in range(-2, 0):
                            r4_sum += image[i + k][j + l]
                    r1_mean = round(r1_sum / 6)
                    r2_mean = round(r2_sum / 6)
                    r3_mean = round(r3_sum / 6)
                    r4_mean = round(r4_sum / 6)
                    r1_var = r2_var = r3_var = r4_var = 0
                    for k in range(-2, 0):
                        for l in range(0, 2):
                            r1_var += (image[i + k][j + l] - r1_mean) ** 2
                    r1_var = round(r1_var / 6)
                    for k in range(0, 2):
                        for l in range(1, 3):
                            r2_var += (image[i + k][j + l] - r2_mean) ** 2
                    r2_var = round(r2_var / 6)
                    for k in range(1, 3):
                        for l in range(-2, 0):
                            r3_var += (image[i + k][j + l] - r3_mean) ** 2
                    r3_var = round(r3_var / 6)
                    for k in range(-2, 1):
                        for l in range(-2, 0):
                            r4_var += (image[i + k][j + l] - r4_mean) ** 2
                    r4_var = round(r4_var / 6)
                    min = 999999999999
                    if r1_var < min:
                        min = r1_var
                        result[i][j] = r1_mean
                    if r2_var < min:
                        min = r2_var
                        result[i][j] = r2_mean
                    if r3_var < min:
                        min = r3_var
                        result[i][j] = r3_mean
                    if r4_var < min:
                        min = r4_var
                        result[i][j] = r4_mean
            else:
                r1_sum = r2_sum = r3_sum = r4_sum = 0
                for k in range(-2, 0):
                    for l in range(0, 3):
                        r1_sum += padded5[i + k][j + l]
                for k in range(0, 3):
                    for l in range(1, 3):
                        r2_sum += padded5[i + k][j + l]
                for k in range(1, 3):
                    for l in range(-2, 1):
                        r3_sum += padded5[i + k][j + l]
                for k in range(-2, 1):
                    for l in range(-2, 0):
                        r4_sum += padded5[i + k][j + l]
                r1_mean = round(r1_sum / 6)
                r2_mean = round(r2_sum / 6)
                r3_mean = round(r3_sum / 6)
                r4_mean = round(r4_sum / 6)
                r1_var = r2_var = r3_var = r4_var = 0
                for k in range(-2, 0):
                    for l in range(0, 2):
                        r1_var += (padded5[i + k][j + l] - r1_mean) ** 2
                r1_var = round(r1_var / 6)
                for k in range(0, 2):
                    for l in range(1, 3):
                        r2_var += (padded5[i + k][j + l] - r2_mean) ** 2
                r2_var = round(r2_var / 6)
                for k in range(1, 3):
                    for l in range(-2, 0):
                        r3_var += (padded5[i + k][j + l] - r3_mean) ** 2
                r3_var = round(r3_var / 6)
                for k in range(-2, 1):
                    for l in range(-2, 0):
                        r4_var += (padded5[i + k][j + l] - r4_mean) ** 2
                r4_var = round(r4_var / 6)
                min = 999999999999
                if r1_var < min:
                    min = r1_var
                    result[i][j] = r1_mean
                if r2_var < min:
                    min = r2_var
                    result[i][j] = r2_mean
                if r3_var < min:
                    min = r3_var
                    result[i][j] = r3_mean
                if r4_var < min:
                    min = r4_var
                    result[i][j] = r4_mean

# Show the image after filtering
plt.imshow(result, cmap = 'gray')
plt.title('Image After Filtering')
plt.axis('off')
plt.show()