l=str(input())
num=[int(char) for char in l]
n=len(num)
if(n==1):
    print(num[0])
if(n>1):
    if(n%2!=0):
        num[n//2]+=1
    else:
        num[n//2]+=1
        num[(n)//2-1]+=1
    num=[str(char) for char in num]
    print("".join(num))