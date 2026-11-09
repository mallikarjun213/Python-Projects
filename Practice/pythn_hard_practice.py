# numbers = [10, -5, 0, 20, -8, 0, 15]
# postive_count = 0
# negative_count = 0
# zero_count = 0
# for i in numbers:
#     if i > 0:
#         postive_count +=1

#     elif i < 0:
#         negative_count += 1

#     else:
#         zero_count +=1

# print("postive",postive_count)
# print("negative", negative_count)
# print("zero", zero_count)



# def find_largest_even(numbers):
#     largest_even = None
#     for i in numbers:
#         if i % 2 == 0:
#             if largest_even is None  or i > largest_even:
#                 largest_even = i

#     return largest_even

# print(find_largest_even([3, 12, 7, 18, 5, 24, 11]))
# print(find_largest_even([3, 7, 9, 11]))
# print(find_largest_even([-12, -5, -2, -9]))
# print(find_largest_even([]))



# def analyze_numbers(*args):
#     total_numbers_count = 0
#     postive_numbers_count = 0
#     negative_numbers_count = 0
#     zero_count = 0
#     for i in args:
#         if i > 0:
#             postive_numbers_count += 1

#         elif i < 0:
#             negative_numbers_count += 1

#         else:
#             zero_count += 1

#         total_numbers_count += 1

#     return(total_numbers_count , postive_numbers_count , negative_numbers_count , zero_count)

# print(analyze_numbers(10, -5, 0, 20, -8, 0))

# print(analyze_numbers(5, 10, 15))

# print(analyze_numbers(-2, -4, -6))

# print(analyze_numbers())
    


# def student_report(**kwargs):
#     total_student = 0

#     highest_marks = None
#     highest_marks_student = []

#     lowest_marks = None
#     lowest_marks_student = None
    
#     total_marks = 0

   

#     dic = {}


#     for key , value in kwargs.items():
#         if highest_marks is None or value > highest_marks:
#             highest_marks = value
#             highest_marks_student.clear()
#             highest_marks_student.append(key)

#         elif value == highest_marks_student:
#             highest_marks_student.append(key)

#         if lowest_marks is None or value < lowest_marks:
#             lowest_marks = value
#             lowest_marks_student = key

#         total_marks += value

#         total_student += 1

#     if total_student == 0:
#         average = 0
#     else:
#         average = total_marks / total_student

#     dic["total_students"] = total_student
#     dic["topper"]= highest_marks_student
#     dic["highest_marks"] = highest_marks
#     dic["lowest_student"]= lowest_marks_student
#     dic["lowest_marks"] = lowest_marks
#     dic["average"] = average


#     return dic
# # print(student_report(Anu=95, Ravi=75, Kiran=85, Sneha=60))

# # print(student_report())
# print(student_report(Anu=95, Ravi=75, Kiran=85))
# print(student_report(Anu=95, Ravi=75, Kiran=95))
# print(student_report(Anu=70, Ravi=90, Kiran=100))



# def find_smallest(numbers):
#     smallest = None

#     for i in numbers:
#         if smallest is None or i < smallest:
#             smallest = i

#     return smallest

# print(find_smallest([-8, -4, -10, -2]))

 


# def find_smallest_even(numbers):
#     smallest_even = None

#     for i in numbers:
#         if i % 2== 0:
#             if smallest_even is None or i < smallest_even:
#                 smallest_even = i

#     return smallest_even
# # print(find_smallest_even([3, -8, 5, -12, 7, 4]))
# print(find_smallest_even([]))
# print(find_smallest_even([3, 5, 7, 9]))



# def find_largest_odd(numbers):
#     largest_odd_numbers = None

#     for i in numbers:
#         if i % 2 != 0 and (largest_odd_numbers is None or i > largest_odd_numbers):
#             largest_odd_numbers = i

#     return(largest_odd_numbers)
# print(find_largest_odd([3, -8, 5, -12, 7, 4]))


# def find_largest_even(numbers):
#     largest_even = None

#     for i in numbers:
#         if i % 2 == 0 and (largest_even is None or i > largest_even):
#             largest_even = i


