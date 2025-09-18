# Course task: A2_T4: Average and rounding

print("Program starting.")
print("Estimate how many minutes you spent on programming tasks...")

a1_t1 = int(input("A1_T1: "))
a1_t2 = int(input("A1_T2: "))
a1_t3 = int(input("A1_T3: "))
a1_t4 = int(input("A1_T4: "))
a1_t5 = int(input("A1_T5: "))
a1_t6 = int(input("A1_T6: "))
a1_t7 = int(input("A1_T7: "))

total_time = a1_t1 + a1_t2 + a1_t3 + a1_t4 + a1_t5 + a1_t6 + a1_t7
average = round(total_time / 7, 2)
average_rounded_integer = round(average)

print(f"In total you spent {total_time} minutes on programming.")
print(f"Average per task was {average} min and same rounded to the nearest integer {average_rounded_integer} min.")
print("Program ending.")
