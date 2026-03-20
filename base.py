from datetime import datetime


# storage                  
events = []   # each items


# core logic 
def add_event():
    print("\n Add New Event ")

    topic = input("Topic : ").strip()
    if not topic:
        print("Error: Topic cannot be empty.")
        return

    # date input loop
    while True:
        date_str = input("Date in (DD-MM-YYYY) : ").strip()
        try:
            date_part = datetime.strptime(date_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Invalid date. Please use DD-MM-YYYY format (e.g. 25-12-2025).")

    # time input loop
    while True:
        time_str = input("Time in (HH:MM, 24-hour) : ").strip()
        try:
            time_part = datetime.strptime(time_str, "%H:%M").time()
            break
        except ValueError:
            print("Invalid time. Please use HH:MM format (e.g. 09:30 or 14:00).")

    event_dt = datetime.combine(date_part, time_part)
    events.append({"topic": topic, "datetime": event_dt})
    print(f"\nEvent '{topic}' added for {event_dt.strftime('%d %b %Y at %H:%M')}.")


def display_events():
    if not events:
        print("\nNo events found. Add one first!")
        return

    sorted_events = sorted(events, key=lambda e: e["datetime"])

    print("")
    print(f"{'  #':<4} {'TOPIC':<20} {'DATE & TIME'}")
    print("")

    for i, event in enumerate(sorted_events, start=1):
        dt_str = event["datetime"].strftime("%d %b %Y  %H:%M")
        print(f"  {i:<3} {event['topic']:<20} {dt_str}")

    print("")
    print(f"  Total: {len(events)} event(s)")



#menu printing
def show_menu():
    print("")
    print(" M Y C A L A N D E R ")
    print("  1. Add event")
    print("  2. View all events")
    print("  3. Quit")
   

#main function here
def main():
    print("\nWelcome to Calander!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_event()
        elif choice == "2":
            display_events()
        elif choice == "3":
            print("\nbye\n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
