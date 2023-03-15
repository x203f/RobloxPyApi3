import random

from .Enums import Gender
from .Captcha import Captcha,SessionCaptcha
import requests
class Date:
    def __init__(self,day,month,Year):
        self.d: int = day
        self.year: int = Year
        self.month = month.value

def signup(Username,password,gender,birthday:Date,WaitAfterCaptcha = 4.5):
    m = 0
    if gender == Gender.male:
        m = 'male'
    elif gender == Gender.female:
        m = "female"
    elif gender == Gender.Random:
        m = random.choice(["female",'male',0])
    elif gender == Gender.Unknown:
        m = 0
    else:
        m = gender
    JSONSignup = {
        "agreementIds": [
            "848d8d8f-0e33-4176-bcd9-aa4e22ae7905",
            "54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3"
        ],

        "birthday": f"{birthday.d} {birthday.month} {birthday.year}",
        "context": "MultiverseSignupForm",
        "gender": m,
        "isTosAgreementBoxChecked": True,
        "password": password,
        "username": Username,
        "referralData": None,
        'abTestVariation': 0
    }
    c = Captcha("https://auth.roblox.com/v2/signup", data=JSONSignup,
                Headers={"Accept": "application/json", "x-csrf-token": requests.post(
                    'https://auth.roblox.com/v1/usernames/validate'
                ).headers['x-csrf-token']},WaitAfterComplete=WaitAfterCaptcha)

    def MakePost():
        post = requests.post("https://auth.roblox.com/v2/signup",
                             headers={"Accept": "application/json", "x-csrf-token": requests.post(
                                 'https://auth.roblox.com/v1/usernames/validate'
                             ).headers['x-csrf-token']}, json=JSONSignup)
        return post

    a = MakePost()
    b = a.json()['failureDetails'][0]['fieldData']
    if b:
        print("Captcha is required!")
        td = c.GetDetailsFromFieldData(b)
        f = c.StartSessionFromDetails(td['TokenID'], td['location'], td['id'], td['blob'])
    return f.json(),{"Username":Username,'Password':password}
    #details = c.GetDetails()
    #c.StartSession()
    #print(c.Token, c.ID)
def signupSession(Username,password,gender,birthday:Date,WaitAfterCaptcha = 4.5):
    with requests.session() as session:
        m = 0
        if gender == Gender.male:
            m = 'male'
        elif gender == Gender.female:
            m = "female"
        elif gender == Gender.Random:
            m = random.choice(["female",'male',0])
        elif gender == Gender.Unknown:
            m = 0
        else:
            m = gender
        JSONSignup = {
            "agreementIds": [
                "848d8d8f-0e33-4176-bcd9-aa4e22ae7905",
                "54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3"
            ],

            "birthday": f"{birthday.d} {birthday.month} {birthday.year}",
            "context": "MultiverseSignupForm",
            "gender": m,
            "isTosAgreementBoxChecked": True,
            "password": password,
            "username": Username,
            "referralData": None,
            'abTestVariation': 0
        }
        c = SessionCaptcha("https://auth.roblox.com/v2/signup", data=JSONSignup,
                    Headers={"Accept": "application/json", "x-csrf-token": requests.post(
                        'https://auth.roblox.com/v1/usernames/validate'
                    ).headers['x-csrf-token']},session=session,WaitAfterComplete=WaitAfterCaptcha)

        def MakePost():
            post = session.post("https://auth.roblox.com/v2/signup",
                                 headers={"Accept": "application/json", "x-csrf-token": requests.post(
                                     'https://auth.roblox.com/v1/usernames/validate'
                                 ).headers['x-csrf-token']}, json=JSONSignup)
            return post

        a = MakePost()
        b = a.json()['failureDetails'][0]['fieldData']
        if b:
            print("Captcha is required!")
            td = c.GetDetailsFromFieldData(b)
            f = c.StartSessionFromDetails(td['TokenID'], td['location'])
        print('Cookies = ')
        for cookie in session.cookies:
            print(cookie)
        return f.json(),{"Username":Username,'Password':password}
        #details = c.GetDetails()
        #c.StartSession()
        #print(c.Token, c.ID)
