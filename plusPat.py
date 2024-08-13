def plusPat(num):
   for i in range(2*num+1):
      for j in range(2*num+1):
         if(i==0 and j==num):
            print("+",end="")
         elif(j == num and i == 2*num):
            print("-",end="")
         elif(i+j==num):
            print("+",end="")
         elif(j-i==num):
            print("+",end="")
         elif(i-j==num):
            print("+",end="")
         elif(i+j==3*num):
            print("+",end="")
         else:
            print(" ",end="")
      print()
         
print(plusPat(4))