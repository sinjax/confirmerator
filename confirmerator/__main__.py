import sys, os
sys.path.append(os.getcwd())
from confirmerator.models import db
from confirmerator import app
from IPython import embed


db.create_all()
app.run(port=7171)
