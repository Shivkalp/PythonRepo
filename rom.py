text = input("Enter the text")
text_base = int(input("Enter the text-base"))
len1 = len(text)
digit = 0
list1 = []
def convert_to_int(text, text_base):
   val = 0
   for i in range(len1):
      digit = int(text[i])
      len2 = len1-(i+1)
      val += (digit*(text_base**len2))
      
   return val
   
def rom(result):
   rom_repr = ''
   dict1 = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',400:'CD', 500:'D',600:'DC',700:'DCC',800:'DCCC', 900:'CM', 1000:'M'}  
   hundreds = (result//100)*100
   tens = ((result-hundreds)//10)*10
   units = result%10
   
   list1.append(dict1.get(hundreds))
   list1.append(dict1.get(tens))
   list1.append(dict1.get(units))
      
   for i in range(len(list1)):
      rom_repr += list1[i]
   return rom_repr
   
result = convert_to_int(text, text_base)

print(rom(result))