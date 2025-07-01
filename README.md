# restaurant-menu-order-system
A console-based Python project that allows restaurant owners to add dynamic menu items (starters, main course, desserts) and lets customers place orders by selecting from the available items. It demonstrates the use of lists, functions, loops, and user input handling to simulate a simple restaurant ordering system.



This Python project is a console-based Restaurant Menu and Ordering System built in two main phases: admin-controlled menu creation and customer order selection. It aims to simulate a simple restaurant ordering process using Python's core features like lists, loops, functions, and conditionals.

🔧 Phase 1: Admin Menu Setup
In this phase, the admin is responsible for adding food items to the restaurant's menu under three categories:

Starters

Main Course

Desserts

Each category has its own function (starters(), maincourse(), and desert()), where the admin enters the number of items and their names. These items are stored in lists (s1, m, and d1) and can be added continuously based on user input.

🍽️ Phase 2: Customer Ordering
After the menu setup, the program shifts to customer mode. Customers can:

View all available items in each category.

Choose one item from Starters, Main Course, and Desserts.

Have their selections validated against the admin-created menu.

Functions like starter2(), main(), and des() are used to take customer selections and store them in separate lists (l1, l2, l3). If a selected item is not available in the menu, the system displays a warning message.

This project provides a simple yet functional simulation of how a restaurant menu and ordering process works. It demonstrates modular design, user input handling, and list-based data storage, making it ideal for beginners learning Python.


