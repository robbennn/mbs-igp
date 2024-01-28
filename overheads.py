from pathlib import Path
import csv

def overheads_function():
    overheads_fp_read = Path.cwd() / "Overheads.csv"
    fp_write = Path.cwd() / "Summary_report.txt"
    fp_write.touch()

    # Clear the content of the summary_report.txt file
    with fp_write.open(mode="w", encoding="UTF-8", newline=""):
        pass

    overheads_list = []

    with overheads_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[0]
            overhead = float(row[1])
            overheads_list.append([category, overhead])

    highest_overhead_category = ""
    highest_overhead_percentage = 0.00  # 0 is the placeholder, look at the data later for percentage

    for category, overhead in overheads_list:
        if overhead > highest_overhead_percentage:
            highest_overhead_percentage = overhead
            highest_overhead_category = category

    highest_overhead_result = f"[HIGHEST OVERHEAD] {highest_overhead_category} : {highest_overhead_percentage}"

    # Writing to file within the function, but checking if it was already written
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        file.write(highest_overhead_result + "\n")
    return highest_overhead_result

result = overheads_function()
print(result)