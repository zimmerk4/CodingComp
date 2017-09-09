def enhance_path(s):
    cd_commands = s.strip().split(chr(92))[1:]  # Get dirs but ignore the root dir
    dir_out = []
    for command in cd_commands:
        command_chars = set(command)
        if command == "":
            pass  # Strips any blank chars from duplicate \'s
        elif command_chars == {"."}:
            dot_cnt = command.count(".")
            if dot_cnt > 1:
                dir_out = dir_out[:1-dot_cnt]  # Pop last elem. Works with empty list w/out throwing
        elif command_chars == {"*"}:
            if command.count("*") < 2:
                dir_out = []  # Goes to root
            else:
                dir_out.append(command)
        else:
            dir_out.append(command)
    print(chr(92) + chr(92).join(dir_out))  # Add root dir
    return chr(92) + chr(92).join(dir_out)

with open("ep.txt") as ep, open("out.txt") as out:
    for iline, oline in zip(ep, out):
        ans = enhance_path(iline)
        if ans != oline.strip():
            print("shit!", iline, ans, oline)
