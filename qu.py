import time

def get_even_odd_count1(l):
    even_count,odd_count = 0,0
    for i in l:
        if(i%2==0):
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

def get_even_odd_count2(l):
    even_count,odd_count = 0,0
    for i in l:
        t = i%2
        even_count += 1-t
        odd_count += t
    return even_count, odd_count
    
def get_even_odd_count3(l):
    even_count,odd_count = 0,0
    for i in l:
        if i%2:
            odd_count += 1
        else:
            even_count += 1
def check_performance(methods, l):
    time_taken = []
    for method in methods:
        temp_time = []
        for i in range(100):
            start_time = time.time()
            method(l)
            end_time = time.time()
            temp_time.append(end_time-start_time)
        time_taken.append(sum(temp_time)/100)
    return time_taken    

l=[1,2,3,4,5,6]    
print(get_even_odd_count1([1,2,3,4,5,6]))
t = (check_performance([get_even_odd_count1,get_even_odd_count2,get_even_odd_count3],l))
print(t)
t1 = t[0]
t2 = (t1-t[1])*100/t1
t3 = (t1-t[2])*100/t1

print(t1,t2,t3)