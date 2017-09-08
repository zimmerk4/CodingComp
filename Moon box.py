def moonbox(str_list):
    strings = str_list
    all = set(str_list)
    cnt = 0
    message = ""

    for string in all:
        num_strings = strings.count(string)
        if num_strings > cnt:
            message = string
            cnt = num_strings
    print(message)
    print(cnt)
    return

with open("submission.txt") as mb1:
    str_list = []
    for line in mb1:
        str_list.append(line.strip())
    moonbox(str_list)



