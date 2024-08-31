def q0(text):  
   if len(text)>0: 
      symbol = text[0] 
      if symbol in alpha:
         if symbol == 'a':
            return q0(text[1:])
         elif symbol == 'b':
            return q1(text[1:])
      else:
         return "Rejected" 
         
   else:
      return "q0"  
      
def q1(text):  
   if len(text)>0:
      symbol = text[0]  
      if symbol in alpha:
         if symbol == 'a':
            return q0(text[1:])
         elif symbol == 'b':
            return q1(text[1:])
      else:
         return "Rejected" 
         
   else:
      return "q1"      

def dfa():
   
   text = input("Enter the text")
   if text=='':
      return "q0"
   else:
      return q0(text)


alpha = {'a','b'}
final_states = {'q1'}
result = dfa()

if result in final_states:
   print("Accepted")
   
else:
   print("Rejected")