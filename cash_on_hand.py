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

    # Find the top 3 highest cash deficits
    if cash_on_hand_difference:
        top_3_deficits = sorted(cash_on_hand_difference, key=lambda x: int(x.split(":")[2].split(" ")[-1]), reverse=True)[:3]

        if top_3_deficits:
            with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
                for i, deficit in enumerate(top_3_deficits, start=1):
                    file.write(f"[HIGHEST CASH DEFICIT] {deficit}\n")
                    print(f"Highest Cash Deficit {i} written to summary_report.txt:", deficit)

                for deficit in cash_on_hand_difference:
                    file.write(f"{deficit}\n")
                    print("Cash Deficit written to summary_report.txt:", deficit)

cash_on_hand_function()