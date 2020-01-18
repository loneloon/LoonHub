def safe_pawns(pawns: set):
    def left_guard(col: str, row: str):
        columns = ['a','b','c','d','e','f','g','h']
        rows = ['1','2','3','4','5','6','7','8']
        if col == 'a' or row == '1':
            return None
        else:
            return str(columns[columns.index(col) - 1] + rows[rows.index(row) - 1])
    
    def right_guard(col: str, row: str):
        columns = ['a','b','c','d','e','f','g','h']
        rows = ['1','2','3','4','5','6','7','8']
        if col == 'h' or row == '1':
            return None
        else:
            return str(columns[columns.index(col) + 1] + rows[rows.index(row) - 1])
    
    safe_pawns = []
    for l in pawns:
        if l[1] == '1':
            pass
        elif left_guard(l[0], l[1]) in pawns or right_guard(l[0], l[1]) in pawns:
            safe_pawns.append(l)
        else:
            pass
    return int(len(safe_pawns))