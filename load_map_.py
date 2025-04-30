def load_map(filename: str) -> list[list[int]]:
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    col_size, row_size = map(int, lines[0].strip().split('x'))
    start_line = 1
    list_out = []
    
    for line in lines[start_line:]:
        line = line.strip()
        list_in = []
        for i in line:
            list_in.append(int(i))
        list_out.append(list_in)
    
    return list_out

print(load_map("map1.txt"))