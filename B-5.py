
# 合計値
def calc_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 最大値
def calc_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

# 最小値
def calc_min(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

# 平均値
def calc_avg(numbers):
    total = calc_sum(numbers)
    return total / len(numbers)

# 計算値の出力
def main():
    data = input("データを入力してください(スペース区切り) > ")
    numbers = list(map(int, data.split()))
    
    print("合計値:", calc_sum(numbers))
    print("最大値:", calc_max(numbers))
    print("最小値:", calc_min(numbers))
    print("平均値:", calc_avg(numbers))

# 実行
if __name__ == "__main__":
    main()
