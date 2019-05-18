import random
import time

cardList = []
AList = []
BList = []
CList = []
DList = []


def initialize ():
    baseList = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    global cardList
    global AList
    global BList
    global CList
    global DList

    cardList.extend(baseList)
    cardList.extend(baseList)
    cardList.extend(baseList)
    cardList.extend(baseList)

    random.shuffle(cardList)

    for x in range(len(cardList)):
        if x%4 == 1:
            AList.append(cardList[x])
        elif x%4 == 2:
            BList.append(cardList[x])
        elif x%4 == 3:
            CList.append(cardList[x])
        else:
            DList.append(cardList[x])

def start ():
    tableList = []
    ALoser = 0
    BLoser = 0
    CLoser = 0
    DLoser = 0
    rounds = 0


    while ALoser + BLoser + CLoser + DLoser < 3:
        rounds += 1
        print("------------------------- New Round (" + str(rounds) + ")-------------------------")
        print("Card on Table: " + ','.join(tableList) + '(' + str(len(tableList)) + ')')
        print("Player A: " + ','.join(AList) + '(' + str(len(AList)) + ')')
        print("Player B: " + ','.join(BList) + '(' + str(len(BList)) + ')')
        print("Player C: " + ','.join(CList) + '(' + str(len(CList)) + ')')
        print("Player D: " + ','.join(DList) + '(' + str(len(DList)) + ')')
        print("\n\n")

        if len(AList) >0:
            tableList.append(AList.pop(0))
            print("(Player A) Card on Table: " + ','.join(tableList) + '(' + str(len(tableList)) + ')')
            for i in range(len(tableList)-1):
                if tableList[i] == tableList[-1]:
                    print("*** Match Found  for  Player A (Win: " + str(len(tableList) - i) + ") ***")
                    #print("Player A: " + ','.join(AList))
                    AList.extend(tableList[i:])
                    #print("Player A: " + ','.join(AList))
                    if i == 0:
                        tableList = []
                    else:
                        tableList = tableList[0:i]
                    break
            if (len(AList) ==0 ):
                ALoser = 1


        if len(BList) >0:
            tableList.append(BList.pop(0))
            print("(Player B) Card on Table: " + ','.join(tableList) + '(' + str(len(tableList)) + ')')
            for i in range(len(tableList)-1):
                if tableList[i] == tableList[-1]:
                    print("*** Match Found  for  Player B (Win: " + str(len(tableList) - i) + ") ***")
                    #print(tableList)
                    #print("Player B: " + ','.join(BList))
                    BList.extend(tableList[i:])
                    #print("Player B: " + ','.join(BList))
                    if i == 0:
                        tableList = []
                    else:
                        tableList = tableList[0:i]
                    break
            if (len(BList) == 0):
                BLoser = 1

        if len(CList) >0:
            tableList.append(CList.pop(0))
            print("(Player C) Card on Table: " + ','.join(tableList) + '(' + str(len(tableList)) + ')')
            for i in range(len(tableList)-1):
                if tableList[i] == tableList[-1]:
                    print("*** Match Found  for  Player C (Win: " + str(len(tableList) - i) + ") ***")
                    #print(tableList)
                    #print("Player C: " + ','.join(CList))
                    CList.extend(tableList[i:])
                    #print("Player C: " + ','.join(CList))
                    if i == 0:
                        tableList = []
                    else:
                        tableList = tableList[0:i]
                    break
            if (len(CList) == 0):
                CLoser = 1

        if len(DList) >0:
            tableList.append(DList.pop(0))
            print("(Player D) Card on Table: " + ','.join(tableList) + '(' + str(len(tableList)) + ')')
            for i in range(len(tableList)-1):
                if tableList[i] == tableList[-1]:
                    print("*** Match Found  for  Player D (Win: " + str(len(tableList) - i) + ") ***")
                    #print(tableList)
                    #print("Player D: " + ','.join(DList))
                    DList.extend(tableList[i:])
                    #print("Player D: " + ','.join(DList))
                    if i == 0:
                        tableList = []
                    else:
                        tableList = tableList[0:i]
                    break
            if (len(DList) == 0):
                DLoser = 1

        print("\n\n")

        time.sleep(0.01)


if __name__ == "__main__":
    initialize()
    print("Player A: " + ','.join(AList) + '(' + str(len(AList)) + ')')
    print("Player B: " + ','.join(BList) + '(' + str(len(BList)) + ')')
    print("Player C: " + ','.join(CList) + '(' + str(len(CList)) + ')')
    print("Player D: " + ','.join(DList) + '(' + str(len(DList)) + ')')
    start()
    print("------------------------- Game End-------------------------")

