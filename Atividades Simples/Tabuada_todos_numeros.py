num = 1

for i in range(10):
    for i in range(10):
        x = num * (i + 1)
        print(f"{num} * {i+1} = {x}")
    print("--------------------")
    num += 1