calls = 0
def can_win(matches):
    global calls
    calls+=1
    if matches <= 0:
        return (True , 'enemy took last match')
    if matches < 2:
        return (False, 'you have to take last match')
    by2 = ()
    if matches % 2 == 0:
        by2 = can_win(matches//2)
        if by2[0] == False:
            return(True,(((f'/2 = {matches//2}',)+by2[1]),))
        minus4 = can_win(matches - 4)
    if minus4[0] == False:
        return (True, (((f'-4 = {matches - 4}',)+ minus4[1]),))
    minus3 = can_win(matches-3)
    if minus3[0] == False:
        return (True, (((f'-3 = {matches - 3}',)+minus3[1]),))
    minus2 = can_win(matches-2)
    if minus2[0] == False:
        return (True, (((f'-2 = {matches -2}',)+ minus2[1]),))
    return (False,(((f'even if -2 = {matches -2}',) + minus2[1],) +
            ((f'even if -3 = {matches - 3}',) + minus3[1],) +
            ((f'even if -4 = {matches - 4}',) + minus4[1],)+
            (((f'even if /2 = {matches // 2}',) + by2[1]) if (matches % 2 == 0) else ()),))
for m in range(1,34):
    print(m,can_win(m))
    print()
print(can_win(33))
print(calls)