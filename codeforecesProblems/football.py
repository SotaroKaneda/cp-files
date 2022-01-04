players = input()
onePlayers = 0
zeroPlayers = 0
dangerous = False
#counter = 0
for player in players:
    #print(counter)
    #print(zeroPlayers)
    #print(onePlayers)
    if player == '0':
        zeroPlayers += 1
        onePlayers = 0
        if zeroPlayers > 6:
            dangerous = True
    #        print("danger")
    else:
        onePlayers += 1
        zeroPlayers = 0
        if onePlayers > 6:
            dangerous = True 
    #        print("danger")
    #counter += 1
if dangerous:
    print("YES")
else:
    print("NO")

