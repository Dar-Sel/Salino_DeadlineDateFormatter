import datetime

eventTitle: str = input("Enter Event Title: ")
year: int = int(input("Enter Year: "))
month: int = int(input("Enter Month: "))
day: int = int(input("Enter Day: "))
eventDate = datetime.date(year, month, day)

print("\nOutput: ")
print(
  f"Event: {eventTitle.upper()}\n"
  f"Date: {eventDate.strftime("%B %-d, %Y")}\n"
  f"Year: {eventDate.strftime("%Y")}\n"
  f"Month: {eventDate.strftime("%B")}\n"
  f"Day: {eventDate.strftime("%-d")}\n"
  f"Weekday: {eventDate.strftime("%A")}"
)
