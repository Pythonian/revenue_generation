Project Scope
---

**Web Application: Nkanu East L.G.A revenue generation system**

The aim of the study is to develop a system that will automate revenue generation and accountability of Local Government Areas. The objectives of the study are as follows: 
1. To design a system that ensures all records are kept in a database and users of the system can easily search to get records very fast from a secure and centralized database. 
2. To develop an automated system that will generate adequate and accurate report of revenue generated so as to promote transparency and accountability. 

### Project Installation

**Requirements**

- Python 3

_Follow the steps below to get the program working on your system locally. These steps are tailored for users developing on Windows OS._

1. Clone the repo
   ```sh
   git clone https://github.com/Pythonian/revenue_generation.git
   ```
2. Change into the directory of the cloned repo
   ```sh
   cd revenue_generation
   ```
3. Setup a Python virtual environment
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment
   ```sh
   .\venv\Scripts\activate
   ```
5. Install project requirements
   ```sh
   pip install -r requirements.txt
   ```
6. Run database migrations
   ```sh
   python manage.py migrate
   ```
7. Create an admin superuser
   ```sh
   python manage.py createsuperuser
   ```
   _Note: Use `admin` for both the `username` and `password`, and skip entering the `email`. Also type `y` to bypass Password validation._
8. Populate the database with fake data (Optional)
   ```sh
   python manage.py populate_db
   ```
9. Run the development server
   ```sh
   python manage.py runserver
   ```
10. Visit the URL in your browser
   ```sh
   127.0.0.1:8000
   ```
   You can also visit the admin dashboard in a new tab and login with the credentials used in step 7.
   ```sh
   127.0.0.1:8000/admin/
   ```