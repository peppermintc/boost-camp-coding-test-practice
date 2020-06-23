def solution(record):
    answer = []
    nicknames = []
    bottle = []
    for r in record:
        a = list(r.split(' '))
        if a[0] == 'Enter':
            bottle.append([a[0], a[1]])
            nicknames.append([a[1], a[2]])
        elif a[0] == 'Leave':
            bottle.append([a[0], a[1]])
            for i in range(0, len(nicknames)):
                if nicknames[i][0] == a[1]:
                    nicknames.remove(nicknames[i])
        elif a[0] == 'Change':
            for i in range(0, len(nicknames)):
                if a[1] == nicknames[i][0]:
                    nicknames[i][1] = a[2]
    for b in bottle:
        enterorleave = ''
        if b[0] == 'Enter':
            enterorleave = '님이 들어왔습니다.'
        else:
            enterorleave = '님이 나갔습니다.'
        for i in range(0, len(nicknames)):
            if b[1] == nicknames[i][0]:
                answer.append(nicknames[i][1] + enterorleave)
    print(answer)
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])