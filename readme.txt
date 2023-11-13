purpose: py9/django rest api example w/ postgres. a store example w/ products and customers
source = https://realpython.com/api-integration-in-python/

to run app:
  1-venv  .venv\scripts\activate & launch postgres (this is localhost only, not an external instance that is just up and running)
  2-automated- select debug icon to left and start/stop server
  -- or-- manual- term cmd = python manage.py runserver   
  then launch a new CLI (external to vscode).  and curl -i http://127.0.0.1:8000/products/   if successful this will return an unformatted response 
  -- or--
  launch your api consumer [havent built this yet]

launch postgres 15:
un/pwd: postgres, admin. To start use pgadmin4.  to swtich from sqlite (test) to postgres (prod) comment settings.py.
  see djangoWebapp readme.  need pip install psycopg2 for postgres + settings.py.  using db = django_store

venv:
 instantiate (once at start): py -3 -m venv .venv  -- or -- cmd pallet (cntl+shift+p) & & Python Create Environment
 term cmd = .venv\scripts\activate            (.venv) in green at begining of line should show up
   Create New Terminal command, Ctrl+Shift+`   
   -note you will not be in the virtual environment in debugger launch-it launces a new terminal
   -note you can change py interpreter by cntl+shift+p (cmd pallet) and python: create environment.  but it will delete your pip installs,  so you have to run them again in the terminal
      this is what I had to do for postgres (ie went from py 12 to py 9)
 
py db updates:  
term = python manage.py makemigrations
then python manage.py migrate

django- project = web_rest
       app = store_api

new venv / py 9/ pip summary- quick ref:
Django djangorestframework
pyscopg2
django-environ