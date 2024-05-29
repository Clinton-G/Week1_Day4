import random


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

breakfast = ['bacon', 'waffle', 'poptart', 'toast', 'eggs']
lunch = ['sandwhich', 'pasta', 'soup', 'mac n cheese', 'pho']
dinner = ['chicken', 'wings', 'burger', 'ribs', 'carne asada']

<<<<<<< HEAD
for day in days:
    print("On", day, "I'll Be Having:")
    print(random.choice(breakfast), "For Breakfast")
    print(random.choice(lunch), "For Lunch")
    print("And", random.choice(dinner), "For Dinner")
    print("----------")
=======
for eachday in days:
    print(eachday, 'im going to have', random.choice(breakfast))

for eachday in days:
    print(eachday, 'im going to have', random.choice(lunch))

for eachday in days:
    print(eachday, 'im going to have', random.choice(dinner))
>>>>>>> 660db2726e18c5e06fac4accb31973d3d52325c1
