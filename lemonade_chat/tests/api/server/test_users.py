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


def test_create_user(users):

    email = 'eli.polonsky@gmail.com'

    users.create(email)

    user = users.get(email)

    assert email == user.email
    assert user.age is None
    assert user.gender is None
    assert user.name is None


def test_update_name(users):

    email = 'eli.polonsky@gmail.com'

    users.create(email)

    expected_name = 'eli'

    users.update_name(email, expected_name)

    user = users.get(email)

    assert email == user.email
    assert expected_name == user.name
    assert user.age is None
    assert user.gender is None


def test_update_age(users):

    email = 'eli.polonsky@gmail.com'

    users.create(email)

    expected_age = 50

    users.update_age(email, expected_age)

    user = users.get(email)

    assert email == user.email
    assert expected_age == user.age
    assert user.gender is None
    assert user.name is None


def test_update_gender(users):

    email = 'eli.polonsky@gmail.com'

    users.create(email)

    expected_gender = 'm'

    users.update_gender(email, expected_gender)

    user = users.get(email)

    assert email == user.email
    assert expected_gender == user.gender
    assert user.age is None
    assert user.name is None
