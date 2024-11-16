@echo off
REM Navigate to the Django project directory
cd C:\Apache24\htdocs\finalProject\school_academic


call C:\Apache24\htdocs\finalProject\myenv\Scripts\activate

start /min python manage.py runserver 127.0.0.1:8000
