def check_char(str1, char1):
   if char1 in str1:
      return ''
   else:
      return char1
      
def substr_wo_repeat(main_str):
   len_main = len(main_str)
   list1 = []
   str2 = ''
   str3 = ''
   p=0
   q=0
   for i in range(len_main):
     if i<(len_main-1): 
      str1 = ''
      str1 += main_str[i]
      str2 = main_str[i+1:]
      len3 = len(str2)
      for j in range(i+1,len_main):
         
         str3 = check_char(str1, main_str[j])
         if (str3 == ''):
            list1.append(str1)
            break
         else:
            str1 += str3
         if(j == len_main-1):
            list1.append(str1)
         
     else:
        str1 = ''
        str1 = main_str[i]
        list1.append(str1)
   return list1
   
def length(list1):
   i = 1
   index = 0
   max_val = len(list1[0])
   while(i<len(list1)):
      if (max_val < len(list1[i])):
         max_val = len(list1[i])
         index = i
         i += 1
      else:
         i += 1
         
   print(max_val)
   return list1[index]
         
l = []
main_str = input("Enter the main string") 
l = (substr_wo_repeat(main_str))
print(length(l))