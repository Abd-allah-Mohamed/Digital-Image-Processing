image = [[0, 0, 200, 200, 0, 0],
         [0, 200, 200, 201, 0, 0],
         [0, 0, 0, 199, 198, 0],
         [199, 200, 200, 198, 199, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 199, 199, 200],
         [0, 0, 0, 201, 201, 199]]

connectivity_set = [198, 199, 200, 201]

rows = len(image)
columns = len(image[0])

checker = [[0] * columns for i in range(rows)]
changer = [[0] * columns for i in range(rows)]

label_map = {}
current_label = 1

# Labeling connected regions using N4
def labelingN4(image):
    count = 0
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if pixel in connectivity_set:
                if i == 0 and j == 0:
                    count += 1
                    checker[i][j] = count
                elif i == 0 and j != 0:
                    if checker[i][j - 1] != 0:
                        checker[i][j] = checker[i][j - 1]
                    else:
                        count += 1
                        checker[i][j] = count
                elif i != 0 and j == 0:
                    if checker[i - 1][j] != 0:
                        checker[i][j] = checker[i - 1][j]
                    else:
                        count += 1
                        checker[i][j] = count
                else:
                    if checker[i - 1][j] != 0:
                        checker[i][j] = checker[i - 1][j]
                    elif checker[i][j - 1] != 0:
                        checker[i][j] = checker[i][j - 1]
                    else:
                        count += 1
                        checker[i][j] = count
    for i, row in enumerate(checker):
        for j, pixel in enumerate(row):
            if pixel != 0:
                for x in range(rows):
                    for y in range(columns):
                        changer[x][y] = 0
                checker[i][j] = min(checker[i][j], connectN4(i, j, checker[i][j]))

# Recursive function to find the minimum value of the connected region using N4
def connectN4(i, j, min_val):
    if i < 0 or i > rows - 1 or j < 0 or j > columns - 1 or checker[i][j] == 0:
        return min_val
    if changer[i][j] == 1:
        return min_val
    changer[i][j] = 1
    min_val = min(min_val, checker[i][j])
    min_val = min(min_val, connectN4(i + 1, j, min_val))
    min_val = min(min_val, connectN4(i - 1, j, min_val))
    min_val = min(min_val, connectN4(i, j + 1, min_val))
    min_val = min(min_val, connectN4(i, j - 1, min_val))
    return min_val

# Labeling connected regions using Nd
def labelingNd(image):
    count = 0
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if pixel in connectivity_set:
                if i == 0 and j == 0:
                    count += 1
                    checker[i][j] = count
                elif i == 0 and j != 0:
                    count += 1
                    checker[i][j] = count
                elif i != 0 and j == 0:
                    if checker[i - 1][j + 1] != 0:
                        checker[i][j] = checker[i - 1][j + 1]
                    else:
                        count += 1
                        checker[i][j] = count
                elif j == columns - 1:
                    if checker[i - 1][j - 1] != 0:
                        checker[i][j] = checker[i - 1][j - 1]
                    else:
                        count += 1
                        checker[i][j] = count
                else:
                    if checker[i - 1][j - 1] != 0:
                        checker[i][j] = checker[i - 1][j - 1]
                    elif checker[i - 1][j + 1] != 0:
                        checker[i][j] = checker[i - 1][j + 1]
                    else:
                        count += 1
                        checker[i][j] = count
    for i, row in enumerate(checker):
        for j, pixel in enumerate(row):
            if pixel != 0:
                for x in range(rows):
                    for y in range(columns):
                        changer[x][y] = 0
                checker[i][j] = min(checker[i][j], connectNd(i, j, checker[i][j]))

# Recursive function to find the minimum value of the connected region using Nd
def connectNd(i, j, min_val):
    if i < 0 or i > rows - 1 or j < 0 or j > columns - 1 or checker[i][j] == 0:
        return min_val
    if changer[i][j] == 1:
        return min_val
    changer[i][j] = 1
    min_val = min(min_val, checker[i][j])
    min_val = min(min_val, connectNd(i + 1, j + 1, min_val))
    min_val = min(min_val, connectNd(i - 1, j - 1, min_val))
    min_val = min(min_val, connectNd(i - 1, j + 1, min_val))
    min_val = min(min_val, connectNd(i + 1, j - 1, min_val))
    return min_val

# Labeling connected regions using N8
def labelingN8(image):
    count = 0
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if pixel in connectivity_set:
                if i == 0 and j == 0:
                    count += 1
                    checker[i][j] = count
                elif i == 0 and j != 0:
                    if checker[i][j - 1] != 0:
                        checker[i][j] = checker[i][j - 1]
                    else:
                        count += 1
                        checker[i][j] = count
                elif i != 0 and j == 0:
                    if checker[i - 1][j] != 0:
                        checker[i][j] = checker[i - 1][j]
                    elif checker[i - 1][j + 1] != 0:
                        checker[i][j] = checker[i - 1][j + 1]
                    else:
                        count += 1
                        checker[i][j] = count
                elif j == columns - 1:
                    if checker[i - 1][j - 1] != 0:
                        checker[i][j] = checker[i - 1][j - 1]
                    elif checker[i - 1][j] != 0:
                        checker[i][j] = checker[i - 1][j]
                    elif checker[i][j - 1] != 0:
                        checker[i][j] = checker[i][j - 1]
                    else:
                        count += 1
                        checker[i][j] = count
                else:
                    if checker[i - 1][j - 1] != 0:
                        checker[i][j] = checker[i - 1][j - 1]
                    elif checker[i - 1][j] != 0:
                        checker[i][j] = checker[i - 1][j]
                    elif checker[i - 1][j + 1] != 0:
                        checker[i][j] = checker[i - 1][j + 1]
                    elif checker[i][j - 1] != 0:
                        checker[i][j] = checker[i][j - 1]
                    else:
                        count += 1
                        checker[i][j] = count
    for i, row in enumerate(checker):
        for j, pixel in enumerate(row):
            if pixel != 0:
                for x in range(rows):
                    for y in range(columns):
                        changer[x][y] = 0
                checker[i][j] = min(checker[i][j], connectN8(i, j, checker[i][j]))

# Recursive function to find the minimum value of the connected region using N8
def connectN8(i, j, min_val):
    if i < 0 or i > rows - 1 or j < 0 or j > columns - 1 or checker[i][j] == 0:
        return min_val
    if changer[i][j] == 1:
        return min_val
    changer[i][j] = 1
    min_val = min(min_val, checker[i][j])
    min_val = min(min_val, connectN8(i + 1, j, min_val))
    min_val = min(min_val, connectN8(i - 1, j, min_val))
    min_val = min(min_val, connectN8(i, j + 1, min_val))
    min_val = min(min_val, connectN8(i, j - 1, min_val))
    min_val = min(min_val, connectN8(i + 1, j + 1, min_val))
    min_val = min(min_val, connectN8(i - 1, j - 1, min_val))
    min_val = min(min_val, connectN8(i - 1, j + 1, min_val))
    min_val = min(min_val, connectN8(i + 1, j - 1, min_val))
    return min_val

print('Welcome to the labeling connected regions program!')
print('Which method would you like to use?')
print('1. N4')
print('2. Nd')
print('3. N8')
n = int(input('Enter your choice: '))
if n == 1:
    labelingN4(image)
elif n == 2:
    labelingNd(image)
else:
    labelingN8(image)

for i, row in enumerate(checker):
    for j, pixel in enumerate(row):
        if pixel != 0:
            if pixel not in label_map:
                label_map[pixel] = current_label
                current_label += 1
            checker[i][j] = label_map[pixel]

for row in checker:
    print(row)