def check_pal(text):
    text_len = len(text)
    str1 = ''
    str2 = ''
    if (text_len%2==0):
        half = text_len//2
    else:
        half = (text_len-1)//2
    str1 = text[:half]
    str2 = text[-1:(-(half+1)):-1]
    if(str1==str2):
        return text
    else:
        return "Not"
    

def to_check_sub_pal(main_text):
    len1 = len(main_text)
    str3 = ''
    str4 = ''
    list1 = []
    for i in range(len1-1):
        str3 = main_text[i]
        s = main_text[i+1:]
        for j in s:
            str3 += j
            str4 = check_pal(str3)
            if(str4 == str3):
                list1.append(str4)
    index = 0
    if list1:
       max_val = len(list1[0])
       i = 1
       while(i<len(list1)):
         if (max_val < len(list1[i])):
            max_val = len(list1[i])
            index = i
            i += 1
         else:
            i += 1
    
       return list1[index]
    
    else:
       return "No palindrome substring"
main_text = input("Enter the text")
print(to_check_sub_pal(main_text))