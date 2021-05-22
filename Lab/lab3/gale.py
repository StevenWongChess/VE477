
def first(list):
    return list[0]

def gale(man, woman, people):
    marrylist = []
    free_man = []
    woman_current = []
    man_propose = [[0 for i in range(people)]for i in range(people)]

    for i in range(people):
        woman_current.append(-1)# available
        free_man.append(i)

    while len(free_man) > 0: # there is a free man
        m = free_man[0] # select a man
        propose_woman = 0
        while man_propose[m][man[m][propose_woman]] == 1:# has not proposed yet
            propose_woman = propose_woman + 1 

        w = man[m][propose_woman]
        man_propose[m][w] = 1
        if woman_current[w] == -1:
            woman_current[w] = m
            free_man.pop(0)
        else:
            breakup = woman_current[w]
            if woman[w].index(m) < woman[w].index(breakup):
                woman_current[w] = m
                free_man.append(breakup)
                free_man.pop(0)
        print(m, w)
        if m == 3:
            print(free_man)
            print(woman_current)
            print(man_propose)
    for i in range(people):
        marrylist.append([woman_current[i], i])
    marrylist.sort(key = first)
    return marrylist

if __name__ == '__main__':
    people = int(input())
    man = []
    woman = []
    for i in range(people):
        l = list(map(int, input().split()))
        man.append(l)
    input()
    for i in range(people):
        woman.append(list(map(int, input().split())))

    marrylist = gale(man, woman, people)
    print(marrylist)
