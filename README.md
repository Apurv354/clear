# CLEAR
Our CLEAR app. 
Our app takes keyword from the user and automatically push like button to keyword-related video.
This code includes python backend server and vanilla html&CSS&JS frontend.

# Setup

## Make virtual environment using venv or conda

If you want to use venv, follow below command.
You can use conda instead of venv.
``` bash
python -m venv .venv
```
You can select .venv environment from the button on the bottom right in vs code.

In bash(linux) terminal, you can activate this environment using below command.
``` bash
source .venv/bin/activate
```

In powershell(windows), you can use below command.
``` powershell
. .venv\Scripts\activate
```

## Install Dependencies
``` bash
pip install flask # This is the backend framework
pip install google-auth-oauthlib google-api-python-client google-auth # Pacakges for installing youtube api call
```

## Unzip keys.zip
In keys.zip file, there are keys for calling youtube api. Unzip it to this directory.
Keys are set to be ignored in this git project. Do not try to upload this keys to remote branch. 
It will be blocked by github.

# Excution
You can host the server in your local by executing below command.
``` bash
python connectingtoOathtesting_ratelikeall_web.py
```
You can use python debug(F5) button also.

Then, access the hosted webpage via localhost:5000
Press `ctrl+c` to quit.
