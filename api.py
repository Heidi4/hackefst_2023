import requests

# Canister ID
CANISTER_ID = "your_canister_id"

# RPC endpoint
ENDPOINT = f"https://ic0.app/ic/api/v2/canisters/{CANISTER_ID}/call"

def login():
    # Send request to login and authenticate through Kybra
    response = requests.post(
        ENDPOINT, json={"method": "handle_command", "args": {"type": "Command::Login"}}
    )
    return response.json()

def get_courses():
    # Send request to retrieve available courses
    response = requests.post(
        ENDPOINT, json={"method": "get_courses", "args": {}}
    )
    return response.json()

def enroll_in_course(course_id):
    # Send request to enroll user in a specific course
    response = requests.post(
        ENDPOINT,
        json={
            "method": "handle_command",
            "args": {
                "type": "Command::EnrollInCourse",
                "course_id": course_id,
            },
        },
    )
    return response.json()

def get_enrollment_progress(course_id):
    # Send request to retrieve user's progress in a course
    response = requests.post(
        ENDPOINT,
        json={
            "method": "get_enrollment_progress",
            "args": {"course_id": course_id},
        },
    )
    return response.json()