#     return largest_even



# def find_smallest_odd(numbers):
#     smallest_odd = None

#     for i in numbers:
#         if i % 2 != 0 and (smallest_odd is None or i < smallest_odd):
#             smallest_odd = i

#     return smallest_odd


# def find_second_largest_even(numbers):
#     result = sorted(numbers)
#     second_largest = result[-2]


#     return second_largest

# print(find_second_largest_even([4, 12, 8, 20, 16, 6]))




# def find_second_largest_even(numbers):
#     even_numbers = []

#     for i in numbers:
#         if i % 2== 0:
#             even_numbers.append(i)

#     result = sorted(set(even_numbers))

#     if len(result) < 2:
#         return None

#     return result[-2]


# score = 50

# def increase_score():
#     global score
#     score += 10 
#     print(score)

# increase_score()
# print(score)



# balance = 5000

# def withdraw():
#     global balance
#     balance = balance - 1000
#     print(balance)

# withdraw()
# print(balance)

# points = 100
# def update_points():
#     global points
#     points*= 3
#     print(points)

# update_points()
# print(points)



# def outer():
#     count = 0

#     def inner():
#         nonlocal count
#         count += 1
#     inner()
#     inner()
#     inner()
#     print(count)

# outer()


# def outer():
#     balance = 100

#     def deposit():
#         nonlocal balance
#         balance += 500
#         print(balance)

#     deposit()
#     deposit()
#     print(balance)


# outer()





# def welcome():
#     print("Welcome to python")

# my_func = welcome

# my_func()



# def add(a, b):
#     return a + b

# def calculator(func, x, y):
#     func = x + y
#     return func


# result = calculator(add, 10, 20)
# print(result)


# def subtract(a, b):
#     return a - b

# def calculator(func , x , y):
#     result = func(x,y)
#     return result

# result = calculator(subtract, 20, 5)
# print(result)


# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# def division(a,b):
#     if b != 0:
#         return a/b
#     else:
#         return "Cannot divide by zero"

# def subtract(a,b):
#     return a-b

# def calculator(func, x, y):
#     result = func(x,y)

#     return result


# result1 = calculator(add, 10, 20)
# result2 = calculator(multiply, 10, 20)
# result3 = calculator(division, 20,5)
# result4 = calculator(division, 20,0)
# result5 = calculator(subtract, 50, 20)

# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)



# def outer():
#     def inner():
#         return 50

#     return inner

# my_func = outer()

# print(my_func)
# print(my_func())



# def multiplier(n):
#     def multiply(x):
#         return n * x
#     return multiply 
# double = multiplier(2)
# print(double(5))



# def bank_account(balance):
#     def check_balance():
#         return balance

#     return check_balance


# account = bank_account(5000)

# print(account())



# def bank_account(balance):
#     def check_balance():
#         nonlocal balance
#         balance += amount





# def bank_account(balance):
#     transactions = []
#     total_deposit = 0
#     total_withdraw = 0
#     def check_balance():
        
#         return balance

#     def deposit(amount):
#         nonlocal balance
#         nonlocal total_deposit

#         if amount <= 0:
#             return "Invalid deposit"
#         else:
#             balance += amount
#             total_deposit += amount
#             transactions.append(f"Deposited {amount}")

#             return balance

#     def withdraw(amount):
#         nonlocal balance
#         nonlocal total_withdraw
    
#         if amount == 0 or amount < 0:
#             return "Invalid amount"
#         elif amount > balance:
#             return "Insufficient Balance"
#         else:
#             balance -= amount
#             total_withdraw += amount
#             transactions.append(f"withdraw {amount}")
#             return balance

#     def show_transaction():
#         return transactions

#     def show_summary():
#         return total_deposit, total_withdraw

#     return check_balance ,deposit , withdraw, show_transaction, show_summary


# account = bank_account(5000)

# check_balance ,deposit , withdraw, history , summary = account


# deposit(1000)
# withdraw(500)
# deposited, withdrawn = summary()
# print(history())
# print(summary())



