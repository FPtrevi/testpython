while True:
    name = input("이름을 입력하세요 : ")
    gender = input("성별을 입력하세요(남자, 여자) : ")
    waist = int(input("허리둘레를 입력하세요(cm) : "))
    hip = int(input("엉덩이 둘레를 입력하세요(cm) : "))
    height = int(input("키를 입력하세요(cm) : "))/100
    weight = int(input("체중을 입력하세요(kg) : "))

    WHP = waist/hip
    if(gender=="남자"):
        if(WHP > 0.9):
            resultWHP = "비만"
        else:
            resultWHP = "정상"
    elif(gender=="여자"):
        if(WHP > 0.85):
            resultWHP = "비만"
        else:
            resultWHP = "정상"
    else:
        resultWHP = "성별오류"

    BMI = (weight/height**2)
    if(BMI<=19.9):
        resultBMI = "재측정"
    elif(BMI<=24.9):
        resultBMI = "정상"
    elif(BMI<=29.9):
        resultBMI = "과체중"
    else:
        resultBMI = "비만"

    if(resultWHP=="성별오류"):
        print("성별 오류로 재측정 합니다")
    else:
        if(resultBMI=="재측정"):
            print("BMI값 오류로 재측정합니다")
        else:
            print('''
            이름 : {0}
            성별 : {1}
            WHP : {2} ({3})
            BMI : {4}({5})
            '''.format(name, gender, WHP, resultWHP, BMI, resultBMI))
            break

