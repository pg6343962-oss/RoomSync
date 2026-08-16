RoomSync 🏠

RoomSync is a Django-based roommate matching web application that helps users find compatible roommates based on their profile and preferences.

Features

- User Registration and Login
- User Profile Management
- Edit Profile
- Find Roommates
- View Roommate Profiles
- Send Roommate Requests
- Sent Requests Tracking
- Received Requests Management
- Accept or Reject Requests
- User Dashboard
- Logout and Authentication Protection
- Responsive Bootstrap-based Interface

Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite
- Git & GitHub

Project Structure

RoomSync/
│
├── accounts/
├── requests_app/
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md

Installation

Clone the repository:

git clone https://github.com/pg6343962-oss/RoomSync.git
cd RoomSync

Create and activate a virtual environment:

python -m venv venv

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

Open the application in your browser:

http://127.0.0.1:8000/

How It Works

1. Create an account or log in.
2. Complete your profile.
3. Browse available roommates.
4. View a roommate's profile.
5. Send a roommate request.
6. Track sent requests.
7. View received requests.
8. Accept or reject requests.

Future Improvements

- Real-time chat between matched roommates
- Advanced roommate compatibility scoring
- Profile image upload
- Location-based roommate search
- Email notifications
- Production database integration

Author

Developed as a Django web application project.
