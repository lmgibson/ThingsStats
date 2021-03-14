def getInputs(inputsList):
    if inputsList[1] in ['month', 'week']:
        timeFrame = inputsList[1]
    else:
        print("Please provide a timeframe of 'month' or 'week'")
        exit()

    return timeFrame
