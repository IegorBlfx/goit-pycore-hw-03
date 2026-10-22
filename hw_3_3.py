import re

# Зробив домашнє завдання з перевіркою на "+", відповідно до ТЗ в LMS, але обʼєктивно - можна було б
# викинути цей крок і просто видалити всі символи і додати + на початок.



def normalize_phone(phone_number): # normalize the phone number to the format +380XXXXXXXXX
    
    phone_number = phone_number.strip() # remove leading and trailing whitespace    
    if re.search(r'\d', phone_number): # check if the phone number contains at least one digit
        if phone_number[0] == '+': # check if the phone number starts with a plus sign
            return re.sub(r'(?!^\+)\D', '', phone_number) # keep the existing prefix, remove other symbols
            
        else:
            phone_number = re.sub(r'\D', '', phone_number)
            if re.match(r"380", phone_number): # check if the phone number starts with 380
                return "+" + phone_number 
            elif re.match(r"0", phone_number):
                return "+38" + phone_number 
            else:
                return "+380" + phone_number 
    else:
        return None # empty string or no digits - nothing to normalize