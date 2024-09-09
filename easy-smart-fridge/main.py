import pandas as pd # Shortened name of our package for reference in this file

# Read the CSV file
file_path = 'RAW_recipes.csv'
df = pd.read_csv(file_path)

# Extract specific columns
columns_to_extract = ['name', 'id', 'minutes', 'n_ingredients', 'ingredients', 'steps']
df = df[columns_to_extract]

# Display the first few rows of the DataFrame
# print(df.head())

# Hard-coded ingredients
# ingredients = ['winter squash', 'mexican seasoning', 'mixed spice', 'honey', 'butter', 'olive oil', 'salt']

# Accept a list of up to 10 ingredients from the user
user_input = input("Enter up to 10 ingredients, separated by commas: ")

# Convert the input string into a list of ingredients
ingredients = [ingredient.strip() for ingredient in user_input.split(',')][:10]

# Display the list of ingredients
print("Ingredients list:", ingredients)

columns_to_check = []

for ingredient in ingredients:
    new_column_name = f'contains_{ingredient.replace(" ", "_")}'
    df[new_column_name] = df['ingredients'].str.contains(ingredient, case=False, na=False)
    columns_to_check.append(new_column_name)

    # print(df[df[new_column_name]].head())

# Calculate the percentage of 'True' values across the specified columns for each row
df['true_percentage'] = df[columns_to_check].mean(axis=1)

# Filter rows where the percentage of 'True' values is at least 80% (0.8)
filtered_df = df[df['true_percentage'] >= 0.8]

# Display the filtered rows
print(filtered_df.head())
