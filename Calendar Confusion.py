import re


def calendarize(line):
    delim_regex = re.compile(r"\W")
    date, cur_form, new_form = line.strip().split()  # Pulls the strings
    cur_delim = delim_regex.search(cur_form).group()  # Finds the delimiter used in the date
    new_delim = delim_regex.search(new_form).group()  # Finds the delimiter to be used in output date
    cur_date_tup = date.split(cur_delim)  # Unpack the date by its delimiter into tuple
    cur_form_tup = cur_form.split(cur_delim)  # Unpack the current format by its delimiter into tuple
    new_form_tup = new_form.split(new_delim)  # Unpack the new format by its delimiter into tuple
    new_date = []
    for mdy in new_form_tup:  # Locates the index of the required mm, dd, or yyyy and pulls its value from the date
        new_date.append(cur_date_tup[cur_form_tup.index(mdy)])
    print(new_delim.join(new_date))  # Prints the new date joined by the new delimiter


with open("calendar.txt") as cal:
    for line in cal:
        calendarize(line)
