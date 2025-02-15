## Bynry-Assignment
This repository contains a Django-based web application developed as an assignment project. The application is designed to manage gas utility services, providing functionalities for both service providers and customers.

## Features
Service Management: Allows service providers to add, update, and delete gas services.
Customer Management: Enables customers to view available services and subscribe to them.

## Prerequisites
Before setting up the project, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv

## Setup Instructions
Follow these steps to set up and run the project locally:

1. **Clone the Repository:**

      ```bash
      git clone https://github.com/MahakGupta03/Bynry-Assignment.git
      cd Bynry-Assignment

2. **Create a Virtual Environment:**
      ```bash
      virtualenv venv
   
If virtualenv is not installed, you can install it using:
      ```
      pip install virtualenv
      ```

4. **Activate the Virtual Environment:**

 - On Windows:
   ```bash
      venv\Scripts\activate
 - On macOS and Linux:
   ```bash
   source venv/bin/activate

5. **Install Dependencies:**
   ```bash
      pip install -r requirements.txt
This will install all the required packages listed in the requirements.txt file.

6. **Apply Migrations:**

   ```bash
      python manage.py migrate
This command applies the necessary database migrations.

7. **Create a Superuser:**

   ```bash
      python manage.py createsuperuser
Follow the prompts to create an admin user for accessing the Django admin interface.

8. **Run the Development Server:**

   ```bash
      python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/.
