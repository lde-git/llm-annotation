import csv
import os
import sys

# Set a large field size limit
csv.field_size_limit(2**31-1)

def remove_user_ids(modified_file_path):
    # Construct the absolute path to the modified CSV file
    absolute_path = os.path.join(os.path.dirname(__file__), 'datasets', modified_file_path)

    # Read the modified CSV file and store its content in a list of dictionaries
    data = []
    with open(absolute_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Remove the 'userId' field from each row
    for row in data:
        del row['userId']

    # Write the modified data (without 'userId') back to the CSV file
    output_file_path = os.path.join(os.path.dirname(__file__), 'datasets', 'jester_ratings_removed_userIds.csv')
    with open(output_file_path, 'w', newline='') as file:
        fieldnames = ['jokeId', 'rating']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header
        csv_writer.writeheader()

        # Write rows without 'userId'
        for row in data:
            csv_writer.writerow(row)

    print(f"UserIds removed. Output saved to {output_file_path}")

# Call the function to remove user ids from the modified file
remove_user_ids('modified_jester_ratings.csv')
