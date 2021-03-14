def parseInputs(inputsList):
    if inputsList[1] in ['month', 'week']:
        timeFrame = inputsList[1]
    else:
        print("Please provide a timeframe of 'month' or 'week'")
        exit()

    return timeFrame


def askPrintTasks(createdTasks):
    printTasks = input(
        "Would you like to see the created tasks [y/N]?\n").lower()

    if printTasks == 'y':
        for i in createdTasks:
            print(i)
    elif printTasks == 'n':
        pass
    else:
        print("Please answer with: y or N")
        askPrintTasks(createdTasks)

    return
