import click


@click.command()
@click.argument(
    "files",
    nargs=-1,
    type=click.File("r"),
)
def cli(files):
    for file in files:
        click.echo(file.read())


if __name__ == "__main__":
    cli()
