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

******************
Development Server
******************

Run the inbuilt local webserver with :github-source:`tools/run.sh`::

    ./tools/run.sh

This is a convenience script which also performs the following actions:

* Activate the virtual environment
* Migrate database
* Import test data on first start
* Regenerate and compile translation file

If you want to speed up this process and don't need the extra functionality, you might also use::

    ./tools/run.sh --fast

After that, open your browser and navigate to http://localhost:8086/. By default, the following users exist:

=============  ==================
Personnel ID   Group
=============  ==================
ROOT_00001     \-
ZBM_000001     ZBM
STATION_MG     STATION_MANAGEMENT
DR_0000001     MEDICAL_PERSONNEL
NURSE_0001     MEDICAL_PERSONNEL
=============  ==================

All default users share the password `changeme`.

.. Note::

    If you want to use another port than ``8086``, edit :github-source:`tools/utils/_functions.sh`.
