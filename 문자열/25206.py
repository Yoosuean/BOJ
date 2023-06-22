#BOJ 25206 너의 평점은
grade=['A+','A0','B+','B0','C+','C0','D+','D0','F','P']
grade_n=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
sum=0

total =0
for i in range(20):
    _,a,b= map(str,input().split())
    if b==grade[9]:
        continue
    sum=sum+float(a)
    idx=grade.index(b)
    total = total+float(a)*(grade_n[idx])

print("%.6f" %(total/sum))