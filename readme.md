Python script to download best backtested pairs from Bitsgap and perform technical analysis using a TradingView library.

<br/>

# **Table of contents**

<!--ts-->
* [Installation](#installation)
    * [Requirements](#requirements)
    * [Environment Variables](#environment-variables)
    * [Virtual Environment](#virtual-environment)
    * [Install Dependencies](#install-dependencies)
* [Creating the DB](#creating-the-db)
* [Usage](#usage)

<br/>

**Installation**
================

Requirements
------------
Base requirements: [Python 3](https://www.python.org/) & [pip](https://pip.pypa.io/en/stable/).

Dependencies are handled using [Pipenv](https://pypi.org/project/pipenv/). To install it:

```sh
$ pip install pipenv
```

It also needs a MySQL database.

<br/>

Environment Variables
------------
Duplicate the `.env.example` file and rename it to `.env`. Place your Bitsgap and MySQL credentials there.


<br/>

Virtual Environment
------------
Start a new virtual environment:
```
$ pipenv shell
```

<br/>

Install Dependencies
------------
```
$ pipenv install
```


<br/><br/>

**Creating the DB**
==================

Run the script `Data/db_schema.sql` to create the initial schema.


<br/><br/>

**Usage**
==================

The script `fetch_and_query_pairs.py` will download the best pairs from Bitsgap and perform TA to them and save the results on the DB.

`oscillators.py` will show a list of the best pairs according to its oscillator and will create a txt file to be imported in TradingView.
