import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = "change_it_in_production"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'shop.db')}"

