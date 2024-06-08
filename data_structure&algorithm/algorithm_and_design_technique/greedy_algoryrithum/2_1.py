N = int(input())

num_rest = N
day_count = 0

while num_rest > 0:
    if num_rest%2 ==0:
        num_rest = num_rest/2
        day_count +=1
    else:
        num_rest -= 1
        day_count +=1
        
print(day_count)
