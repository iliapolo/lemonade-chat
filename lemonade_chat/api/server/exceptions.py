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


class ApiException(Exception):
    pass


class UserDoesNotExistException(ApiException):

    status_code = 404

    message_code = 'user_doesnt_exists'

    def __init__(self, email: object) -> None:
        self.email = email
        super().__init__(self.__str__())

    def __str__(self):
        return 'User does not exist: {}'.format(self.email)


class UserAlreadyExistsException(ApiException):

    status_code = 409

    message_code = 'user_already_exists'

    def __init__(self, email: object) -> None:
        self.email = email
        super().__init__(self.__str__())

    def __str__(self):
        return 'User already exists: {}'.format(self.email)


class InvalidEmailException(ApiException):

    status_code = 400

    message_code = 'invalid_email'

    def __init__(self, email: object) -> None:
        self.email = email
        super().__init__(self.__str__())

    def __str__(self):
        return 'Invalid email: {}. Should contain exactly one @ and at least one . (dot) ' \
               'after'.format(self.email)


class InvalidGenderException(ApiException):

    status_code = 400

    message_code = 'invalid_gender'

    def __init__(self, gender: object) -> None:
        self.gender = gender
        super().__init__(self.__str__())

    def __str__(self):
        return "Invalid gender: {}. Should be either 'f' (female) or 'm' (male) "\
            .format(self.gender)


class InvalidAgeException(ApiException):

    status_code = 400

    message_code = 'invalid_age'

    def __init__(self, age: object) -> None:
        self.age = age
        super().__init__(self.__str__())

    def __str__(self):
        return "Invalid age: {}. Should be in the range of 18 -> 120 " \
               "after".format(self.age)
