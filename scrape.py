import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
import nltk

nltk.download('punkt')

def scrape_and_store(url, database_name):
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract information (modify this based on the structure of the webpage)
        title = soup.title.text
        paragraphs = [p.text for p in soup.find_all('p')]

        # Tokenize paragraphs into sentences
        sentences = [sentence for paragraph in paragraphs for sentence in nltk.sent_tokenize(paragraph)]

        # Store the information in a SQLite database
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()

        # Create a table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS webpage_data 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, sentence TEXT)''')

        # Insert data into the table
        for sentence in sentences:
            cursor.execute('INSERT INTO webpage_data (title, sentence) VALUES (?, ?)', (title, sentence))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

        print("Scraping and storing completed successfully.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")


scrape_and_store("https://en.wikipedia.org/wiki/India", "webpage_data.db")





def convert_db_to_excel(database_name, excel_file):
    connection = sqlite3.connect(database_name)
    query = "SELECT * FROM webpage_data"
    df = pd.read_sql_query(query, connection)
    connection.close()

    # Use ExcelWriter to write to Excel file
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
        writer.save()  # This ensures the file is properly closed

    print(f"Data converted to {excel_file} successfully.")


convert_db_to_excel("webpage_data.db", "webpage_data.xlsx")




