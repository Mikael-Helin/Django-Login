# Django Login Example

This project demonstrates how to create a basic Django application with the following features:
- A **login page** as the landing page.
- A **public page** accessible to everyone.
- A **private page** restricted to logged-in users.
- A **profile creation page** (user registration).

---

## **Features**
1. **Landing Page (Login Page)**  
   Users can log in using their username and password. On successful login, they are redirected to the private page.
   
   Users that are already logged in will be redirected to the private page. They must logout before they can see the landing page.
   
   The landing page has a link to the pulic page.

2. **Public Page**  
   Anyone can view this page without logging in. The public page shows registered users user_id and uploaded image.
   
   The public page has a link to the landing page.

3. **Private Page**  
   Only logged-in users can access this page. Non-logged-in users are redirected to the login page.
   
   In this private page, users can upload an image of themselves, max one image. They can also delete current image.
   
   The private page has a link to the public page.

4. **Profile Creation Page**  
   Users can create an account by providing a username, password, and email address. After successful regiastration, the user is redirected to the landing page.   
   
   The profile creation page cannot be shown by logged in users.
   
   The profile creation page has a link to the landing page.

5. **Logout Functionality**  
   Logged-in users can log out by pressing the Logout button.
   
   The Logout button is visisble for logged in users at the public page and private page.

---

## **Requirements**
- Python 3.8+
- Django 4.x

---

## **Setup**

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/django-auth-tutorial.git
cd django-auth-tutorial
```

### 2. Create a virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install django
```

### 4. Run migrations
Apply database migrations to create the necessary tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server
Run the development server:
```bash
python manage.py runserver
```

### 6. Access the application
- Visit `http://127.0.0.1:8000` to access the login page.
- Register a user at `http://127.0.0.1:8000/register/`.

---

## **Project Structure**
```
myproject/
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       ├── public.html
│   │       ├── private.html
│   │       └── register.html
│   ├── urls.py
│   ├── views.py
│   └── models.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

---

## **Usage**

1. **Register a new user**:  
   Go to `/register/`, enter a username, password, and email, then submit the form.

2. **Log in**:  
   Go to `/`, enter your username and password, and access the private page.

3. **Access public page**:  
   Visit `/public/` without logging in.

4. **Logout**:  
   Log out from the private page to return to the login page.

---

## **Extending the App**
This app is a foundational starting point. You can:
- Add additional user profile fields.
- Implement email verification.
- Use Django's built-in `UserCreationForm` for user registration.
