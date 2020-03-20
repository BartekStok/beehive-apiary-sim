 [![BeeHive](staticfiles/images/My_bee_small.png)](https://apiary-beehive-sim.herokuapp.com/) 

# Bee Hive and Apiary simulation

Simple app to help maintain Apiary.

Made on completion of a programming course Back-End Python Developer.

## Getting started

Try this app online on Heroku, **just click on this lovely Bee above...**

### Prerequisites

What You need to have:

```
$ Python 3.6
```

### Installing

It is best to use the python `virtualenv` tool to build locally:

```sh
$ git clone https://github.com/BartekStok/beehive-apiary-sim
$ cd apiary
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use gunicorn to run the server locally.


## License

This project is licensed under the MIT License 



- Copyright 2020 © Bartłomiej Stokłosa
