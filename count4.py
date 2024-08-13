def count(str1, sub):
   len1 = len(str1)
   len2 = len(sub)
   count = 0
   
   for i in range(len1-len2+1):
      if (str1[i:i+len2] == sub and (i+len2)<=(len1)):
         count += 1
   return count
   
print(count("sggggs","gg"))