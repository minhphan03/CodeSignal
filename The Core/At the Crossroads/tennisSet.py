# Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to be finished with a final score of score1 : score2.
def solution(score1, score2):
    if (score1 == 6) is not (score2 == 6):
        if score1 < 5 or score2 < 5:
            return True
    if (score1 == 7) is not (score2 == 7):
        if 5<= score1 <=6 or 5<= score2 <=6:
            return True
    return False 
