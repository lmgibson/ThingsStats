import click
import ThingsReport
import ThingsAddDaily


@click.group()
def things():
    pass


@click.command()
def report():
    """
    Interactive reporting
    """
    ThingsReport.main()


@click.command()
@click.argument('message')
def add(message):
    """
    Adds a checklist item to a daily todo tracker
    """
    ThingsAddDaily.main(message)


things.add_command(report)
things.add_command(add)


def main():
    things()


if __name__ == '__main__':
    main()
