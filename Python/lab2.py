# 1 - Ask the user to enter 5 numbers.
# Store them, then display them in ascending order and descending order.
def list_order(nums):
        print(f"Numbers in asc order: {sorted(nums)}")
        print(f"Numbers in asc order: {sorted(nums, reverse=True)}")



# 2 - Write a function that takes two numbers: (length, start).
#     Generate a sequence of numbers with the given length,
#     starting from the given start number and increasing by one each time.
#     Print the result.

def generate_sequence(start, length):
    print("Sequence is : ", [num for num in range(start, start+length)])


# 3 - Keep asking the user for numbers until they type "done".
#         When finished, print:
#             * The total of all numbers entered
#             * The count of valid entries
#             * The average

def math_ops(nums):
    print(f"Numbers count is: {len(nums)}")
    print(f"Numbers Total is: {sum(nums)}")
    print(f"Numbers AVG is: {sum(nums)/len(nums)}")

# 4 - Ask the user to enter a list of numbers.
# Remove any duplicates, sort the result, and display it.

def remove_duplicates(nums):
    print(f"Unduplicate Orderd list is: {sorted(list(set(nums)))}")


# 6 - Ask the user to enter a sentence.
# Count how many times each word appears in the sentence
# and display the result.

def words_count(sentence):
    hash = {}

    for word in sentence.split():
        if word not in hash:
            hash[word] = 1
        else:
            hash[word] += 1
    
    for key, value in hash.items():
        print(f"word: {key} => {value} time(s)")


#  7 - Create a small gradebook system:
#         - The user enters 5 students names and their scores.
#         - At the end, show:
#             * The highest score
#             * The lowest score
#             * The average score.

def gradebook(scores):
    print(f"max score is: {max(scores)}")
    print(f"lowest score is: {min(scores)}")
    print(f"avg scores is: {sum(scores)/len(scores)}")

#  8 - Write a program that simulates a shopping cart:
#         - The user can add items with a name and a price.
#         - The user can remove items by name.
#         - The user can view all items with their prices.
#         - At the end, display the total cost.

def shopping_cart():
    hash = {"item1": 50, "item2": 100}
    while True:
        print("###### Shopping Cart ######## ")
        print("""
        1 - Add item (name price)
        2 - Remove item (name)
        3 - View Items
        4 - Total cost 
        0 - exist
        """)
        try : 
            userIput = int(input("Enter Your Choice: "))
            if userIput == 1:
                item = input("Enter item name and price: ").split()
                if item[0] not in hash:
                    hash[item[0]] = int(item[1])
                    print("item added")
                else:
                    print("item already exist")
            elif userIput == 2:
                item = input("Enter item name to remove: ")
                if item in hash:
                    hash.pop(item)
                else:
                    print("item not found")
            elif userIput == 3:
                if not hash:
                    print("No items in the cart")
                else:
                    for key, value in hash.items():
                        print(f"item: {key} => price: {value}")
            elif userIput == 4:
                print(f"total cost is: {sum(hash.values())}")
            elif userIput == 0:
                break
            else:
                print("Invalid Input")

        except :
            print("Enter an integer only")

    # 9 - Create a number guessing game:
#         - The program randomly selects a number between 1 and 20.
#         - The user keeps guessing until they get it right.
#         - After each guess, show if the guess was too high or too low.
#         - When correct, display the number of attempts
import random   

def guesing_game():
    # number = random.randint(1, 20)
    number = 10
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 20")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 20:
                print("Please guess a number within the range of 1 to 20.")
                continue
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                break
        except:
            print("Invalid input. Please enter a valid number.")
####################################################################
while True: 
    print("#### Choose Function ####")
    print("""
        1 - List Order
        2 - Generate Series
        3 - Math Operations 
        4 - Remove Duplicates
        5 - Count Words in Sentence
        6 - Grade Book System
        7 - Shopping Cart
        8 - Gessing Game
        0 - Exist 
""")
    try:
        userInput = int(input("Enter Your Choice: "))
        
        if userInput == 1:
            while True:
                try:
                    nums = list(map(int, input("Please Enter 5 numbers: ").split()))
                    if len(nums) != 5:
                        print(f"You entered {len(nums)} numbers, Please enter 5 integers")
                        # break
                    else:
                        list_order(nums)
                        break
                except: 
                    print("Invalid Input, Please enter integer values")
        
        elif userInput == 2:
            while True:
                try:
                    l = list(map(int, input("Please Enter sequence start and length: ").split()))
                    if len(l) != 2:
                        print(f"You entered {len(l)} number(s), Please enter 2 integers for start and length only")
                        # break
                    else:
                        start, length = l
                        generate_sequence(start, length)
                        break
                except: 
                    print("Invalid Input, Please enter integer values")
        
        elif userInput == 3:
            nums = []
            while True:
                n = input("Enter a number: ")
                if n == "done" : 
                    break
                elif n.isdigit():
                    print("appended")
                    nums.append(int(n))
                else:
                    print("pleaes enter integer number")
                
            math_ops(nums)
            break
        
        elif userInput == 5:
            while True:
                
                sentence = input("Enter a sentence: ")
                words_count(sentence)
                break
        
        elif userInput == 0:
            print("Thanks bro")
            break

        elif userInput == 6:
            while True:
                try: 
                    scores = []
                    for i in range(5):
                        data = input(f"Please Enter name score ({i+1}/5): ").split()
                        scores.append(int(data[1]))
                    
                    gradebook(scores)
                    break
                except:
                    print("Invalid Input, Please enter names and scores in this formate =>  name score")
        elif userInput == 7:
            shopping_cart()

        elif userInput == 8:
            guesing_game()

        elif userInput == 0:
            print("Thanks bro")
            break
            
        else:
            print("Invalid Input")
    except:
        print("Enter Integer Value")
    

