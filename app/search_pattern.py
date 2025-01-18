from . import matching_speed, getArgument, print_text

def search_pattern(text, df, mode='boyer_more'):
    args = getArgument(); v = args.verbose
    # print(f'[*] text \t: {text}')
    # print(f'    mode \t: {mode}')
    print_text(f'[*] text \t: {text}', v, 1)
    print_text(f'    text \t: {mode}', v, 1)

    patterns, match, match_same = [], [], []

    # print(f'[-] -----------------------------------------')
    print_text(f"[-] {'-'*40}", v, 1)
    for index, row in df.iterrows():
        pattern = row['pattern']
        position, elapsed_time = matching_speed(text.lower(), pattern.lower(), mode)
        if position != -1:
            value = row['value']
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
    print_text(f"[-] {'-'*40}", v, 1)

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
        return 'hewan tidak ditemukan'