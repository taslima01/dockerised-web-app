dockerised-web-app

Description

A simple Python Flask application containerised using Docker. The app demonstrates how to set up, build, and run a Docker container for a basic "Hello, World!" web application.

Features

Python Flask web application.

Docker containerisation for platform-independent deployment.

Prerequisites

Python 3.9 or later.

Docker installed on your system.

Setup Instructions

Clone the repository:
bash
Copy code
git clone git@github.com:taslima01/dockerised-web-app.git
cd dockerised-web-app
Build the Docker image:
bash
Copy code
docker build -t flask-app .
Run the Docker container:
bash
Copy code
docker run -d -p 5000:5000 --name flask-container flask-app
Access the Application
Once the container is running, visit http://localhost:5000 in your browser to see the app.

Future Plans
Add a more meaningful Flask app.
Implement Terraform for AWS deployment.
License
This project is open-source and available under the MIT License.

