from typing import List

def xo_game(game_result: List[str]):
    def check_vert(sym: str):
        if sym == game_result[0][0] and sym == game_result[1][0] and sym == game_result[2][0]:
            return sym
        elif sym == game_result[0][1] and sym == game_result[1][1] and sym == game_result[2][1]:
            return sym
        elif sym == game_result[0][2] and sym == game_result[1][2] and sym == game_result[2][2]:
            return sym
        else:
            return None

    def check_hor(sym: str):
        if sym*3 in game_result:
            return sym
        else:
            return None

    def check_diag(sym: str):
        if sym == game_result[0][0] and sym == game_result[1][1] and sym == game_result[2][2]:
            return sym
        elif sym == game_result[0][2] and sym == game_result[1][1] and sym == game_result[2][0]:
            return sym
        else:
            return None

    symb = ['X','O']
    result = 0

    for l in symb:
        if check_vert(l) != None:
            result = check_vert(l)
            break
        elif check_hor(l) != None:
            result = check_hor(l)
            break
        elif check_diag(l) != None:
            result = check_diag(l)
            break
        else:
            pass

    if result == 0:
        return "D"
    else:
        return result


print(xo_game([
        "XO.",
        "XXO",
        ".OX"]))