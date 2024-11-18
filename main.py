filePath = "data\grade11results-2024.csv"       
with open(filePath, 'r') as file:
    lines = file.readlines()[4:]  
    for line in lines:
        print(f"Candidate Number: {line[1]}")
