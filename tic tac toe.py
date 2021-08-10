board = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' '
}

def printBoard(board): 
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')

def main():
    turn = 'X'
    count = 0

    for i in range (10):
        printBoard(board)
        print("It's " + turn + "'s turn. Move to which position?")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count = count + 1
        else:
            print("Position already filled. Enter a valid position.")
            continue

        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ':
                print("Game over.")
                print("**" + turn + " won. **")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                print("Game over.")
                print("**" + turn + " won. **")
                break
            elif board['7'] == board['8'] == board['9'] != ' ':
                print("Game over.")
                print("**" + turn + " won. **")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                print("Game over.")
                print("**" + turn + " won. **")
                break
            elif board['3'] == board['5'] == board['7'] != ' ':
                print("Game over.")
                print("**" + turn + " won. **")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                print("Game over.")
                print("**" + turn + " won. **")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                print("Game over.")
                print("**" + turn + " won. **")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                print("Game over.")
                print("**" + turn + " won. **")
                break

    # in case of tie
        if count == 9:
            print("TIE")
        

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


main()

