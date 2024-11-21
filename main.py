import csv

# File path to the data
file_path = "data\\grade11results-2024.csv"

# Initialize a list to store structured data
structured_data = []

try:
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
        
        # Split content by quotation marks to extract rows
        rows = [row.strip() for row in content.split('"') if row.strip()]
        
        # Process each row
        for row in rows:
            # Split row into fields
            fields = row.split()  # Splitting by whitespace
            try:
                
                student_data = {
                    "Student ID": fields[0],
                    "Class": fields[1],
                    "School": fields[2],
                    "Subjects": fields[3:]
                }
                structured_data.append(student_data)
            catch IndexError:
                print(f"Invalid row: {row}")
    
    # Print extracted structured data
    for entry in structured_data:
        print(entry)

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
