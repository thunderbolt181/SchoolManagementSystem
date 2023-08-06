# Errors to fix

1. New Entry link now working from Student, Teacher and Staff Panel in dashboard. (Fixed in user.type -> staff)[✅]
2. Find the way to update attendance in teacher and staff. It opens search panel (Change it to attandance marking panel).[✅]
    - Checking for multiple update remaining.(First make multiple accounts and then test).
3. Cannot view my profile from user drop down menu in top right corner. [✅]
4. Mark which fields are necessory in create new entry form in student, teacher and staff.[✅]
5. Check yearly attendance dashboard, might be displaying the pie chart wrong.[✅]
6. Users cannot change their passwords, might have to make it from scratch.
7. Take a look how a UserEditForm is displayed(Profile Pic field should be changed, DOB should be re-formatted).[✅]



# Username and password for testing
    - Teacher :
        username - vwits@teacher
        password - vwits@1234

    - Student :
        username - vwits@student
        password - vwits@1234

    - Staff : 
        username - vwits@admin
        password - vwits@1234


# Functionalities to add.
    - combine both user model and profile model in BaseAbstractUser and fix all the error caused due to change.[✅]
        - Build a custom user model[✅]
        - integrate custom user model and profile model[✅]
    - Enable the register button.
    - Try to add permission mixin or decorator in the current app.
    - Make page for students.
    - Make page for teachers.
    - Make page for parents.


# Things that could be better
    - attendance is created for all users like user who are not part of any insitiute i.e admin of website