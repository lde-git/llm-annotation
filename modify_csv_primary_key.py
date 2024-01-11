import csv
import os

def change_primary_key(csv_file_path):
    # Construct the absolute path to the CSV file
    absolute_path = os.path.join(os.path.dirname(__file__), csv_file_path)

    # Read the CSV file and store its content in a list of dictionaries
    data = []
    with open(absolute_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Create a dictionary to store ratings for each jokeId
    joke_ratings = {}
    for row in data:
        joke_id = row['jokeId']
        rating = float(row['rating'])
        
        if joke_id not in joke_ratings:
            joke_ratings[joke_id] = {
                'ratings': [rating],
                'userId': row['userId']
            }
        else:
            joke_ratings[joke_id]['ratings'].append(rating)
            joke_ratings[joke_id]['userId'] += ',' + row['userId']

    # Calculate the average rating for each jokeId
    modified_data = []
    for joke_id, rating_data in joke_ratings.items():
        average_rating = sum(rating_data['ratings']) / len(rating_data['ratings'])
        modified_data.append({
            'jokeId': joke_id,
            'userId': rating_data['userId'],
            'rating': average_rating
        })

    # Sort the modified data by jokeId
    sorted_data = sorted(modified_data, key=lambda x: int(x['jokeId']))

    # Write the sorted and modified data back to a new CSV file in the same "datasets" folder
    output_file_path = os.path.join(os.path.dirname(__file__), 'datasets', 'modified_' + os.path.basename(csv_file_path))
    with open(output_file_path, 'w', newline='') as file:
        fieldnames = ['jokeId', 'userId', 'rating']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header
        csv_writer.writeheader()

        # Write sorted rows
        for row in sorted_data:
            csv_writer.writerow(row)

    print(f"CSV file has been modified and sorted by jokeId. Output saved to {output_file_path}")


    

# Specify the folder and file name
folder_name = 'datasets'
file_name = 'jester_ratings.csv'

# Create the relative path
input_file_path = os.path.join(folder_name, file_name)

# Call the function with the updated path
change_primary_key(input_file_path)
