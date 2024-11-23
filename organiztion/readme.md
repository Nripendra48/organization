Django User Management Application
This is a Django-based user management application that allows the management of users, roles, and permissions. Users can be assigned roles, and admins have the ability to delete users, while also preventing the deletion of the logged-in user.

Features
User List: Displays a list of all users, with options to assign roles, and delete users (except the logged-in user).
Assign Roles: Admin users can assign roles to other users.
Delete Users: Admin users can delete users, but not their own account.
Add Users: Admin users can add new users to the system.
Logout: Users can log out of the application.
Redirect to Organizations: Users can navigate to the organization page.
Requirements
Python 3.x
Django 3.x or later
PostgreSQL (or any other compatible database)
Redis (for background task management, if used)
Setup Instructions
1. Clone the repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/django-user-management.git
cd django-user-management
2. Create a Virtual Environment
It's recommended to use a virtual environment for managing dependencies. You can create one with the following commands:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install Dependencies
Install the necessary dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
4. Setup the Database
Make sure you have PostgreSQL (or any other database) set up. Modify your database settings in settings.py if necessary.

After setting up your database, run the following commands to set up your tables and apply migrations:

bash
Copy code
python manage.py migrate
5. Create a Superuser
To manage the application, you need to create a superuser account. Run the following command to create one:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create the superuser account.

6. Start the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.

Features Details
User List Page
Displays a list of users, excluding the currently logged-in user.
Roles assigned to users are displayed.
Admin users can assign roles to users.
Admin users can delete users, but cannot delete their own account.
Admin users can also add new users using the "Add User" button.
User Role Management
Admin users can assign roles to users from the user list page. A user can have multiple roles.
Add User
Admin users can add new users using the "Add User" button, which redirects them to a form where they can input new user details.
Logout
Users can log out of the application using the "Logout" button.
Organization Navigation
Admin users can navigate to the "Organizations" page via the "Go to Organizations" button.
URL Configuration
/ - Home page with the list of users and user management actions.
/login/ - Login page.
/logout/ - Log out the user.
/user_create/ - Add a new user.
/assign_role/<user_id>/ - Assign a role to a user.
/delete_user/<user_id>/ - Delete a user (except the logged-in user).
/organization_list/ - List of organizations.
Admin Panel
The Django admin panel can be accessed at http://127.0.0.1:8000/admin/. Log in using the superuser credentials you created.

Running Tests
To run the tests for this application, use the following command:

bash
Copy code
python manage.py test
This will run any tests you've created for your application.

Deployment
To deploy this application to production, follow these steps:

Configure the application for production in settings.py (e.g., set DEBUG=False, configure ALLOWED_HOSTS, set up static and media files).
Set up a production-ready web server like Gunicorn or uWSGI behind Nginx.
Configure the database, Redis (if used), and other production services.
Troubleshooting
If you encounter any issues, please check the following:

Ensure all dependencies are installed.
Verify your database is set up correctly and migrations have been applied.
Check the Django logs for error messages.
License
This project is licensed under the MIT License.

