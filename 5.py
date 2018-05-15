s={"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}
a=0
while True:
    n=input("제품명 : ")
    if n in s:
        a = a + s[n]
        print("[%s:%d] > %d"%(n,s[n],a))
    elif n=="":
        print("총 급액 :",a)
        break
    else:
        print(n,"는 미등록 제품입니다.")
        
