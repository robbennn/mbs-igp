from pathlib import Path
import csv

def profit_loss_function():
    net_profit_fp = Path.cwd() / "Profit_and_Loss.csv"  # Ensure correct file path
    fp_write = Path.cwd() / "Summary_report.txt"
    fp_write.touch()

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

    # Writing to file within the function
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        for deficit in profit_deficit_list:
            print(deficit)
            file.write(deficit + "\n")

    # Optionally, return the list if needed
    return profit_deficit_list
