import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
import requests
from email.message import EmailMessage

# scope = ['https://wwww.googleapis.com/auth/spreadsheets']
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Your Sheet name here").sheet1 # Open the spreadhseet


data = sheet.get_all_records() 

# Get a specific row
row = sheet.row_values(3)
# Get a specific column
col = sheet.col_values(3)
# Get the value of a specific cell
cell = sheet.cell(1,2).value

#Test 1
firstShiftEmployeeName = sheet.cell(2,1).value
firstShiftEmployeeStartTime = sheet.cell(2,2).value
firstShiftEmployeeEndTime = sheet.cell(2,6).value
firstShiftEmployeePhoneNumber = sheet.cell(2,7).value
firstShiftEmployeeCellularProvider = sheet.cell(2,8).value

firstShiftEmployeeContact = (firstShiftEmployeePhoneNumber) + (firstShiftEmployeeCellularProvider)
print(firstShiftEmployeeName, firstShiftEmployeeStartTime, firstShiftEmployeeEndTime, firstShiftEmployeePhoneNumber, firstShiftEmployeeCellularProvider)



# Texting Part


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    


    user = "Your@gmail.com"
    msg['from'] = user
    password = "****************"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    #Use for sending an email
    # email_alert("Hello", "Work place test", "Email Address")

    #Used for sending an sms
  
    email_alert("Hello", (firstShiftEmployeeName) + " Your Shift Starts " + (firstShiftEmployeeStartTime) + " And Ends " + (firstShiftEmployeeEndTime), (firstShiftEmployeeContact))
    
