from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import cv2
import pytesseract
import csv
import schedule
import random
from twilio.rest import Client 
one=[]
with open('german.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='@')
    for row in csv_reader:
        one.append(row)
#preparing the german message to send