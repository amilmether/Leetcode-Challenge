def fixer(text):
    text = text.replace('.', '')            # Remove all dots
    text = '_'.join(text.split())           # Replace spaces with underscores
    filename = text + '.py'                 # Add .py extension
    
    with open(filename, 'w') as f:          # Create and open the file
        f.write("# New Python file\n")      # Add some default content (optional)

    print(f"{filename} created successfully!")

# Example usage
fixer("2833. Furthest Point From Origin")