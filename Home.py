data=[6,4,3,7,2]
t=0
i=0

while i<5:
    t=t+data[i]
    i=i+1

x=t/len(data)
print('Mean:',x)

data.sort()
x=len(data)/2
if len(data)%2==1:
    print('Median',data[int(x)])