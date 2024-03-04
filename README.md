# Django Backend for React Authentication System

This Django project serves as the backend for the React-based authentication system. The backend uses Django, Django REST framework, and SQLite as the default database. Email functionality is incorporated for user registration and login, but email verification by sending a link is not implemented.

## Setup Instructions

1. **Clone Repository**: Clone the repository to your local machine.

    ```bash
    git clone <repository-url>
    ```

2. **Create Virtual Environment**: Navigate to the project directory and create a virtual environment.

    ```bash
    cd <project-directory>
    python -m venv venv
    ```

3. **Activate Virtual Environment**: Activate the virtual environment.

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies**: Install the required Python packages using `pip` with the provided `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Email Settings**: Open `usermanagement/settings.py` and fill in the email and password sections with your email ID and password.

    ```python
    EMAIL_HOST_USER = 'your-email@gmail.com'
    EMAIL_HOST_PASSWORD = 'your-email-password'
    ```

6. **Run Migrations**: Apply initial database migrations.

    ```bash
    python manage.py migrate
    ```

7. **Run Django Development Server**: Start the Django development server.

    ```bash
    python manage.py runserver
    ```

    The server should be accessible at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- `/allusernames/` (GET): Get a list of all usernames.
- `/verifyusernames/<str:username>/` (GET): Verify if a username is available.
- `/verifycredentials/<str:email>/<str:password>/` (GET): Verify user credentials and send an email.
- `/userregistration/` (POST): Register a new user and send a registration email.
- `/userdetail/<str:username>/` (GET): Get details of a specific user.
- `/userupdate/<str:username>/` (PUT): Update user credentials and send an email.

## Note

- The frontend part is implemented [here][1].
- For security reasons, it is recommended to use environment variables for sensitive information like email credentials.
- Make sure to adapt the Django settings according to your production environment requirements.
- Ensure that your email provider supports SMTP to use the email sending functionality.

[1]: https://github.com/rampreethamkanchi/opensoft-assignment-frontend  "here"
