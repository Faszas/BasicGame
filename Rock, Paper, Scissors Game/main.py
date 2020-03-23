# TỶ LỆ THẮNG, THUA VA HÒA KHI CHƠI VỚI  CHIẾN THUẬT NGẪU NHIÊN TRONG TRÒ KÉO BÚA BAO
import random
from collections import Counter

def gamePlay(num):
    count = 0
    tyle = []
    choices = ['keo', 'bua', 'bao']
    while count < num:
        myChoice = random.choice(choices)
        computerChoice = random.choice(choices)
        if myChoice == computerChoice:
            tyle.append('draw')
        elif (myChoice == "keo" and computerChoice == "bao") or (myChoice == 'bua' and computerChoice == 'keo') or (myChoice == 'bao' and computerChoice == 'bua'):
            tyle.append('win')
        elif (computerChoice == "keo" and myChoice == "bao") or (computerChoice == 'bua' and myChoice == 'keo') or (computerChoice == 'bao' and myChoice == 'bua'):
            tyle.append('lose')
        count += 1
    print("Tỷ lệ thắng là: {}%".format(Counter(tyle)['win']/num * 100))
    print("Tỷ lệ thua là: {}%".format(Counter(tyle)['lose']/num * 100))
    print("Tỷ lệ hoà là: {}%".format(Counter(tyle)['draw']/num * 100))


# Chơi 1000000 ván
gamePlay(1000000)
    