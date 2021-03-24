from datetime import datetime
import numpy as np
from pywebio.input import select, input, radio
from pywebio.output import put_text, put_markdown, put_table, put_link


def askPrintTasks(tasksList):
    """Asks user if they would like to see the tasks they made
    in the past week. Will repeat until the user answers yes
    or no.

    Args:
        createdTasks (list): list of tuples containing information
        on the tasks that have been created in the past week or month.
    """
    printTasks = radio(
        "Would you like to see the uncompleted tasks?", options=['Yes', 'No']).lower()

    if printTasks == 'yes':
        # Formatting Table
        for i in tasksList:
            i[2] = "things:///show?id=%s" % i[2]
        put_markdown('### Task List')
        put_table(tasksList, header=['Date', 'Title', 'Link'])
    elif printTasks == 'no':
        pass
    else:
        print("Please answer with: y or N")
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
    """Presents a terminal list so the user can select their
    timeframe of analysis.

    Returns:
        integer: timeframe in integer values 30 for month, 6 for week.
    """
    menu_choice = select('Select a timeframe', ['Month', 'Week', 'Custom'])

    if menu_choice == 'Month':
        timeFrame = 30
    elif menu_choice == 'Week':
        timeFrame = 6
    else:
        timeFrame = customTimeFrame()

    return timeFrame


def askPrintTrends(monthlyCompletions):
    """Asks user if they would like to see trends in tasks. Prints
    datatable of trends by month
    """
    printTasks = radio(
        "Would you like to see monthly trends in tasks?", options=['Yes', 'No']).lower()

    if printTasks == 'yes':
        # Print table
        put_markdown("### Trends")
        put_text("\n\t Month     # Created   # Completed")

        completionRates = []
        for dates in monthlyCompletions:
            data = [data for data in dates]

            # Format date as we would like. This is due to limitations of SQlite.
            data[0] = datetime.strptime(data[0], "%Y-%m-%d").strftime("%b-%y")

            # Print trends
            put_text("\t%s        %s           %s" %
                     (data[0], data[1], data[2]))

            # Calculate completion rate by month-year
            if data[1] != 0:
                completionRates.append(round(data[2]/data[1], 3)*100)
            else:
                pass

        # Print summary message
        put_text("You complete %.2f %% of your tasks, per month, on average" %
                 np.mean(np.array(completionRates)))

    elif printTasks == 'no':
        pass
    else:
        print("Please answer with: y or n")
        askPrintTrends(monthlyCompletions)
