from datetime import datetime, timedelta


def clock_in():
    return datetime.now()


def clock_out():
    return datetime.now()


def calculate_work_hours(clock_in_time, clock_out_time, break_duration):
    total_work_time = clock_out_time - clock_in_time
    net_work_time = total_work_time - break_duration
    return total_work_time, net_work_time


# Main program
print("Welcome to the Work Time Tracker!")
clock_in_time = None
clock_out_time = None
break_start_time = None
break_end_time = None
break_duration = timedelta()

while True:
    print("\nOptions:")
    print("1. Clock In")
    print("2. Start Break")
    print("3. End Break")
    print("4. Clock Out")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        if clock_in_time is None:
            clock_in_time = clock_in()
            print(f"Clocked in at {clock_in_time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("You have already clocked in!")

    elif choice == "2":
        if clock_in_time is None:
            print("You need to clock in before starting a break!")
        elif break_start_time is None:
            break_start_time = clock_in()
            print(f"Break started at {break_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("You are already on a break!")

    elif choice == "3":
        if break_start_time is None:
            print("You need to start a break first!")
        else:
            break_end_time = clock_out()
            current_break_duration = break_end_time - break_start_time
            break_duration += current_break_duration
            print(f"Break ended at {break_end_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Break duration this session: {current_break_duration}")
            break_start_time = None  # Reset break start time for next break

    elif choice == "4":
        if clock_in_time is None:
            print("You need to clock in before clocking out!")
        else:
            clock_out_time = clock_out()
            print(f"Clocked out at {clock_out_time.strftime('%Y-%m-%d %H:%M:%S')}")

            total_time, net_time = calculate_work_hours(clock_in_time, clock_out_time, break_duration)
            print(f"Total work time: {total_time}")
            print(f"Total break time: {break_duration}")
            print(f"Net work time (excluding breaks): {net_time}")

            # Reset for the next session
            clock_in_time = None
            clock_out_time = None
            break_duration = timedelta()

    elif choice == "5":
        print("Exiting the Work Time Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")