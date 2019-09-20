# Timeapp-MA

We have created a time tracking app in Slack. Its purpose is the facilitation of organized and effective labour in workplace environments by tracking time spent working in general and on specific projects.The app contains several commands, for both management and standard users, that, among other things, allow for the creation and configuration of teams and various projects as well as viewing valuable statistics concerning time spent working.
Python was used to create the application.

## Dependancies
* Python 3.7 (or newer)
* Some kind of server
* Docker (Optional (Currently in development))
## Python package Dependancies
* [DotENV](https://github.com/theskumar/python-dotenv)
* [Flask](https://pypi.org/project/Flask/)
* [MySQL Connector](https://pypi.org/project/mysql-connector-python/)
## Quick start
Getting started with the flask server you'll need the Python dependancies above.
For a more detailed guide on getting started see the [wiki page](https://github.com/te4umea2019/Tidsapp-MA/wiki/Installation)
After installing the dependancies and cloning the repository, starting the server is as easy as opening a terminal in the folder and writing ``python3 timer.py``
## Even Quicker start using docker (docker-compose)
For quickly getting this Repo simply do
```
$ git clone https://github.com/te4umea2019/Tidsapp-MA.git
$ cd Tidsapp-MA
$ docker-compose up -d
```
This will after a downloading all the dependencies start a swarm for this web app on The local computes IP on port 8080
