# Overview

I developed this cook book application to deepen my understanding of SQL and integrating SQL
relational databases with programming languages to create user-friendly database management
systems.

For this project, I created a simple CRUD application for storing, retrieving, altering, and
deleting recipes from a SQL database. The user can create new recipes, storing a name, description,
and a collection of ingredients and steps. From the menu, the user can choose to view all stored
recipes and retrieve details of certain recipes, users can add new recipes, update existing recipes,
and delete existing recipes.

My purpose in developing this software was to further my understanding of database concepts, as I
know it is an important skill to have as a software engineer. I wanted to explore best practices and
create something that can be used in every day life. As I've become more familiar with integrating
SQL databases with this cook book application, I'm excited to continue learning by implementing what
I've learned and creating new projects.

[Software Demo Video](https://www.youtube.com/watch?v=BVejGXwj5y8)

# Relational Database

The project uses SQLite as the relational database, chosen for its lightweight nature and seamless Python integration. SQLite provides all the essential features needed for this application while maintaining simplicity in setup and maintenance.

The database consists of a single table with the following structure:

Recipe Table

- recipe_id: INTEGER (auto incrementing primary key)
- name: TEXT NOT NULL
- description: TEXT NOT NULL
- ingredients: TEXT NOT NULL
- steps: TEXT NOT NULL
- date_created: TEXT DEFAULT CURRENT_TIMESTAMP

# Development Environment

Tools used in development:

- Visual Studio Code
- Git for version control
- Python 3

Programming Languages and Libraries:

- Python
- SQLite3
- JSON

# Useful Websites

- [Python Classes](https://www.w3schools.com/python/python_classes.asp)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [ChatGPT](https://chatgpt.com)

# Future Work

- Fix the get_recipe_input function as code is duplicated from the get_ingredients_input and get_steps_input functions
- Add search functionality
- Expand the database
