def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def execute_function(func, *args):
    return func(*args)

def main():
    
    num1 = 10
    num2 = 5

    addition_result = execute_function(add, num1, num2)
    print(f"addition: {addition_result}")

    subtraction_result = execute_function(subtract, num1, num2)
    print(f"subtraction: {subtraction_result}")

if __name__ == "__main__":
    main()
