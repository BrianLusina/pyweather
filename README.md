# Hangman

[![Build](https://github.com/BrianLusina/hangman/actions/workflows/build.yml/badge.svg)](https://github.com/BrianLusina/hangman/actions/workflows/build.yml)
[![Lint](https://github.com/BrianLusina/hangman/actions/workflows/lint.yml/badge.svg)](https://github.com/BrianLusina/hangman/actions/workflows/lint.yml)
[![Tests](https://github.com/BrianLusina/hangman/actions/workflows/tests.yaml/badge.svg)](https://github.com/BrianLusina/hangman/actions/workflows/tests.yaml)

This is a command line game application inspired by [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) which is a
word skill game that teaches basic language skills. This game is between the computer and one human player. The computer
will act as the selecting plater and will select
the word to guess, process human input and handle all output.
The human player is the guessing player, simply referred to as the player. When the player knows the word, they continue
to guess correct letters until the word is complete.

You can change the words the game will select in the [words.txt](./hangman/words.txt) file with a different choice of
words.

## Pre-requisites

1. Ensure that you have [Python version 3.12.0](https://www.python.org/) setup locally, you can set this up
   using [pyenv](https://github.com/pyenv/pyenv) if you have multiple versions of Python on your local development
   environment.
2. [Poetry](https://python-poetry.org/) is used for managing dependencies, ensure you have that setup locally.
3. [Virtualenv](https://virtualenv.pypa.io/) Not a hard requirement as poetry should setup a virtual environment for
   you, but can be used as well to setup a virtual environment.

## Setup

1. After cloning the project, install the dependencies required with:

   ```shell
   poetry install
   ```
   > When using poetry

   Or
   ```shell
   make install
   ```
   > When using [GNU Make](https://www.gnu.org/s/make/manual/make.html), this is a wrapper around the top commend

2. Install `hangman` in editable mode:
   ```shell
   cd hangman
   pip install -e .
   ```

## Execution

To execute `hangman`, go ahead and run the below command:

```shell
python hangman
```

Which will run the game. Enjoy!
