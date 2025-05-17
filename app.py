# Given OTP Verification system has three main parts:- Acquiring Email Addresses ,
# Generating OTPs , 
# Sending OTP to the user's email address acquired 
# finally authentication
from email_validator import validate_email, EmailNotValidError
import random, os, sendgrid
from sendgrid.helpers.mail import *
import redis
from flask import Flask
from dotenv import load_dotenv

print("Hello there .... successful run")