import things
import utilities
from PyInquirer import prompt, Separator
from rich.console import Console
from rich.table import Table


def askWhatNext(incompleteTasks, console):
    questions = [
        {
            'type': 'list',
            'name': 'whatNext',
            'message': 'What would you like to view next?',
            'choices': [
                'View incomplete tasks',
                'Count incomplete tasks by project',
                Separator(),
                'View monthly completion rate',
                Separator(),
                'Select a new timeframe',
                'exit'
            ]
        }
    ]
    next = prompt(questions)['whatNext']

    if next == 'View incomplete tasks':
        # Print incomplete tasks within X last days
        utilities.printIncompleteTasks(incompleteTasks, console)
        askWhatNext(incompleteTasks, console)
    elif next == 'Count incomplete tasks by project':
        utilities.getIncompleteByProject(console)
        askWhatNext(incompleteTasks, console)
    elif next == 'View monthly completion rate':
        # Print trends in task completions
        utilities.printTrends(console)
        askWhatNext(incompleteTasks, console)
    elif next == 'Select a new timeframe':
        main()
    elif next == 'exit':
        exit()


def main():
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


if __name__ == "__main__":
    main()
