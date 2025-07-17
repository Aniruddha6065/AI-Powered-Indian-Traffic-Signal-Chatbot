import json
import pandas as pd

# Load the FAQ data from JSON
with open('faq_data.json', 'r', encoding='utf-8') as f:
    faq_data = json.load(f)

# Convert to DataFrame
faq_df = pd.DataFrame(faq_data)

# Rename columns for clarity
faq_df.columns = ['Question', 'Answer']

# Export to Excel
faq_df.to_excel('faq_data.xlsx', index=False)

print('Exported faq_data.json to faq_data.xlsx successfully.') 
import pandas as pd

# Step 1: Read the Excel file
df = pd.read_excel('faq_data.xlsx')

# Step 2: Save as JSON
df.to_json('faq_data.json', orient='records', indent=4)

print("Excel data successfully written to faq_data.json")
