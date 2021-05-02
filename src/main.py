import click
import ThingsReport
import ThingsAddDaily


@click.group()
def things():
    pass


@click.command()
def report():
    """
    Initializes interactive reporting
    """
    ThingsReport.main()


@click.command()
@click.argument('message')
def add(message):
    ThingsAddDaily.main(message)


things.add_command(report)
things.add_command(add)


if __name__ == '__main__':
    things()
