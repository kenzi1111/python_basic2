gyou = int(input("行数を入力してください:"))
retu = int(input("列数を入力してください:"))

for i in range(1,gyou + 1):
    for j in range(1,retu + 1):
        print(str(i) + "+" + str(j) + "=" + str(i * j) + "|", end =" ")
    print()


