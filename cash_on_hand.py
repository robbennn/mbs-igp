from pathlib import Path
import csv

def cash_on_hand_function():
    cash_on_hand_fp = Path.cwd() / "Cash_On_Hand.csv" # change file directory later, whoever using this
    fp_write = Path.cwd() / "summary_report.txt"
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
            cash_on_hand_difference.append(f"[CASH DEFICIT] Day: {cash_on_hand_list[cash][0]}, AMOUNT: SGD{abs(difference)}")
            
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        for cash_deficit in cash_on_hand_difference:
            print(cash_deficit)
            file.write(cash_deficit + "\n") 
    
    highest_cash_deficit = max(cash_on_hand_difference, key=lambda x: int(x.split(":")[1].split(" ")[-1]))
    
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        file.write(highest_cash_deficit + "\n")

cash_on_hand_function()
