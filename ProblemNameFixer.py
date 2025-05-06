def fixer(text):
    text = text.replace('.', '')            # Remove all dots
    text = '_'.join(text.split())           # Replace spaces with underscores
    filename = text + '.py'                 # Add .py extension
    
    with open(filename, 'w') as f:          # Create and open the file
        f.write("")      # Add some default content (optional)

    print(f"{filename} created successfully!")

# Example usage
fixer("3000. Maximum Area of Longest Diagonal Rectangle")