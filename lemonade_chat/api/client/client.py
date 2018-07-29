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

import json

import requests

from lemonade_chat.api.client import exceptions


class LemonadeClient(object):

    def __init__(self, server_port) -> None:
        super().__init__()
        self.server_port = server_port

    def welcome(self):

        response = requests.get('http://localhost:{}/welcome'.format(self.server_port))

        return deserialize(response)

    def identify(self, email):

        response = requests.post('http://localhost:{}/identify'.format(self.server_port), json={
            'answer': email
        })

        return deserialize(response)

    def view(self, email):

        response = requests.get('http://localhost:{}/users/{}'.format(self.server_port, email))

        return deserialize(response)

    def exchange(self, email, ans):

        response = requests.put('http://localhost:{}/exchange'.format(self.server_port), json={
            'answer': ans,
            'email': email
        })

        return deserialize(response)


def deserialize(response):

    if response.ok:
        return json.loads(response.text)['data']

    if response.status_code == 400:
        error = json.loads(response.text)
        raise exceptions.BadRequestException(code=error['code'], message=error['message'])

    if response.status_code == 404:
        error = json.loads(response.text)
        raise exceptions.ResourceNotFoundException(code=error['code'], message=error['message'])

    raise RuntimeError(response.text)
