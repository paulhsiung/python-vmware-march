python
====

## Contents

1. Installation
	1. Why virtual environments?
	1. Installing Python & `pip`
1. Setting up virtual environments
	1. Installing `virtualenv` & `virtualenvwrapper`
	1. Managing environments
1. Alternate setup: using a VM

## Setup

Note that this document focuses on Unix environments - those of you on Windows will need to make sure you pay attention to the installation documentation for Windows on each site as you install the setup.

### Why virtual environments?

For this class (and Python use in general), your life will be much easier if you aren't mucking around with your system Python installation. The folks in the open source community have come up with a great solution: virtual Python environments. 

This is accomplished via [`virtualenv`](https://virtualenv.readthedocs.org/en/latest/) and augmented with [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.org/en/latest/).  

Advantages:

* No more destroying your system Python just to get a single project to work
* Easily allow different projects to have differnt versions of libraries and coexist peacefully
* Easy command line tools to create, switch, and destory `virtualenv`s

Additionally, `virtualenv` plays very nice with Python's package installer, `pip`.

Let's start by getting you up and running with Python & `pip`.

# Installation

Start by pulling down the repository, either using git or downloading the ZIP. 

Next, use the section appropriate for your OS for the installation. After you're finished, you'll move to setting up environments.  

## Mac OS X Installation

You will need Python 2.7.x. If this command doesn't work:

	$ python --version

You'll need to install it. [Simply download and install from here](https://www.python.org/downloads/).

There's a good chance you already have `pip` installed, check with:

	$ pip --version
	pip 1.5.4 from /Users/will/.virtualenvs/di/lib/python2.7/site-packages (python 2.7)

Visit the `pip` [website for instructions](https://pip.pypa.io/en/stable/installing/). Most likely you'll download a Python script and run it:

	$ python get-pip.py

Now you should have working Python 2.7.x and `pip` installed. Skip to below to setup `virtualenv`s.

## Ubuntu Installation

	$ sudo apt-get install python-pip - y

Now you should have working Python 2.7.x and `pip` installed. Skip to below to setup `virtualenv`s.

## CentOS Installation

	$ sudo yum -y install python-pip

Now you should have working Python 2.7.x and `pip` installed. Skip to below to setup `virtualenv`s.

# Setup 

This applies to all Unix flavors. 

## `virtualenv` & `virtualenvwrapper` Setup

Install virtualenv libs at system level:

	$ sudo pip install virtualenv
	$ sudo pip install virtualenvwrapper

This should be the last time you ever use `sudo pip ...`!

Put into your `~/.bash_profile` (Mac OSX) or `~/.bashrc` (Linux):

     # for virtuallenvwrapper
     export WORKON_HOME=$HOME/.virtualenvs
     source /usr/local/bin/virtualenvwrapper_lazy.sh
	
Then initialize it:

	$ source ~/.bash_profile
	$ workon

This ensures whenever you start a new shell, you'll be able to get up and running with virtual environments if you want to. Then to create an environment:

	$ mkvirtualenv temp
	$ workon # should now display our env!
	temp
	$ workon temp
	(temp)$ pip install requests # now we’re in!
	(temp)$ python
	>>> import requests  # it worked!
	(temp)$ deactivate
	$ python
	>>> import requests
	ImportError: No module named requests  # we're not in our environment anymore!
	$ rmvirtualenv temp
	removing...

Great, you can now create new environments, destroy old ones, and manage existing ones! 

Let's create the environment specific to this class. 

	$ cd /path/to/this/repo
	$ mkvirtualenv di
	$ workon di
	(di)$ pip install -r /path/to/requirements.txt

And if you don't see any errors, you're ready to go!

## Alternate setup: using a VM

If you have Windows and are unable to get it set up, or are simply just having issues with a Unix installation, you can always follow the following failproof steps:

1. [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
1. [Install Vagrant](https://www.vagrantup.com/downloads.html)

Now, fire up a terminal:

```
$ cd /path/to/repo
$ vagrant up
$ vagrant ssh
vagrant@di_python:~$ touch /home/vagrant/.bash_profile
vagrant@di_python:~$ echo "# for virtuallenvwrapper" | tee -a /home/vagrant/.bash_profile
vagrant@di_python:~$ echo "export WORKON_HOME=$HOME/.virtualenvs" | tee -a /home/vagrant/.bash_profile
vagrant@di_python:~$ echo "source /usr/local/bin/virtualenvwrapper_lazy.sh" | tee -a /home/vagrant/.bash_profile
vagrant@di_python:~$ source /home/vagrant/.bash_profile
vagrant@di_python:~$ pip install -r /local/requirements.txt
```

If you'd like, you can inspect the `Vagrantfile` included in this repo to learn how to set up your own virtual environment.
