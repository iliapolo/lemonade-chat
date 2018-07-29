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

import click


from lemonade_chat.api.server import server as app


@click.command()
@click.option('--port', default=5000,
              help='Which port should the server listen on')
@click.option('--db', default='lemonade.db',
              help='Path to a db file, one will be created if it doesnt exist')
def start(db, port):
    app.start(db=db, port=port)
