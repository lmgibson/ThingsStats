from simple_term_menu import TerminalMenu

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