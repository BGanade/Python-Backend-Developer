""" Ana is developing a portfolio to showcase the Python projects she has completed. 
She has organized a list containing the name of each project but noticed that some items
 might be missing, appearing as `None`:


Copy
projects = ["website", "game", "data analysis", None, "mobile app"]

Create a program that helps Ana iterate through the list of projects and displays the 
names of the valid projects. If it encounters a `None` item, the program should display 
the message: "Missing project". """

projects = ["website", "game", "data analysis", None, "mobile app"]

for project in projects:
    if project is not None:
        print(project)
    else:
        print("Missing project")

