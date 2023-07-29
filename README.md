# Store and warehouse

### Description
This is an interesting test case from a job interview. <br>
There are three django apps (Auth, Store and Warehouse) with three separate databases in one django project. The Store provides orders. The warehouse receives these orders via the API and push back information to the Store. So when Store creates and order, this is synced to the Warehouse. If Warehouse changes some information this will update the information in Store. The applications can only communicate via Rest API.

### Run service:
To run the service, use the commands:
```
# Clone the repository:
git clone <github_link>

# Create virtual environment:
python3 -m venv venv

# Activate virtual environment:
source venv/bin/activate  # for Linux/MacOS
source venv/scripts/activate  # for windows

# Install dependencies form the "requirements.txt" file:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# Apply migrations for all the databases:
python manage.py migrate --database=auth_db
python manage.py migrate --database=store_db
python manage.py migrate --database=warehouse_db

# Create superuser:
python manage.py createsuperuser --database=auth_db

# Run the first instance of the project:
python manage.py runserver 8001

# Open another terminal and run the second instance of the project:
python manage.py runserver 8002
```

### Technologies
Python 3 <br>
Django 4 <br>
Django Rest Framework <br>

### Author
Anton Akulov - https://github.com/Nekustetnaz
