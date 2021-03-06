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

from flask import Flask
from flask import request
from flask import g
from flask import jsonify
from werkzeug.local import LocalProxy

from lemonade_chat.api.server import exceptions
from lemonade_chat.api.server import utils
from lemonade_chat.api.server.users import Users
from lemonade_chat.api.server import questions


app = Flask(__name__)
db_file = None


def get_users():

    if 'users' not in g:
        g.users = Users(db_file)

    return g.users


users = LocalProxy(get_users)


@app.route('/welcome')
def welcome():

    return response(
        {
            'is_over': False,
            'text': 'Welcome to Lemonade!\n\nWhat is your email address'
        }
    )


@app.route('/identify', methods=['POST'])
def identify():

    data = json.loads(request.data)

    email = data['answer']

    try:
        users.create(email)
    except exceptions.UserAlreadyExistsException:
        pass

    question = questions.start_for(email, users)

    while question:
        if not question.is_answered():
            return response({
                'is_over': False,
                'text': question.ask()
            })

        question = question.next()

    return response(
        {
            'is_over': True,
            'text': 'You are already registered with us, yey! :)'
        }
    )


@app.route('/exchange', methods=['PUT'])
def exchange():

    data = json.loads(request.data)

    email = data['email']
    answer = data['answer']

    question = questions.start_for(email, users)

    while question:
        if not question.is_answered():
            question.answer(answer)

            if question.next():
                return response({
                    'is_over': False,
                    'text': question.next().ask()
                })
            break
        question = question.next()

    return response(
        {
            'is_over': True,
            'text': 'You successfully registered for lemonade, thanks!'
        }
    )


@app.route('/users/<email>')
def view(email):

    user = users.get(email)

    return response(user.to_dict())


@app.errorhandler(exceptions.ApiException)
def handle_api_exception(error):
    res = jsonify({
        'message': str(error),
        'code': error.message_code
    })
    res.status_code = error.status_code
    return res


@app.teardown_appcontext
def teardown_db(*_):

    storage = g.pop('users', None)

    if storage is not None:
        storage.close()


def response(data):

    return utils.serialize({
        'data': data
    })


def start(db='lemonade.db', port=5000):

    global db_file
    db_file = db
    app.run(port=port)
