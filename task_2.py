import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME,"r", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, "r", encoding="utf-8") as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")