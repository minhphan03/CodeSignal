def solution(young, beautiful, loved):
    if loved and (not young or not beautiful):
        return True
    if young and beautiful and not loved:
        return True
    return False