<center><h1>Databas01</h1></center>
<!-- TABLE OF CONTENTS -->

<!--ts-->
## Table of Contents ##
* [Background](#background)
* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Made by](#made-by)
<!--te-->

## Background ##
Assignment in a database course, where we got to know about MySQL and MongoDB, using orm. We got criterias for a car sparepart dealership from a customer who wanted a database for his business.

<!-- ABOUT THE PROJECT -->
## About The Project
The project Builds a Mysql database with alembic and sqlalchemy using orm. It generates some dummy data and the migrates the mysql database to a document driven database Manager MongoDB with the help of pymongo. The database is built on a Multilayered structure (UI, BL, DATA) Where the user communicates with UI.

### Built With
* [sqlalchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [pymongo](https://pymongo.readthedocs.io/en/stable/)


<!-- GETTING STARTED -->
## Getting Started

Follow the [installation](#installation) to get started

### Prerequisites

* Python 3+
* Docker
* Docker-compose

### Installation

1. Clone the repo
```sh
git clone https://github.com/AntonMaxen/Databas01.git
```
2. Install requirements
```sh
pip install requirements.txt 
```
3. start docker containers
```sh
docker-compose up
```
4. run alembic upgrade
```
alembic upgrade head
```
5. run setup_databases file in app
6. Done


<!-- USAGE EXAMPLES -->
## Made by
Anton Maxén, Måns Ewards Öberg, Marcus Johnsson
