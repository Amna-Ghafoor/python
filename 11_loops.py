#while and for loop

#while loop
x=0
while(x<=5):
    print(x)
    x=x+1

#for loop
for x in range(5,10):
    print(x)

#array
day=("Mon","Tue","Wed","Thur","Fri","Sat","Sun")
for d in day:
    # if (d=="Fri"):break #loop stops
 if(d=="Fri"):continue    #skips d
 print(d)