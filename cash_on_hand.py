from pathlib import Path
import csv

def cash_on_hand_function():
    cash_on_hand_fp = Path.cwd() / "Cash_On_Hand.csv"
    fp_write = Path.cwd() / "Summary_report.txt"
    fp_write.touch()

    cash_on_hand_list = []

    with cash_on_hand_fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cash_on_hand_list.append(row)

    cash_on_hand_difference = []

    for cash in range(1, len(cash_on_hand_list)):
        current_day = int(cash_on_hand_list[cash][1])
        previous_day = int(cash_on_hand_list[cash - 1][1])

        difference = current_day - previous_day

        if difference < 0:
            cash_on_hand_difference.append(f"[CASH DEFICIT] DAY: {cash_on_hand_list[cash][0]}, AMOUNT: SGD {abs(difference)}")

    if cash_on_hand_difference:
        top_3_deficits = sorted(cash_on_hand_difference,key=lambda x: int(x.split(":")[2].split(" ")[-1]),reverse=True,)[:3]
# lambda specifies how to extract a value from each element in profit_deficit_list for the purpose of sorting
    # the lambda function converts this extracted value to an integer for proper numeric comparison during sorting.

        with fp_write.open(mode="w", encoding="UTF-8", newline="") as file:
            for i, deficit in enumerate(top_3_deficits, start=1):
                ordinal_suffix = ["ST", "ND", "RD", "TH"][i % 4 - 1]  # Determines the suffix
                prefix = f"[{'HIGHEST' if i == 1 else f'{i}{ordinal_suffix}'} CASH DEFICIT]"
                #[index][0] retrieves the day as it is stored in your list but starts from 0, e.g [DAY 0]
                #[index][0] + 1 adjusts the day number to 1.
                file.write(f"{prefix}: {deficit[15:]}\n")
                # Write all deficits
            for deficit in cash_on_hand_difference:
                file.write(f"{deficit}\n")
cash_on_hand_function()
