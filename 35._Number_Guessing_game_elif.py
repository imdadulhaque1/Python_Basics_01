ori_num=6;
g_num=int(input("Enter a number for Guessing: "));
if ori_num == g_num:
    print("YOU WIN !!!")
else:
    if ori_num > g_num:
        print("Too Low")
    elif ori_num < g_num:
        print("Too high")
