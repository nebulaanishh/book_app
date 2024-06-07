## Book App 
Features:
- Allows users to make a new book in database.
- One user can add one review along with rating for each book.
- custom User model with jwt token based authentication.
- Swagger docs. 

Tech stack:
- Django/DRF
- PostgreSQL

### Backend Setup
- Go to backend folder.
- Create .env in backend folder and create required environment variables including database in postgres. (see `.env.example`)
- Create a new virtual environment: `python -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install packages: `pip install -r requirements.txt`
- Run migrations: `python manage.py migrate`
- Start server: `python manage.py runserver`
