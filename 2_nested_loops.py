import random


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

breakfast = ['bacon', 'waffle', 'poptart', 'toast', 'eggs']
lunch = ['sandwhich', 'pasta', 'soup', 'mac n cheese', 'pho']
dinner = ['chicken', 'wings', 'burger', 'ribs', 'carne asada']

for day in days:
    print("On", day, "I'll Be Having:")
    print(random.choice(breakfast), "For Breakfast")
    print(random.choice(lunch), "For Lunch")
    print("And", random.choice(dinner), "For Dinner")
    print("----------")