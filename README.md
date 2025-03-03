# Heart Disease Prediction App

This project is a Flask-based web application that predicts the likelihood of heart disease based on user inputs. 
The model utilizes machine learning techniques to analyze key health indicators and provide predictions. 
The app is containerized using Docker and deployed on AWS EC2, making it easily accessible and scalable.
Link : http://ec2-51-21-192-243.eu-north-1.compute.amazonaws.com:5000/

## Features
- User-friendly interface for inputting health data
- Machine learning-based prediction of heart disease
- Dockerized for easy deployment
- Hosted on AWS EC2 for accessibility

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/heart-disease-app.git
cd heart-disease-app
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run Locally
```bash
python app.py
```
The app will be available at `http://127.0.0.1:5000`.

## Docker Setup

### 1. Build Docker Image
```bash
docker build -t heart-disease-app .
```

### 2. Run Docker Container
```bash
docker run -p 5000:5000 heart-disease-app
```
The app will be available at `http://localhost:5000`.

## Deployment on AWS EC2

### 1. Launch an EC2 Instance
- Choose an Ubuntu instance (or Linux kernel if free-tier applicable)
- Allow the following security rules:
  - HTTP (Port 80)
  - HTTPS (Port 443)
  - Custom TCP Rule (Port 5000)
  - SSH (Port 22)

### 2. Connect to EC2 via SSH
```bash
ssh -i your-key.pem ubuntu@your-ec2-instance-ip
```

### 3. Install Docker on EC2
```bash
sudo apt update && sudo apt install docker.io -y
```

### 4. Clone the Repository on EC2
```bash
git clone https://github.com/yourusername/heart-disease-app.git
cd heart-disease-app
```

### 5. Build and Run Docker on EC2
```bash
sudo docker build -t heart-disease-app .
sudo docker run -d -p 5000:5000 heart-disease-app
```

The application will be accessible at `http://your-ec2-instance-ip:5000`.

## Author
Developed by Chethan Kashyap.

## Images
![Screenshot (321)](https://github.com/user-attachments/assets/0ebb155e-f809-4948-b498-2b83e4cdca3d)
![Screenshot (322)](https://github.com/user-attachments/assets/f344db55-4e6f-4cad-b7c8-726640a71bf7)
![Screenshot (323)](https://github.com/user-attachments/assets/6d423d4a-d17b-4edd-b685-9816999a41d6)
![image](https://github.com/user-attachments/assets/12ac4a24-27fb-472c-9ea0-885ad81dc2c7)




