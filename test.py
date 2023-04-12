import random
import numpy as np

#사용자로부터 100 이하의 정수 5개를 입력받아 리스트로 저장
userArr = []
for i in range(5):
    userNum = int(input("100이하의 정수 값을 입력하세요(%d/5) : " % (i+1)))
    userArr.append(userNum)

# 컴퓨터가 무작위로 100이하의 정수 5개를 생성하고 리스트로 저장
# 리스트 생성
randArr = []
for i in range(5):
    randNum = random.randint(1,100)
    randArr.append(randNum)

# 사용자와 컴퓨터가 입력 받은 값의 총합, 평균, 분산, 표준편차를 계산
# 총합
randSum = np.sum(randArr)
userSum = np.sum(userArr)

#평균
randMean = np.mean(randArr)
userMean = np.mean(userArr)

#분산
randVar = np.var(randArr)
userVar = np.var(userArr)

#표준편차
randStd = np.std(randArr)
userStd = np.std(userArr)

print('''
사용자의 총합 : {0}
사용자의 평균 : {1}
사용자의 분산 : {2}
사용자의 표준편차 : {3}

컴퓨터의 총합 : {4}
컴퓨터의 평균 : {5}
컴퓨터의 분산 : {6}
컴퓨터의 표준편차 : {7}
'''.format(userSum, userMean, userVar, userStd, randSum, randMean, randVar, randStd))
