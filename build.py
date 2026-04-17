import csv
import os

DROP = {1, 3}
processed_data = []

with open("heads.csv", "r", encoding="utf-8") as infile, open(
    "heads_temp.csv", "w", newline="", encoding="utf-8"
) as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) == 4:
            next(reader, None)  # remove first line
            new_row = [
                val for i, val in enumerate(row) if i not in DROP
            ]  # remove 2nd and 4th columns, they are unnecessary
        else:
            new_row = row  # keep unchanged if not 4 columns

        writer.writerow(new_row)
        processed_data.append(new_row)

# Replace original file
os.replace("heads_temp.csv", "heads.csv")

with open("heads.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
