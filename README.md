<!-- Copyright [2019] [Integreat Project] -->
<!-- Copyright [2023] [YCMS] -->
<!---->
<!-- Licensed under the Apache License, Version 2.0 (the "License"); -->
<!-- you may not use this file except in compliance with the License. -->
<!-- You may obtain a copy of the License at -->
<!---->
<!--     http://www.apache.org/licenses/LICENSE-2.0 -->
<!---->
<!-- Unless required by applicable law or agreed to in writing, software -->
<!-- distributed under the License is distributed on an "AS IS" BASIS, -->
<!-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. -->
<!-- See the License for the specific language governing permissions and -->
<!-- limitations under the License. -->
[![CircleCI](https://circleci.com/gh/charludo/ycms.svg?style=shield)](https://circleci.com/gh/charludo/ycms)
[![ReadTheDocs](https://readthedocs.org/projects/ycms/badge/?version=latest)](https://ycms.readthedocs.io/en/latest/)

This is a Django 4 based web application. The main goal is to...

## TL;DR

### Prerequisites

**Note:** if you absolutely MUST use Windows, follow the guide in `WSL.md`. No guarantees though.

Following packages are required before installing the project (install them with your package manager):

* `npm` version 7 or later
* `nodejs` version 12 or later
* `python3` version 3.9 or later
* `python3-pip` (Debian-based distributions) / `python-pip` (Arch-based distributions)
* `python3-venv` (only on Debian-based distributions)
* `docker` to run a local database server

### Installation

````
git clone git@github.com:charludo/ycms.git
cd ycms
./tools/install.sh --pre-commit
````

### Run development server

````
./tools/run.sh
````

* Go to your browser and open the URL `http://localhost:8086`
* By default, the following users exist:

| Email                  | Group   |
|------------------------|---------|
| root@ycms.de    | -       |
| manager@ycms.de | MANAGER |
| doctor@ycms.de  | DOCTOR  |
| nurse@ycms.de   | NURSE   |

All default users share the password `changeme`.

## Documentation

Read the docs at [ycms.readthedocs.io](https://ycms.readthedocs.io/en/latest/).


## License

This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0), see [LICENSE](./LICENSE) and [NOTICE.md](./NOTICE.md).
It is based on [digitalfabrik/integreat_cms](https://github.com/digitalfabrik/integreat-cms/), Copyright © 2023 [Tür an Tür - Digitalfabrik gGmbH](https://github.com/digitalfabrik) and [individual contributors](https://github.com/digitalfabrik/integreat-compass/graphs/contributors).
All rights reserved.
