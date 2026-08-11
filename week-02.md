# ISYS5002 - Week 2

_Adapted from original materials written by Michael Borck._

## 1. Personalised Greeting & User Preferences

Welcome to your first hands-on project in Python. In this activity, you will create a program that collects user information, processes it, and displays a personalised message.

- **Collect User Input:** Use the `input()` function to ask for details such as the user's name, favourite colour, and favourite food.

    - Tip: Think of `input()` as a way to start a conversation with your computer.

- **Store Responses in Variables:** Assign each input value to a variable.

    - Tip: Choose descriptive names for your variables (e.g., `user_name`, `fav_colour`).

- **Output a Summary Message:** Use the `print()` function to display a personalised greeting that includes all the user's inputs.

- **Extend and Experiment:** Add extra prompts like asking for a favourite hobby or a spirit animal. Experiment with string manipulation methods and see what fun outputs you can create.

### Step 1: Collecting User Input

Below is a code snippet to capture user input. Feel free to adjust the prompts as needed.

```python
# Collect basic user inputs
user_name = input("What is your name? ")
fav_colour = input("What is your favourite colour? ")
fav_food = input("What is your favourite food? ")

# Display the captured inputs
print("Name:", user_name)
print("Favourite Colour:", fav_colour)
print("Favourite Food:", fav_food)
```

### Step 2: Outputting a Personalised Summary

Now combine your inputs into a friendly greeting using string concatenation.

```python
# Output a summary message combining the inputs
print("Hello, " + user_name + "! Your favourite colour is " + fav_colour +
      " and you love " + fav_food + ".")
```

- The `+` operator is used here to join, or "concatenate," multiple strings together to build up your final message. Think of it as gluing pieces of text into one complete sentence.

- Using the `+` operator for strings lets you create new strings by combining literal text with variables. This is one of the fundamental ways to build messages dynamically in Python.

- Experiment with different ways of joining strings – try using _f-strings_ (more on this later!) for cleaner code as you become more comfortable.

### Step 3: Your Turn – Extend the Program

It’s time to add an extra input. For instance, ask the user for their favourite hobby and update your greeting message accordingly.

### Step 4: Experiment with input()

Try a different twist by asking for something unique, like the user’s 'spirit animal'. This is a fun way to practice with `input()`.

```python
spirit_animal = input("What's your spirit animal? ")
print("Interesting choice! I wonder why a", spirit_animal, "resonates with you.")
```

**Tip:** Think about how different input types (like numbers or strings) can change your approach to programming.

### Step 5: Simple String Manipulation

Discover how to change the style of your text. The code below shows your name transformed to all uppercase letters.

```python
print("Your name in all caps is", user_name.upper() + "!")
```

When you see a dot (.) following a variable in Python, like in `user_name.upper()`, you're using a function that belongs to that variable's type. In this example, `user_name` is a string, and `.upper()` is a function that converts all characters to uppercase.

### Challenge 1: Multi-line Greeting

Modify your greeting message so it prints on two lines.

**Tip:** Insert the newline character `\n` in your string to start a new line.

### Challenge 2: Age Calculator

Ask the user for their birth year and calculate their age for the current year.

**Tip:** some of these may be helpful:

- `import datetime`
- `current_year = datetime.datetime.now().year`
- `birth_year = int(user_entered_text)`

**Tip:** Make sure to convert the input from a string to an integer using `int()` before doing arithmetic.

## 2. User Preferences Survey

Explore how to gather and display user preferences through an open-ended programming task. This activity encourages experimentation and resourcefulness with the concepts of input and output in Python.

Remember, using clear and descriptive variable names can make your code easier to understand as your codebase grows.

- **Write a Python Script:** Develop a programme that asks the user about their preferences and then presents those preferences back to them.

    - Tip: Think of your script as a conversation between you and the computer. Ask questions and respond with a summary!

- **Gather Preferences:** Choose at least three different preferences to ask the user about (for example, favourite colour, favourite food, favourite hobby, favourite movie, etc.).

    - Tip: Use the `input()` function to capture the user’s responses.

- **Present Preferences:** Use the `print()` function to display the gathered preferences in a clear and organised manner.

    - Tip: Consider constructing a summary message that incorporates the user’s inputs, for example: _"Hello, [name]! Your favourite colour is [colour], you love [food], and you enjoy [hobby]."_

    - The `print()` function can take multiple arguments separated by commas, automatically adding a space between them. This is a simple way to format your output without needing to manually insert spaces.

