engkor_dict=dict()
a=input("영어 단어 : ")
print("사전이 비었습니다.")
print("단어를 추가합니다.")
b=input("한글 단어 : ")
engkor_dict[a]=b
while True:
    a=input("영어 단어 : ")
    if a=="":
        break
    else:
        if a in engkor_dict:
            print(a,":",engkor_dict[a])
        else:
            print(a,"단어가 등록되어 있지 않습니다.")
            print("단어를 추가합니다.")
            b=input("한글 단어 : ")
            engkor_dict[a]=b
print (engkor_dict)
