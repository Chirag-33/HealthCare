1) In all the views Permission class Is_authenticated is use due to that first you will need a user which u can create using register url 
http://127.0.0.1:8000/api/auth/register/
2) Than go to login route http://127.0.0.1:8000/api/auth/login/ . I have use simple jwt for authentication so please pass the access token to 
bearer
3)for mapping url . To assign a doctor to patient run this on POST http://127.0.0.1:8000/api/doctor/mappings/ and in body pass doctor_id and than patient_id
4)TO  - Retrieve all patient-doctor mappings. use this point on GET http://127.0.0.1:8000/api/doctor/mappings/
5)TO Get all doctors assigned to a specific patient. http://127.0.0.1:8000/api/doctor/mappings/1/
6)TO remove any doctor from patient - Run this command http://127.0.0.1:8000/api/doctor/mappings/5/remove/ in URl pass the patient id and in body pass doctor_id {
    "doctor_id":1
}