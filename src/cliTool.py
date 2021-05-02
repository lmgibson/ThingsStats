import things
import utilities
from PyInquirer import prompt
from rich.console import Console
from rich.table import Table


def askWhatNext(incompleteTasks, console):
    questions = [
        {
            'type': 'list',
            'name': 'whatNext',
            'message': 'What would you like to view next?',
            'choices': [
                'Incomplete tasks',
                'Monthly completion rate',
                'exit'
            ]
        }
    ]
    next = prompt(questions)['whatNext']

    if next == 'Incomplete tasks':
        # Print incomplete tasks within X last days
        utilities.printIncompleteTasks(incompleteTasks, console)
        askWhatNext(incompleteTasks, console)
    elif next == 'Monthly completion rate':
        # Print trends in task completions
        utilities.printTrends(console)
        askWhatNext(incompleteTasks, console)
    elif next == 'exit':
        exit()


if __name__ == "__main__":
    console = Console()

    # Get requested timeframe
    timeFrame = utilities.askForTimeFrame()

    # Get stats
    totalTaskCount = things.todos(last=timeFrame, status=None,
                                  trashed=False, count_only=True)
    completedTasks = things.todos(
        last=timeFrame, status='completed')
    incompleteTasks = things.todos(
        last=timeFrame, status='incomplete')

    # Report to standard output
    report = """
          :raccoon: Stats Overview :raccoon: 
    ------------------------------------
    In the past %s days you have [bold]created[/bold] 
    %s tasks of which you have [bold]completed[/bold] %s.
    """ % (timeFrame[:-1],
           totalTaskCount,
           len(completedTasks))

    console.print(report)

    # What would you like to do next
    askWhatNext(incompleteTasks, console)
