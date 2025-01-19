from . import matching_speed, getArgument, print_text

def search_pattern_with(text, df, df_2, mode='boyer_more'):
    args = getArgument()
    v = args.verbose
    print_text(f'[*] text \t: {text}', v, 1)
    print_text(f'    mode \t: {mode}', v, 1)

    pattern_template = []
    patterns, match, match_same = [], [], []
    
    for index, row in df_2.iterrows():
        p = row[df_2.columns[0]]
        pattern_template.append(p.lower())
    # print(pattern_template)

    print_text(f"[-] {'-'*40}", v, 1)
    for index, row in df.iterrows():
        lists = row[df.columns[0]]
        # print(lists)
        list = lists.split()
        
        for pattern in list:
            if pattern.lower() not in pattern_template:
                continue  # If pattern doesn't exist in pattern_template, skip it
            position, elapsed_time = matching_speed(text.lower(), pattern.lower(), mode)

            if position == -1:
                continue

            value = row['solusi']
            if pattern not in patterns:
                patterns.append(pattern)
            if value not in match:  # Only add to match if it's not already there
                match.append(value)
                print_text(f'    {pattern} \t: {value[:50].ljust(50)} \t found at {elapsed_time}s', v, 2)
            else:
                match_same.append(value)  # Add to match_same if it waas already matched
                print_text(f'    {pattern} \t: {value[:50].ljust(50)} \t found at {elapsed_time}s', v, 2)

    print_text(f"[-] {'-'*40}", v, 2)

    # if len(match_same) != -1:
        # print_text(f"    pattern \t: {', '.join(patterns)}", v, 1)
        # print_text(f"    value \t: {', '.join(match_same)} \n", v, 1)
        # return ', '.join(match_same)
        # return ', '.join(match)
    # else:
    print_text(f"    pattern \t: {', '.join(patterns)}", v, 1)
    print_text(f"    value \t: {', '.join(match)} \n", v, 1)
    if len(match) != 0:
        return ', '.join(match)
    return 'tidak ditemukan'

def search_pattern(text, df, mode='boyer_more', list=['pattern', 'value', 'priority']):
    args = getArgument(); v = args.verbose
    # print(f'[*] text \t: {text}')
    # print(f'    mode \t: {mode}')
    print_text(f'[*] text \t: {text}', v, 1)
    print_text(f'    text \t: {mode}', v, 1)

    patterns, match, match_same = [], [], []

    # print(f'[-] -----------------------------------------')
    print_text(f"[-] {'-'*40}", v, 1)
    for index, row in df.iterrows():
        pattern = row[list[0]]
        position, elapsed_time = matching_speed(text.lower(), pattern.lower(), mode)
        if position != -1:
            value = row[list[1]]
            if pattern not in patterns:
                patterns.append(pattern)
            if value in match:
                match_same.append(value)
                # print(f'    {value} with {pattern} found at {elapsed_time}s')
                print_text(f'    {pattern} \t: {value[:50].ljust(50)} \t found at {elapsed_time}s', v, 2)
            else:
                match.append(value)
                # print(f'    {value} with {pattern} found at {elapsed_time}s')
                print_text(f'    {pattern} \t: {value[:50].ljust(50)} \t found at {elapsed_time}s', v, 2)
                
    # print(f'[-] -----------------------------------------')
    print_text(f"[-] {'-'*40}", v, 2)

    if len(match_same) != 0:
        # print(f"    pattern \t: {', '.join(patterns)}")
        # print(f"    value \t: {', '.join(match_same)} \n")
        print_text(f"    pattern \t: {', '.join(patterns)}", v, 1)
        print_text(f"    value \t: {', '.join(match_same)} \n", v, 1)
        return ', '.join(match_same)
    else:
        # print(f"    pattern \t: {', '.join(patterns)}")
        # print(f"    value \t: {', '.join(match)} \n")
        print_text(f"    pattern \t: {', '.join(patterns)}", v, 1)
        print_text(f"    value \t: {', '.join(match)} \n", v, 1)
        if len(match) != 0:
            return ', '.join(match)
        return 'tidak ditemukan'