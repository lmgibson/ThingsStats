from simple_term_menu import TerminalMenu
import numpy as np


def askPrintTasks(tasksList):
    """Asks user if they would like to see the tasks they made
    in the past week. Will repeat until the user answers yes
    or no.

    Args:
        createdTasks (list): list of tuples containing information
        on the tasks that have been created in the past week or month.
    """
    printTasks = input(
        "Would you like to see the uncompleted tasks? [y/n]: ").lower()

    if printTasks == 'y':
        print("\n\t  Date            Task")
        for taskTuple in tasksList:
            data = [task for task in taskTuple]
            print("\t%s:    %s" % (data[0], data[1]))
    elif printTasks == 'n':
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
    print("Please select a timeframe for your report:")
    terminal_menu = TerminalMenu(["Month", "Week", "Custom"])
    menu_choice = terminal_menu.show()
    if menu_choice == 0:
        timeFrame = 30
    elif menu_choice == 1:
        timeFrame = 6
    else:
        timeFrame = customTimeFrame()

    return timeFrame


def askPrintTrends(monthlyCompletions):
    """Asks user if they would like to see trends in tasks. Prints
    datatable of trends by month
    """
    printTasks = input(
        "\nWould you like to see monthly trends in tasks? [y/n]: ").lower()

    if printTasks == 'y':
        # Print table
        print("\n\t Month     # Created   # Completed")

        completionRates = [0]*len(monthlyCompletions)
        for idx, dates in enumerate(monthlyCompletions):
            data = [data for data in dates]
            print("\t%s        %s           %s" % (data[0], data[1], data[2]))
            completionRates[idx] = round(data[2]/data[1], 3)*100

        # Print summary message
        print("\nYou complete %s %% of your tasks, per month, on average" %
              np.mean(np.array(completionRates)))

    elif printTasks == 'n':
        pass
    else:
        print("Please answer with: y or n")
        askPrintTrends(monthlyCompletions)
