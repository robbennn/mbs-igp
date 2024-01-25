from pathlib import Path
import csv

def cash_on_hand_function():
    cash_on_hand_fp = Path.cwd()/"Cash_On_Hand.csv" # change file directory later, whoever using this
    fp_write = Path.cwd()/"summary_report.txt"
    fp_write.touch

    list = []

    with cash_on_hand_fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            list.append(row)
        # print(list)
        
        cash_on_hand_difference = []

        for cash in range(1,len(list)):
            current_day = int(list[cash][1])
            previous_day = int(list[cash - 1][1])

            difference = current_day - previous_day

            if difference < 0:
               cash_on_hand_difference.append(f"[Cash deficit] Day: {list[cash][0]}, Amount: SGD{abs(difference)}")

        with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
            for cash_deficit in cash_on_hand_difference:
                print(cash_deficit)
                file.write(cash_deficit+"\n") 

        return cash
                


