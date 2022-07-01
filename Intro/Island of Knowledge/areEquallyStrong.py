def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return (max(yourLeft, yourRight) == max(friendsLeft, friendsRight)) and (min(yourRight, yourLeft) == min(friendsRight, friendsLeft))