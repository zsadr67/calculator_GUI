import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "خطا")

def clear():
    entry.delete(0, tk.END)
import tkinter as tk

# محاسبه عبارت ریاضی به صورت دستی
def calculate_expression(expr):
    try:
        tokens = []
        num = ''
        for char in expr:
            if char in '0123456789.':
                num += char
            else:
                if num:
                    tokens.append(float(num))
                    num = ''
                tokens.append(char)
               
                
        if num:
            tokens.append(float(num))

        # اولویت ضرب و تقسیم
        i = 0
        while i < len(tokens):
            if tokens[i] == '*':
                tokens[i-1] = tokens[i-1] * tokens[i+1]
                del tokens[i:i+2]
            elif tokens[i] == '/':
                tokens[i-1] = tokens[i-1] / tokens[i+1]
                del tokens[i:i+2]
            else:
                i += 1

        
        # حالا جمع و تفریق
        result = tokens[0]
        i = 1
        while i < len(tokens):
            if tokens[i] == '+':
                result += tokens[i+1]
            elif tokens[i] == '-':
                result -= tokens[i+1]
            i += 2
        
        return result
        
    except:
        return "خطا"

# ---------------------- GUI -----------------------
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def calculate():
    expr = entry.get()
    result = calculate_expression(expr)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

def clear():
    entry.delete(0, tk.END)

# ایجاد پنجره
root = tk.Tk()
root.title("ماشین حساب بدون eval")

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == '=':
            btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=calculate)
        else:
            btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: button_click(t))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

clear_btn = tk.Button(root, text='C', font=("Arial", 18), width=22, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()

# پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب")

# ورودی
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# تعریف دکمه‌ها و عملکرد آن‌ها
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == '=':
            btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
                            command=calculate)
        else:
            btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
                            command=lambda t=text: button_click(t))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

# دکمه پاک کردن
clear_btn = tk.Button(root, text='C', font=("Arial", 18), width=22, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()


def add(number1 , number2):
    return (number1 + number2)

def subtract(number1 , number2):
    return (number1 - number2)

def multiply(number1 , number2):
    return (number1 * number2)

def divide(number1 , number2):
    return (number1 / number2)

def get_number(prompt, memory):
    """Prompts the user to enter a number or use 'M' to recall memory."""
    while True:
        user_input = input(prompt)
        if user_input.upper() == "M":
            if memory:
                return memory[-1]
            else:
                print("Memory is empty. Please enter a number.")
                continue
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'M'.")


if __name__ == '__main__':

    from collections import deque
    
    mymemory = deque(maxlen=5)

    while True:

        number1 = get_number("Enter number1 (or 'M' for memory): ", mymemory)
        number2 = get_number("Enter number2 (or 'M' for memory): ", mymemory)


        operator = input("Enter operation (+ , - , * , /): ")
            

        if operator not in ["+", "-", "*", "/"]:
            print("You did not enter the correct operator")
            continue


        if operator == "+" :
            result = add(number1 , number2)
                
        elif operator == "-" :
            result = subtract(number1 , number2)
                
        elif operator == "*" :
            result = multiply(number1 , number2)
                
        elif operator == "/" :
            try:
                result = divide(number1 , number2)
                        
            except ZeroDivisionError:
                print ("number2 is zero")
                continue
    

        print(f"Result: {number1} {operator} {number2} = {result}")  

        mymemory.append(result)
        

        user_input = input("Do you want to continue, exit, or see your memory? (type 'e', 'c', or 'M'): ")

        user_input = user_input.strip().lower()
        if user_input == "e":
            break
        elif user_input == "c":
            continue
        elif user_input == "m":
            print("mymemory is:", mymemory)