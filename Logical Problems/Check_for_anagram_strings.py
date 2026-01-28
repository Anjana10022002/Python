# s1 = "listen"
# s2 = "silent"

# s1 = s1.lower()
# s2 = s2. lower()

# freq1 = {}
# freq2 = {}

# if len(s1) != len(s2):
#     print("Not anagram")
# else:
#     for i in s1:
#         if i in freq1:
#             freq1[i] +=1
#         else:
#             freq1[i] = 1

#     for i in s2:
#         if i in freq2:
#             freq2[i] +=1
#         else:
#             freq2[i] = 1

#     if freq1 == freq2:
#         print("Anagram")



s1 = 'listen'
s2= 'silent'

s1= s1.lower()
s2= s2.lower()
freq1 = {}
freq2 = {}

if len(s1) != len(s2):
    print("Not anagram")
else:
    for i in s1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1
        
    for i in s2:
        if i in freq2:
            freq2[i] += 1
        else: 
            freq2[i] = 1

    if freq1[i] == freq2[i]:
        print ("Anagram")
