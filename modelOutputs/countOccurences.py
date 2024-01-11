import os
import csv
import math

def count_integer_occurrences(file_name):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file_name)
    integer_counts = {}
    skipped_rows = 0

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row if present

        for row_num, row in enumerate(reader, start=1):
            # Assuming $fr is in the second column (index 1)
            fr_value_str = row[1].strip()  # Remove leading and trailing whitespaces

            # Check if the value is numeric
            if fr_value_str.replace('.', '', 1).replace('-', '', 1).lstrip('0').isdigit():
                fr_value = float(fr_value_str)
                rounded_fr = math.floor(fr_value)

                # Print debug information
                print(f"Row {row_num}: Original Value: {fr_value}, Rounded Value: {rounded_fr}")

                # Count occurrences
                if rounded_fr in integer_counts:
                    integer_counts[rounded_fr] += 1
                else:
                    integer_counts[rounded_fr] = 1
            else:
                print(f"Row {row_num}: Skipping non-numeric value: {fr_value_str}")
                skipped_rows += 1
    

    print(f"Skipped {skipped_rows} rows with non-numeric values.")
    return integer_counts

def write_occurrences_to_csv(integer_counts, output_file):
    with open(output_file, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['rating', 'occurrences'])

        for rating, occurrences in integer_counts.items():
            writer.writerow([rating, occurrences])

# Example usage
file_name = 'GPT_selfEnhancing_fr_pcr.csv'
output_csv_file = 'rating_occurrences.csv'
result = count_integer_occurrences(file_name)

# Write occurrences to CSV
write_occurrences_to_csv(result, output_csv_file)
