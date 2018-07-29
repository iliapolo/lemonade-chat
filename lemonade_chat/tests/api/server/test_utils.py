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

import pytest

from lemonade_chat.api.server import utils
from lemonade_chat.api.server.users import User
from lemonade_chat.api.server import exceptions


def test_validate_email_correct():

    utils.validate_email('eli.polonsky@gmail.com')


def test_validate_email_no_at_sign():

    with pytest.raises(exceptions.InvalidEmailException):
        utils.validate_email('eli.polonskygmail.com')


def test_validate_email_no_dot_after_at_sign():

    with pytest.raises(exceptions.InvalidEmailException):
        utils.validate_email('eli.polonsky@gmailcom')


def test_validate_age_correct():

    utils.validate_age(50)


def test_validate_age_not_a_number():

    with pytest.raises(exceptions.InvalidAgeException):
        utils.validate_age("age")


def test_validate_age_smaller_than_min():

    with pytest.raises(exceptions.InvalidAgeException):
        utils.validate_age(17)


def test_validate_age_greater_than_max():

    with pytest.raises(exceptions.InvalidAgeException):
        utils.validate_age(150)


def test_validate_gender_correct():

    utils.validate_gender('f')
    utils.validate_gender('m')


def test_validate_gender_invalid():

    with pytest.raises(exceptions.InvalidGenderException):
        utils.validate_gender('t')


def test_serialize_dict():

    serialized = utils.serialize({
        'a': 'b'
    })

    expected = '{"a": "b"}'

    assert expected == serialized
