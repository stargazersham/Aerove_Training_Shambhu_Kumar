import math
file1 = open("/home/stargazersham/Desktop/python_stuff/project1/myFirstFile.txt", "w+")
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
        file1.write(str(i))
        file1.write(" ")
        file1.write(str(j))
        file1.write("\n")

d=int(input())
twins(10**(d-1),10**d-1)
