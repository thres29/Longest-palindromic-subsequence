def max_len_palin(data):
    print("input data :", data)
    start, end=0, len(data)-1 
    return max_len_palin_util(data, start, end)
    
def max_len_palin_util(data, start, end):
   
    if (start > end):
        return 0
        
    if (start==end):
        return 1
        
    if (data[start] == data[end]):
        return 2 + max_len_palin_util(data, start + 1, end - 1)
    else:
        skip_start = max_len_palin_util(data, start + 1, end)
        skip_end = max_len_palin_util(data, start, end - 1)
        return max(skip_start, skip_end)
print ("recursive method")
print(max_len_palin("abdccba"))