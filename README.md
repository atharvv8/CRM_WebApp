# Customer Record Management Web App

This is a simple Customer Record Management web application built with Django. It stores details of customers such as name, phone number, address, email, and zipcode.

## Live Demo

Check out the live demo [here]([https://your-live-app-link.com](https://crm-webapp-ztez.onrender.com/)).

## Features

- Add new customer records
- Edit existing customer records
- Delete customer records
- View a list of all customer records

## Technologies Used

- Python
- Django
- PostgreSQL
- Gunicorn
- Uvicorn

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- PostgreSQL
- Git
- Django

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/atharvv8/CRM_WebApp.git
    cd CRM_WebApp
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database:
    ```sql
    CREATE DATABASE mysite;
    CREATE USER postgres WITH PASSWORD 'admin';
    ALTER ROLE postgres SET client_encoding TO 'utf8';
    ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
    ALTER ROLE postgres SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE mysite TO postgres;
    ```

5. Set up the environment variables:
    Create a `.env` file in the root of the project and add the following:
    ```env
    DATABASE_URL=postgres://postgres:admin@localhost:5432/mysite
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

6. Apply migrations:
    ```bash
    python manage.py migrate
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Contributing

If you would like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Gunicorn](https://gunicorn.org/)
- [Uvicorn](https://www.uvicorn.org/)
