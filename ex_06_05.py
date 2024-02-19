nums = []
while True:
    sval = input("Enter a number or 'done': ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Input!")
        continue
    nums.append(fval)

if len(nums) == 0:
    print("No numbers entered!")
else:
    print("\nSmallest: ", min(nums), "\nLargest: ", max(nums))
