# import pandas as pd
from .. import boyer_more

def search_animals(text, df):
    print(df)
    print(f"[*] text \t: {text}")
    patterns, match, match_same = [], [], []

    for index, row in df.iterrows():
        pattern = row['pattern']
        position = boyer_more(text.lower(), pattern.lower())
        if position != -1:
            value = row["value"]
            if pattern not in patterns:
                patterns.append(pattern)
            if value in match:
                match_same.append(value)
            else:
                match.append(value)

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
