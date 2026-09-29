# Expense Tracker Project

**Name:** Dhanraj Gupta  
**Registration Number:** 26BCE11532  
**College:** VIT Bhopal University

## About the Project

This is a simple **Expense Tracker** program made in Python. It allows the user to add expenses, view all the added expenses, and calculate the total spending.

The program runs through a menu where the user can select what they want to do.

## Features

The program provides four options:

1. **Add Expense**
   - Enter the date of the expense.
   - Enter the category, such as food, travel, makeup, books, etc.
   - Enter a description of the product or expense.
   - Enter the amount.

2. **View All Expenses**
   - Displays all the expenses that have been added.
   - If there are no expenses, it displays a message saying that no expenses have been added.

3. **View Total Spending**
   - Calculates and displays the total amount of all the expenses added.

4. **Exit**
   - Exits the program.

## Concepts Used

The program uses the following Python concepts:

- List
- Dictionary
- `while` loop
- `if-elif-else` statements
- `for` loop
- User input using `input()`
- `float` for storing expense amounts
- `append()` to add expenses to the list
- Dictionary keys and values
- Basic addition for calculating total spending

## How the Program Stores Expenses

All expenses are stored in a list named `ExpensesList`.

Each expense is stored as a dictionary with four details:

- Date
- Category
- Description
- Amount

Example structure:

```python
expense = {
    "Date": date,
    "Category": category,
    "Description": description,
    "Amount": amount
}
```

## How to Run

1. Install Python on your computer.
2. Open the Python file.
3. Run the program.
4. Select an option from the menu.
5. Enter the required details.

## Project Flow

```text
Start
  ↓
Display Menu
  ↓
Choose an Option
  ↓
1. Add Expense → Store Expense
  ↓
2. View Expenses → Display Expenses
  ↓
3. Total Spending → Calculate Total
  ↓
4. Exit → End Program
```

## Conclusion

This project is a basic Python expense tracker that helps the user keep a record of expenses and calculate total spending. It was made using basic Python concepts such as lists, dictionaries, loops, conditions, and user input.

## Author

**Dhanraj Gupta**  
**Registration Number: 26BCE11532**
