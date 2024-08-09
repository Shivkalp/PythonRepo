def plusPattern3(num):
   for i in range(3*num-num):
      for j in range(2*num+3):
         if(i==0 and j==num+1):
            print("*",end="")
         elif(i+j==num+1 and i<num+1 and j<num+1):
            print("*",end="")
         elif(j-i==num+1 and i<num+1 and j>num+1):
            print("*",end="")
         elif(i==num and j==num+1):
            print(num,end="")
         elif(i-j==num-1 and i>num and j<num+1):
            print("*",end="")
         elif(i+j==3*num+1 and i>num and j>num+1):
            print("*",end="")
         else:
            print(" ",end="")
      print()
            
   for i in range(num):
      for j in range(2*num+3):
         print("*",end="")
      print()
         
print(plusPattern3(4))