s=0
while(s<=100 and s>=0):
    s=int(input("점수 :"))
    if s<=100 and s>=90:
        print(s,": A")
    elif s<=89 and s>=80:
        print(s,": B")
    elif s<=79 and s>=70:
        print(s,": C")
    elif s<=69 and s>=60:
        print(s,": D")
    elif s<=59 and s>=0:
        print(s,": F")
    else:
        print("입력 가능한 점수 범위는 0~100입니다.")
