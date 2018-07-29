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

import os
import shutil
import tempfile


import pytest


from lemonade_chat.api.server import users


@pytest.fixture(name='temp_file')
def _temp_file(request, temp_dir):

    name = request.node.name

    file_path = os.path.join(temp_dir, name)

    with open(file_path, 'w') as stream:
        stream.write('')

    yield file_path


@pytest.fixture(name='temp_dir')
def _temp_dir():

    dir_path = tempfile.mkdtemp()

    try:
        yield dir_path
    finally:
        rmf(dir_path)


@pytest.fixture(name='users')
def _users(temp_file):
    storage = users.Users(db=temp_file)
    try:
        yield storage
    finally:
        storage.close()


def rmf(directory):

    """
    Delete the entire directory. This function also handles windows "Access Denied" errors when the
    directory contains read-only files. This function is equivalent to 'rm -rf' on linux systems.

    Args:
        directory (str): Path to the directory to delete.
    """

    def remove_read_only(func, path, _):
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWRITE)
        func(path)

    shutil.rmtree(directory, onerror=remove_read_only)
