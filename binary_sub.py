def binary_sub(num1, num2): #Value of num1 > length of num2.
    num1 = list(num1[::-1])
    num2 = list(num2[::-1])
    sub = []
    str_sub = ''
    for i in range(len(num1)-len(num2)):
        num2.append('0')
    for i in range(len(num1)):
        if (num1[i] == '0' and num2[i] == '0') or (num1[i] == '1' and num2[i] == '1'):
            sub.append('0')
        elif (num1[i] == '1' and num2[i] == '0'):
            sub.append('1')
        elif (num1[i] == '0' and num2[i] == '1'):
            sub.append('1')
            for j in range(i+1, len(num1)):
                if (num1[j] == '0'):
                    num1.pop(j)
                    num1.insert(j,'1')
                else:
                    num1.pop(j)
                    num1.insert(j,'0')
                    break                    
    for i in sub:
        str_sub += i
    str_sub = str_sub[::-1]    
    return str_sub
    
num1 = input("Enter first number")
num2 = input("Enter second number")
print(binary_sub(num1, num2))