# def make_multiplier(number):
#     def multiply(n):
#         result = number * n
#         return result

#     return multiply

# value = make_multiplier(8)

# print(value(4))



# def bank_account():
#     balance = 10000

#     def withdraw(amount):
#         nonlocal balance
#         balance = balance - amount
#         return balance

#     return withdraw

# account = bank_account()
# print(account(2000))
# print(account(1000))
# print(account(500))


# def bank_account():
#     balance = 5000

#     def deposoit(amount):
#         nonlocal balance
#         balance += amount
#         return balance

#     return deposoit

# amount = bank_account()

# print(amount(1000))
# print(amount(2000))
# print(amount(500))



# def add():
#     return 10 + 20

# def show_result(func):
#     result = func()
#     print(result)

# show_result(add)


# def main_function():
#     def wellcome():
#         print("Hello Python")

#     return wellcome

# result = main_function()
# result()


# def multiply():
#     return 10 * 5

# def calculator(func):
#     return func()

# result = calculator(multiply)
# print(result)      



# def add():
#     return 20 + 10

# def subtract():
#     return 20 - 10

# def calculater(func):
#     result = func()

#     return result

# print(calculater(add))
# print(calculater(subtract))


# def student_detials():
#     name = "Ravi"
#     age = 25
#     city = "Bengaluru" 
#     return name , age , city
  
# name , age , city = student_detials()

# print(name)
# print(age)
# print(city)


# def get_result():
#     print("calculating")
#     return 50,60,70

# a,b,c = get_result()

# print(a)
# print(b)
# print(c)


# def withdraw(amount):
#     balance = 10000
#     transaction =[]
#     def withdraw_amount():
#         nonlocal balance
#         if amount > balance:
#             return "insfuciant balance"

#         elif  amount <= 0:
#             return "Invalid input"
#         else:
#             balance -= amount
#             transaction.append(f"withadraw amout {amount}")
#             return "withdraw successfull"

# amount = withdraw(0)

# print(amount)



# def bank_account():
#     balance = 10000
#     transactions = []

#     def withdraw(amount):
#         nonlocal balance
#         if type(amount) is not int:
#             return "Invalid input"
#         elif amount <= 0:
#             return("Invalid amount")
#         elif amount > balance:
#             return("Insufficient balance")
#         else:
#             balance -= amount
#             transactions.append(f"withdraw amount {amount}")
#             return balance

#     def show_history():
#         return transactions

#     return withdraw, show_history

# withdraw, history = bank_account()

# print(withdraw(5000))
# print(withdraw(-500))
# print(withdraw(True))
# print(history())




# def bank_account():
#     balance = 10000
#     transactions = []

#     def deposit(amount):
#         pass

#     def withdraw(amount):
#         pass

#     def show_history():
#         return transactions

#     def reset_account():
#         nonlocal balance
#         balance = 10000
#         transactions.clear()
#         return balance

#     return deposit, withdraw, show_history, reset_account


# deposit, withdraw, history, reset = bank_account()

# print(deposit(2000))
# print(withdraw(1000))

# print("Before Reset:", history())

# print("Reset Balance:", reset())

# print("After Reset:", history())




# def count(n):
#     if n == 0:
#         return

#     print(n)
#     count(n-1)

# count(3)



# def sum_numbers(n):
#     if n == 0:
#         return 0
#     return n + sum_numbers(n-1)
 
# print(sum_numbers(5))



# def factorial(n):
#     if type(n) is not int:
#         return "Invalid input"
#     elif n < 0:
#         return "Invalid input"
#     elif n == 0:
#         return 1

#     return n * factorial(n-1)

# print(factorial(5))
# print(factorial(0))
# print(factorial(-3))
# print(factorial(5.5))
# print(factorial("hello"))
# print(factorial(True))



# def factorial(n):
#     result = 1
#     if type(n) is not int:
#         return "Invalid input"
#     elif n < 0:
#         return "Invalid input"
#     else:

#         for i in range(1, n + 1 ):
#             result *= i
#         return result

# print(factorial(5))




# add_ten = lambda n : n + 10

# print(add_ten(5))


