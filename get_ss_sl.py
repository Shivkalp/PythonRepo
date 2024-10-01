def get_ss_sl(l):
    num_list = []
    for obj in l:
        if(type(obj)==set or type(obj)==list or type(obj)==tuple):
            num_list += get_ss_sl(list(obj))
        elif(type(obj)==str):
            continue
        elif(type(obj)==int):
            num_list.append(obj)
        elif(type(obj)==dict): 
            num_list += get_ss_sl(list(obj.keys()))
            num_list += get_ss_sl(list(obj.values()))
    return sorted(num_list)

def ss_sl_num(num_list):
    if(len(num_list)<2):
        return ()
    elif(len(num_list)>=2):
        return num_list[1], num_list[-2]      

l = [1,3,"sggs",("23",45,"dfg"),{2,9,"set"},[34,(55,2)],{5:'a',6:'b'}]    
num_list = get_ss_sl(l)
print(num_list)
ss_sl = ss_sl_num(num_list)
print(ss_sl)