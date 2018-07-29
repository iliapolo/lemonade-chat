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
import re


from lemonade_chat.api.server import exceptions


EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')


def serialize(obj):

    return json.dumps(obj)


def validate_age(age):

    try:
        num = int(age)
        if num > 120 or num < 18:
            raise exceptions.InvalidAgeException(age)
    except ValueError:
        raise exceptions.InvalidAgeException(age)


def validate_gender(gender):

    if gender not in ('f', 'm'):
        raise exceptions.InvalidGenderException(gender)


def validate_email(email):

    if not EMAIL_REGEX.match(email):
        raise exceptions.InvalidEmailException(email)