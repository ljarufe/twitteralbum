# Twitter album
(Tested on Ubuntu 14.04 or greater)

## Installation

### Core

```
$ sudo apt-get install build-essential python-dev python python-virtualenv python-pip libjpeg8 libjpeg62-dev
```

## Run the project

### Create a virtualenv

```
$ virtualenv twitteralbum
```

This command will create a new folder with the name `twitteralbum`

### Clone the project

First verify your SSH Keys on github cofiguration

```
$ cd twitteralbum/
$ git clone git@github.com:ljarufe/twitteralbum.git
```

### Activate your enviroment
Inside the `twitteralbum` folder run the following command

```
$ source bin/activate
```

After this you will see the virtualenv name in your promp. i.e.:

```
(twitteralbum) $
```

### Install requirements and update static files and database

```
(twitteralbum)$ pip install -r requirements.txt
```

### Run de migrations
In order to check that everything is ok. Run this command:

```
(twitteralbum) $ ./manage.py check
```

To run the migrations execute the following command:
```
(twitteralbum)$ ./manage.py migrate
```

#### Cronjobs
To install the every 20 minutes task open your cron table:
```
crontab -e
```

Add this line changing the path to the project:
```
*/20 * * * * cd <path_to_virtual_environment>; source bin/activate; twitteralbum/manage.py collect
```

### Tests
To make tests we need to put in console:

```
(twitteralbum) $ ./manage.py test  --settings=twitteralbum.test_settings
```

### Run the project
```
(twitteralbum)$ ./manage.py runserver
```

This is the url for photos: `/album/`

This is the url for the api: `/api/get_album/`
