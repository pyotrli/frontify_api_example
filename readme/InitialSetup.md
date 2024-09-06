# Initial Setup
## Set ENV variables
Ensure that you have created a `.env` file, using `.env.example` as a base. This file should contain your Frontify domain (without `https://`), and Access Token.

The AccesstToken will inherit the permissions of the user creating it, and should be set with the scopes `basic: read` and `basic: write`. Access tokens can be generated at `https://<your-frontify-domain>/api/developer/token` when logged into Frontify

## Ensure that requirements are installed
To install all Python packages used in this repository, run `pip install -r requirements.txt` from the base of directory of this repository. 

### Best practice
Before installing requirements, it is recommended to create a virtual environment using [pyenv](https://github.com/pyenv/pyenv) or [venv](https://docs.python.org/3/library/venv.html).

A simple pyenv example follows:
```
pip install pyenv

pyenv virtualenv 3.10.0 api-examples .

pyenv activate api-examples

pip install -r requirements.txt
```