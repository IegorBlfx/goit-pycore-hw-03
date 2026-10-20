import re

# Зробив домашнє завдання з перевіркою на "+", відповідно до ТЗ в LMS, але обʼєктивно - можна було б
# викинути цей крок і просто видалити всі символи і додати + на початок.



def normalize_phone(phone_number): # normalize the phone number to the format +380XXXXXXXXX
    
    if phone_number[0] == '+': # check if the phone number starts with a plus sign
        phone_number = re.sub(r'(?!^\+)\D', '', phone_number.strip())
        if re.match(r"\+380", phone_number): # check if the phone number starts with +380
            return phone_number
        elif re.match(r"\+0", phone_number): # check if the phone number starts with +0
            return phone_number[0] + "38" + phone_number[1:]
        else:
            return phone_number[0] + "380" + phone_number[1:]
        
    else:
        phone_number = re.sub(r'\D', '', phone_number.strip())
        if re.match(r"380", phone_number): # check if the phone number starts with 380
            return "+" + phone_number 
        elif re.match(r"0", phone_number):
            return "+38" + phone_number 
        else:
            return "+380" + phone_number 