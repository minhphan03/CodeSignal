def solution(name):
    if name[0].isdigit():
        return False
    for c in name:
        if not c.isalnum() and c != "_":
            return False
    return True