# ISYS5002 - Week 3

_Adapted from original materials written by Michael Borck._

## 1. Crafting the Weather Menu

A user interface (UI) is the part of a computer program that allows users to interact with it. In this activity, we are using a text-based menu—a simple yet effective form of UI—to present options to the user. This approach is a great starting point because it helps you understand the fundamentals of user interaction in a program, which is a stepping stone to building more sophisticated graphical interfaces in the future.

In this activity you will create a text-based menu that presents the following options:

1. Check Temperature  
2. Check Humidity  
3. Check Wind Speed  
4. Exit  

The goal is to use the `print()` function to display these options and `input()` to capture the user’s selection. Later, you can extend your program so that each option triggers a different response in the code.

**Tip:** When planning your menu, consider how clear and concise text can help guide the user through your program.

### Step 1: Display the Menu

Use the `print()` function to list your menu options.  
Run the cell below to see an example of how to display a menu.

```python
# Displaying the weather menu options
print("Weather Menu:")
print("1. Check Temperature")
print("2. Check Humidity")
print("3. Check Wind Speed")
print("4. Exit")
```

**Tip:** Organising your menu in a numbered list makes it easier for the user to understand their options.

### Step 2: Capturing User Input

After displaying the menu, you need to capture the user’s selection.  
Use the `input()` function to prompt the user.  
Run the cell below to see how to capture and store the user's choice.

```python
# Prompting the user to enter their choice
choice = input("Enter your choice (1-4): ")
print("You selected option:", choice)
```

**Tip:** Using clear prompts with `input()` helps avoid confusion and ensures users know what is expected.

### Step 3: Discussing the Options

Each option in your menu could trigger a different block of code in your program. For example:

- **Option 1: Check Temperature**
  This option might prompt the user for the current temperature and then display a message based on the temperature value.

- **Option 2: Check Humidity**
  Here, the program could ask for the humidity level and provide a message like "It's quite humid today" or "The air is dry."

- **Option 3: Check Wind Speed**
  This might involve asking for the wind speed and advising the user on the weather conditions accordingly.

- **Option 4: Exit**
  This option will end the program.

**Tip:** Think of each menu option as a separate branch of your program logic. Later you can use conditionals to determine what happens based on the user's choice.

### Challenge: Experiment and Extend

Now it is your turn. Start by adding an if-else structure:

```python
# Example of a simple decision structure based on the user's choice
if choice == "1":
    print("You chose to check the temperature.")
elif choice == "2":
    print("You chose to check the humidity.")
elif choice == "3":
    print("You chose to check the wind speed.")
elif choice == "4":
    print("Exiting the program.")
else:
    print("Invalid choice. Please select a valid option.")
```

Next, think of some other relevant weather-related things to check for, and extend the program accordingly. **Do not worry about actually telling the user about the weather just yet - that's for part 2 below.** 

### Summary

In this activity, you learned to:  
- Use `print()` to display a menu of options.  
- Use `input()` to capture a user’s selection.  
- Begin thinking about how each menu option could trigger different code responses.

**Tip:** This activity lays the groundwork for building interactive, user-driven applications. Continue experimenting and extending your code to develop a more robust weather menu.

Enjoy exploring and extending your weather menu!

# 2. Writing Weather Decision Logic

## Overview

In this activity you will write code that uses if-else statements to provide a weather forecast based on the user's menu selection.  
For example, if the user selects "Check Temperature", your program should prompt them to enter the current temperature and then use nested if-else statements to display messages such as "It’s cold – wear a jacket" or "It’s warm – enjoy the day!"  
This exercise will help you practise writing nested if-else statements and understanding logical comparisons.

**Advanced Concept:** In previous activities, we've written simple programs that execute one line after another, which is known as "sequence"—a fundamental building block of programming. This week, we introduce the if-else statement, which allows the program to decide which block of code to execute based on conditions. This decision-making process is called "selection" and is another essential concept in building dynamic and interactive programs.

