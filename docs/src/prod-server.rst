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

*****************
Production Server
*****************

.. highlight:: bash


.. Note::

    This guide explains how to set up a production server on
    `Ubuntu 20.04.3 LTS (Focal Fossa) <https://releases.ubuntu.com/20.04/>`_. Other linux distributions should work just
    fine, but we don't provide detailed instructions for them.


System requirements
===================

    1. Upgrade all::

        sudo apt update && sudo apt -y upgrade

    2. Install system requirements::

        sudo apt -y install python3-venv python3-pip libpq-dev ffmpeg


YCMS CMS Package
=============================

    1. Choose a location for your installation, e.g. ``/opt/ycms/``::

        sudo mkdir /opt/ycms
        sudo chown www-data:www-data /opt/ycms

    2. Create config and log files and set more restrictive permissions::

        sudo touch /var/log/ycms.log /etc/ycms.ini
        sudo chown www-data:www-data /var/log/ycms.log /etc/ycms.ini
        sudo chmod 660 /var/log/ycms.log /etc/ycms.ini

    3. Change to a shell with the permissions of the webserver's user ``www-data``::

        sudo -u www-data bash

    4. Create a virtual environment::

        cd /opt/ycms
        python3 -m venv .venv
        source .venv/bin/activate

    5. Install the ycms cms inside the virtual environment::

        pip3 install ycms

       .. Note::1

           If you want to set up a test system with the latest changes from the develop branch instead of the main
           branch, use TestPyPI (with the normal PyPI repository a fallback for the dependencies)::

               pip3 install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple ycms

    6. Create a symlink to the :github-source:`ycms_cms/core/wsgi.py` file to facilitate the Apache configuration::

        ln -s $(python -c "from ycms_cms.core import wsgi; print(wsgi.__file__)") .

    7. Set the initial configuration by adding the following to ``/etc/ycms.ini`` (for a full list of all
       possible configuration values, have a look at :github-source:`example-configs/ycms.ini`)::

        [ycms]

        SECRET_KEY = <your-secret-key>
        FCM_KEY = <your-firebase-key>
        BASE_URL = https://cms.ycms-app.de
        LOGFILE = /var/ycms.log

    8. Leave the www-data shell::

        exit


Static Files
============

    1. Create root directories for all static files. It's usually good practise to separate code and data, so e.g.
       create the directory ``/var/www/ycms/`` with the sub-directories ``static`` and ``media``::

        sudo mkdir -p /var/www/ycms/{static,media}

    2. Make the Apache user ``www-data`` owner of these directories::

        sudo chown -R www-data:www-data /var/www/ycms

    3. Add the static directories to the config in ``/etc/ycms.ini``::

        STATIC_ROOT = /var/www/ycms/static
        MEDIA_ROOT = /var/www/ycms/media

    4. Collect static files::

        cd /opt/ycms
        sudo -u www-data bash
        source .venv/bin/activate
        ycms-cli collectstatic
        exit


Webserver
=========

    1. Install an `Apache2 <https://httpd.apache.org/>`_ server with `mod_wsgi <https://modwsgi.readthedocs.io/en/develop/>`_::

        sudo apt -y install apache2 libapache2-mod-wsgi-py3

    2. Enable the ``rewrite`` and ``wsgi``::

        sudo a2enmod rewrite wsgi

    3. Setup a vhost for the ycms by using our example config: :github-source:`example-configs/apache2-ycms-vhost.conf`
       and edit the your domain and the paths for static files.


Database
========

    1. Install a `PostgreSQL <https://www.postgresql.org/>`_ database on your system::

        sudo apt -y install postgresql

    2. Create a database user ``ycms`` and set a password::

        sudo -u postgres createuser -P -d ycms

    3. Create a database ``ycms``::

        sudo -u postgres createdb -O ycms ycms

    4. Add the database credentials to the config in ``/etc/ycms.ini``::

        DB_PASSWORD = <your-password>

    5. Execute initial migrations::

        cd /opt/ycms
        sudo -u www-data bash
        source .venv/bin/activate
        ycms-cli migrate


Email configuration
===================

    1. Add your SMTP credentials to ``/etc/ycms.ini`` (for the default values, see :github-source:`example-configs/ycms.ini`)::

        EMAIL_HOST = <your-smtp-server>
        EMAIL_HOST_USER = <your-username>
        EMAIL_HOST_PASSWORD = <your-password>
