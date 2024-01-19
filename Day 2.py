print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

final = total_bill*(percentage/100)
total_final = total_bill+final
final_split = round(total_final/split, 2)
print(f"Each person should pay: {final_split}")