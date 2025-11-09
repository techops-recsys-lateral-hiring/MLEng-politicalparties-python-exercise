# Tweet Prediction

The election is coming! We want to build an application that can parse a Tweet and determine which political party to associate with the Tweet, Republican or Democrat. As a consulting machine learning engineer you are tasked with taking the initial efforts of building the application and making it functional.

This repository contains the necessary setup and code base to help guide you in creating this application.

## Project Setup

### Default, manual

#### Pre-requisites

Please make sure you have the following software installed

- Python (3.10 or 3.11)

#### Install all python dependencies

Before you install dependencies make sure you add your python path to the makefile.

```bash
make install
```

### Nix-Shell

Nix is able to create a shell environment that has all the tool dependencies needed, such as docker, python, etc.

1. Install Nix package manager, [instructions](https://nixos.org/download/)
1. Enter the nix-shell, `nix-shell`

### Run tests & checks

The unit tests can be run either by using the make commands (given in the makefile) or by using the commands from the respective packages.
For example, unit tests can be executed using:

```bash
make test
```

<!-- markdownlint-disable-next-line -->
**Note: this command should execute with failed unit tests**

## Gearing Up for the Pairing Session

Please be sure to complete the below tasks before the pairing session.

1. Get a high-level understanding of the dataset
2. Have your coding environment ready by installing python and dependencies.
3. Ensure that you are able to run all commands mentioned in this README (except for pytest errors)

<!-- markdownlint-disable-next-line -->
**Note: you DO NOT have to complete the code/tasks inside the `src/` folder. It is meant to be done together during a pairing session.**
