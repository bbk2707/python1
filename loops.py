n=int(input("length of the series"))
x=0
y=1

for num in range(0,n):
    if(num<=1):
        next=num
    else:
        next=x+y
        x=y
        y=next
    print(next)
