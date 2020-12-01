with open("day1-input", "r") as f:
    expenses = f.read()

expenses = expenses.split('\n')

# Use list for fast iteration
expenses_list = list(map(int, expenses[:-1]))
# Use set for O(1) lookup
expenses_set = set(expenses_list)


## Part One
for ex in expenses_list:
    if 2020-ex in expenses_set:
        print((2020-ex)*ex)
        break


## Part Two
done = False
for ex1 in expenses_list:
    if done: break
    for ex2 in expenses_list:
        if done: break
        if 2020-ex1-ex2 in expenses_set:
            print((2020-ex1-ex2)*ex1*ex2)
            done = True
