# REST Countries API Application - Django REST Framework
A Django-based web application that fetches country data from the REST Countries API and provides a comprehensive interface for exploring country information with RESTful APIs and user authentication.

## Project Overview

This application demonstrates:
- Data fetching from external APIs
- Django model design and database management
- RESTful API development with Django REST Framework
- Secure authentication system
- Modern web UI with Bulma CSS
- Search and filter functionality

## Features

- **Country Data Management**: Fetch and store country information from REST Countries API
- **RESTful APIs**: Complete CRUD operations for countries
- **Advanced Filtering**: Search by name, filter by language and region
- **User Authentication**: Secure access control
- **Modern UI**: Responsive design with Bulma CSS framework
- **Real-time Search**: Client-side search functionality
- **Country Details**: Modal display with regional countries and languages

## Technology Stack

- **Backend**: Django 4.2+
- **API**: Django REST Framework 3.14+
- **Database**: SQLite (default)
- **API Documentation**: drf-yasg==1.21.10
- **Frontend**: HTML5, JavaScript, Bulma CSS
- **Authentication**: Django's built-in auth system

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Git
- Virtual environment tool (venv)


## Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/shamimkhaled/rest-countries-api.git
cd rest-countries-api
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Project

Run the initialization command to set up the database, create a superuser and fetch the country api data via custom management command:


i. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

ii. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

iii. **Fetch Country Data**
   ```bash
   python manage.py country_api
   ```

### 5. Run the Application

```bash
python manage.py runserver
```


## Required Dependencies

### Core Dependencies

```
Django==5.2
djangorestframework==3.16.0
python-dotenv==1.1.0
requests==2.32.3
drf-yasg==1.21.10
```



## Database Configuration

### Default Configuration (SQLite)

The application uses SQLite by default. The database file is created automatically as `db.sqlite3`.

### PostgreSQL Configuration (Production)

To use PostgreSQL, update `rest_countries_app_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'country_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Environment Variables 

Create a `.env` file in the project root for sensitive data:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=your-database-url
```


## API Documentation

### Swagger Documentation

Access the interactive API documentation at: `http://localhost:8000/api/docs/`

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login/` | User login |
| POST | `/logout/` | User logout |

### Country Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/countries/` | List all countries |
| POST | `/api/countries/` | Create new country |
| GET | `/api/countries/{id}/` | Get country details |
| PUT | `/api/countries/{id}/` | Update country |
| PATCH | `/api/countries/{id}/` | Partial update country |
| DELETE | `/api/countries/{id}/` | Delete country |
| GET | `/api/countries/{id}/regional_countries/` | Get regional countries |
| GET | `/api/countries/by_language/?language={code}` | Filter by language |
| GET | `/api/countries/?search={name}` | Search by name |



### API Usage Examples

```bash
# List all countries
curl -u admin:password http://localhost:8000/api/countries/

# Get country by ID
curl -u admin:password http://localhost:8000/api/countries/1/

# Search for countries
curl -u admin:password "http://localhost:8000/api/countries/?search=bangladesh"

# Filter by language
curl -u admin:password "http://localhost:8000/api/countries/by_language/?language=eng"
```


## Project Structure

```
rest-countries-api/
├── rest_countries_app_project/                # Main project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL configuration
│   └── wsgi.py
├── country_app/                   # Countries application
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   |       └── country_api.py     # Fetching the country data 
|   |
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                   # Admin interface config
│   ├── models.py                  # Country model
│   ├── serializers.py             # DRF serializers
│   ├── tests.py                   # Unit tests
│   ├── urls.py                    # App URL configuration
│   └── views.py                   # Views and API viewsets
├── templates/                      # HTML templates
│   ├── base.html                  # Base template
│   ├── countries/
│   │   └── country_list.html      # Country list page
│   └── registration/
│       └── login.html             # Login page
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # This file
```


## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Support

For support and questions:
- Create an issue in the repository
- Contact: i.amshamim94@gmail.com

## Acknowledgments

- REST Countries API for providing country data
- Django and Django REST Framework communities
- Bulma CSS framework

## Version History

- Development version
  - Basic country data management
  - RESTful API implementation
  - User authentication
  - Web interface with search


