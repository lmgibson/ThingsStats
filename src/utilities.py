from datetime import datetime
import things
import numpy as np
from PyInquirer import prompt
from rich.console import Console
from rich.table import Table
import cliTool


def askPrintTasks(tasksList, console):
    """
    Asks user if they would like to see the tasks they made
    in the past week. Will repeat until the user answers yes
    or no.

    Args:
        createdTasks (list): list of tuples containing information
        on the tasks that have been created in the past week or month.
    """

    questions = [
        {
            'type': 'list',
            'name': 'printIncompleTasks',
            'message': 'Would you like to see the uncompleted tasks?',
            'choices': [
                'Yes',
                'No',
            ]
        }
    ]
    answers = prompt(questions)

    if answers['printIncompleTasks'] == 'Yes':
        # Sort Tasks by Date
        sortedTable = sorted(
            tasksList, key=lambda e: e['created'], reverse=True)

        table = Table(title="Incomplete Tasks")
        table.add_column("Project", justify="center")
        table.add_column("Date Created", justify="center")
        table.add_column("Title", justify="center")
        table.add_column("URL")

        for i in sortedTable:
            url = f"things:///show?id={i['uuid']}"
            table.add_row(i['project_title'],
                          i['created'][0:10],
                          i['title'],
                          url)

        print("\n")
        console.print(table)
        print("\n")

    elif answers['printIncompleTasks'] == 'No':
        pass
    else:
        console.print("Please answer with: 'Yes' or 'No'")
        askPrintTasks(tasksList)


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
        },
        {
            'type': 'input',
            'name': 'daysBack',
            'message': 'How many days back would you like?:',
            'default': lambda x: '7',
            'validate': lambda val: int(val) > 0,
            'when': lambda answers: answers['timeframe'] == 'Custom'
        }
    ]
    answers = prompt(questions)

    if answers['timeframe'] == 'Month':
        timeFrame = "30d"
    elif answers['timeframe'] == 'Week':
        timeFrame = "7d"
    elif answers['timeframe'] == 'Custom':
        timeFrame = answers['daysBack'] + "d"
    else:
        raise ValueError(
            "Something went wrong when parsing days back"
        )

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


def askPrintTrends(console):
    """
    Asks user if they would like to see trends in tasks. Prints
    datatable of trends by month sorted by year/month
    """

    questions = [
        {
            'type': 'list',
            'name': 'printTrends',
            'message': 'Would you like to see monthly trends in tasks?',
            'choices': [
                'Yes',
                'No',
            ]
        }
    ]
    answers = prompt(questions)

    if answers['printTrends'] == 'Yes':
        allTasks = things.tasks(type='to-do', status=None, index='todayIndex')

        tasksCountsByMonth = collectTaskCountsByMonth(allTasks)
        table = Table(title="Monthly Task Completion Rate")
        table.add_column("Date", justify="center")
        table.add_column("Number Created", justify="center")
        table.add_column("Number Completed", justify="center")
        table.add_column("Percent Completed", justify="center")

        for i in tasksCountsByMonth:
            completionRate = round((i['CountCompleted']/i['Count']) * 100, 0)
            table.add_row(i['YearMonth'],
                          str(i['Count']),
                          str(i['CountCompleted']),
                          str(completionRate) + "%")

        print("\n")
        console.print(table)
        print("\n")
    elif answers['printTrends'] == 'No':
        pass
    else:
        console.print("Please answer with: 'Yes' or 'No'")
        askPrintTrends()


def askStartAgain():
    questions = [
        {
            'type': 'list',
            'name': 'startAgain',
            'message': 'Would you like to do that again?',
            'choices': [
                'Yes',
                'No',
            ],
            'default': 'No'
        }
    ]
    answers = prompt(questions)

    if answers['startAgain'] == 'Yes':
        print("\n")
        cliTool.main()
