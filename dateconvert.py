import datetime

 # input
birthday = "1-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.datetime.strptime(birthday, date_format)

print parsed_date.strftime("%-m/%-d/%y") # Goal 5/1/17