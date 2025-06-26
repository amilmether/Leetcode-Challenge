import os
import pandas as pd
import ast

# Load your CSV file
CSV_FILE = "questions.csv"  # Rename if needed
df = pd.read_csv(CSV_FILE)

# Print available column names for debugging
print("Column Names Found in CSV:")
print(df.columns.tolist())
print()

# Detect the correct question ID column
possible_id_cols = ["questionId", "frontendQuestionId", "id", "QID"]
qid_column = next((col for col in possible_id_cols if col in df.columns), None)

if not qid_column:
    raise ValueError("❌ Could not find a valid question ID column.")

# Function to create the file
def fixer(qid):
    # Match question ID
    row = df[df[qid_column].astype(str) == str(qid)]

    if row.empty:
        print(f"[ERROR] Question ID {qid} not found in column '{qid_column}'.")
        return

    # Extract title and difficulty
    title = row.iloc[0]['title']
    difficulty = row.iloc[0]['difficulty'].lower()

    # Parse topic tags
    tags_raw = row.iloc[0].get('topicTags', "[]")
    try:
        tags = ast.literal_eval(tags_raw)
    except:
        tags = []

    if not tags:
        tags = ['misc']

    # Clean title for filename
    clean_title = title.replace('.', '').replace(',', '')
    file_name = f"{qid}_{'_'.join(clean_title.split())}.py"

    # Create folder and file
    for tag in tags:
        tag = tag.lower().replace(" ", "_")
        folder_path = os.path.join(difficulty, tag)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, file_name)

        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(f"# {qid}. {title} [{difficulty.capitalize()}]\n")
                f.write(f"# Tags: {', '.join(tags)}\n\n")
                f.write("class Solution:\n    def method(self):\n        pass\n")
            print(f"[OK] Created: {file_path}")
        else:
            print(f"[SKIP] Already exists: {file_path}")

# ✅ Example: run this to create a file for problem 83
fixer(36)
