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

from setuptools import setup


BASE_PACKAGE_NAME = 'lemonade_chat'

PROGRAM_NAME = 'lemonade-chat'

setup(
    name=PROGRAM_NAME,
    version='0.1.0',
    author='Eli Polonsky',
    author_email='eli.polonsky@gmail.com',
    packages=[
        BASE_PACKAGE_NAME,
        '{0}.api'.format(BASE_PACKAGE_NAME),
        '{0}.api.server'.format(BASE_PACKAGE_NAME),
        '{0}.api.client'.format(BASE_PACKAGE_NAME),
        '{0}.shell'.format(BASE_PACKAGE_NAME),
        '{0}.shell.subcommands'.format(BASE_PACKAGE_NAME)
    ],
    entry_points={
        'console_scripts': [
            '{0} = {1}.shell.main:app'.format(PROGRAM_NAME, BASE_PACKAGE_NAME)
        ]
    },
    install_requires=[
        'click==6.7',
        'Flask==1.0.2',
        'requests==2.19.1',
        'prettytable==0.7.2'
    ]
)
