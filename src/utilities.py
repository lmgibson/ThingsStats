from datetime import datetime
import things
import numpy as np
from PyInquirer import prompt


def askPrintTasks(tasksList):
    """
    Asks user if they would like to see the tasks they made
    in the past week. Will repeat until the user answers yes
    or no.

    Args:
        createdTasks (list): list of tuples containing information
        on the tasks that have been created in the past week or month.
    """
    printTasks = radio(
        "Would you like to see the uncompleted tasks?", options=['Yes', 'No'])

    if printTasks == 'Yes':
        # Sort Tasks by Date
        sortedTable = sorted(
            tasksList, key=lambda e: e['created'], reverse=True)

        # Formatting Table
        tableList = []
        for i in sortedTable:
            tableList.append([i['created'], put_link(
                i['title'], "things:///show?id=%s" % i['uuid'])])
            # i[1] = put_link(i['created'], "things:///show?id=%s" % i['uuid'])
            # _ = i.pop()
        put_markdown('### Task List')
        put_table(tableList, header=['Date', 'Title'])
    elif printTasks == 'No':
        pass
    else:
        put_text("Please answer with: 'Yes' or 'No'")
        askPrintTasks(tasksList)


def customTimeFrame():
    questions = [
        {
            'type': 'input',
            'name': 'daysBack',
            'message': 'How many days back would you like?:',
            'validate': lambda val: int(val) >= 0
        }
    ]

    answers = prompt(questions)

    # notValidInput = 1
    # while notValidInput:
    #     customTimeFrame = input("How many days back would you like?: ")
    #     try:
    #         timeFrame = int(customTimeFrame)
    #         if timeFrame <= 0:
    #             print("Please enter a number greater than 0")
    #         elif timeFrame > 0:
    #             notValidInput = 0
    #     except:
    #         print("Please enter a positive number.")

    return answers['daysBack']


def askForTimeFrame():
    """
    Presents a terminal list so the user can select their
    timeframe of analysis.

    Returns:
        integer: timeframe in integer values 30 for month, 6 for week.
    """

    questions = [
        {
            'type': 'list',
            'name': 'timeframe',
            'message': 'How many days back?',
            'choices': [
                'Month',
                'Week',
                'Custom',
            ]
        }
    ]
    answers = prompt(questions)

    if answers['timeframe'] == 'Month':
        timeFrame = "30d"
    elif answers['timeframe'] == 'Week':
        timeFrame = "7d"
    else:
        timeFrame = str(customTimeFrame()) + "d"

    return timeFrame


def collectTaskCountsByMonth(taskList):
    """
    Takes in a list of tasks and returns a sorted table counting the 
    number of tasks created in each month and the number completed
    in each month.

    Args:
        allTasks ([list of dicts]): A list of dictionaries where each
        dictionary is a task.

    Returns:
        [list of dicts]: Returns a sorted list of dictionaries that
        has information on the # of tasks created by year-month and
        # completed.
    """

    yearMonth = [datetime.strptime(
        i['created'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m') for i in taskList]

    yearMonthCompleted = [datetime.strptime(
        i['created'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m') for i in taskList if i['status'] == 'completed']

    countDict = {}
    for i in yearMonth:
        if i not in countDict.keys():
            countDict[i] = yearMonth.count(i)

    completedCountDict = {}
    for i in yearMonthCompleted:
        if i not in completedCountDict.keys():
            completedCountDict[i] = yearMonthCompleted.count(i)

    combinedCountsListDict = []
    for i, val in enumerate(countDict):
        combinedCountsListDict.append({'YearMonth': val, 'Count': countDict[val],
                                       'CountCompleted': completedCountDict[val],
                                       'Year': int(val[0:4]), 'Month': int(val[5:7])})

    sortedTable = sorted(
        combinedCountsListDict, key=lambda x: (x['Year'], x['Month']), reverse=True)

    for i in sortedTable:
        del i['Year']
        del i['Month']

    return sortedTable


def askPrintTrends():
    """
    Asks user if they would like to see trends in tasks. Prints
    datatable of trends by month sorted by year/month
    """
    printTasks = radio(
        "Would you like to see monthly trends in tasks?", options=['Yes', 'No'])

    if printTasks == 'Yes':
        allTasks = things.tasks(type='to-do', status=None, index='todayIndex')

        tasksCountsByMonth = collectTaskCountsByMonth(allTasks)
        tableColumnNames = list(tasksCountsByMonth[0].keys())

        put_markdown("### Trends")
        put_table(tasksCountsByMonth, header=tableColumnNames)

    elif printTasks == 'No':
        pass
    else:
        put_text("Please answer with: 'Yes' or 'No'")
        askPrintTrends()
