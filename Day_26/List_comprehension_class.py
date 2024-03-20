# numbers = [1,2,3]
# new_numbers = [i+30 for i in numbers]
# print(new_numbers)

# name = "Amanda"
# letters = [letter for letter in name]
# print(letters)

# new_range = [n*2 for n in range(1,5)]
# print(new_range)

### Conditional list comprehension

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# upper_case = [name.upper() for name in names if len(name) > 5]
# print(upper_case)

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_score = {name:random.randint(1,100) for name in names}
  
#passed_students = {key:value for (key, value) in student_score.items() if value >59}
#print(passed_students)

############ Dataframe iteration

import pandas as pd

student_dict = {"student":['Alex','Beth','Caroline'],
                "score": [56,76,98]}


student_data_frame = pd.DataFrame(student_dict)
#print(student_data_frame)

for index, row in student_data_frame.iterrows():
    print(row.score)
 

 