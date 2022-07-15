def solution(candlesNumber, makeNew):
    sol = candlesNumber
    while candlesNumber >= makeNew:
        sol += candlesNumber // makeNew
        candlesNumber = candlesNumber % makeNew + candlesNumber // makeNew
    return sol
