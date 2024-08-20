object = input("Enter the object")
slicing_parameter = [2,5,2]
len1 = len(object)
len2 = len(slicing_parameter)
p=0
def slice(object, slicing_parameter):
   string = ''
   if len2==0:
      return "SyntaxError: invalid syntax"
   elif len2==1:
      for i in range(len1-slicing_parameter[0]):
         p = i+slicing_parameter[0]
         string += object[p]
      return string
   elif len2==2:
      for i in range(slicing_parameter[1]-slicing_parameter[0]):
         p = i+slicing_parameter[0]
         string += object[p]
      return string
   elif len2==3:
      i=slicing_parameter[0]
      while (i<slicing_parameter[1]):
         string += object[i]
         i = i+slicing_parameter[2]
      return string
   else:
      return "Wrong slicing_parameter list"
      
print(slice(object,slicing_parameter))
      