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

***********************************
YCMS CMS documentation
***********************************

This is the developer documentation for the YCMS project.

.. Note::
    For general help with the Django framework, please refer to the :doc:`django:index`.


First Steps
===========

.. toctree::
    :caption: First Steps
    :hidden:

    installation
    dev-server
    dev-tools

* :doc:`installation`: Installation guide
* :doc:`dev-server`: Run local development server
* :doc:`dev-tools`: Introduction to development tools

Basic Concepts
==============
.. toctree::
    :caption: Basic Concepts
    :hidden:

    internationalization
    documentation
    continuous-integration

* :doc:`internationalization`: Internationalization (i18n)
* :doc:`documentation`: Documentation (Sphinx)
* :doc:`continuous-integration`: Continuous Integration (Circle CI)

Deployment
==========

.. toctree::
    :caption: Deployment
    :hidden:

    packaging
    prod-server
    changelog

* :doc:`packaging`: Create an easily installable python package
* :doc:`prod-server`: Setup the production server
* :doc:`changelog`: The release history including all relevant changes

Contributing
============
.. toctree::
    :caption: Contributing
    :hidden:

    issue-reporting
    code-style-guidelines
    git-workflow
    code-of-conduct

* :doc:`issue-reporting`: How to report issues four our project
* :doc:`code-style-guidelines`: Guidelines on how to style your code
* :doc:`git-workflow`: Description of our Git workflow
* :doc:`code-of-conduct`: Our code of conduct

Reference
==============

.. toctree::
    :caption: Reference
    :hidden:

    ref/ycms

* :doc:`ref/ycms`: The main of the ycms with the following sub-packages:

  - :doc:`ref/ycms.cms`: This is the content management system for backend users which contains all database models, views, forms and templates.
  - :doc:`ref/ycms.core`: This is the project's main app which contains all configuration files.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
