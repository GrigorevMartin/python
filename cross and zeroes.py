#создание массива для игры
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#вывод таблицы
print("_____________")
for i in range(3):
    row = "| "
    for j in range(3):
        row += board[i][j] + " | "
    print(row)
    print("-------------")
player = "X"
count = 0
win = False
while (count < 9) and (win == False):
    print("Игрок", player, "твой ход.")
    row = int(input("Введите номер строки (0-2): "))
    col = int(input("Введите номер столбца (0-2): "))

    if board[row][col] == " ":
        board[row][col] = player
        count += 1

        print("_____________")
        for i in range(3):
            row = "| "
            for j in range(3):
                row += board[i][j] + " | "
            print(row)
            print("-------------")

        for i in range(3):
            if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
                print("Поздравляем! Игрок", player, "выиграл!")
                win = True
            break
            if (board[0][i] == player and board[1][i] == player and board[2][i] == player):
                print("Поздравляем! Игрок", player, "выиграл!")
                win = True
                break
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
            print("Поздравляем! Игрок", player, "выиграл!")
            win = True
            break
        if (board[2][0] == player and board[1][1] == player and board[0][2] == player):
            print("Поздравляем! Игрок", player, "выиграл!")
            win = True
            break
        if player == "X":
            player = "0"
        else:
            player = "X"
    else:
        print("Эта клетка занята, попробуйте ещё раз")


if win == False:
    print("Ничья!")

