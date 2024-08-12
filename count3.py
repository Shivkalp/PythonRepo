def count(str1, sub, boolean):
   
   len1 = len(str1)
   sublen = len(sub)
   count = 0
   if (boolean.capitalize()=='True'):
      for i in range(len1-(sublen-1)):
         p = i
         str2 = ""
         for j in range(sublen):
            str2 = str2 + str1[p]
            p = p+1
         if(str2 == sub):
            count = count + 1
      return count
   else:
      i=0
      while i<= len1-sublen:
         p = i
         str2 = ""
         for j in range(sublen):
            
            str2 = str2 + str1[p]
            p = p+1
         if(str2 == sub):
            count += 1
            i = i+sublen
         else :
            i = i+1
            
      return count
                     

str1 = input("Enter the string : ")
sub = input("Enter the sub-string : ")
boolean = input("Enter the boolean value : ")
print(count(str1,sub,boolean))

Author - Shashwat Shivkumar Girwalkar