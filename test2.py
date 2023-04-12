import random
textList = ["가위","바위","보"]
i = 0
#승,패,무승부 설정.
win = 0
lose = 0
draw = 0
while True:
    user = input("가위 바위 보 중 하나를 입력하세요 : ")
    if(user in textList):
        #게임시작
        #랜덤한 가위바위보
        computer = random.randint(0,2)
        if(computer == 0):
            card = "바위"
        elif(computer == 1):
            card = "가위"
        else:
            card = "보"

        

        if(user=="바위" and card=="바위"):
            draw += 1
        elif(user=="바위"and card=="가위"):
            win += 1
        elif(user=="바위" and card=="보"):
            lose += 1
        elif(user=="가위" and card=="바위"):
            win += 1
        elif(user=="가위" and card=="가위"):
            draw += 1
        elif(user=="가위" and card=="보"):
            lose += 1
        elif(user=="보" and card=="바위"):
            win += 1
        elif(user=="보" and card=="가위"):
            lose += 1
        elif(user=="보" and card=="보"):
            draw += 1

    else:
        user = input("정확히 입력했는지 확인해 주세요 : ")
        i -= 1

    if(i==4):
        print("게임을 종료합니다")
        print('''
        시행횟수 : {0}
        승 : {1}
        패 : {2}
        무승부 : {3}
        '''.format(i+1, win, lose, draw))
        break

    i+=1
    

