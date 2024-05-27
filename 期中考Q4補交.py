import random
num=random.randint(1,100)
counter=0
print("請從1~100猜一數字，猜中數字遊戲才會結束")
while True:
    counter=counter+1
    guess=int(input())
    if guess==num:
        print("猜對了")
        break
    elif guess>num:
        print("太大了")
    else:
        print("太小了") 
print("遊戲結束，你一共猜了",counter,"次")
