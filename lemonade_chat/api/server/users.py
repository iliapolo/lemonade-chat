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

import sqlite3

from lemonade_chat.api.server import utils
from lemonade_chat.api.server import exceptions


class User(object):

    def __init__(self, email, name=None, age=None, gender=None) -> None:
        self.email = email
        self.name = name
        self.age = age
        self.gender = gender

    def to_dict(self):
        return self.__dict__


class Users(object):

    def __init__(self, db) -> None:
        self._conn = sqlite3.connect(db)
        self._execute_sql('CREATE TABLE IF NOT EXISTS users '
                          '(email text unique, name text, gender text, age int)')

    def create(self, email):

        utils.validate_email(email)

        try:
            self._execute_sql("INSERT INTO users (email) values ('{}')".format(email))
        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed: users.email' in str(e):
                raise exceptions.UserAlreadyExistsException(email)
            raise

    def update_age(self, email, age):

        utils.validate_age(age)

        self._execute_sql("UPDATE users SET age = '{}' WHERE email = '{}'".format(age, email))

    def update_gender(self, email, gender):

        utils.validate_gender(gender)

        self._execute_sql("UPDATE users SET gender = '{}' WHERE email = '{}'".format(gender, email))

    def update_name(self, email, name):

        self._execute_sql("UPDATE users SET name = '{}' WHERE email = '{}'".format(name, email))

    def get(self, email):

        result = self._execute_sql("SELECT * FROM users WHERE email = '{}'".format(email))

        user = User(email)

        if not result:
            raise exceptions.UserDoesNotExistException(email)

        user.name = result[0][1]
        user.gender = result[0][2]
        user.age = result[0][3]

        return user

    def close(self):
        self._conn.close()

    def _execute_sql(self, statement):

        c = self._conn.cursor()

        c.execute(statement)

        self._conn.commit()

        result = c.fetchall()

        return result
