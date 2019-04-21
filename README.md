 # LOG ANALYSIS PROJECT


## What it is and does
Runs a python module that runs SQL queries against a data set to answers analyitical questions.


You can run the project in a Vagrant managed virtual machine (VM) which includes all the
required dependencies (see below for how to run the VM). For this you will need
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from [Vagrant](https://www.vagrantup.com/downloads). Install the version for your operating system.
Virtual Box is the software that actually runs the VM. You can download it from [VirtualBox](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.
You will need to set up a vagrant enviroment to run this code. That environment can be downloaded from [Environment](https://github.com/udacity/fullstack-nanodegree-vm/archive/master.zip). 

## Project contents
This project consists for the following files in the `loganalysis` directory:

* `loganalysis.py` - Is the python module that will return answers for analyitical questions .
* `results.txt` - Text document showing the print results of the loganalysis.py module.

## How to Run the Project
After you have downloaded and unzipped the vagrant [Environment](https://github.com/udacity/fullstack-nanodegree-vm/archive/master.zip) file. 

Download the project zip file to you computer and unzip the file. Or clone this
repository into the vagrant directory of the vagrant environment.

You will also need to download and unzip the SQL [dataset](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) into the loganalysis directory. 

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows).

Navigate to the project directory and then enter the `vagrant` directory.

### Bringing the VM up
Bring up the VM with the following command:

```bash
vagrant up
```

This step can take a while if it is your first time running it.

You can then log into the VM with the following command:

```bash
vagrant ssh
```

To get into the VM directory

```bash
cd /vagrant/
```

### Run loganalysis.py
First you want to run `newsdata.sql` because there will be no database present, so it creates
one and populates it with sample data. Type this into the command line:

```bash
psql -d news -f newsdata.sql
```

To start the run the log analysis just run `loganalysis.py` Type this into the command line:

```bash
python loganalysis.py
```

You should now see these results in the terminal.

```

What are the most popular three articles of all time?
Articles: Candidate is jerk, alleges rival - 342102 VIEWS
Articles: Bears love berries, alleges bear - 256365 VIEWS
Articles: Bad things gone, say good people - 171762 VIEWS


Who are the most popular article authors of all time?
Authors: Ursula La Multa - 512805 VIEWS
Authors: Rudolf von Treppenwitz - 427781 VIEWS
Authors: Anonymous Contributor - 171762 VIEWS
Authors: Markoff Chaney - 85387 VIEWS


On which days did more than 1% of requests lead to errors?
2016-07-17 - 2.000% errors
```



