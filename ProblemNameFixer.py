def fixer(text):
    text = text.replace('.', '')            # Remove all dots
    text = '_'.join(text.split())           # Replace spaces with underscores
    filename = text + '.py'                 # Add .py extension
    
    with open(filename, 'w') as f:          # Create and open the file
        f.write("")      # Add some default content (optional)

    print(f"{filename} created successfully!")

# Example usage
fixer("2859. Sum of Values at Indices With K Set Bits")