from datetime import datetime
from utils.logger import setup_logger


logger = setup_logger()

def transform_all(data_list):
    transform_list = []
    for record in data_list:
        transformed = transform_record(record)
        if transformed:
            transform_list.append(transformed)
    
    return transform_list


def calculate_age(dob):
    try:
        birth = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.date) < (birth.month, birth.date))
    except:
        logger.warning(f"{dob}--Invalid DOB")
        return None
        

def transform_record(data):
    
    #full name

    try:
        name = f"{data.get('first_name', "")} {data.get("last_name", "")}"
    except:
        name = ""
        logger.warning(f"invalid first and last name")
        
    #print(name)
    
    #phone number split
    
    phone_no = data.get("phone","")
    
    if "-" in phone_no:
        country_code, phone_number = phone_no.replace("+", "").split('-')
    else:
        country_code, phone_number = "", phone_no
        
    #print(country_code,phone_number)
    
    #age calculation and adult
    
    age = calculate_age(data.get("dob", ""))
    
    if age != None and age >= 18:
        is_adult = True
    else:
        is_adult = False
    
    #print(age, is_adult)
    
    #Address
    
    try:
        address = data.get("address","")
        lis = address.split(',')
        city = lis[1].strip()
        country = lis[2].strip()
    except:
        address = ""
        city = ""
        country = ""
        logger.warning(f"{address} -- invalid address")
    
    #print(address,city,country)
    
    #last_login
    
    try:
        login = data.get("last_login", "")
        last_login_ts = int(datetime.fromisoformat(login).timestamp())
    except:
        last_login_ts = None
        logger.warning(f"{login} -- invalid last_login formate")
    #print(last_login_ts)
    
    #language_main
    try:
        lang = data.get("language", "")
        language_main = lang.split('-')[0]
    except:
        language_main = ""
        logger.warning(f"{lang} -- No main language available")
    #print(language_main)    
    
    #contact_preferance
    
    try:
        contact = data.get("preferred_contact", "")
        contact_preference = contact.lower()
    except:
        contact_preference = ""
        logger.warning(f"{contact} -- No contact prefered")
    
    #print(contact_preference)
    
    #social handling formatting
    
    try:
        social = data.get("social", {})
        if "twitter" in social and social["twitter"].startswith("@"):
            social["twitter"] = f"https://twitter.com/{social["twitter"][1:]}"
    except:
        social["twitter"] = ""
        logger.warning(f"{social} -- No twitter id is available")
    #print(social['twitter'])
    
    #status code
    try:
        status = data.get("subscription_status", "")
        if status == 'Active':
            status_code = 1
        elif status == 'Inactive':
            status_code = 0
    except:
        status_code = -1
        logger.warning(f"{status} -- status unavailable")
    #print(status_code)
    
    return {
        "name": name,
        "email": data.get("email", ""),
        "country_code": country_code,
        "phone_number": phone_number,
        "age": age,
        "is_adult": is_adult,
        "location": {
            "full_address": address,
            "city": city,
            "country": country
        },
        "last_login_ts": last_login_ts,
        "language_main": language_main,
        "contact_preference": contact_preference,
        "social_links": social,
        "status_code": status_code
    }

    