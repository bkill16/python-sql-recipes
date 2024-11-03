from database.connection import get_connection
from .recipe import Recipe
import json

class RecipeManager:
    """
    A class to manage CRUD operations for recipes in the database.
    
    This class provides static methods to create, read, update, and delete recipes.
    All database operations are handled with automatic connection management using
    context managers.
    """

    @staticmethod
    def create_recipe(name: str, description: str, ingredients: list, steps: list) -> int:
        """
        Create a new recipe in the database.

        Parameters:
            name (str): The name of the recipe
            description (str): A detailed description of the recipe
            ingredients (list): List of dictionaries containing ingredient information
                Each dictionary should have:
                - 'quantity': The amount of the ingredient (str or float)
                - 'name': The name of the ingredient (str)
            steps (list): List of strings describing each step of the recipe

        Returns:
            int: The ID of the newly created recipe (lastrowid)

        Notes:
            - Ingredients and steps are stored as JSON strings in the database
            - The database connection is automatically managed using a context manager
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            # Convert lists to JSON for storage in database
            cursor.execute(
                """
                INSERT INTO Recipe (name, description, ingredients, steps)
                VALUES (?, ?, ?, ?)
                """,
                (name, description, json.dumps(ingredients), json.dumps(steps))
            )
            return cursor.lastrowid

    @staticmethod
    def get_all_recipes() -> list:
        """
        Retrieve all recipes with basic information.

        Returns:
            list: A list of tuples containing basic recipe information
                Each tuple contains:
                - recipe_id (int)
                - name (str)
                - description (str)

        Notes:
            This method only returns basic recipe information for efficiency.
            For complete recipe details, use get_recipe_by_id().
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT recipe_id, name, description FROM Recipe")
            return cursor.fetchall()

    @staticmethod
    def get_recipe_by_id(recipe_id: int) -> Recipe | None:
        """
        Retrieve a complete recipe by its ID.

        Parameters:
            recipe_id (int): The unique identifier of the recipe

        Returns:
            Recipe | None: A Recipe object containing all recipe information,
                          or None if no recipe is found with the given ID

        Notes:
            - The ingredients and steps are stored as JSON strings in the database
              and are automatically converted back to Python objects
            - Returns a Recipe object which encapsulates all recipe data
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Recipe WHERE recipe_id = ?", (recipe_id,))
            row = cursor.fetchone()
            if row:
                # Parse JSON strings back into Python objects
                ingredients = json.loads(row['ingredients'])
                steps = json.loads(row['steps'])
                return Recipe(
                    recipe_id=row['recipe_id'],
                    name=row['name'],
                    description=row['description'],
                    ingredients=ingredients, 
                    steps=steps
                )
            return None

    @staticmethod
    def update_recipe(recipe_id: int, name: str, description: str, 
                     ingredients: list, steps: list) -> bool:
        """
        Update an existing recipe.

        Parameters:
            recipe_id (int): The ID of the recipe to update
            name (str): The new name of the recipe
            description (str): The new description of the recipe
            ingredients (list): Updated list of ingredient dictionaries
            steps (list): Updated list of recipe steps

        Returns:
            bool: True if the recipe was successfully updated,
                 False if no recipe was found with the given ID

        Notes:
            - All fields must be provided, even if they haven't changed
            - Returns False if the recipe_id doesn't exist
            - Ingredients and steps are converted to JSON for storage
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Recipe 
                SET name = ?, description = ?, ingredients = ?, steps = ?
                WHERE recipe_id = ?
                """,
                (name, description, json.dumps(ingredients), json.dumps(steps), recipe_id)
            )
            return cursor.rowcount > 0

    @staticmethod
    def delete_recipe(recipe_id: int) -> bool:
        """
        Delete a recipe by its ID.

        Parameters:
            recipe_id (int): The ID of the recipe to delete

        Returns:
            bool: True if the recipe was successfully deleted,
                 False if no recipe was found with the given ID

        Notes:
            This operation cannot be undone. Make sure to confirm deletion
            with the user before calling this method.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Recipe WHERE recipe_id = ?", (recipe_id,))
            return cursor.rowcount > 0