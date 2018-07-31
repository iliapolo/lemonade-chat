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

from lemonade_chat.api.server.questions import BaseQuestion
from lemonade_chat.api.server.questions.qage import AgeQuestion
from lemonade_chat.api.server import utils


class GenderQuestion(BaseQuestion):

    def __init__(self, email, users) -> None:
        super().__init__(email, users)
        self._next = AgeQuestion(email, users)

    def answer(self, ans):
        utils.validate_gender(ans)
        self._users.update_gender(self._email, ans)

    def is_answered(self):

        user = self._users.get(self._email)

        return user.gender is not None

    def ask(self):
        return 'What is your gender'

    def next(self):
        return self._next
