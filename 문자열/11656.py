#BOJ 11656 접미사 배열
s=input()
s_list=[]

for i in range(len(s)):
    s_list.append(s[i:])
s_list.sort()
for word in s_list:
    print(word)