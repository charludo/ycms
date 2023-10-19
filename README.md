[![CircleCI](https://circleci.com/gh/charludo/ycms.svg?style=shield)](https://circleci.com/gh/charludo/ycms)
[![ReadTheDocs](https://readthedocs.org/projects/ycms/badge/?version=latest)](https://ycms.readthedocs.io/en/latest/)

This is a Django 4 based web application. The main goal is to...

## TL;DR

### Prerequisites

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

This project is licensed under the Apache 2.0 License, see [LICENSE](./LICENSE).
It is based on [digitalfabrik/integreat_cms](https://github.com/digitalfabrik/integreat-cms/).
