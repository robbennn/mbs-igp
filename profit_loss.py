from pathlib import Path
import csv

def profit_loss_function():
    net_profit_fp = Path.cwd() / "Profit_and_Loss.csv"
    fp_write = Path.cwd() / "Summary_report.txt"
    fp_write.touch()

    net_profit_list = []

    with net_profit_fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            day = int(row[0])
            net_profit = int(row[4])
            net_profit_list.append([day, net_profit])

    profit_deficit_list = []
    previous_day_profit = 0

    for day, net_profit_amount in net_profit_list:
        if net_profit_amount < previous_day_profit:
            profit_deficit = previous_day_profit - net_profit_amount
            profit_deficit_list.append(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {profit_deficit}")
        previous_day_profit = net_profit_amount

    # Find the top 3 highest net profit deficits
    if profit_deficit_list:
        top_3_deficits = sorted(profit_deficit_list, key=lambda x: int(x.split(":")[-1].split(" ")[-1]), reverse=True)[:3]

        if top_3_deficits:
            with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
                for i, deficit in enumerate(top_3_deficits, start=1):
                    file.write(f"[Highest Net Profit Deficit] Day {i}: {deficit}\n")
                    print(f"Highest Net Profit Deficit {i} written to summary_report.txt:", deficit)

profit_loss_function()