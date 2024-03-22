# #Handling errors

# try:
#     file = open("file.txt")
#     dictionary = {"b":1}
#     print(dictionary["a"])
# except FileNotFoundError:
#     # if I dont find the file, I'll write a file saying hello
#     file = open("file.txt","w")
#     file.write("Hello")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exists")
# else:
#     # this will not work at the first time, because the file was just created
#     # also, this will only work when the dict key is correct (bc error)
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File Closed")

#Generating my own exeption

#try, except, else and finally >> now we're adding raise

# height = 44 #no one is that tall
# weight = int(60)

# #here I'll fix if the user add something like 44 in meters
# if height > 3:
#     raise ValueError("This is not a proper height")

# bmi = weight/height **2
# print(bmi)




fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
      fruit = fruits[index]
    except IndexError:
      print("Fruit pie")
    else:
      print(fruit + " pie")
make_pie(4)



facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass

print(total_likes)
