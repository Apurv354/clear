# clear
Weather app for Flask demo

Hello user:
This is a small demonstration of how the backend and the frontend could work together.
Below are some more detailed information:

Front End:
File: .html
Language: javascript

Back End:
File: .py
Langaug: Python

Make virtual environment using venv or conda

If you want to use venv, copy paste below.
``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Install flask
``` bash
pip install flask
```

Execute the app
``` bash
python app.py
```

Then flask will host a server in local environment. Then you can access with via localhost:5000.

If you put those city names then you'll get following result.
"New York": {"temp": 5, "condition": "Cloudy"},
"Tokyo": {"temp": 10, "condition": "Sunny"},
"London": {"temp": 7, "condition": "Rainy"}

Press `ctrl+c` to quit.
