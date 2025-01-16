from . import matching, matching_speed

def search_pattern(text, df):
    print(f"[*] text \t: {text}")
    patterns, match, match_same = [], [], []

    print(f"[-] -----------------------------------------")
    for index, row in df.iterrows():
        pattern = row['pattern']
        # position = matching_speed(text.lower(), pattern.lower())
        position, elapsed_time = matching_speed(text.lower(), pattern.lower())
        if position != -1:
            value = row["value"]
            if pattern not in patterns:
                patterns.append(pattern)
            if value in match:
                match_same.append(value)
                print(f"    {value} with {pattern} found at {elapsed_time}s")
            else:
                match.append(value)
                print(f"    {value} with {pattern} found at {elapsed_time}s")
    print(f"[-] -----------------------------------------")

    if len(match_same) != 0:
        print(f"    pattern \t: {', '.join(patterns)}")
        print(f"    value \t: {', '.join(match_same)} \n")
        return ', '.join(match_same)
    else:
        print(f"    pattern \t: {', '.join(patterns)}")
        print(f"    value \t: {', '.join(match)} \n")
        if len(match) != 0:
            return ', '.join(match)
        return "hewan tidak ditemukan"