### Step 1: Creating the Survey

Below is an example code cell that gathers several user preferences. Run this cell to see how it works. Feel free to modify the prompts or add new ones as you experiment.

```python
# Sample survey programme

# Ask the user for their preferences
name = input("What's your name? ")
favourite_colour = input("What's your favourite colour? ")
favourite_food = input("What's your favourite food? ")
favourite_movie = input("What's your favourite movie? ")

# Construct and display a summary message
print("\nHello, " + name + "!")
print("Your favourite colour is " + favourite_colour + ", you love " + favourite_food +
      ", and your favourite movie is " + favourite_movie + ".")
```

Notice how the `+` operator is used to join strings together. This is known as concatenation—combining separate pieces of text to form one continuous message.

### Step 2: Experimentation and Extension

Now it's your turn. Extend the programme by adding more preferences or by reformatting the output. Here are a few ideas to experiment with:

- **Additional Preferences:** Add another input prompt, such as asking for the user's favourite hobby. Tip: More inputs mean more chances to practise variable assignment and string manipulation.

- **Output Formatting:** Experiment with printing your summary message on multiple lines or using different string methods (e.g., `.upper()` or `.lower()`). Advanced Tip: Try utilising Python’s f-string formatting for a neater way to embed variables within your text. For example:

```python
print(f"Hello, {user_provided_name}!")
```

Try the following skeleton code to guide your modifications:

```python
# TODO: Add another preference.
# For example:
# favourite_hobby = input("What's your favourite hobby? ")

# TODO: Update the summary message to include your new preference.
# For example:
# print("Hello, " + name + "!")
# print("Your favourite colour is " + favourite_colour +
#       ", you love " + favourite_food +
#       ", your favourite movie is " + favourite_movie +
#       ", and you enjoy " + favourite_hobby + ".")
```

Guidance:

- **Approach Freely:** You are free to design your programme in any way that demonstrates your understanding of the concepts. There is no single correct solution; experimentation is key to learning.

- **Utilise Resources:** Feel free to explore online tutorials, ask peers, or use reference materials that support your learning. Understanding how functions work (like `input()` and `print()`) is essential. Think of functions as little machines that take inputs (arguments), process them, and then give you an output.

- **Experiment and Explore:** The goal is to experiment with the concepts you have learned so far. Creativity is encouraged. There is no single correct way to complete this task.

### Challenge 1: Starred Preferences

Print each preference on a separate line, with a star (`*`) at the beginning of each line. For example, the output could look like:

```
* Name: John
* Favourite Colour: Blue
* Favourite Food: Pizza
* Favourite Movie: Inception
```

### Challenge 2: F-String Formatting Challenge

Refactor your summary message to use Python's f-string formatting instead of string concatenation. (See step 2.)

## 3. Crafting the Weather Menu

A **user interface (UI)** is the part of a computer program that allows users to interact with it. In this activity, we are using a text-based menu—a simple yet effective form of UI—to present options to the user. This approach is a great starting point because it helps you understand the fundamentals of user interaction in a program, which is a stepping stone to building more sophisticated graphical interfaces in the future.

In this activity you will create a text-based menu that presents the following options:

- Check Temperature
- Check Humidity
- Check Wind Speed
- Exit

The goal is to use the print() function to display these options and `input()` to capture the user’s selection. Later, you can extend your program so that each option triggers a different response in the code.

**Tip:** When planning your menu, consider how clear and concise text can help guide the user through your program.

### Step 1: Display the Menu

Use the print() function to list your menu options.
Run the cell below to see an example of how to display a menu.

```python
# Displaying the weather menu options
print("Weather Menu:")
print("1. Check Temperature")
print("2. Check Humidity")
print("3. Check Wind Speed")
print("4. Exit")
```

### Step 2: Capturing User Input

After displaying the menu, you need to capture the user’s selection.
Use the input() function to prompt the user.
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

### Step 4: Experiment and Extend

Now it is your turn:  
- Modify the menu or add additional options if you like.  
- Try adding simple conditionals (using if-else) so that your program prints a different message for each menu option.

For example, you can start by adding an if-else structure:

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

**Tip:** Begin with a simple if-else structure to handle the user's input, and then expand your code gradually as you become more comfortable with conditionals.
