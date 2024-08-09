Database Connection and Data Insertion Using Flask
This README provides steps to execute code that connects to a MySQL database and inserts data using a Flask application.
Prerequisites
1. MySQL Server: Ensure you have a MySQL server running on your localhost.
2. Python and Flask: Python and Flask framework need to be installed.
Steps to Execute the Code:
1. Install Required Packages
Ensure you have the necessary packages installed. Run the following command in your terminal:
       pip install Flask mysql-connector-python

2. Database Configuration
       The code connects to a MySQL database with the following configurations:
       Host: localhost
       Username: root
       Password: Yadnyesh@6119
       Database: webdata
       You might need to adjust these configurations according to your MySQL setup.
3. Run the Flask application 
       Save the provided code in a file, for example, app.py.
       Execute the Flask application by running this command in the terminal:
       		python app.py
       This will start the server.
4. Accessing the endpoints
The code provides several routes (/patinfo, /patcont, /patinsu, /patschem, /docinfo, /doccont, /doclic, /hosinfo, /hoscont, /hosleg) to input data for different entities related to patients, doctors, and hospitals.
Access these endpoints using your browser or tools like Postman by visiting http://127.0.0.1:5000/<endpoint_name>. For example, http://127.0.0.1:5000/patinfo for patient information entry.
5. Input Form Submission
Enter the required data in the input forms presented by the web pages served by the Flask application. After submitting the forms, the data will be stored in the MySQL database.
Notes:
* Ensure your MySQL server is running before executing the Flask application.
* This code includes inserting data into multiple tables. Make sure the tables (patient_info, patient_contact, patient_insurance, etc.) are created in the webdata database in your MySQL server with respective columns as indicated in the code.



