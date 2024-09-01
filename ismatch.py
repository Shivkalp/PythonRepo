def ismatch(s, p):
   s_len = len(s)
   p_len = len(p)
   i,j = 0,0
   p_sub = ''
   s_sub = ''
   while (i != p_len):
      if(p[i]=='.'):
         j += 1
         i += 1
      elif(p[i].isalpha()):
         if(p[i] == s[j]):
            j += 1
            i += 1
         else:
            return False
      elif(p[i]=='*'):
         if(i<p_len-1):
            p_sub = p[i+1:]
            x = i+1
            while (not(p[x].isalpha()) and x<p_len):
               x += 1
            i = x
            s_sub = s[j:]
            if p[i] in s_sub:
               j += (s_sub.index(p[i])+1)
               i += 1
            else:
               return False
         else:
            return True  
   if(j != s_len):
      return False
   else:
      return True 
            
print(ismatch("aab","c*a*b")) 