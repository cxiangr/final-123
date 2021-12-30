import random

min=1
max=100
password=random.randint(min,max)

while True:
    x=input("終極密碼請開始，1~100：")
    try:
        x=int(x)
    except:
        print("輸入錯誤，請輸入有效數字")
        continue

    if x<=min or x>=max:
        print("請輸入有效範圍",min,"~",max)
    elif x<password:
        min=x
        print(min,"~",max,"，請繼續")
    elif x>password:
        max=x
        print(min,"~",max,"，請繼續")
    else:
        print("恭喜中了，密碼為",password,"遊戲結束")
        break
