def find_last_person(n):
    colleagues = list(range(1, n + 1))
    index = 0

    while len(colleagues) > 1:
        index = (index + 2) % len(colleagues)
        del colleagues[index]

    return colleagues[0]

n = int(input("請輸入同事的總人數："))
result = find_last_person(n)
print("最後留下的同事是第", result, "順位。")