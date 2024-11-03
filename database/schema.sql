-- Create recipe table with fields recipe_id (auto incrementing primary key),
-- name, description, ingredients, steps, and date_created
CREATE TABLE IF NOT EXISTS Recipe (
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    steps TEXT NOT NULL,
    date_created TEXT DEFAULT CURRENT_TIMESTAMP
);