from kybra import query, update, void

import kybra.did as did
import requests

def get_user_information(did: str) -> dict:
    # Get user information from the Kybra DID registry
    response = requests.get(f"https://registry.kybra.io/did/{did}")
    user_information = response.json()
    return user_information

def get_available_courses() -> list:
    # Fetch a list of available courses from the EduLand backend
    response = requests.get("https://edu-land.com/api/courses")
    available_courses = response.json()
    return available_courses

def render_page(user_information: dict, available_courses: list) -> str:
    # Render the HTML page with the user's name and the list of courses
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>EduLand - Welcome!</title>
      <link rel="stylesheet" href="assets/css/app.css">
    </head>
    <body>
      <header>
        <h1>EduLand</h1>
        <nav>
          <ul>
            <li><a href="#">Courses</a></li>
            <li><a href="#">My Profile</a></li>
            <li><a href="#">Logout</a></li>
          </ul>
        </nav>
      </header>

      <main>
        <h2>Welcome to EduLand, [user name]!</h2>
        <p>
          You are now logged in and can access all the features of the EduLand platform.
        </p>
</main>
</body>
</html>
        
