#BOJ 1735 분수 합

a,b = list(map(int,input().split(' ')))
c,d = list(map(int,input().split(' ')))

numerator = (b*c+a*d) #분자
denominator = b*d #분모

#최대공약수
def GCD(x,y):
    while y:
        x,y = y,x%y
    return x

gcd = GCD(numerator,denominator)

numerator = int(numerator/gcd)
denominator = int(denominator/gcd)

print(f"{numerator} {denominator}") 