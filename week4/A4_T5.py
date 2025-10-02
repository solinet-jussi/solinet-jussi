# Course task: A4_T5 Break and continue

print("Program starting.")
print()

starting_point = int(input("Insert starting point: "))
stopping_point = int(input("Insert stopping point: "))
inspection_point = int(input("Insert inspection point: "))

print()

rule_broken = False

if starting_point >= stopping_point:
    print("Starting point value must be less than the stopping point value.")
    rule_broken = True

if inspection_point < starting_point or inspection_point > stopping_point:
    print("Inspection value must be within the range of start and stop.")
    rule_broken = True

if not rule_broken:
    print("First loop - inspection with break:")
    
    # First loop with break
    output = ""
    for i in range(starting_point, stopping_point + 1):
        if i == inspection_point:
            break
        if output:
            output += " "
        output += str(i)
    print(output)
    
    print("Second loop - inspection with continue:")
    
    # Second loop with continue
    output = ""
    for i in range(starting_point, stopping_point):
        if i == inspection_point:
            continue
        if output:
            output += " "
        output += str(i)
    print(output)

print("\nProgram ending.")