# Task 1:


import random


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

breakfast = ['bacon', 'waffle', 'poptart', 'toast', 'eggs']
lunch = ['sandwhich', 'pasta', 'soup', 'mac n cheese', 'pho']
dinner = ['chicken', 'wings', 'burger', 'ribs', 'carne asada']

for eachday in days:
    print(eachday, 'im going to have', random.choice(breakfast))

for eachday in days:
    print(eachday, 'im going to have', random.choice(lunch))

for eachday in days:
    print(eachday, 'im going to have', random.choice(dinner))
