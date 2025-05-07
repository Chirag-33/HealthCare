# HealthCare
HealthCare is a Django based app which provides a robust solution for managing user authentication and doctor-patient relationships in a healthcare system. Leveraging Django REST Framework and Simple JWT for secure token-based authentication, it enables seamless user registration, login, and management of doctor-patient mappings. All endpoints, except registration and login, are protected by the `IsAuthenticated` permission class, ensuring secure and authorized access to healthcare functionalities.

## Overview
This API facilitates secure user authentication and the management of doctor-patient relationships. It allows for registering users, authenticating them, assigning doctors to patients, retrieving mappings, and removing assignments. All endpoints are protected and require a valid JWT access token in the `Authorization` header.

## API Endpoints
### User Authentication
#### User Registration
- **Endpoint**: `POST http://127.0.0.1:8000/api/auth/register/`
- **Description**: Creates a new user account.
- **Method**: POST
- **Request Body**:
  ```json
  {
    "username": "<username>",
    "email": "<email>",
    "password": "<password>"
  }
  ```
- **Response**: Returns user details and a success message upon successful registration.
- **Authentication**: None required.

#### User Login
- **Endpoint**: `POST http://127.0.0.1:8000/api/auth/login/`
- **Description**: Authenticates a user and returns a JWT access token.
- **Method**: POST
- **Request Body**:
  ```json
  {
    "username": "<username>",
    "password": "<password>"
  }
  ```
- **Response**: Returns a JWT access token.
- **Authentication**: None required.
- **Usage**: Include the token in subsequent requests as:
  ```
  Authorization: Bearer <access_token>
  ```

### Doctor-Patient Mappings
#### Assign a Doctor to a Patient
- **Endpoint**: `POST http://127.0.0.1:8000/api/doctor/mappings/`
- **Description**: Creates a mapping between a doctor and a patient.
- **Method**: POST
- **Request Body**:
  ```json
  {
    "doctor_id": <doctor_id>,
    "patient_id": <patient_id>
  }
  ```
- **Authentication**: Requires Bearer token.
- **Response**: Returns the created mapping details.

#### Retrieve All Patient-Doctor Mappings
- **Endpoint**: `GET http://127.0.0.1:8000/api/doctor/mappings/`
- **Description**: Fetches all doctor-patient mappings.
- **Method**: GET
- **Authentication**: Requires Bearer token.
- **Response**: Returns a list of all doctor-patient mappings.

#### Get Doctors Assigned to a Specific Patient
- **Endpoint**: `GET http://127.0.0.1:8000/api/doctor/mappings/<patient_id>/`
- **Description**: Retrieves all doctors assigned to a specific patient.
- **Method**: GET
- **Example**: `GET http://127.0.0.1:8000/api/doctor/mappings/1/`
- **Authentication**: Requires Bearer token.
- **Response**: Returns a list of doctors assigned to the specified patient.

#### Remove a Doctor from a Patient
- **Endpoint**: `POST http://127.0.0.1:8000/api/doctor/mappings/<patient_id>/remove/`
- **Description**: Removes a doctor from a patient's assigned doctors.
- **Method**: POST
- **Example**: `POST http://127.0.0.1:8000/api/doctor/mappings/5/remove/`
- **Request Body**:
  ```json
  {
    "doctor_id": <doctor_id>
  }
  ```
- **Authentication**: Requires Bearer token.
- **Response**: Returns a success message upon removal.

## Authentication
All endpoints except user registration and login require a valid JWT access token. Obtain the token via the login endpoint and include it in the `Authorization` header as follows:
```
Authorization: Bearer <access_token>
```

## Notes
- Ensure the server is running locally at `http://127.0.0.1:8000/` for the endpoints to work.
- The API uses Django's `Simple JWT` for token-based authentication.