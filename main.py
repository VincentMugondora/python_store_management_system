# name = ""

# # Validate name
# while True:
#     name = input("Enter your name: ")
#     if  len(name) < 3:
#         print("Name must be at least 3 characters long.")
#     elif name == "exit":
#         print("l am exiting the program")
#         exit()


# string = "vincent"
# vowels = "aeiou"
# count = 0

# for char in string:
#     if char.lower() in vowels:
#         count += 1

# if count == 0:
#     print("No vowel in this string")
# else:
#     print(f"Total vowels found: {count}")


# command = ""
# start = False

# while True:
#     command = input("Enter a command (exit to quit): ")
#     if command == "start":
#         if start:
#             print("Car is already started!")
#         elif not start:
#             print("Starting the car!")
#             start = True
#     elif command == "stop":
#         if not start:
#             print("Car is already stopped!")
#         elif start:
#             start = False
#             print("Stopping the car!")
#     elif command == "help":
#         print("""Available commands: 
#         start => to start the car 
#         stop => to stop the car
#         exit => to exit the game
#         """)
#     elif command == "exit":
#         print("Exiting the game!")
#         break
#     else:
#         print("Invalid command. Please try again.")

# number = int(input("Enter a number: "))

# for n in range(number):
#     if n == 0 or n == 1:
#         continue
#     if number % n == 0:
#         print(f"{number} is divisible by {n}")
# else:
#     print(f"{number} is a prime number")


# def prime_checker(number):
#     for n in range(number):
#         if n == 0 or n == 1:
#             continue
#         if number % n == 0:
#             return False
#         return True 


# number = int(input("Enter a number: "))
# print(prime_checker(number))

# def con_vow_checker(word):
#     vowels = "aeiou"
#     consonants = "bcdfghjklmnpqrstvwxyz"
#     word = word.lower()
    
#     vow = []
#     con = []

#     for char in word:
#         if char in vowels:
#             vow.append(char)
#         elif char in consonants:
#             con.append(char)
#     print(vow)
#     print(con)


# word="abcdefghij"
# con_vow_checker(word)

# my_list = [3, 6, 5, 8]
# number = 0

# for digit in my_list:
#     number = number * 10 + digit

# print(number)  # Output: 3658


# def missing_number(numbers):
#     # Edge case: empty list
#     if not numbers:
#         print("List is empty.")
#         return
    
#     # Find the expected max based on sequence (assuming numbers should be 1 to max_value)
#     max_value = max(numbers)
    
#     # Check for missing numbers between 1 and max_value
#     missing = []
#     for x in range(1, max_value + 1):  # Include max_value in the check
#         if x not in numbers:
#             missing.append(x)
    
#     if missing:
#         print("Missing number(s):", missing)
#     else:
#         print("No missing numbers found.")

# # Example usage
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# missing_number(numbers)

name = input("Name: ")
name_list = []

for item in name:
    name_list.append(item)
    
print(name_list)