import random

dice_side = int(input("サイコロの面の数は?:"))
execution = int(input("何回振りますか?"))

dice_list = []

for i in range(execution):
    number = random.randint(1,dice_side)
    dice_list.append(number)

print(dice_list)