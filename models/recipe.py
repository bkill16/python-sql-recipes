class Recipe:
    """
    A class representing a cooking recipe with its details and methods for display.

    This class handles the storage and formatting of recipe information including
    ingredients and preparation steps. It provides methods to display the recipe
    in a readable format.

    Attributes:
        recipe_id (int): Unique identifier for the recipe
        name (str): Name of the recipe
        description (str): Description or summary of the recipe
        ingredients (list): List of tuples (quantity, name) or list of dicts with
                          'quantity' and 'name' keys
        steps (list): Ordered list of strings describing preparation steps
    """

    def __init__(self, recipe_id: int, name: str, description: str, 
                 ingredients: list, steps: list) -> None:
        """
        Initialize a new Recipe instance.

        Parameters:
            recipe_id (int): Unique identifier for the recipe
            name (str): Name of the recipe
            description (str): Description or summary of the recipe
            ingredients (list): Either:
                - A list of dictionaries with 'quantity' and 'name' keys
                - A list of tuples containing (quantity, name)
            steps (list): List of strings describing preparation steps

        Notes:
            - If ingredients are provided as dictionaries, they will be converted
              to tuples in the format (quantity, name)
            - The ingredients format conversion is handled automatically based on
              the input format detected
        """
        self.recipe_id = recipe_id
        self.name = name
        self.description = description
        # Convert ingredients from dict format to tuple format if necessary
        if ingredients and isinstance(ingredients[0], dict):
            self.ingredients = [(ingredient['quantity'], ingredient['name']) 
                              for ingredient in ingredients]
        else:
            self.ingredients = ingredients
        self.steps = steps

    def __repr__(self) -> str:
        """
        Return a string representation of the Recipe object.

        Returns:
            str: A string in the format "Recipe(id, name, description)"
                suitable for debugging and development

        Note:
            This representation includes only basic recipe information for brevity.
            For full recipe details, use the display_recipe() method.
        """
        return f"Recipe({self.recipe_id}, {self.name}, {self.description})"
    
    def display_recipe(self) -> None:
        """
        Print a formatted version of the complete recipe.

        This method displays all recipe information in a user-friendly format,
        including:
        - Recipe ID and basic information
        - List of ingredients with quantities
        - Numbered steps for preparation

        Example output:
            Recipe ID: 1
            Name: Chocolate Cake
            Description: A delicious dessert

            Ingredients:
            - 2 cups of flour
            - 1 cup of sugar

            Steps:
            1. Preheat oven to 350°F
            2. Mix dry ingredients
        """
        print(f"Recipe ID: {self.recipe_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print("\nIngredients:")
        # Display each ingredient with its quantity
        for quantity, name in self.ingredients:
            print(f"- {quantity} of {name}")
        print("\nSteps:")
        # Display numbered steps starting from 1
        for step_number, step in enumerate(self.steps, start=1):
            print(f"{step_number}. {step}")