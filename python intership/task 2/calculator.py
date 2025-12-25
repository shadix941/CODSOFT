def get_numbers(): #takes numbers from user
    while 1:
        nums = input("Enter the numbers: ").split()
        numbers = []
        try:
            for n in nums:
                numbers.append(float(n))
            return numbers
        except ValueError:
            print("Error: Please enter only numbers!")
def add_numbers(numbers):  #adds all numbers in list
    total=0         
    for n in numbers:
        total=total+n
    return total
def subtract_numbers(numbers): #subtracts all numbers in list
    result = numbers[0]
    for n in numbers[1:]:
        result=result-n
    return result
def multiply_numbers(numbers): #Multiplies all numbers in list
    result = 1
    for n in numbers:
        result=result*n
    return result
def divide_numbers(numbers): #divides numbers except cannot be divide by zero 
    result = numbers[0]
    for n in numbers[1:]:
        if n ==0:
            print("Cannot divide by zero")
            return None
        else:
            result=result/n
    return result
def calculator():
    last_result = None   # to store previous answer 

    while 1:
        print("\n--- CALCULATOR MENU ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice =="":
            continue
        if choice not in ["1","2","3","4","5"]:
            print("Invalid option")
            continue

        if choice == "5": #Exit condition
            print("Calculator closed.")
            break
        if last_result is not None: #ask user if  want use previous answer if not takes new numbers
            use_ans = input("Use previous answer (ANS)? yes/no: ").lower()
            if use_ans == "yes":
                numbers = [last_result]      
                more_numbers = get_numbers()   #take new numbers from the user
                numbers.extend(more_numbers)   #add the new numbers and last number to list 
            else:                              #if user dont want use last result
                numbers = get_numbers()        
        else:
            numbers = get_numbers()            #if no last result none

        if choice=="1":  
            last_result = add_numbers(numbers)

        elif choice=="2":
            last_result = subtract_numbers(numbers)

        elif choice=="3":
            last_result = multiply_numbers(numbers)

        elif choice=="4":
            last_result = divide_numbers(numbers)
        if last_result is None:
            continue
        print("Result =", last_result)

calculator()