# subtract = lambda a,b : a - b

# print(subtract(5,4))


# largest = lambda a, b : a  if a > b else b
# print(largest(10,25))


# numbers = [2, 4, 6, 8]

# result = list(map(lambda n: n * n , numbers))

# print(result)



# numbers = [5, 10, 15, 20]

# result = list(map(lambda n: n + 100 , numbers))

# print(result)


# numbers = [2, 4, 6, 8]

# result = list(map(lambda n: n * 3 , numbers))

# # print(result)

# numbers = [3, 5, 7, 9]

# result = list(map(lambda n: n * n , numbers))

# print(result)


# numbers = [5, 10, 15, 20]

# result = list(map(lambda n: n + 10 , numbers))

# result_2 = list(map(lambda n: "even" if n % 2 == 0 else "odd", result))

# print(result_2)



# numbers = [5, 10, 15, 20, 25, 30]


# result = list(filter(lambda n:  n % 2 == 0 , numbers))

# print(result)



# numbers = [5, 12, 8, 25, 10, 30, 3]

# result = list(filter(lambda n: n > 10, numbers))

# print(result)



# numbers = [10, -5, 20, -15, 0, 8, -3]

# result = list(filter(lambda n: n < 0 , numbers))

# print(result)


# numbers = [2, -4, 6, -8, 9, 12, 15, 0]


# result = list(filter(lambda n:  n > 0 , numbers))

# result_2 = list(filter(lambda n: n % 2 == 0 , result))
# print(result_2)
 

# numbers = [5, 12, 15, 20, 23, 30, 35, 8]

# result = list(filter(lambda n: n > 10 and n % 2 != 0, numbers))

# print(result)


# numbers = [2, 5, 8, 11, 14, 17, 20]

# result_1 = list(filter(lambda n: n% 2==0 , numbers))
# result_2 = list(map(lambda n: n + 10, result_1)) 

# print(result_2)

# numbers = [-3, 2, -5, 4, 6, -1, 8]


# result_1 = list(filter(lambda n: n > 0, numbers))

# result_2 = list(map(lambda n: n*n , result_1))

# print(result_2)



from functools import reduce

# numbers = [5, 10, 15, 20]


# result = reduce(lambda a , b : a + b , numbers)

# print(result)


# numbers = [2, 3, 4, 5]

# result = reduce(lambda a , b : a * b , numbers)

# print(result)



# numbers = [15, 8, 25, 12, 30, 5]

# result = reduce(lambda a, b: a if a > b else b , numbers)

# print(result)



# numbers = [15, 8, 25, 12, 30, 5]

# result = reduce(lambda a,b : a if a < b else b , numbers)

# print(result)



# numbers = [10, -5, 20, -8, 15, 0, -3]

# result_1 = list(filter(lambda n: n > 0 , numbers ))

# result_2 = reduce(lambda a, b : a + b , result_1) 

# print(result_2)



# numbers = [5, 12, 8, 20, 3, 15, 10]

# result_1 = list(filter(lambda n: n > 10 , numbers))

# result_2 = list(map(lambda n: n* n , result_1))

# result_3 = reduce(lambda a , b : a + b , result_2)

# print(result_3)



# prices = [100, 250, 150, 300, 200]

# result = reduce(lambda a,b : a + b , prices)

# print(result)


# prices = [450, 120, 890, 300, 650, 200]

# result = reduce(lambda a, b : a if a > b else b , prices)

# # print(result)


# prices = [500, 1200, 800, 2000, 300]

# result_1 = list(filter(lambda n:  n > 500 , prices))

# result_2 = list(map(lambda n: n * 10 / 100 , result_1))

# result_3 = reduce(lambda a, b : a + b , result_2)



# prices = [1000, 500, 1500, 2000, 800]

# result_1 = list(filter(lambda n: n > 1000 , prices))

# result_2 = list(map(lambda n: n * 20 / 100 , result_1))

# result_3 = reduce(lambda a, b : a + b , result_2)

# print(result_3)


# prices = [500, 1200, 800, 2000, 300, 1500]


