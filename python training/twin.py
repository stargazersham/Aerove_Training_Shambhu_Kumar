import math
def is_prime(n):
    
   if(n==1):
       return False
   for i in range(2, int(math.sqrt(n))+1):
      if n % i == 0:
         return False
   return True

def twins(start, end):
   for i in range(start, end):
       j = i + 2
       if(is_prime(i) and is_prime(j)):
         print(str(i), file=open("myFirstFile.txt", "a"))
         print(str(j), file=open("myFirstFile.txt", "a"))

d=int(input())
twins(10**(d-1),10**d-1)