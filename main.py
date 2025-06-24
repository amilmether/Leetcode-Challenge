from leetscrape import GetQuestionsList

def generate_csv():
    ls = GetQuestionsList()
    ls.scrape()                 # Scrape all questions
    ls.to_csv(directory=".")   # Save to CSV files in current directory

if __name__ == "__main__":
    generate_csv()
    print("✅ questions.csv generated.")