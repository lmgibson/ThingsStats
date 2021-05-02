import click
import ThingsReport


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
def hello():
    """
    Prints hello.
    """
    print("Hello!")


things.add_command(report)
things.add_command(hello)


if __name__ == '__main__':
    things()
