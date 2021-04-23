# OCTO_API_DEMO

## REFRESH_TOKEN

**!!!This is only for non-berkeley student users!!!**

use this for the refresh token

"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoicmVmcmVzaCIsInVpZCI6IkQ5QktldHVWRGZOSm5UZWtCN2pqYXp4M3BQdDEifQ.Bb0AgJhDiYAIGnBFFHETbfxF327aX9Xynqmxs5FiXt4"


## Setup Instructions

1. create a directory and cd into that directory

2. create a new virtual environment with the command (you may have to pip install virtualenv)
```
virtualenv [your venv name]
```

3. activate the virtual environment with the command
```
source ./[your venv namne]/bin/activate
```

4. clone the github project with the command
```
git clone https://github.com/seongminchoob/OCTO_API_DEMO.git
```

5. install django and requests in the virtual environment with the command
```
pip install django
pip install requests
```

6. run the project with the command
```
python manage.py runserver
```

7. open up your browser at http://127.0.0.1:8000/page/
