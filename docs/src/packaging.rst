.. Copyright [2019] [Integreat Project]
.. Copyright [2023] [YCMS]
..
.. Licensed under the Apache License, Version 2.0 (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..     http://www.apache.org/licenses/LICENSE-2.0
..
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.

*********
Packaging
*********

.. highlight:: bash


Create python package
=====================

Packaging for a Python repository like e.g. `PyPI <https://pypi.org/>`__ is automated via our CircleCI workflow.
If you want to do the packaging process manually, build the python package with :doc:`setuptools <setuptools:index>`::

    pip3 install --upgrade pip setuptools wheel
    python3 setup.py sdist bdist_wheel

   Then, the built can be found in ``./dist/``.

Publish package
===============

You can publish the to a python repository like e.g. `PyPI <https://pypi.org/>`__ with :doc:`twine:index`:

1. Read the required authentication secrets into environment variables::

    export TWINE_USERNAME="__token__"
    read -rs TWINE_PASSWORD
    # Enter your API token and press Enter
    export TWINE_PASSWORD

2. Optionally, if you want to publish to `TestPyPI <https://test.pypi.org/>`__ instead of `PyPI <https://pypi.org/>`__::

    export TWINE_REPOSITORY=testpypi

3. Publish the package::

    twine upload --non-interactive ./dist/ycms-*.tar.gz

See the :doc:`Twine documentation <twine:index>` for all configuration options of this command.
