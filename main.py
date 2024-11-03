# main.py
"""
Recipe Management System
A command-line application for managing cooking recipes.
Allows users to create, view, update, and delete recipes with ingredients and steps.
"""

from models.recipe_manager import RecipeManager

def display_menu() -> str:
    """
    Display the main menu options to the user.
    
    The menu shows numbered options for viewing recipes, adding new recipes,
    updating existing recipes, deleting recipes, and exiting the program.
    
    Returns:
        str: The user's menu choice as a string ('1'-'5')
    """
    print("\n---------- Cook Book ----------")
    print(" 1. View recipes")
    print(" 2. Add new recipe")
    print(" 3. Update recipe")
    print(" 4. Delete recipe")
    print(" 5. Exit")
    return input("Choose an option (1-5): ")

def display_recipes_and_get_choice(purpose="view"):
    """
    Display all recipes and let user select one for viewing, updating, or deleting.
    
    This function serves multiple purposes based on the 'purpose' parameter.
    It shows all recipes and handles user input for selecting a specific recipe,
    with different prompts based on whether the user is viewing, updating, or deleting.
    
    Parameters:
        purpose (str): Determines the action being performed ('view', 'update', or 'delete')
                      This affects the prompt shown to the user
    
    Returns:
        Recipe | None: Selected Recipe object if user chooses a valid recipe,
                      None if user chooses to go back or if no recipes exist
    """
    recipes = RecipeManager.get_all_recipes()
    if not recipes:
        print("\nNo recipes found.")
        return None

    # Display all available recipes with their IDs and descriptions
    print("\n---------- Stored Recipes ----------")
    for recipe in recipes:
        print(f"{recipe['recipe_id']}. {recipe['name']} - {recipe['description']}")
    
    # Different prompts for different actions
    prompts = {
        "view": "Enter recipe number to view details",
        "update": "Enter recipe number to update",
        "delete": "Enter recipe number to delete"
    }
    
    while True:
        choice = input(f"\n{prompts.get(purpose, 'Enter recipe number')} (or 'back' to return to menu): ")
        if choice.lower() == 'back':
            return None
        
        try:
            recipe_id = int(choice)
            recipe = RecipeManager.get_recipe_by_id(recipe_id)
            if recipe:
                return recipe
            print("Recipe not found. Please try again.")
        except ValueError:
            print("Please enter a valid number or 'back'.")

def get_recipe_input():
    """
    Collect all information needed for a new recipe from the user.
    
    Prompts user for:
    - Recipe name
    - Description
    - List of ingredients (quantity and name pairs)
    - List of preparation steps
    
    Returns:
        tuple: (recipe_name: str, description: str, 
                ingredients: list[dict], steps: list[str])
        where ingredients is a list of dicts with 'quantity' and 'name' keys
    """
    recipe_name = input("Enter recipe name: ") 
    description = input("Enter recipe description: ")
    
    # Collect ingredients until user enters empty quantity
    ingredients = []
    print("\nEnter ingredients (press enter without quantity to finish):")
    while True:
        quantity = input("Enter ingredient quantity: ")
        if not quantity:
            break
        ingredient_name = input("Enter ingredient name: ") 
        ingredients.append({"quantity": quantity, "name": ingredient_name})
    
    # Collect steps until user enters empty step
    steps = []
    print("\nEnter steps (press enter with empty step to finish):")
    step_num = 1
    while True:
        step = input(f"Step {step_num}: ")
        if not step:
            break
        steps.append(step)
        step_num += 1
    
    return recipe_name, description, ingredients, steps  

def get_ingredients_input():
    """
    Collect only ingredients information from the user.
    Used when updating recipe ingredients separately.
    
    Returns:
        list[dict]: List of ingredient dictionaries, each containing
                   'quantity' and 'name' keys
    """
    ingredients = []
    print("\nEnter ingredients (press enter without quantity to finish):")
    while True:
        quantity = input("Enter ingredient quantity: ")
        if not quantity:
            break
        ingredient_name = input("Enter ingredient name: ")
        ingredients.append({"quantity": quantity, "name": ingredient_name})
    return ingredients

def get_steps_input():
    """
    Collect only preparation steps from the user.
    Used when updating recipe steps separately.
    
    Returns:
        list[str]: List of recipe preparation steps
    """
    steps = []
    print("\nEnter steps (press enter with empty step to finish):")
    step_num = 1
    while True:
        step = input(f"Step {step_num}: ")
        if not step:
            break
        steps.append(step)
        step_num += 1
    return steps

def main():
    """
    Main application loop.
    
    Handles the primary program flow:
    - Displays menu and processes user choices
    - Manages recipe operations (view/add/update/delete)
    - Continues running until user chooses to exit
    """
    while True:
        choice = display_menu()
        
        if choice == "1":
            # View recipes and their details
            recipe = display_recipes_and_get_choice(purpose="view")
            if recipe:
                print("\n---------- Recipe Details ----------")
                recipe.display_recipe()
                input("\nPress Enter to continue...")  # Pause to let user read the details

        elif choice == "2":
            # Add a new recipe to the database
            print("\n---------- Add New Recipe ----------")
            name, description, ingredients, steps = get_recipe_input()
            recipe_id = RecipeManager.create_recipe(name, description, ingredients, steps)
            print(f"\nRecipe created with ID: {recipe_id}")

        elif choice == "3":
            # Update an existing recipe
            print("\n---------- Update Recipe ----------")
            recipe = display_recipes_and_get_choice(purpose="update")
            if recipe:
                # Allow user to keep existing values by pressing enter
                print("\nEnter new details (or press enter to keep current values):")
                name = input(f"Enter new name [{recipe.name}]: ") or recipe.name
                description = input(f"Enter new description [{recipe.description}]: ") or recipe.description
                
                # Handle ingredient updates
                update_ingredients = input("Do you want to update ingredients? (y/n): ").lower() == 'y'
                if update_ingredients:
                    ingredients = get_ingredients_input()
                else:
                    ingredients = [{"quantity": qty, "name": name} for qty, name in recipe.ingredients]

                # Handle step updates
                update_steps = input("Do you want to update steps? (y/n): ").lower() == 'y'
                if update_steps:
                    steps = get_steps_input()
                else:
                    steps = recipe.steps

                # Attempt to update and provide feedback
                if RecipeManager.update_recipe(recipe.recipe_id, name, description, ingredients, steps):
                    print("Recipe updated successfully!")
                else:
                    print("Failed to update recipe.")

        elif choice == "4":
            # Delete an existing recipe
            print("\n---------- Delete Recipe ----------")
            recipe = display_recipes_and_get_choice(purpose="delete")
            if recipe:
                # Confirm before deletion to prevent accidents
                confirm = input(f"Are you sure you want to delete '{recipe.name}'? (y/n): ")
                if confirm.lower() == 'y':
                    if RecipeManager.delete_recipe(recipe.recipe_id):
                        print("Recipe deleted successfully!")
                    else:
                        print("Failed to delete recipe.")

        elif choice == "5":
            print("Goodbye!\n")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()