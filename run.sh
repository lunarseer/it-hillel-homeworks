export SQLDBFILE=$PWD/app.db
export FLASK_APP=app.py
export FLASK_ENV=development

python db_fill.py
flask run