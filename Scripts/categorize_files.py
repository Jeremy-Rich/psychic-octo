import os
import json
import magic
import pandas as pd

# Initialize the categorized files dictionary
categorized_files = {
    "Documents": [],
    "Images": [],
    "Videos": [],
    "Code": [],
    "Archives": [],
    "Others": []
}

# Function to categorize file based on its extension
def categorize_file(filepath):
    mime = magic.Magic(mime=True)
    try:
        file_type = mime.from_file(filepath)
    except:
        return "Others"
    
    if file_type.startswith('application/pdf') or file_type.startswith('application/msword') or file_type.startswith('text'):
        return "Documents"
    elif file_type.startswith('image'):
        return "Images"
    elif file_type.startswith('video'):
        return "Videos"
    elif file_type in ['application/zip', 'application/x-tar']:
        return "Archives"
    elif file_type.startswith('text/x-python') or file_type.startswith('application/x-javascript'):
        return "Code"
    else:
        return "Others"

# Process the large JSON file in chunks
with open('/Volumes/akron/bear_projects/data/output/drive_map.json', 'r') as f:
    data = json.load(f)
    for directory, contents in data.items():
        for subdir, files in contents.items():
            for file in files:
                filepath = os.path.join(directory, subdir, file)
                if os.path.exists(filepath):
                    category = categorize_file(filepath)
                    categorized_files[category].append(filepath)

# Convert categorized files to a DataFrame for easy analysis
df = pd.DataFrame.from_dict(categorized_files, orient='index').transpose()

# Save the categorized data
df.to_csv('/Volumes/akron/bear_projects/data/output/categorized_files.csv', index=False)
print("Categorization complete! Data saved to 'categorized_files.csv'.")
