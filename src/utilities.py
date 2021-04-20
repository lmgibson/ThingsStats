from datetime import datetime
import things
import numpy as np
from pywebio.input import select, input, radio
from pywebio.output import put_text, put_markdown, put_table, put_link


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
        # Formatting Table
        tableList = []
        for i in tasksList:
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
    notValidInput = 1
    while notValidInput:
        customTimeFrame = input("How many days back would you like?: ")
        try:
            timeFrame = int(customTimeFrame)
            if timeFrame <= 0:
                print("Please enter a number greater than 0")
            elif timeFrame > 0:
                notValidInput = 0
        except:
            print("Please enter a positive number.")

    return timeFrame


def askForTimeFrame():
    """
    Presents a terminal list so the user can select their
    timeframe of analysis.

    Returns:
        integer: timeframe in integer values 30 for month, 6 for week.
    """
    menu_choice = select('Select a timeframe', ['Month', 'Week', 'Custom'])

    if menu_choice == 'Month':
        timeFrame = "30d"
    elif menu_choice == 'Week':
        timeFrame = "7d"
    else:
        timeFrame = str(customTimeFrame()) + "d"

    return timeFrame


def askPrintTrends():
    """Asks user if they would like to see trends in tasks. Prints
    datatable of trends by month
    """
    printTasks = radio(
        "Would you like to see monthly trends in tasks?", options=['Yes', 'No'])

    if printTasks == 'Yes':
        allTasks = things.tasks(type='to-do', status=None, index='todayIndex')

        monthlyCompletions = {'yrMonth': [], 'Count': [], 'CountCompleted': []}
        for i in allTasks:
            createdDate = datetime.strptime(i['created'], '%Y-%m-%d %H:%M:%S')
            yearMonth = createdDate.strftime("%Y-%m")

            if yearMonth in monthlyCompletions['yrMonth']:
                monthlyCompletions['Count'][monthlyCompletions['yrMonth'].index(
                    yearMonth)] += 1
                if i['status'] == "completed":
                    monthlyCompletions['CountCompleted'][monthlyCompletions['yrMonth'].index(
                        yearMonth)] += 1
            else:
                monthlyCompletions['yrMonth'].append(yearMonth)
                monthlyCompletions['Count'].append(1)
                if i['status'] == "completed":
                    monthlyCompletions['CountCompleted'].append(1)

        # Print table
        put_markdown("### Trends")
        put_text("Date          Count            Count Completed")
        for i in range(0, len(monthlyCompletions['yrMonth'])):
            put_text("%s %s %s" % (
                monthlyCompletions['yrMonth'][i], monthlyCompletions['Count'][i], monthlyCompletions['CountCompleted'][i]))
        # Print summary message
        # put_text("You complete %.2f %% of your tasks, per month, on average" %
        #  np.mean(np.array(completionRates)))

    elif printTasks == 'No':
        pass
    else:
        put_text("Please answer with: 'Yes' or 'No'")
        askPrintTrends()