# result_1 = list(filter(lambda n: n > 1000 , prices))

# result_2 = list(map(lambda n: n - (n * 15 / 100) , result_1))

# result_3 = reduce(lambda a,b : a + b , result_2)

# print(result_3)


# marks = [45, 80, 92, 35, 67, 88, 25, 95]


# result = list(filter(lambda n: n > 60 , marks))

# result_1 = list(map(lambda n: n + (n * 5 / 100), result))

# result_2 = reduce(lambda a , b : a + b , result_1)

# print(result_2)


# def my_decorator(func):
#     def wrap():
#         print("Starting python")
#         func()
#         print("Python completed")

#     return wrap

# @my_decorator
# def greet():
#     print("good mornning")


# # greet()




# def my_decorator(func):
#     def wrap(*args, **kwargs):
#         print("Function Started")
#         result = func(*args, **kwargs)
#         print("Function Ended")
#         return result
#     return wrap
# @my_decorator
# def greet(name):
#     return "Hello " + name

# x = greet("ravi")
# print(x)



# def my_decorate(func):
#     def wrap(*args, **kwargs):
#         print("Starting Calculation")

#         result = func(*args, **kwargs)

#         return result * 2
#     return wrap
# @my_decorate
# def multiply(a, b):
#     return a * b

# x = multiply(10,10)

# print(x)



# def my_decorate(func):
#     def wrap(*args , **kwargs):
#         print("Processing Started")
#         result = func(*args, **kwargs)
#         print("Orignal result:",result)
#         return result + 50

#     return wrap

# @my_decorate
# def calculate(a, b):
#     return a + b

# x = calculate(50 , 30)

# print("final result:", x)



# def my_decorate(func):
#     def wrap(*args, **kwargs):
#         print("Calculation Started")
#         result = func(*args, **kwargs)
#         print("Orginal result:", result)
#         if result % 2 == 0:
#             return result + 100
#         else:
#             return result
#     return wrap

# @my_decorate
# def calculate(a, b):
#     return a + b

# x1 = calculate(10, 20)
# x2 = calculate(10, 15) 

# print("final 1:" , x1)
# print("final 1:" , x2)


# def my_decorator(func):
#     def wrap(*args , **kwargs):
#         result = func(*args , **kwargs)
#         print("Original bill amount:" , result)

#         if result >= 1000:
#             discount = result * 20 / 100
#             return result - discount
#         else:
#             discount = result
#             return discount
#     return wrap

# @my_decorator
# def calculate_bill(a):
#     return a 


# x1 = calculate_bill(1200)
# x2 = calculate_bill(800) 


# print("final bill 1:", x1)
# print("final bill 2:", x2)



# def my_decorator(func):
#     def warp(*args , **kwargs):
#         print("Student Result Started")
#         result = func(*args, **kwargs)
#         name = kwargs.get("name", args[0] if args else None)
#         marks = kwargs.get("marks", args[1] if len(args) > 1 else None)

#         print("Name:", name)
#         print("Marks:", marks)

#         if marks >= 35:
#             print("pass")
#         else:
#             print("fail")

#         return result
      
  


#     return warp



# @my_decorator
# def student_result(name, marks):
#     return marks 

# x1 = student_result("Ravi", 80)
# x2 = student_result(name="Kiran", marks=30)

# print(x1)
# print(x2)



# def add(a, b):
#     return a + b

# x = add(10, 20)
# print(x)


# def check_number(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# result = check_number(10) 
# print(result)

# result = check_number(7)  
# print(result)



# def largest(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# result = largest(10, 20)
# print(result)
# result = largest(50, 30)
# # print(result)


# def largest(a,b,c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)

# largest(10, 20, 30)  # 30
# largest(50, 30, 40)  # 50
# largest(10, 60, 40)  # 60



# def total_sum(*args):
#     list_1 = list(*args)
#     result = sum(list_1)
#     return result

# final_result = total_sum([10, 20, 30])
# print(final_result)
# final_result = total_sum([5, 5, 5, 5])
# print(final_result)


# def total_sum(numbers):
#     result = 0

