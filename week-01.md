# ISYS5002 - Week 1

_Adapted from original materials written by Michael Borck._

## 1. Hello Python!

### Printing "Hello World!"

Task: Print "Hello World!"

Your mission: Copy the code below and print "Hello World!" to see your first output in action.

```python
print("Hello world!")
```

### Understanding print() Function

Think of `print()` as a magic spell 🧙‍♂️ that makes text appear on the screen. Now, print another message to cast your magic spell.

Task: Print another message of your choice

💡 Hint: Replace the blank space inside the quotes with any text you want to see on the screen.

```python
print("  ")
```

### Printing Multiple Lines

When you use multiple `print()` statements, each one creates a new line on your screen. First, predict what the output will be before running the code below.

```python
print("Hello World!")
print("I am learning Python.")
```

What was printed? Is it what you expected?

Task: Print two messages on separate lines

Time to level up your printing skills! Use two print statements to display:

```
Python is versatile!
I am learning Python!
```

## 2. Fixing Mistakes in Python

Making mistakes is a natural part of learning to code. In fact, every programmer—no matter how experienced—runs into errors. The good news? Python is great at telling us when something is wrong. Our job is simply to **read the message carefully and make small corrections** to get the code working.

In this notebook, you'll practice fixing common beginner mistakes like:

- ✅ Using the correct spelling for Python commands
- ✅ Making sure parentheses and quotation marks are complete
- ✅ Using the right spacing (indentation)
- ✅ Paying attention to uppercase and lowercase letters

Each section contains a small mistake in the code. Your task is to spot the error and fix it so the program runs correctly!

> 💡 Advanced Note: This process of finding and fixing mistakes is called debugging. Later in the semester, we’ll explore more advanced techniques to help us do this even faster!

Let's get started! 🚀

### Fixing Indentation Errors

Python is **indentation-sensitive**. The following code has an indentation error. Run the code first so you can see the error message, then fix it!

```python
print("Hello")
     print("Python!")
```

> 💡 Try to read the error message carefully. Often, you won't understand the full message but only parts of it—use those clues to find the problem. 

### Case Sensitivity Matters!

Python treats `print`, `Print`, and `PRINT` as different things! Run the code first so you can see the error message, then fix the incorrect function call!

```python
PRINT("All caps")
```

### Common Typos

Watch out for typos! Run the code first so you can see the error message, then fix it!

```python
pint("Hello, World!")
```

### Closing Strings Properly

Make sure all strings have both opening and closing quotation marks! Run the code first so you can see the error message, then fix it!

Task: Fix the missing quote

```python
print("Python)
```

### Matching Parentheses

Every opening parenthesis `(` must have a closing parenthesis `)`. Fix the error below.

```python
print("I have no end"
```

### Debugging a Beginner's Code

Bob wrote his first Python script, but it has some errors. Can you fix them?

```python
prinT("Good morning!"
Print("Python is amazing!")
     print("Let's learn Python together!"
print("Coding is exciting")
print("I have no idea what's going on!"
```

## 3. Making Your Python Code Clear and Readable

When writing code, **how** you format your output is just as important as **what** you print. Imagine reading a book without spaces between paragraphs—it would be confusing, right? The same idea applies to programming!

In this notebook, you'll learn how to:

- ✅ Add **blank lines** to make your output easier to read
- ✅ Print **multiple lines** using different techniques
- ✅ Use **comments** to explain your code (just like adding notes in a notebook!)

💡 **Why does this matter?**

- Blank lines help **organise** your output.
- Comments help **explain** your code so that you (and others) can understand it later.
- Writing clear, readable code is a skill that **every great programmer** develops over time!

Let's make your Python programs **clear, structured, and easy to read!** 🚀

### Skipping a Line in Code

Skipping a line in the code without a print statement has no effect on the output. For example:

```python
print("Apple")

print("or Orange?")
```

Output:

