import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes_left = remaining_time // 60
        seconds_left = remaining_time % 60
        print(f"Remaining Time: {minutes_left:02d}:{seconds_left:02d}", end="\r")
        time.sleep(1)

    print("Focus time is over!")

if __name__ == "__main__":
    focus_minutes = int(input("Enter the focus time in minutes: "))
    focus_timer(focus_minutes)
