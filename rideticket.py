# Enter y hight e.g., 1.55
height = float(input("Enter the height in CM: "))
age =int(input("enter your age : "))
bill=0
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if height >=120:
    if age <12:
        bill=5
        print("child ticket is $5")
    elif age <18:
        bill=7
        print("ticket ammount is $7")
# logical operater
    # A and B
    # A or B
    # not B        
    elif age >=45 and age <=55 :
        print("Everything is ok. Have a free ride")
    else :
        bill=12
        print("the ticket value is $12")    
 #photo:               
    photo_pick =input("Are you intrested to take an pick YES/NO ")
    if photo_pick =="YES":
        bill +=3
        print(f"The total Amount is: ${bill}")
    else:
        print(f"The total value is: ${bill}")         
else:
    print("you could not ride Becouse you are under 120cm")