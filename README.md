# Wine and Cheese App

## Description

This is a CRUD web application that allows a user to record their choice of Wine and Cheeses and to create pairings between them to their taste.

## Dependencies

This application runs in Flask so as a pre-requisite Python3, pip3 and a virtual environment need to be installed for the app to run.


````bash
sudo apt install python3 python3-venv python3-pip
```

To install dependencies within the virutal environment it must first be activated.

```bash
python3 -m venv venv
. venv/bin/activate
```

The applications required for the app to run are within the requirements text file:

```bash
pip3 install -r requirements.txt
```

The app can now be run:

```bash
python3 app.py
```

The port the app will be run on is: '0.0.0.0:5000'.



