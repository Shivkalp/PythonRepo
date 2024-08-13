def change_case_cap(text):
   len1 = len(text)
   print(len(text))
   new_text = ""
   p = 0
   l = []
   for i in range(len1):
      l.append(text[i])
      if (text[i].isalpha()):
         p = ord(text[i])
         if (p<123 and p>96):
            p = p-32
            l[i] = chr(p)
         elif (text[i] == " "):
            l[i]=" "
            
      new_text += l[i]
   return new_text

def change_case_zigzag(text):
   len1 = len(text)
   str2 = ""
   p = ord(text[0])
   q = 0
   l = []
   if(p<91):
      for i in range(len1):
        if(text[i].isalpha()):
         if(i%2==0):
            if(ord(text[i])>96):
               q = ord(text[i])
               q -= 32
               l.append(chr(q))
            else:
               l.append(text[i])
               
         else:
            if(ord(text[i])<91):
               q = ord(text[i])
               q += 32
               l.append(chr(q))
            else:
               l.append(text[i])
        else:
           l.append(text[i])
           
        str2 += l[i]
      return str2                         
           
   elif(p>96):
      for i in range(len1):
        if(text[i].isalpha()):
         if(i%2==0):
            if(ord(text[i])<91):
               q = ord(text[i])
               q += 32
               l.append(chr(q))
            else:
               l.append(text[i])
               
         else:
            if(ord(text[i])>96):
               q = ord(text[i])
               q -= 32
               l.append(chr(q))
            else:
               l.append(text[i])
        else:
           l.append(text[i])
        str2 += l[i]
      return str2

def change_case_reverse(text):
   len1 = len(text)
   l = []
   p = 0
   str2 = ""
   for i in range(len1):
      if(text[i].isalpha()):  
         p = ord(text[i])
         if(p<91):
            p = p+32
         elif(p>96):
            p = p-32
         l.append(chr(p))
         
      else:
         l.append(text[i])
      str2 += l[i]
      
   return str2
   
def change_case_small(text):
   len1 = len(text)
   print(len(text))
   new_text = ""
   p = 0
   l = []
   for i in range(len1):
      l.append(text[i])
      if (text[i].isalpha()):
         p = ord(text[i])
         if (p<91 and p>64):
            p = p+32
            l[i] = chr(p)
         elif (text[i] == " "):
            l[i]=" "
            
      new_text += l[i]
   return new_text

def change_case(text,style):
   if style in ['c','C','s','S','r','R','z','Z']:
      if style in ['c','C']:
         return change_case_cap(text)
      elif style in ['s','S']:
         return change_case_small(text)
      elif style in ['r','R']:
         return change_case_reverse(text)
      elif style in ['z','Z']:
         return change_case_zigzag(text)
   else:
      return "Invalid style"

text = input("Enter the text : ")
style = input("Enter the style : ")      
print(change_case(text,style))