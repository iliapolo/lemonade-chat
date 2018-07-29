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

import sys

import click

from lemonade_chat.shell.subcommands import server as server_group
from lemonade_chat.shell.subcommands import client as client_group
from lemonade_chat.api.client.client import LemonadeClient


@click.group()
def app():
    pass


@click.group()
def server():
    pass


@click.group()
@click.option('--server-port', default=5000,
              help='Which port does the server listen to')
@click.pass_context
def client(ctx, server_port):

    ctx.client = LemonadeClient(server_port)


server.add_command(server_group.start)
client.add_command(client_group.register)
client.add_command(client_group.view)

app.add_command(server)
app.add_command(client)

# allows running the application as a single executable
# created by pyinstaller
if getattr(sys, 'frozen', False):
    app(sys.argv[1:])
