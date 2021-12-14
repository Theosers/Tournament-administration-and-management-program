# Tournament-administration-and-management-program

## Table of Contents

1. General Info
2. How to use this repository

### General Info

***
This program is a user interface for creating a chess tournament according to the Swiss system and uses a database (tinyDB) to store the data entered.
- You can create a tournament
- Change the rank of a player at any time
- Add new players to the database
- Consult the list of players, tournaments or rounds of a tournament registered in the database.

Each tournament has the following information:

- Name
- Place 
- Date
- Number of rounds
- List of players
- Time control
- Type of tournament (bullet, blitz or fast)
- Description

Each player has the following information:
- Last name
- First name
- Date of birth
- Gender
- Rating

## How to use this repository

***

This program will require python 3.9.6 installed : https://www.python.org/downloads/

In a new virtual environment, install all dependency :
```
pip install -r requirements.txt
```
To generate a new flake8-html file :

```
flake8 --format=html --htmldir=flake-report --max-line-length=119
```
