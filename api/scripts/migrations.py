#!/usr/bin/env python

import click

from app.models.BaseModel import Base
from app.models.Extractor import Extractor
from app.database import ENGINE


@click.group()
def cli() -> None:
    """This is a database migration tool"""
    pass


@cli.command()
def create():
    click.echo('Initialized the database')
    Base.metadata.create_all(ENGINE)
    click.echo('Database tables created')


@cli.command()
@click.confirmation_option(prompt='Are you sure you want to drop the database?')
def drop():
    click.echo('Dropped the database')
    Base.metadata.drop_all(ENGINE)
    click.echo('Database tables dropped')


if __name__ == '__main__':
    cli()