#     for num in numbers:
#         result += num

#     return result

# final_result = total_sum([10, 20, 30])
# print(final_result)
# final_result = total_sum([5, 5, 5, 5])
# print(final_result)


# def count_even(n):
#     count = 0

#     for i in n:
#         if i % 2 == 0:
#             count += 1

#     return count

# result = count_even([10, 15, 20, 25, 30])
# print(result)

# result = count_even([1, 3, 5, 7])
# print(result)


# def postive_numbers(n):

#     postive_count = 0

#     for i in n:
#         if i > 0:
#             postive_count += 1

#     return postive_count

# result = postive_numbers([-5, 10, 20, -2, 0, 8])
# print(result)



# def find_max(n):
#     largest_number = None

#     for i in n:
#         if largest_number is None or i > largest_number:
#             largest_number = i

#     return largest_number

# result = find_max([10, 50, 20, 80, 30])

# print(result)

# def find_min(n):
#     smallest = None

#     for i in n:
#         if smallest is None or i < smallest:
#             smallest = i

#     return smallest

# result = find_min([10, 50, 20, 5, 30])

# print(result)


# def count_number(n , target):
#     count = 0

#     for i in n:
#         if i == target:
#             count += 1

#     return count

# result = count_number([10, 20, 10, 30, 10], 10)
# # print(result)


# def sum_of_even(n):
#     total_sum = 0

#     for i in n:
#         if i % 2 == 0:
#             total_sum += i

#     return total_sum


# result = sum_of_even([10, 15, 20, 25, 30])
# print(result)

# result = sum_of_even([1, 3, 5, 7])
# print(result)


# def add(a , b)-> int:
#     return a + b

# result = add(10 , 10)

# print(result)



# def get_number(n):
#     try:
#         result = int(n)
#         return result
#     except ValueError:
#         return "Please enter a valid number"

# final = get_number("hello")
# print(final)
# final = get_number(100)
# print(final)


# def even_numbers(n):

#     for i in range(1, n+1):
#         if i % 2 == 0:
#             yield i
# result = even_numbers(10)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


# def odd_numbers(n):
#     for i in range(1 , n+1):
#         if i % 2 != 0:
#             yield i

# result = odd_numbers(10)

# for i in result:
#     print(i)


# def square_number(n):

#     for i in range(1, n + 1):
#         yield i * i

# result = square_number(5)

# for i in result:
#     print(i)



# def calculate_marks(marks):
#     total_marks = 0
#     count = 0

#     for i in marks:
#         total_marks += i
#         count += 1

#     average = total_marks / count

#     return average

# print(calculate_marks([80, 70, 90, 60]))



# def calculate_marks(marks):
#     total_marks = 0

#     for i in marks:
#         total_marks += i

#     average = total_marks / len(marks)

#     if average >= 35:
#         result = "Pass"
#     else:
#         result = "Fail"

#     return average, result

# average , result = calculate_marks([80, 70, 90, 60])

# print(average)
# print(result)

# from functools import reduce


# def calculate_total(*args):
#     total = 0

#     for i in args:
#         total += i


#     return total


# print(calculate_total(10, 20, 30, 40, 50))



# def find_max(*args):
#     largest = None

#     for i in args:
#         if largest is None or i > largest:
#             largest = i

#     return largest
# print(find_max(10, 50, 20, 90, 40))




# def find_min(*args):
#     smallest = None

#     for i in args:
#         if smallest is None or  i < smallest:
#             smallest = i

#     return smallest


# print(find_min(10, 50, 20, 90, 40))



# def count_even(*args):
#     even_count = 0

#     for i in args:
#         if i% 2== 0:
#             even_count += 1
#     return even_count

# print(count_even(10, 15, 20, 25, 30, 35))



# def sum_even(*args):
#     sum_of_even = 0

#     for i in args:
#         if i % 2 == 0:
#             sum_of_even += i

#     return sum_of_even

# print(sum_even(10, 15, 20, 25, 30, 35))



# def student_details(**kwargs):
#     for key , value in kwargs.items():
#         print(key,value)


