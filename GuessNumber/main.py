import random


def game():
    guess = int(input("Your number guess: "))
    Number = random.randint(0, 21)
    count = 1
    while 1:
        if Number > guess:
            print('Your number is too low')
            guess = int(input("Your number guess: "))
        elif Number < guess:
            print('Your number is too high')
            guess = int(input("Your number guess: "))
        else:
            print("Congratulation!")
            print("Bạn đã đoán chính xác số cần tìm sau {} lần".format(count))
            quit()
        count += 1
game()