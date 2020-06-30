# athlete leaderboard
# 12/06/2020
# Mac

athlete_no = 0
athlete_times = []
mwr = 9.58
mer = 9.86
mbr = 9.87
wwr = 10.49
wer = 10.73
wbr = 10.99
gender = ""
while True:
    try:
        gender = input("Is it a male or female race?: (M/F)").lower()
        if gender not in ["m", "f"]:
            print("please enter a valid choice")
            continue
        athlete_no = int(input("How many athletes are there? (4-8): "))
        if athlete_no < 4 or athlete_no > 8:
            print("please enter a number in the specified range")
            continue
        for i in range(athlete_no):
            athlete = []
            athlete.append(i+1)
            athlete_time = float(input("What are the athlete's times?: "))
            athlete.append(athlete_time)
            athlete_times.append(athlete)
            athlete_times.sort(key=lambda x: x[1])

            
            
            
            
        break


    except ValueError:
        print("please enter a number in the specified range ")


for athlete in athlete_times:
    athlete_time = athlete[1]
    for i in athlete:
        print(i, end=" ")

    if gender == "m" and athlete_time < mwr:
        print("Congratulations you have beaten the Men's world record!", end="")
    elif gender == "m" and athlete_time < mer:
        print("Congratulations you have beaten the Men's European record!", end="")
    elif gender == "m" and athlete_time < mbr:
        print("Congratulations you have beaten the Men's British record!", end="")
    elif gender == "f" and athlete_time < wwr:
        print("Congratulations you have beaten the Women's world record!", end="")
    elif gender == "f" and athlete_time < wer:
        print("Congratulations you have beaten the Women's European record!", end="")
    elif gender == "f" and athlete_time < wbr:
        print("Congratulations you have beaten the Women's British record!", end="")
    print()