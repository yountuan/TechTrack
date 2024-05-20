# TechTrack_app

Task: Developing a RESTful API for Equipment Monitoring and Management

Customer company: TechTrack

Description of the task:

TechTrack develops a platform for monitoring and managing technical equipment such as industrial robots, manufacturing equipment, quality control systems, etc. The company is facing challenges in managing data on the technical condition of their equipment.

Your task is to develop a RESTful API using Django REST Framework and PostgreSQL to manage a list of equipment, data readings, and alerts. The API should allow users to be created, read, updated, and deleted. Basic authentication and authorization must be implemented to secure the API. The system should handle simultaneous requests from multiple clients and ensure high data availability.

Additional requirements:

The API should be well documented using Swagger/OpenAPI.
Provide support for standard HTTP methods (GET, POST, PUT, DELETE) for each resource.
Implement error handling and return appropriate HTTP statuses and messages.
Restrictions:

The API must use Django REST Framework and PostgreSQL.
The system should ensure data consistency across parallel queries using transaction mechanisms.
The API should use JSON format for data exchange between client and server.
Answers to possible questions:

How will you ensure the security of your API?

We will use Access Tokens to authenticate users and restrict access based on roles and permissions.
What measures will you take to ensure the performance of your API?

We will use data caching and database query optimization. Additionally, the application can be scaled horizontally to handle large volumes of requests.
How will you test your API?

We will write unit tests using tools like unittest for Python to test core functionality. Integration testing will also be conducted to check how the API interacts with other system components.
What data formats will you use to pass information through the API?

JSON format will be used to exchange data between client and server as it is easy to read and supported by many programming languages.
How will you ensure data consistency across parallel queries?

We will use transaction mechanisms in the database to ensure data integrity during create, update, and delete operations.

Screenshots:

API Endpoints Overview:

Successful Equipment Creation:

Database Schema:

Error Handling Example:

Video description of the work:

For a detailed demonstration of the project, please refer to the video linked below. This video walks through the setup, key features, and functionalities of the API:

Video Presentation:
For a detailed demonstration of the project, please refer to the video linked below. This video walks through the setup, key features, and functionalities of the API:
https://drive.google.com/drive/folders/1BR_qLzhz5P1JVFfpLAKOqZHvO-NuY4hR?usp=sharing

Deploy on Free Cloud Server (Render): https://store-8r6h.onrender.com
(Since it's a free server, it could work very slow. Sorry for that T_T)
Credentials to log in to admin panel are 
'admin' for username and 
'1' for password.
