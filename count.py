
def count(str1, sub):
   len1 = len(str1)
   sublen = len(sub)
   count = 0
   
   for i in range(len1-(sublen-1)):
         p = i
         str2 = ""
         for j in range(sublen):
            str2 = str2 + str1[p]
            p = p+1
         if(str2 == sub):
            count = count + 1
   return count

str1 = input("Enter the string : ")
sub = input("Enter the sub-string : ")

print(count(str1,sub))

Author - Shashwat Shivkumar Girwalkar