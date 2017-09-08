def moonbox(str_list):
    strings = str_list
    all = set(str_list)
    cnt = 0
    message = ""

    for str in all:
        num_strings = strings.count(str)
        if num_strings > cnt:
            message = str
            cnt = num_strings
    print(message)
    print(cnt)
    return

with open("submission.txt") as mb1:
    str_list = []
    for line in mb1:
        str_list.append(line.strip())
    moonbox(str_list)