# student_details(name="Rahul", age=22, city="Bengaluru")


# def student_info(*args, **kwargs):
#     for args , kwargs in args , kwargs.items():
#         print(args)
#         print(kwargs)
# student_info("Python", "AI", name="Rahul", age=22)



# def calculate_total(*args, tax=0):
#     total = 0
#     for i in args:
#         total += i 

    
#     tax_amount = total * tax / 100

#     total += tax_amount

#     return total

# print(calculate_total(100, 200, 300, tax=10))


     
# def calculate_bill(*args , discount = 0):

#     total = 0

#     for i in args:
#         total += i

#     discount = total * discount / 100

#     final_amount  = total - discount

#     return final_amount


# # print(calculate_bill(500, 300, 200, discount=10))

# def add_student(name , age , marks):
#     student_data = {}
#     student_data["Name"] = name
#     student_data["Age"] = age
#     student_data["Marks"] = marks


# def calculate_average(student):
    

# student = add_student("Rahul", 22, [80, 70, 90])
# average = calculate_average(student)
# print(average)




# students = [
#     {"name": "Rahul", "age": 22, "marks": [80, 70, 90]},
#     {"name": "Priya", "age": 21, "marks": [60, 75, 85]}
# ]

# for student in students:
#     print(student[0]["name"])


# students = [
#     {"name": "Rahul", "age": 22, "marks": [80, 70, 90]},
#     {"name": "Priya", "age": 21, "marks": [60, 75, 85]}
# ]

# students.append({"name":"anu", "marks": [80,85,90], "age": 22})

# # print(students)


# for student in students:
#     print(student["name"])
#     print(student["age"])



# students = [
#     {"name": "Rahul", "age": 22, "marks": [80, 70, 90]},
#     {"name": "Priya", "age": 21, "marks": [60, 75, 85]}
# ]
# def calculate_average()
#     marks = student["marks"]

#     total = 0
#     for i in marks:
#         total += i

#     average = total / len(marks)

#     print(student["name"], average)


# def student_data(name,age,marks):
#     dictionary = {}

#     dictionary["name"] = name
#     dictionary["age"] = age
#     dictionary["marks"] = marks
#     return dictionary

# students = []

# student1 = student_data("Rahul", 22, [80, 70, 90])
# student2 = student_data("Priya", 21, [60, 75, 85])
# student3 = student_data("Kiran", 23, [75, 85, 95])





# def student_data(name, age, marks):
#     dictionary = {}

#     dictionary["name"] = name
#     dictionary["age"] = age
#     dictionary["marks"] = marks

#     return dictionary


# students = []

# student1 = student_data("Rahul", 22, [80, 70, 90])
# student2 = student_data("Priya", 21, [60, 75, 85])
# student3 = student_data("Kiran", 23, [75, 85, 95])

# students.append(student1)
# students.append(student2)
# students.append(student3)

# print(students)





# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def multiply(a,b):
#     return a * b

# def division(a , b):
#     return a / b

# def moduels(a , b):
#     return a % b

# def power(a, b):
#     return a ** b

# while True:
#     try:
#         num1 = float(input("Enter number1: "))
#         operation = input("Enter your choice: (+ , - , x , / , %, **, Exit : ").strip().lower()
#         if operation == "exit":
#             print("Calculator closed. Thank you!")
#             break
#         num2 = float(input("Enter number2: "))


#         if operation == "+":
#             print("Addition selected")
#             result = add(num1,num2)
#             print(result)

#         elif operation == "-":
#             print("Subtraction selected")
#             result = sub(num1,num2)
#             print(result)

#         elif operation == "*":
#             print("Multiply selected")
#             result = multiply(num1 , num2)
#             print(result)

#         elif operation == "/":
#             if num2 != 0:
#                 print("Division selecyted")
#                 result = division(num1, num2)
#                 print(result)
#             else:
#                 print("Cannot divided by zero")
#                 break

#         elif operation == "%":
#             if num2 != 0:
#                 print("moduels selected")
#                 result = moduels(num1 , num2)
#                 print(result)
#             else:
#                 print("Cannot moduls by zero")
#                 break

