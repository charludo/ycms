.. Copyright [2019] [Integreat Project]
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

************
Installation
************

.. Note::

    If you want to develop on Windows, we suggest using the `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/>`_ in combination with `Ubuntu <https://ubuntu.com/wsl>`_.


Prerequisites
=============

Followings are required before installing the project (install them with your manager):

* `git <https://git-scm.com/>`_
* `python3.9 <https://www.python.org/downloads/release/python-390/>`_ or higher
* `python3-pip <https://packages.ubuntu.com/search?keywords=python3-pip>`_ (`Debian-based distributions <https://en.wikipedia.org/wiki/Category:Debian-based_distributions>`_, e.g. `Ubuntu <https://ubuntu.com>`__) / `python-pip <https://www.archlinux.de/packages/extra/x86_64/python-pip>`_ (`Arch-based distributions <https://wiki.archlinux.org/index.php/Arch-based_distributions>`_)
* `python3-venv <https://docs.python.org/3/library/venv.html>`__
* `libpq-dev <https://www.postgresql.org/docs/9.5/libpq.html>`__ to compile `psycopg2 <https://www.psycopg.org/docs/install.html#build-prerequisites>`__
* `gettext <https://www.gnu.org/software/gettext/>`_ and `pcregrep <https://pcre.org/original/doc/html/pcregrep.html>`_ to use the translation features

Download sources
================

.. highlight:: bash

Clone the project, either

.. container:: two-columns

    .. container:: left-side

        via SSH:

        .. parsed-literal::

            git clone git\@github.com:|github-username|/|github-repository|.git
            cd |github-repository|

    .. container:: right-side

        or HTTPS:

        .. parsed-literal::

            git clone \https://github.com/|github-username|/|github-repository|.git
            cd |github-repository|


Install dependencies and local
======================================

And install it using our developer tool :github-source:`tools/install.sh`::

    ./tools/install.sh --pre-commit
