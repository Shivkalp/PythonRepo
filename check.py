#def is_palindrome(text):
    #return text==text[::-1]
import time
   
def check1(obj_list):
    count = 0
    for i in obj_list:
        if(type(i)==set or type(i)==tuple or type(i)==list):
            count += check1(i)
        elif(type(i)==int):
            continue
        elif(type(i)==str and len(i)%6==3 and text==text[::-1]):
            count += 1
    return count

def check2(obj_list):
    count = 0
    for i in obj_list:
        if(type(i)==set or type(i)==tuple or type(i)==list):
            count += check1(i)
        elif(type(i)==int):
            continue
        elif(type(i)==str):
            if(len(i)%6==3):
               if(text==text[::-1]):
                  count += 1
    return count
   
def check_performance(approaches, obj_list):
    time_taken = []
    for approach in approaches:
        temp_time = []
        for _ in range(100):
            start_time = time.time()
            approach(obj_list)
            end_time = time.time()
            temp_time.append(end_time-start_time)
        time_taken.append(sum(temp_time)/100)
    return time_taken

obj_list = ["sggs",23,"2332",(12,"sggs")]
print(check1(["sggs",23,"2332",(12,"sggs")]))
print(check_performance([check1,check2],obj_list))