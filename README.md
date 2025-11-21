# PyWeather Assistant

[![Build](https://github.com/BrianLusina/pyweather/actions/workflows/build.yml/badge.svg)](https://github.com/BrianLusina/pyweather/actions/workflows/build.yml)
[![Lint](https://github.com/BrianLusina/pyweather/actions/workflows/lint.yml/badge.svg)](https://github.com/BrianLusina/pyweather/actions/workflows/lint.yml)
[![Tests](https://github.com/BrianLusina/pyweather/actions/workflows/tests.yaml/badge.svg)](https://github.com/BrianLusina/pyweather/actions/workflows/tests.yaml)

This is a command line weather application integrated with MCP servers built in Python to handle weather information 
directly from the terminal using the CLI as well as manage a todo list, manage prompts and perform further actions. 
One can take a city name as required input and an optional flag to display whether in Fahrenheit instead of
Celsius if desired. What one gets back is a display of the city name, the current weather conditions, and the current
temperature formatted visually with colors, spacing and emojis.

## Pre-requisites

1. Ensure that you have [Python version 3.12.0](https://www.python.org/) setup locally, you can set this up
   using [pyenv](https://github.com/pyenv/pyenv) if you have multiple versions of Python on your local development
   environment.
2. [UV](https://docs.astral.sh/uv/guides/install-python/) is used for managing dependencies, ensure you have that setup locally.
3. [Virtualenv](https://virtualenv.pypa.io/) Not a hard requirement as poetry should setup a virtual environment for
   you, but can be used as well to setup a virtual environment.
4. [OpenWeather API Key](https://openweathermap.org/). Register on OpenWeather and setup an API Key. This is going to be
   used with interacting with the API. If you already have an account, then this step can be skipped.
5. [Google Gemini API Key](https://ai.google.dev/gemini-api/docs/api-key). Register and setup a Google Gemini API key. 
   This will be used with interacting with the Gemini LLM. If you already have an account, then this step can be skipped.

## Setup

1. After cloning the project, install the dependencies required with:

   ```shell
   uv pip install -r pyproject.toml
   ```
   > When using uv

   Or
   ```shell
   make install
   ```
   > When using [GNU Make](https://www.gnu.org/s/make/manual/make.html), this is a wrapper around the top commend

2. Setup secrets in a _secrets.ini_ file from a sample [secrets.ini.sample](secrets.ini.sample). This can be done with
   the command:

   ```shell
   cp secrets.ini.sample secrets.ini
   ```

   > Copies over the sample file to a newly created file secrets.ini file. Note that this file is not pushed to a VCS.

   The file should look like this:

   ```ini
   [openweather]
   base_url=http://api.openweathermap.org/data/2.5/weather
   api_key=<YOUR-OPENWEATHER-API-KEY>
      
   [gemini]
   api_key=<GEMINI_API_KEY>
   ```

   > Enter your Open Weather API Key in the provided placeholder. You can optionally change the base url, but this is
   already defaulted. Also, enter your GEMINI_API_KEY in the provided placeholder.

3. Install `pyweather` in editable mode:
   ```shell
   cd pyweather
   uv run pip install -e .
   ```

## Execution

To execute `pyweather`, go ahead and run the below command:

```shell
python pyweather --help
```
