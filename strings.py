test_str=input("enter a String ")
freq={}
for i in test_str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(str(freq))
