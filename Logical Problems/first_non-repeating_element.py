num = [1,4,7,3,8,1]
freq = {}
for n in num:
    if n in freq:
        freq[n] +=1
    else:
        freq[n] = 1

result = -1 

print(freq)
for n in num:
    if freq[n] == 1:
        result = n
        break
print(result)