num = 0
tot = 0
while True:
    user_inp = input("Enter an integer or 'done': ")
    if user_inp == "done":
        break
    try:
        ival = int(user_inp)
    except:
        print("Not an Integer! Try again.")
        continue
    print(ival)
    num = num + 1
    tot = tot + ival

print("All Done")
print(f"Total: {tot}, Count: {num}, Average: {tot/num}")
