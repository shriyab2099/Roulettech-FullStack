# Todo List Django React App

This project is a simple Todo List application with a Django backend and a React frontend. The application allows users to create, update, and delete tasks.

## Setup Backend

1. **Navigate to the project directory:**
   ```bash
   cd /path/to/your/project

2. **Install Virtual Environment::**
   ```bash
   pip install virtualenv

3. **Create and Activate Virtual Environment:**
   ```bash
   pipenv shell

4. **Install Django:**
   ```bash
   pipenv install django

5. **Start a new Django project:**
   ```bash
   django-admin startproject django-react-app

6. **make  kigrations after navigating to backend directory:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
4. **Run the Django server:**
   ```bash
   python manage.py runserver


## Setup Frontend

1. **Navigate to the frontend directory and Initialize a new React application:**
   ```bash
   cd frontend
   npx create-react-app .

2. **install Axios for making HTTP requests:**
   ```bash
   npm install axios

3. **Start the React development server:**
   ```bash
   npm start

## API Endpoints

- **GET /api/tasks/**: Retrieve all tasks.
- **POST /api/tasks/**: Create a new task.
- **PUT /api/tasks/:id/**: Update an existing task.
- **DELETE /api/tasks/:id/**: Delete an existing task.


## Deployment to AWS

### Basic Requirements

#### Deploy Frontend Code to AWS S3

1. **Build the React App:**
   ```bash
   cd frontend
   npm run build

2. **Create an S3 Bucket**
3. **Upload Build Files to S3**
4. **Configure S3 for Static Website Hosting**
    - Enable Static website hosting.
    - Set Index document to index.html 
5. **Go to Permissions and click Bucket Policy:**
   - Navigate to your S3 bucket.
   - Click on the **Permissions** tab.
   - Click **Bucket Policy**.
6. **Add the following policy:**
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::your-bucket-name/*"
       }
     ]
   }

7. **Access the Website:**
   - Use the Endpoint URL from Static website hosting to view React app.







