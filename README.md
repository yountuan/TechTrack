# TechTrack_app
# Task: RESTful API for Equipment Monitoring

**Customer:** TechTrack

## Task Description

TechTrack needs a RESTful API to manage technical equipment data. The API will handle CRUD operations for equipment, data readings, and alerts, using Django REST Framework and PostgreSQL.

## Requirements

- **API Documentation:** Swagger/OpenAPI
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Authentication:** Access Tokens
- **Error Handling:** Appropriate HTTP statuses and messages
- **Data Format:** JSON
- **Data Consistency:** Transaction mechanisms

## Restrictions

- Must use Django REST Framework and PostgreSQL for Backend Track.

## Q&A

- **Security:** Access Tokens for authentication and role-based access.
- **Performance:** Data caching, query optimization, and horizontal scaling.
- **Testing:** Unit and integration testing using unittest.
- **Data Format:** JSON for data exchange.
- **Data Consistency:** Database transactions for integrity.

## Screenshots

1. **API Endpoints Overview:**
   ![API Endpoints Overview](/screenshots/Screenshot2024-05-20at03.13.04.png)
   ![API Endpoints Overview](/screenshots/Screenshot2024-05-20at03.13.14.png)
   ![API Endpoints Overview](/screenshots/Screenshot2024-05-20at03.13.26.png)
   ![API Endpoints Overview](/screenshots/Screenshot2024-05-20at03.13.29.png)

3. **Project configs:**
   Docker-compose
   ![Docker-compose](/screenshots/Screenshot2024-05-22at13.10.51.png)

3. **Database Schema:**
   ![Database Schema](/screenshots/Screenshot2024-05-20at02.33.05.png)

## Video Presentation

For a detailed demonstration of the project, please refer to the video linked below. This video walks through the setup, key features, and functionalities of the API:
https://drive.google.com/drive/folders/1BR_qLzhz5P1JVFfpLAKOqZHvO-NuY4hR?usp=sharing

## Deploy on Free Cloud Server (Render):
(Since it's a free server, it could work very slow. Sorry for that T_T)
https://store-8r6h.onrender.com
Credentials to log in to admin panel are
'admin' for username and
'1' for password.