**Tip:** Remember that the input() function always returns a string. This means that even if the user types a number, it is read as a string. To perform numerical comparisons, you must convert the input to a number using int() (or float()).

### Step 1: Capture the User's Menu Selection

First, we need to capture the user's choice from the weather menu.  
In this example, we will assume that the user has already selected "Check Temperature".

```python
# For the purpose of this activity, we simulate a user choice.
# In a complete program, you might capture this using input() from a menu.
user_choice = "1"  # "1" corresponds to "Check Temperature"
print("User selected option:", user_choice)
```

**Note:** Simulating the user choice is useful for testing your decision logic without building the entire menu interface yet.

### Step 2: Write the Weather Forecast Logic

Now, let's write the code that uses if-else statements to provide a weather forecast based on the temperature.  
If the user has selected "Check Temperature", prompt them for the current temperature and output a message depending on the value.

```python
if user_choice == "1":
    # Ask the user for the current temperature
    temp_input = input("Enter the current temperature (in °C): ")

    # Since we assume the user enters a valid number, convert the input into an integer.
    # Remember: input() returns a string, so we use int() to convert it.
    temperature = int(temp_input)

    # Provide a weather forecast based on the temperature using nested if-else
    if temperature < 15:
        print("It's cold – wear a jacket!")
    elif 15 <= temperature < 25:
        print("It's warm – enjoy the day!")
    else:
        print("It's hot – stay cool!")
```

**Tips:**

- We assume that the user will type the correct input. If you ask for a number, then a number (as a string) is expected. Converting the string to an integer using int() is essential for numerical comparisons.

- In Python, after you write a colon (:) in statements like if or else, you indent the following lines. This indentation creates a "block" of code. The if-else statement then decides which block to run based on the condition, so proper indentation is essential to define what code belongs to which condition.

- Although not shown in this example, you can nest if-else statements. This means that a block of code selected by an if-else can itself contain another if-else. Nested if-else statements allow you to handle multiple conditions in a clear and organised way, making your decision logic easier to follow.

### Step 3: Sample Code Walkthrough

Let's trace through the code with sample inputs:

- **Case 1: Temperature = 10°C**
  The program will print: "It's cold – wear a jacket!"

- **Case 2: Temperature = 20°C**
  The program will print: "It's warm – enjoy the day!"

- **Case 3: Temperature = 30°C**
  The program will print: "It's hot – stay cool!"

**Tip:** Running your code with different sample inputs helps ensure that all branches of your if-else logic work as expected.

### Challenge: Experiment and Extend

Now that you have the basic structure in place:
- _Experiment_ with adding additional conditions, such as a condition for "very cold" or "very hot".
- _Extend_ your logic to include the other weather parameters that you came up with in the previous activity.

For example, you could add a new condition for extremely cold weather:

```python
if temperature < 5:
    print("It's freezing – bundle up!")
elif temperature < 15:
    print("It's cold – wear a jacket!")
elif 15 <= temperature < 25:
    print("It's warm – enjoy the day!")
else:
    print("It's hot – stay cool!")
```

**Do not** perform any queries on real-world data sources just yet; perhaps return some "dummy data" (illustrative sample data).

### Reflection

- How do the nested if-else statements help in making decisions based on the user's input?
- What challenges did you face while converting the input and handling errors?
- How might you further improve the logic for a more detailed weather forecast?

**Tip:** Reflect on these questions to understand how your decision logic works and to identify areas for improvement.

### Summary

In this activity, you learned to:
- Capture a user's menu selection.
- Prompt the user for additional input based on their choice.
- Use nested if-else statements to compare values and output a weather forecast.
- Trace through your code using sample inputs to ensure the logic is sound.

**Tip:** This exercise lays the groundwork for creating more interactive and dynamic weather applications. Continue practising and refining your decision logic to build more robust programs.

Happy coding!
