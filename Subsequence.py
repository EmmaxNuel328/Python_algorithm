def is_subsequence(t):
    sequence = []
    sequence = [t[0]]
    print("sequence: ", sequence)
    for i in range(1,len(t)):
        if t[i] != sequence[-1]:
            print("t[i]: ", t[i])
            sequence.append(t[i])
            
            
            
    return sequence

t = [0,1,1,0]
print(is_subsequence(t))