from datetime import datetime


def day_of_year(datetime_obj):
    days = datetime_obj.timetuple().tm_yday
    return days


if __name__ == "__main__":
    date_strs = ["12/13/2020", "31/03/1999",  "11/16/2020", "1/9/2019", "3/1/2004", "12/31/2000", "12/31/2019"]

    for date_str in date_strs:
        try:
            datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
            print(f"output = {day_of_year(datetime_obj)}")

        except ValueError:
            print("invalid date string format month/day/year")
