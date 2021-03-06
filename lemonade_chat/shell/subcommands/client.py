#############################################################################
# Copyright (c) 2018 Eli Polonsky. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   * See the License for the specific language governing permissions and
#   * limitations under the License.
#
#############################################################################

from prettytable import PrettyTable

import click

from lemonade_chat.api.client import exceptions


@click.command()
@click.pass_context
def register(ctx):

    client = ctx.parent.client

    # let the server know we are here.
    exchange = client.welcome()

    # first thing the server does is ask for our email address.
    # lets give it to him.
    email = click.prompt(exchange['text'])
    exchange, email = _identify(client, email)

    while True:

        # now we keep responding to the server with
        # answers to his questions, until he tells us to stop.
        if exchange['is_over']:
            click.echo(exchange['text'])
            break

        answer = click.prompt(exchange['text'])
        exchange = _exchange(client, email, answer)


@click.command()
@click.pass_context
def view(ctx):

    client = ctx.parent.client

    # let the server know we are here
    exchange = client.welcome()

    # first thing the server does is ask for our email address.
    # lets give it to him.
    email = click.prompt(exchange['text'])
    user = _view(client, email)

    # create a one row table to display the user
    # information in a nice way
    keys = user.keys()
    table = PrettyTable(field_names=keys)
    row = []
    for key in keys:
        row.append(user[key])
    table.add_row(row)

    click.echo(table.get_string())


def _identify(client, email):

    while True:

        # we want to give the user a chance to correct his input.
        # how many chances? don't know, lets say infinity for now
        try:
            return client.identify(email), email
        except exceptions.BadRequestException as e:
            click.echo(e.message)
            email = _try_again()


def _view(client, email):

    while True:

        # we want to give the user a chance to correct his input.
        # how many chances? don't know, lets say infinity for now
        try:
            return client.view(email)
        except exceptions.ResourceNotFoundException as e:
            click.echo(e.message)
            email = _try_again()


def _exchange(client, email, answer):

    while True:

        # we want to give the user a chance to correct his input.
        # how many chances? don't know, lets say infinity for now
        try:
            return client.exchange(email, answer)
        except exceptions.BadRequestException as e:
            click.echo(e.message)
            answer = _try_again()


def _try_again():

    return click.prompt('Try again')
