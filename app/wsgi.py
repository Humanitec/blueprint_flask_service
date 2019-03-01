import os
from app import create_app

os.environ.setdefault("FLASK_APP", "app")

app = create_app()
