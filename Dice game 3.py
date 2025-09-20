def solution(a, b, c, d):
    answer = 0
    numbers = [a, b, c, d]
    freq = {}
    
    for i in numbers:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    dup_val = []
    for val, f in freq.items():
        if f == 4:
            answer = val*1111
        elif f == 3 or f == 2:
            dup_val.append(val)
    other_val = [num for num, f in freq.items() if f == 1]
    
    if len(dup_val) == 1 and len(other_val) == 1:
        answer = (10*dup_val[0]+other_val[0])**2
    elif len(dup_val) == 2 and len(other_val) == 0:
        answer = (dup_val[0]+dup_val[1])*abs(dup_val[0]-dup_val[1])
    elif len(dup_val) == 1 and len(other_val) == 2:
        answer = other_val[0]*other_val[1]
    elif len(dup_val) == 0 and len(other_val) == 4:
        answer = min(other_val)
    
    return answer
