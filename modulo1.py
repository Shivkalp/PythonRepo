def modulo1(n,d):
   x = 0
   y = 0
   div = 0
   rem = 0
   if(n>=0 and d>0):
      div = n//d
      rem = n-div*d
   elif (n==0 and d==0):
      rem = "ZeroDivisionError"
   elif (n<0 and d>0):
      x = int(str(n).removeprefix("-"))
      div = x//d
      rem = (div+1)*d+n
   elif (n<0 and d<0):
      x = int(str(n).removeprefix("-"))
      y = int(str(d).removeprefix("-"))
      div = x//y
      str1 = str(x-y*div)
      rem = int("-"+str1)
   elif (n>0 and d<0):
      y = int(str(d).removeprefix("-"))
      div = n//y
      rem = n-(div+1)*y
   else:
      rem = "we will see later"
   return rem
      
print(modulo1(11,-3))