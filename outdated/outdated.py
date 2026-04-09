def main():
    calendar()

def calendar():
    month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            date = input("Date: ")
            if "," in date:
                date = date.replace(",", "").split()
                m, d, y = date[0], int(date[1]), date[2]
                d = int(d)
                if m in month:
                    m = month.index(m) + 1
                    if 1 <= d <= 31:
                        print(f"{y}-{m:02}-{d:02}")
                        break
            elif "/" in date:
                date = date.replace(" ", "")
                m, d, y = date.split("/")
                m = int(m)
                d = int(d)
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y}-{m:02}-{d:02}")
                    break
        except (ValueError, IndexError):
            pass


calendar()
