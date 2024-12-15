# Rental Motor Django App

A Django-based application for managing motorcycle rentals. This repository contains all the code needed to set up and run the application.

## Features
- Manage motor rentals.
- User authentication and authorization.
- Database integration with Django ORM.
- Responsive design for better user experience.

## Getting Started
Follow the instructions below to clone the project and get it running locally.

### Prerequisites
Make sure you have the following installed on your system:
- Python (>=3.8)
- pip (Python package manager)
- Git
- Virtualenv (optional but recommended)

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/romiwebdev/rentalmotor-django-app.git
cd rentalmotor-django-app
```

2. **Create and Activate a Virtual Environment** (optional but recommended)

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply Database Migrations**

```bash
python manage.py migrate
```

5. **Create a Superuser**

```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin user.

6. **Run the Development Server**

```bash
python manage.py runserver
```

7. **Access the Application**

Open your web browser and go to:
```
http://127.0.0.1:8000
```

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
If you have any questions or issues, feel free to contact me via GitHub:
[romiwebdev](https://github.com/romiwebdev)
