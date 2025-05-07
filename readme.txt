API Documentation for Doctor-Patient Mapping
This document outlines the API endpoints for user authentication and doctor-patient mapping functionality. All views use the IsAuthenticated permission class, requiring user authentication via JWT.
1. User Registration

Endpoint: POST http://127.0.0.1:8000/api/auth/register/
Description: Create a new user account.
Method: POST
Body: Provide user details (e.g., username, email, password) as required by the registration API.

2. User Login

Endpoint: POST http://127.0.0.1:8000/api/auth/login/
Description: Authenticate a user and obtain a JWT access token.
Method: POST
Body: Provide credentials (e.g., username and password).
Authentication: Uses Simple JWT. Include the access token in the Authorization header for subsequent requests:Authorization: Bearer <access_token>



3. Assign a Doctor to a Patient

Endpoint: POST http://127.0.0.1:8000/api/doctor/mappings/
Description: Create a mapping between a doctor and a patient.
Method: POST
Body:{
    "doctor_id": <doctor_id>,
    "patient_id": <patient_id>
}


Authentication: Requires Bearer token.

4. Retrieve All Patient-Doctor Mappings

Endpoint: GET http://127.0.0.1:8000/api/doctor/mappings/
Description: Fetch all doctor-patient mappings.
Method: GET
Authentication: Requires Bearer token.

5. Get Doctors Assigned to a Specific Patient

Endpoint: GET http://127.0.0.1:8000/api/doctor/mappings/<patient_id>/
Description: Retrieve all doctors assigned to a specific patient.
Method: GET
Example: GET http://127.0.0.1:8000/api/doctor/mappings/1/
Authentication: Requires Bearer token.

6. Remove a Doctor from a Patient

Endpoint: POST http://127.0.0.1:8000/api/doctor/mappings/<patient_id>/remove/
Description: Remove a doctor from a patient's assigned doctors.
Method: POST
Example: POST http://127.0.0.1:8000/api/doctor/mappings/5/remove/
Body:{
    "doctor_id": <doctor_id>
}


Authentication: Requires Bearer token.

