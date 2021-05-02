import things
import utilities
from PyInquirer import prompt, Separator
from rich.console import Console


def askWhatNext(incompleteTasks, console):
    """
    Asks the user what they would like to do next by present a list of options
    for the user to select from.

    Params
    -------
        incompleteTasks (list of dicts): A list of incomplete tasks where each
        task is a dictionary.
        console (Console): Console object supplied by Rich for printing
    """
    projects = []
    for i in incompleteTasks:
        if i['project_title'] not in projects:
            projects.append(i['project_title'])
    projects.append("All")

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
        },
        {
            'type': 'list',
            'name': 'project',
            'message': 'Select a project',
            'when': lambda val: val['whatNext'] == 'View incomplete tasks',
            'choices': projects
        }
    ]

    # Extract answers
    answers = prompt(questions)
    next = answers['whatNext']
    try:
        project = answers['project']
    except:
        pass

    # Take action based on answer
    if next == 'View incomplete tasks':
        # Print incomplete tasks within X last days
        utilities.printIncompleteTasks(incompleteTasks, project, console)
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
    In the past %s days you have [bold red]created[/bold red] %s
    tasks of which you have [bold red]completed[/bold red] %s.
    """ % (timeFrame[:-1],
           totalTaskCount,
           len(completedTasks))

    console.print(report)

    # What would you like to do next
    askWhatNext(incompleteTasks, console)


if __name__ == "__main__":
    main()