#         elif operation == "**":
#             print("power selected")
#             result = power(num1 , num2)
#             print(result)

#         else:
#             print("Invalid opreation")
#             break

#     except ValueError:
#         print("Enter valid input only")
#         break


# Student Management System

# students = []
# pass_count = 0
# fail_count = 0

# def add_student(name,age,marks):
#     student = {}
#     student["Name"] = name
#     student["Age"] = age
#     student["Marks"] = marks

#     return student

# result = add_student("Rahul", 22 , [80, 70, 90])
# students.append(result)
# result = add_student("Priya", 21 , [90, 85, 95])
# students.append(result)



# for i in students:
#     print(i["Name"], i["Age"], i["Marks"])
#     total = 0
#     total += sum(i["Marks"])
#     i["Total"] = total
#     print(i["Name"], total)

#     average = total / len(i["Marks"])
#     i["Average"] = average
#     print(average)


#     if average >= 35:
#         i["Result"] = "Pass"
#         print("Pass")
#         pass_count += 1
#     else:
#         print("Fail")
#         i["Result"] = "Fail"
#         fail_count +=1

# for i in students:
#     print(i) 


# search_name = input("Search name: ").strip().lower()
# found = False
# for i in students:
#     if search_name == i["Name"].lower():
#         print(i)
#         found = True


# if found == False:
#     print("Student not found")


# delete_name = input("Delete name: ").strip().lower()
# found = False

# for i in students:
#     if delete_name == i["Name"].lower():
#         students.remove(i)
#         print("Student deleted successfully")
#         found = True
#         break

# if found == False:
#     print("Student not found")

# print("After Delete:")



# name = input("Enter student name: ").strip().lower()
# age = int(input("Enter student age: ").strip())
# marks = list(map(int, input("Enter student marks: ").strip().split()))

# result = add_student(name, age, marks)
# students.append(result)
# print("Student added successfully")
# print(students)


# total = sum(result["Marks"])

# result["Total"] = total


# average = total / len(result["Marks"])
# result["Average"] = average


# if average >= 35:
#     result["Result"] = "Pass"
   
# else:
#     result["Result"] = "Fail"

# print(result)


# for i in students:
#     print(i["Name"],round(i["Average"], 2))
#     print(f"Name: {i['Name']} | Total: {i['Total']} | Average: {round(i['Average'], 2)} | Result: {i['Result']} | Age: {i["Age"] } | Marks: {i["Marks"]}")

# pass_count = 0
# fail_count = 0

# for i in students:
#     if i["Result"] == "Pass":
#         pass_count += 1
#     else:
#         fail_count += 1

# print("Total Students:", len(students))
# print("Pass Students:", pass_count)
# print("Fail Students:", fail_count)



balance = 1000

def deposit(amount):
    global balance
    if amount <= 0:
        return "Invalid input"
    else:
        balance += amount

    return balance

def withdraw(amount):
    global balance
    if amount <= 0:
        return "Invalid input"
    elif amount > balance:
        return "insufficient balance"
    else:
        balance-= amount

    return balance


def check_balance():
    return balance


def main():
    print("Welcome to Banking system")
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                deposit_amount  = int(input("Enter the amount: ").strip())
            except ValueError:
                print("Please enter numbers only")
                continue

        
            result = deposit(deposit_amount)

            if result != "Invalid input":
                print("Deposit successful")
                print("Current Balance:", result)
                
            else:
                print("Deposit failed:", result)

        elif choice == "2":
            try:
                withdraw_amount = int(input("Enter the withdraw amount: ").strip())
            except ValueError:
                print("Please enter numbers only")
                continue

            result = withdraw(withdraw_amount)
            if result != "Invalid input" and result != "insufficient balance":
                print("Withdraw successful")
                print("Current Balance:", result)
                
            else:
                print("Withdraw failed:", result)

        elif choice == "3":

            result = check_balance()
            print("Current Balance:", result)
            
        
        elif choice == "4":
            print("Thank you for banking!")
            break

        else:
            print("Invalid choice")
            

main()

