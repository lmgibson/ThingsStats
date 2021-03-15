from simple_term_menu import TerminalMenu
import numpy as np

def askPrintTasks(createdTasks):
    """Asks user if they would like to see the tasks they made
    in the past week. Will repeat until the user answers yes
    or no.

    Args:
        createdTasks (list): list of tuples containing information
        on the tasks that have been created in the past week or month.
    """
    printTasks = input(
        "Would you like to see the created tasks [y/N]?\n").lower()

    if printTasks == 'y':
        print("\n  Date         Task")
        for taskTuple in createdTasks:
            data = [task for task in taskTuple]
            print("%s: %s" % (data[0], data[1]))
    elif printTasks == 'n':
        pass
    else:
        print("Please answer with: y or N")
        askPrintTasks(createdTasks)

def askForTimeFrame():
    """Presents a terminal list so the user can select their
    timeframe of analysis.

    Returns:
        integer: timeframe in integer values 30 for month, 6 for week.
    """
    print("Please select a timeframe for your report:\n")
    terminal_menu = TerminalMenu(["Month", "Week"])
    menu_choice = terminal_menu.show()
    if menu_choice == 0:
        timeFrame = 30
    elif menu_choice == 1:
        timeFrame = 6

    return timeFrame

def askPrintTrends(monthlyCompletions):
    """Asks user if they would like to see trends in tasks. Prints
    datatable of trends by month
    """
    printTasks = input(
        "Would you like to see monthly trends in tasks? [y/N]?\n").lower()

    if printTasks == 'y':
        # Print table
        print("\n  Month  Tasks Created   Tasks Completed")
        
        completionRates = [0]*len(monthlyCompletions)
        for idx, dates in enumerate(monthlyCompletions):
            data = [data for data in dates]
            print("%s:        %s           %s" % (data[0], data[1], data[2]))
            completionRates[idx] = round(data[2]/data[1],3)*100

        # Print summary message
        print("You complete %s %% of your tasks, per month, on average" % np.mean(np.array(completionRates)))
        
    elif printTasks == 'n':
        pass
    else:
        print("Please answer with: y or N")
        askPrintTrends(monthlyCompletions)