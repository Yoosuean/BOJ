n=input()
a = n.split("-")
if len(a) > 1:
    print(sum(map(int,a[0].split("+")))-sum(map(int,("+".join(a[1:]).split("+")))))
else:
    print(sum(map(int,a[0].split("+"))))