```
Apple
or Orange?
```

What do you think is the result of running this code? Have a guess and then run the cell. Did the output match your expectations?

```python
print("How")

print("are")
print("you?")
```

Hint: Consider how each print() creates a new line.

### We Must Skip a Line

But what if I want a blank line? You might be wondering, "How can we print a blank line in Python?" It's easy! Just use the print() function without anything inside the parentheses.

Check this out:

```python
print("How")
print()
print("are")
print("you?")
```

Output:

```
How

are
you?
```

Notice how we left the second line blank!

Now, let's put this into practice. Rearrange the lines to print:

```
Blank spaces matter
for clarity

and style!
```

> Advanced Tip: Think about the order in which the lines are printed and how blank lines affect the overall output.

### Multiple Lines with One Function

Can we use just one `print()` function to print several lines?

Yes! Use `\n` to start a new line:

```python
print("This is the first line.\nThis is the second line.")
```

Output:

```
This is the first line.
This is the second line.
```

Here, `\n` inside the string tells Python to jump to a new line and continue printing. Easy and efficient, right?

Tip: Use this method when you want to embed newlines within a single string.

### Economical Printing – Using Triple Quotes

Here's another cool trick Python has up its sleeve to print several lines at once: using three single (`'''`) or three double (`"""`) quotes.

```python
print('''My contact:
Email: your_name@gmail.com
Phone: +xx-1234-5678''')
```

Output:

```
My contact:
Email: your_name@gmail.com
Phone: +xx-1234-5678
```

> Advanced Note: When using triple quotes, Python preserves the newlines exactly as you type them, which can be very handy for multi-line output.

### Debugging Multiline String Errors

Let's tackle a challenge with a multi-line string. Notice the problematic code below:

Target Output:

```
To-Do List:
1. Complete Python exercise
2. Review coding concepts
3. Have a cuppa tea
```

Problematic Code:

```python
print('To-Do List:
1. Complete Python exercise
2. Review coding concepts
3. Have a cuppa tea')
```

Hint: Consider how to correctly represent a multi-line string in Python. You might use \n or triple quotes.

Extension: Write two answers, one uses \n and the other uses triple quotes.

### Print a Personal Profile

Now, create a Python program to print a personal profile using a single `print()` function. Here's the target output:

```
Personal Profile:
Name: Alice Smith
Favourite Language: Python
Hobby: Coding and bushwalking
```

Note: You still have three options available (multiple print statements, \n, or triple quotes), but try a different one from the previous challenge.

Tip: Ensure the text format is exactly as shown above, with proper line breaks.

### Comments

Before we end the notebook, let’s talk about the line of code that the program ignores comments!

Comments don’t affect the program but are crucial for readability. By explaining what each part of the code does, comments act like helpful notes, guiding developers through the logic.

> Quick Rule: In Python, start a line with # and it's a comment.

Example:

```python
# This line is a comment and won't be executed
print("Do you have any comment?")
```

Output:

```
Do you have any comment?
The line starting with # is ignored by the computer.
```

### Writing Comments

Anna has recently learnt about multi-line programming in Python and has written a simple script that incorporates all the lessons she learnt:

```python
print("Hello, World!")
print()
print("This is the first line. \nThis is the second line.")
print('''Three quotes can be used also
to print multiple lines using a single print function''')
```

Now, she wants to add these three comments inside her code in the appropriate places:

- `print()` function will leave an empty line
- `\n` is used to signal Python to start a new line
- Three quotation marks can also print multiple lines

Please fill in the blanks below and assist Susan in writing well-commented scripts that she will find easier to understand later.

Tip: Think about where each comment would best explain the corresponding code functionality.

```python
print("Hello, World!")

print()

print("This is the first line. \nThis is the second line.")

print('''Three quotes can be used also
to print multiple lines using a single print function''')
```

Happy coding, and remember—clear and readable code is the first step towards becoming a great programmer!
