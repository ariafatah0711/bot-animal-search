from . import print_text, getArgument

def describe(item, df):
    args = getArgument(); v = args.verbose
    # print('[*] Deskripsi untuk item:', item)
    print_text(f'[*] Deskripsi untuk item:', v, 1)

    for index, row in df.iterrows():
        name = row['name']
        description = row['description']
        if name.lower() in item:
            # print(f'    Name: {name}, Description: {description}\n')
            print_text(f'    Name: {name}, Description: {description}\n', v, 1)
            result = f'Name: {name} \nDescription: {description}'
            return result
    
    return f'Item {item} tidak ditemukan'
    
'''v2'''
# def describe(items, df):
#     items = items.split(',')
#     items = [item.strip().lower() for item in items]

#     print('[*] Deskripsi untuk item:', items)

#     match = []
    
#     for index, row in df.iterrows():
#         name = row['name']
#         description = row['description']
#         if name.lower() in items:
#             print(f'[+] Name: {name}, Description: {description}\n')
#             result = f'Name: {name} \nDescription: {description}'
#             return result
#             match.append(result)
    
#     return '\n\n'.join(match)