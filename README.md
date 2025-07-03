# Tic Tac Toe (OOP Version)

## About This Project

I built this Tic Tac Toe game in Python as a way to learn and practice Object-Oriented Programming (OOP). The main goal was to understand how to use classes and objects to organize code better, and to see how the four main OOP principles work in a real project.

## Why OOP?

OOP (Object-Oriented Programming) is a way of structuring code so that related data and functions are grouped together into "objects." This makes code easier to read, reuse, and maintain.

There are four main principles in OOP:

### 1. **Encapsulation**
Encapsulation means keeping the data (attributes) and the code (methods) that work on that data together in one place—a class. It also means hiding the internal details from the outside, so you only interact with the object through its methods.

**Example from this project:**  
The `Player`, `Menu`, `Board`, and `Game` classes each keep their own data and methods. For example, the `Player` class has the player's name, symbol, and score, and methods to set them.

### 2. **Abstraction**
Abstraction means focusing on what an object does instead of how it does it. You use objects without needing to know all the details inside.

**Example from this project:**  
When you call `board.display_board()`, you don't need to know how the board is printed—you just know it will show the current state.

### 3. **Inheritance**
Inheritance lets you create a new class based on an existing class, reusing code and making it easier to extend.

**Note:**  
In this project, I didn't use inheritance because the game is simple, but in bigger projects, you might have a `Person` class and then make `Player` inherit from it.

### 4. **Polymorphism**
Polymorphism means that different objects can be used in the same way, even if they do things differently.

**Note:**  
This project doesn't have a strong example of polymorphism, but if you had different types of players (like a human and a computer), both could have a `make_move()` method, but each would work differently.

## How to Run

1. Make sure you have Python installed.
2. Run the game with:
   ```
   python python.py
   ```

## Final Thoughts

This project helped me understand the basics of OOP in Python. If you're learning OOP, try building a simple game like this—it's a great way to practice! 