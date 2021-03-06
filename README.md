# MovR

This repo contains the source code for an example implementation of a single-region application for the fictional vehicle-sharing company MovR, as used by the CockroachDB for Python Developers course.

- [Overview](#overview) gives a high-level overview the MovR application stack. 

## Overview

The application stack consists of the following components:

- A CockroachCloud instance / local CockroachDB cluster
- Python class definitions that map to the table(s) in the database.
- A backend API that defines the application's connection to the database and the database transactions.
- A Flask server that handles requests from client web browsers.
- HTML templates that define web pages that the Flask server renders.

## Setup

### Database and Environment Setup (cloud)

You'll need to connect to a [CockroachCloud](https://cockroachlabs.cloud/) cluster.

1. Configure environment variables
     
    When running your server, it's easiest if your CockroachCloud connection
    string is assigned to the DB_URI variable in the `.env` file. You can paste
    it in with the editor of your choice.

1. Initialize the database

    You can do this with

    ~~~ shell
    $ cockroach sql --url '<cockroachcloud_url>' < dbinit.sql
    ~~~

### Database and Environment Setup (local)

1. Install CockroachDB binary as described in [docs](https://www.cockroachlabs.com/docs/stable/install-cockroachdb-linux.html)

1. Start development one-node cluster:
    
    ~~~ shell
    $ cockroach start-single-node --insecure
    ~~~

1. Create database and user for MovR application:

    ~~~ shell
    $ cockroach sql --url 'postgresql://root@<hostname>:26257?sslmode=disable' < dbinit.sql
    ~~~

1. In .env file add DB_URI entry:

    ~~~ shell
    SECRET_KEY='key'
    DB_URI='postgresql://app_user@<hostname>:26257/movr?sslmode=disable'
    ~~~

### Application setup

1. Make sure Python3 is installed:

    ~~~ shell
    $ python3 --version
    Python 3.8.2
    ~~~
1. Install required dependencies:

    ~~~ shell
    $ pip3 install -r requirements.txt
    ~~~

1. To run the application, use the following command in the shell:

    ~~~ shell
    $ ./server.py run
    ~~~

1. Navigate to the url provided (defaults to [http://localhost:36257](http://localhost:36257)) to use the application.

### Clean up

1. To shut down the application, `Ctrl+C` out of the Python process.

## Note: Testing

We are still building out the testing suite. Please use at your own risk.
