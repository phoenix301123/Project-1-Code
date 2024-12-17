n = int(input())
sequence = list(map(int, input().split()))

input()

while True:
    query = input().strip()
    
    if query == "***": 
        break
    
    if query == "find-max":
        print(max(sequence))
    
    elif query == "find-min":
        print(min(sequence))
    
    elif query.startswith("find-max-segment"):
        _, i, j = query.split()
        i, j = int(i), int(j)  
        print(max(sequence[i-1:j]))
    
    elif query == "sum":
        print(sum(sequence))

