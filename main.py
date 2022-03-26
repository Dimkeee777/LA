# def print_2_add_2():
#     result = 2+2
#     print(result)
# print_2_add_2()
# def Hello_world():
#     print("'Hello world'")
#
# Hello_world()
# def mu_func(a, b):
#
#     result = a + b
#
#     return result
#
# c = mu_func(5, 10)
# print(c)
# for i in range(10, 0, (-2)):
#     if i % 2 == 0:
#         print(i, end = " ")

# a * x = b
# x = b/a

# def linear_solve(a,b):
#     return b/a
# print(linear_solve(0, 1))

# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# def positive(x):
#     return x % 2 == 0
#
# result = filter(positive, [-2, -1, 0, 4, 6 , 7])
#
# print(list(result))

# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))
#
# a = ["это", "маленький", "текст", "обидно"]
# print(list(map(str.upper, a)))

# print(quadratic_solve(L = [1, 2, 3]))
#
#
#
#
# myFile = open("filename.txt")
#
# myFile = open("filename.txt", 'rt')
#
# myFile = open("filename.txt.", "rt", encoding="utf8")
#
# myFile = open('filename.txt')
# print(myFile.read(100))
#
# myFile = open('filename.txt')
# print(myFile.readlines())
#
# myFile = open('filename.txt')
# for line in myFile:
#     print(line)



# alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# number = int(input("Введите число, на которое нужно сдвинуть текст: "))
#
# summary = ""
#
# def changeChar(char):
#     if char in alpha:
#         return alpha[alpha.index(char)+number % len(alpha)]
#     elif char in alphaUp:
#         return alphaUp[alphaUp.index(char)+number % len(alphaUp)]
#     else:
#         return char
# with open('filename2.txt', encoding='utf8') as myFile:
#     for line in myFile:
#         for char in line:
#             summary += changeChar(char)
#
# with open('output.txt', 'w', encoding='utf8') as myFile:
#     myFile.write(summary)

# myFile = open("labirint.txt.", "w", encoding="utf8")

def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == weight:
                    # Вниз
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight + 1

                        # Вверх
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight + 1

                    # Вправо
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight + 1

                    # Влево
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight + 1

                    # Конечная точка
                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight + 1
                        return True
        weight += 1
    return False


def printPath(pathArr, finPoint):
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y > 0 and pathArr[y - 1][x] == weight:
            result[weight] = 'Вниз'
            y -= 1
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            result[weight] = 'Вверх'
            y += 1
        elif x > 0 and pathArr[y][x - 1] == weight:
            result[weight] = 'Вправо'
            x -= 1
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            result[weight] = 'Влево'
            x += 1

    return result[1:]


labirint = []
with open("labirint.txt") as myFile:
    for line in myFile:
        labirint.append(line.replace('\n', '').split(' '))

ii = 0
for i in labirint:
    jj = 0
    for j in i:
        if j == 'A':
            labirint[ii][jj] = 1
            pozIn = (ii, jj)
        elif j == 'B':
            labirint[ii][jj] = 0
            pozOut = (ii, jj)
        elif j == '1':
            labirint[ii][jj] = -1
        else:
            labirint[ii][jj] = 0
        jj += 1
    ii += 1

if not found(labirint, pozOut):
    print("Путь не найден!")
else:
    result = printPath(labirint, pozOut)

    for i in labirint:
        for line in i:
            print("{:^3}".format(line), end=" ")
        print()
    print(result)


