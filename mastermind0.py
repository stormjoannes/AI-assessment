import random
import itertools

secret = []
letters = ["A", "B", "C", "D", "E", "F"]
board = [["X" for x in range(4)] for y in range(10)]
turn = 0


def guess():
    letters_combinations = sorted(list(itertools.product("ABCDEF", repeat=4)))
    return random.sample(letters_combinations, k=1)


def check_answer(check):
    red = 0
    white = 0
    visited = []

    for answer in secret:
        for letter_index in range(len(answer)):
            if answer[letter_index] == check[letter_index]:
                red += 1
                visited.append(letter_index)

    for answer in secret:
        for letter_index in range(len(answer)):
            if answer[letter_index] in check and letter_index not in visited:
                white += 1
                visited.append(letter_index)

    if red == 4:
        print("You won!")
        exit()

    return (red, white)


def show_gameplay():
    for y in board:
        print(y)


def input_move():
    move = input("\nInput 4 colors: ").upper().split()
    for letter in move:
        if len(move) != 4 or letter not in letters:
            return input_move()
    return move


def game_loop():
    global turn
    current_move = input_move()
    board[turn] = current_move
    pins = check_answer(current_move)
    show_gameplay()
    print(f"You have {pins[0]} red pin(s) and {pins[1]} white pin(s).")
    turn += 1
    if turn == 10:
        print("The game is over!")
        exit()


secret = guess()
print("-------------------------------------------")
print("Rule: differentiate the letters with spaces!")
print("-------------------------------------------")
while True:
    game_loop()

