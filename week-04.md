# ISYS5002 - Week 4

_Adapted from original materials written by Michael Borck._

We'll learn how to decompose a simple calculator programme into smaller, manageable parts. Instead of facing one long "wall of code," we'll break it into clear, individual steps. This approach helps your mind focus on one task at a time, making the overall problem much easier to understand.

## 1. Guided Walkthrough

**Guided Walkthrough:**  

This is a guided walkthrough designed to show you exactly how to break down a problem into smaller parts and implement each part as a function. Think of it as a warm-up exercise—later worksheets will let you apply these ideas independently in new contexts, such as a weather-themed temperature conversion and using third-party modules.

### Step 1: The Original "Wall of Code"

Below is a basic calculator programme that does everything in one go. It displays a menu, gets input from the user, performs a calculation, and then shows the result. You can run the code if you like to see that it works.

```python
# Define the calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Display the menu
print("Simple Calculator Menu")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get the user's choice
choice = input("Enter your choice (1-4): ")

# Get the two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the chosen operation
if choice == "1":
    result = add(num1, num2)
elif choice == "2":
    result = subtract(num1, num2)
elif choice == "3":
    result = multiply(num1, num2)
elif choice == "4":
    result = divide(num1, num2)
else:
    result = "Invalid choice."

# Display the result
print("Result:", result)
```

### Step 2: Problem Decomposition

Even though the code above works, it can be hard to understand because it does many things at once. Let's break it down into these simple steps:

1. **Display the Menu:** Show the calculator options.
2. **Get the User's Choice:** Ask which operation to perform.
3. **Get the Numbers:** Ask the user for two numbers.
4. **Perform the Calculation:** Use the chosen operation to compute a result.
5. **Display the Result:** Show the computed result to the user.

By splitting the problem into these steps, we make it easier to focus on each part individually.

### Step 3: Create a Function to Display the Menu

First, let’s create a function that displays the calculator menu and gets the user's choice.

**Pseudo-code:**

```
function get_operation():
    Display "Simple Calculator Menu"
    Display "1. Add"
    Display "2. Subtract"
    Display "3. Multiply"
    Display "4. Divide"
    Prompt user for choice
    Return the user's choice
```

**Code:**

```python
def get_operation():
    print("Simple Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice (1-4): ")
    return choice
```

### Step 4: Create a Function to Get a Number

**Pseudo-code:**

```
function get_number(prompt):
    Ask the user for a number using the provided prompt
    Convert the input to a float
    Return the number
```

**Code:**

```python
def get_number(prompt):
    return float(input(prompt))
```

### Step 5: Create a Function to Perform the Calculation

**Pseudo-code:**

```
function perform_calculation(operation, num1, num2):
    if operation is "1":
        return add(num1, num2)
    else if operation is "2":
        return subtract(num1, num2)
    else if operation is "3":
        return multiply(num1, num2)
    else if operation is "4":
        return divide(num1, num2)
    else:
        return "Invalid choice."
```

**Code:**

```python
def perform_calculation(operation, num1, num2):
    if operation == "1":
        return add(num1, num2)
    elif operation == "2":
        return subtract(num1, num2)
    elif operation == "3":
        return multiply(num1, num2)
    elif operation == "4":
        return divide(num1, num2)
    else:
        return "Invalid choice."
```

### Step 6: Improve the Divide Function with Simple Error Checking

We haven’t discussed error handling in depth yet, but we can add a simple check to the `divide()` function to prevent division by zero. This is a common error that can crash a programme. We will discuss error handling more thoroughly later in the semester; for now, we’ll add this basic check.

**Pseudo-code:**

```
function divide(a, b):
    if b equals 0:
        return "Error: Cannot divide by zero."
    else:
        return a divided by b
```

**Code:**

```python
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    else:
        return a / b
```

### Challenge: The Final Modular Code

Now, put all these functions together in our main script, and:

- Try adding a new operation, such as modulus (to get the remainder). Consider:
    - Creating a new function: `def modulus(a, b): return a % b`
    - Updating the menu and the decision structure in `perform_calculation()`.
- Attempt to add error checking for non-numeric inputs, so if the user enters a letter instead of a digit, the programme displays an error message and asks for a valid number.

### Summary

The above process is known as **refactoring**. It is the process of restructuring existing computer code—changing its internal organisation—without changing its external behaviour. Refactoring improves non-functional attributes of software, including code readability and reduced complexity. This can improve maintainability and make it easier to extend your programme in the future. Although this terminology may seem advanced now, it will become useful as you progress and work with more complex code and AI responses.

## 2. More challenges

### Step 1: Discovering pyinputplus

Beginners often discover pyinputplus by exploring online tutorials, coding forums, or by browsing the Python Package Index (PyPI) when they search for ways to improve input validation. A quick search for "Python input validation library" might lead you to pyinputplus as a popular and simple solution.

Furthermore, engaging with the wider Python community—through blogs, tutorials, or course materials—can provide insights into how and why to use external libraries like pyinputplus. Reading the official documentation and experimenting with example code will help you understand its benefits and prepare you to explore other tools that extend Python's capabilities.


### Step 2: Installing pyinputplus

To use pyinputplus, you need to install it.

**Colab / Jupyter:** In a code cell in your notebook, run the following command:

```python
!pip install pyinputplus
```

**Codespaces / Visual Studio Code:** In a terminal, run:

```bash
pip install pyinputplus
```

### Step 3: pyinputplus Basics

The **pyinputplus** library provides functions like `inputInt()`, `inputFloat()`, and `inputChoice()` for getting input with built-in validation. Here are some simple examples:

```python
import pyinputplus as pyip

# Ensures the user enters a float
number = pyip.inputFloat("Enter a number: ")

# Ensures the user enters one of the provided choices
choice = pyip.inputChoice(['1', '2', '3', '4'], prompt="Enter your choice (1-4): ")
```

> *Note:* pyinputplus will repeatedly prompt the user until valid input is entered, which reduces the risk of errors from invalid data.

### Challenge: Reimplementing the Calculator

Your task is to rewrite your simple calculator code from a previous worksheet, but now use pyinputplus to handle user input. Specifically, you should:

- Replace built-in `input()` calls with `pyip.inputChoice()` for getting the operation choice.
- Replace the `input()` calls for numbers with `pyip.inputFloat()` (or `pyip.inputNum()` to allow both integers and floats).

> *Hint:*  Reuse the modular design from your previous worksheet. Your functions for performing calculations can remain largely unchanged, but the way you gather user input will now use pyinputplus.

### Challenge: advanced calculations

- **Division by Zero:**  
  Enhance your divide function by checking for division by zero. You might use an if-statement after obtaining the input, or explore pyinputplus's `applyFunc()` for additional validation.

- **Using Additional pyinputplus Options:**  
  Experiment with `pyip.inputNum()` to accept both integers and floats.  
  Try using the timeout or retry options in pyinputplus to further improve input handling.

### Version Control Reminder

As you work on this project, remember the importance of regularly saving your work to GitHub. Here are some tips:
- **Save Often:**  
  Commit your changes frequently to avoid losing your progress.
- **Meaningful Commit Messages:**  
  Write clear and descriptive commit messages. For example:
  - "Installed pyinputplus and updated input functions"
  - "Reimplemented calculator menu using pyinputplus.inputChoice()"
  - "Added error handling for division by zero"
