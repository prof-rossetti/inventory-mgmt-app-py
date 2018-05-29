# Inventory Management App

A command-line Python application which allows the user to manage an inventory of products. Performs all product "CRUD" operations (i.e. "List", "Show", "Create", "Update", and "Destroy").

Uses a CSV file datastore.

## Installation

Fork this repository under your own control. Then download your forked version of this repository (or "clone" it if you are using command-line git).

Then navigate into the root directory:

```sh
cd path/to/inventory-mgmt-app/
```

> NOTE: all commands in this document assume you are running them from this root directory.

## Setup

Before you run this application for the first time (or anytime you want to reset the database), reset the database by populating it with the default products:

```sh
# For Homebrew-installed Python 3.x on Mac OS:
python3 products_app/reset.py

# All others:
python products_app/reset.py
```

## Usage

Run the application:

```sh
# For Homebrew-installed Python 3.x on Mac OS:
python3 products_app/app.py

# All others:
python products_app/app.py
```
