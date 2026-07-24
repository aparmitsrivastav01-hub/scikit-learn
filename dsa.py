numbers = [2,3,4]

target_sum = 6
index_a = 0
index_b = 0 

index = 0

for num in numbers:
    numbers.pop(index)
    for num1 in numbers:
        temp = index + 1
        if num + num1 == target_sum:
            index_a = index
            index_b = temp
            index += 1
            print(index_a,index_b)
            
    
    
            
