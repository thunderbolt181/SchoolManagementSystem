# SchoolManagementSystem
It's a school management system which keeps track of students, teachers and staff and their attendence

## Features
1. Can manage multiple institutions at once
2. Can maintain details of Students, Teachers and Staff Members
3. Can maintain attendance of students, teachers and staff members

## Technologies Used
1. Python
2. Django
3. PostgreSQL Database
4. HTML/CSS
5. TailwindCSS
7. Javascript
8. Ajax

## How to Use
1. Get project files to local drive by: 
    - Download this project and then extract it.
    - Fork the repository and clone project with command `git clone <project_link>` on local drive
2. Nevigate to downloaded or Cloned folder and open it in code editor.
3. Initiate a new virtual Environment by command `python -m venv <environment_name>`.
4. Activate virtual environment by command `<environmane_name>\Script\activate` 
    > Command in step 4 is only for windows. Linux and macOS have different commands.

    > Steps 3 and 4 are not compulsory by recommended. And virtual Environment can be of your choice.
5. Install required modules by running command `python -m pip install -r requirements.txt`.
6. Install PostgreSQL and set up database
    >PostreSQL is must because some of the fields are not supported in sqlite3
7. Create `.env` file in main folder and save add some Environment Variabels:
    - DB_NAME : Name of Database
    - DN_UNAME : Name of user of Database
    - DB_PASS : Password of Database
8. Migrate to Database by command `python manage.py makemigrations` followed by command `python manage.py migrate`
9. Create super user by command `python manage.py createsuperuser`
10. Run server by command `python manage.py runserver`
11. Visit `127.0.0.1:8000/admin`
12. Login Via super user credentials. 
13. Create a new Institute.
    > Institutes can be created only from admin panel.
14. Add additional information of super in profile section.
15. Add the super user in any one of these three field and fill the info:
    - Student
    - teacher
    - staff

> Setup is complete and the main website can be visited from `127.0.0.1:8000`

> To add another user from admin panel, the user should be add in `user` and `profile` section and any one from the step 15 

> To use Email smtp for password resetting, uncomment last lines in "SchoolManagementSystem/settings.py" and add necessory the details in .env file

## Suggestions of improvements that can be done
- Add landing page for students and Teacher [Currently landing page of staff member is working]
- Add a Fees Structure for students and salary for teachers and staff members.
- Since multiple institutes can be added, a blog feature can be added so that each institutes can update about new events or new about their institute.
- Library management and other features can also be added.