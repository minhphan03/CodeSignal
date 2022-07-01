def solution(a):
    trees = []
    people = []
    for e in range(len(a)):
        if a[e] == -1:
            trees.append(e)
        else:
            people.append(a[e])
    people.sort()
    for tree in trees:
        people.insert(tree, -1)
    return people
