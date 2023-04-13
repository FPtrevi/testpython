disease = {
    "k20" : "식도염",
    "k21" : "위-식도역류병",
    "k22" : "식도의 기타 질환",
    "k23*" : "달리 분류된 질환에서의 식도의 장애",
    "k25" : "위궤양",
    "k26" : "십이지장궤양",
    "k27" : "상세불명 부위의 소화성 궤양",
    "k28" : "위공장궤양",
    "k29" : "위염 및 십이지장염",
    "k30" : "기능성 소화불량",
    "k31" : "위 및 십이지장의 기타 질환",
}

# patientList = {'patient0': {'name': '오현찬', 'code': 'k21'}, 'patient1': {'name': '방재준', 'code': 'k21'}, 'patient2': {'name': '이성영', 'code': 'k30'}, 'patient3': {'name': '하주희', 'code': 'k30'}, 'patient4': {'name': '김민혁', 'code': 'k25'}}
patientList = {}
#5번 반복
i = 0
while (len(patientList) < 3):
    name = input("\n환자의 이름을 입력하세요 : ")
    code = input("환자의 질병 코드를 입력하세요 : ")
    patientList['patient{0}'.format(i)] = {'name' : name, 'code':code}
    i+=1


#참조값 생성
name_arr = []
code_arr = []
for i in range(len(patientList)):
    key = patientList['patient{0}'.format(i)]
    name_arr.append(key['name'])
    code_arr.append(key['code'])

#조회
while True:
    search_name = input("\n\n\n조회할 환자 이름을 입력하세요 : ")
    if(search_name in name_arr):
        #환자이름, 질병코드, 질병명
        for i in range(len(patientList)):
            key = patientList['patient{0}'.format(i)]
            key_name = key['name']
            if(search_name == key_name):
                key_code = key['code']
                key_disease = disease[key_code]
                print("환자이름 : ", key_name)
                print("질병코드 : ", key_code)
                print("질병명 : ", key_disease)   
        break
    else:
        print("이름을 다시 확인 해 주세요")

#질병코드로 조회
while True:
    search_code = input("\n\n\n조회할 코드를 입력하세요 : ")
    if(search_code in disease.keys()):
        if(search_code in code_arr):
            print(disease[search_code])
            for i in range(len(patientList)):
                key = patientList['patient{0}'.format(i)]
                key_code = key['code']
                if(search_code == key_code):
                    key_name = key['name']
                    print("\n환자이름 : ", key_name)
                    print("질병코드 : ", key_code)
                    print("질병명", disease[search_code])
            break    
        else:
            print("해당 질병을 가진 환자가 없습니다.")
    else:
        print("코드를 확인해 주세요")