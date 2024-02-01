from pathlib import Path
import csv

def profit_loss_function():
    net_profit_fp = Path.cwd() / "Profit_and_Loss.csv"  # Ensure correct file path
    fp_write = Path.cwd() / "summary_report.txt"

    net_profit_list = []

    with net_profit_fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            day = int(row[0])  # Corrected day assignment
            net_profit = int(row[4])
            net_profit_list.append([day, net_profit])

    profit_deficit_list = []
    previous_day_profit = 0

    for day, net_profit_amount in net_profit_list:
        if net_profit_amount < previous_day_profit:
            profit_deficit = previous_day_profit - net_profit_amount
            profit_deficit_list.append(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {profit_deficit}")
        previous_day_profit = net_profit_amount

    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        for deficit in profit_deficit_list:
            print(deficit)
            file.write(deficit + "\n")
    # Optionally, return the list if needed
        #return profit_deficit_list
    # Find the top 3 highest net profit deficits
    if profit_deficit_list:
        top_4_deficits = sorted(profit_deficit_list, key=lambda x: int(x.split(":")[-1].split(" ")[-1]), reverse=True)[:4]
    # lambda specifies how to extract a value from each element in profit_deficit_list for the purpose of sorting
    # the lambda function converts this extracted value to an integer for proper numeric comparison during sorting.
    if top_4_deficits:
        with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
            for i, deficit in enumerate(top_4_deficits, start=1):
                ordinal_suffix = ["ST", "ND", "RD", "TH"][i % 4 - 1]  # Handle up to 4th with correct suffixes
                prefix = f"[{'HIGHEST' if i == 1 else f'{i}{ordinal_suffix}'} NET PROFIT DEFICIT]"
                file.write(f"{prefix}: {deficit[17:]}\n")
                #[index][0] retrieves the day as it is stored in your list but starts from 0, e.g [DAY 0]
                #[index][0] + 1 adjusts the day number to 1.

profit_loss_function()
