import requests
import random
import time
import webbrowser as WEB
 #5
class Captcha:
    def __init__(self,CaptchaRequiredRobloxAPI,data,Headers,WaitAfterComplete = 4.5):
        self.URL = CaptchaRequiredRobloxAPI
        self.Token = None
        self.ID = None
        self.blob = None
        self.TokenID = None
        self.Seconds = WaitAfterComplete
        self.TokenDetails = None
        self.location = None
        self.data: dict = data
        self.Headers = Headers
        self.AccessToken = requests.post(
                            'https://auth.roblox.com/v1/usernames/validate'
                        ).headers['x-csrf-token']
    def MakePost(self):
        post = requests.post(self.URL, headers=self.Headers, json=self.data)
        return post
    def GetDetailsFromFieldData(self,fieldData):
        try:

            _details_ = fieldData.split(',')
            self.ID = _details_[0]
            self.blob = _details_[1]
            if self.ID:
                pass
            else:
                print("Failed to get captcha ID.")
            if self.blob:
                pass
            else:
                print("Failed to get captcha BLOB")
            tokpost = requests.post(
                'https://roblox-api.arkoselabs.com/fc/gt2/public_key/A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',

                data={
                    'public_key': 'A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',
                    'userbrowser': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
                    'rnd': f'0.{random.randint(1000, 10000000)}',
                    'data[blob]': self.blob,
                    'language': 'en'
                }
            ).json()['token']
            if tokpost:
                self.Token = tokpost
                self.TokenDetails = self.Token.split('|')
                self.TokenID = self.TokenDetails[0]
                self.location = self.TokenDetails[1]
                return {"Token":self.Token,"TokenID":self.TokenDetails[0],'location':self.TokenDetails[1],"blob":self.blob,'id':self.ID}
            else:
                print("Failed to get captcha TOKEN")
        except Exception as error:
            print(error)
            return error
    def GetDetails(self):
        try:

            _details_ = self.MakePost().json()["failureDetails"][0]["fieldData"].split(',')
            self.ID = _details_[0]
            self.blob = _details_[1]
            if self.ID:
                pass
            else:
                print("Failed to get captcha ID.")
            if self.blob:
                pass
            else:
                print("Failed to get captcha BLOB")
            tokpost = requests.post(
                'https://roblox-api.arkoselabs.com/fc/gt2/public_key/A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',

                data={
                    'public_key': 'A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',
                    'userbrowser': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
                    'rnd': f'0.{random.randint(1000, 10000000)}',
                    'data[blob]': self.blob,
                    'language': 'en'
                }
            ).json()['token']
            if tokpost:
                self.Token = tokpost
                self.TokenDetails = self.Token.split('|')
                self.TokenID = self.TokenDetails[0]
                self.location = self.TokenDetails[1]
                self.StartSession()
                return self.Token
            else:
                print("Failed to get captcha TOKEN")
        except Exception as error:
            print(error)
            return error
    def StartSession(self):
        global t
        if self.TokenDetails:
            solver_url = f'https://roblox-api.arkoselabs.com/fc/gc/?token={self.TokenID}&{self.location}&lang=en&pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F&cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc'
            #print(
                #f'- Received Captcha Details!\n\n\nCaptchaId : {self.ID}\nCaptchaBlob : {self.blob}\nLocation : {self.location}\ntoken : {self.TokenID}\n\n\n(Starting selenium browser to solve the captcha)..\n\n\n')
            print("[INFO] Starting Web browser to solve the captcha.")
            time.sleep(1)
            WEB.open(solver_url)
            time.sleep(1)

            input("[ENTER] Please press Enter (return) after completing the captcha...")
            #input()
            #print("Finished")
            self.data.update({'captchaId': self.ID,
        "captchaProvider": "PROVIDER_ARKOSE_LABS",
        "captchaToken": str(self.Token)})
            print(self.data)
            time.sleep(self.Seconds)
            a = self.MakePost()
            return a
            #print(a.json())
            #input('')
    def StartSessionFromDetails(self,TokenId,Location,ID,blob):
        global t
        if TokenId:
            solver_url = f'https://roblox-api.arkoselabs.com/fc/gc/?token={TokenId}&{Location}&lang=en&pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F&cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc'
            #print(
               # f'- Received Captcha Details!\n\n\nCaptchaId : {ID}\nCaptchaBlob : {blob}\nLocation : {Location}\ntoken : {TokenId}\n\n\n(Starting selenium browser to solve the captcha)..\n\n\n')
            print("[INFO] Starting Web browser to solve the captcha.")
            time.sleep(1)
            WEB.open(solver_url)
            input('[ENTER] Please press Enter (return) after completing the captcha...')
            #input()
            #print("Finished")
            self.data.update({'captchaId': self.ID,
        "captchaProvider": "PROVIDER_ARKOSE_LABS",
        "captchaToken": str(self.Token)})
            print(self.data)
            time.sleep(self.Seconds)
            a = self.MakePost()
            return a
            #print(a.json())
            #input('')

class SessionCaptcha:
    def __init__(self,CaptchaRequiredRobloxAPI,data,Headers,session:requests.session,WaitAfterComplete = 4.5):
        self.URL = CaptchaRequiredRobloxAPI
        self.Token = None
        self.ID = None
        self.blob = None
        self.TokenID = None
        self.session = session
        self.Seconds = WaitAfterComplete
        self.TokenDetails = None
        self.location = None
        self.data: dict = data
        self.Headers = Headers
        self.AccessToken = requests.post(
                            'https://auth.roblox.com/v1/usernames/validate'
                        ).headers['x-csrf-token']
    def MakePost(self):
        post = self.session.post(self.URL, headers=self.Headers, json=self.data)
        return post
    def GetDetailsFromFieldData(self,fieldData):
        try:

            _details_ = fieldData.split(',')
            self.ID = _details_[0]
            self.blob = _details_[1]
            if self.ID:
                pass
            else:
                print("Failed to get captcha ID.")
            if self.blob:
                pass
            else:
                print("Failed to get captcha BLOB")
            tokpost = requests.post(
                'https://roblox-api.arkoselabs.com/fc/gt2/public_key/A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',

                data={
                    'public_key': 'A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',
                    'userbrowser': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
                    'rnd': f'0.{random.randint(1000, 10000000)}',
                    'data[blob]': self.blob,
                    'language': 'en'
                }
            ).json()['token']
            if tokpost:
                self.Token = tokpost
                self.TokenDetails = self.Token.split('|')
                self.TokenID = self.TokenDetails[0]
                self.location = self.TokenDetails[1]
                return {"Token":self.Token,"TokenID":self.TokenDetails[0],'location':self.TokenDetails[1],"blob":self.blob,'id':self.ID}
            else:
                print("Failed to get captcha TOKEN")
        except Exception as error:
            print(error)
            return error
    def GetDetails(self):
        try:

            _details_ = self.MakePost().json()["failureDetails"][0]["fieldData"].split(',')
            self.ID = _details_[0]
            self.blob = _details_[1]
            if self.ID:
                pass
            else:
                print("Failed to get captcha ID.")
            if self.blob:
                pass
            else:
                print("Failed to get captcha BLOB")
            tokpost = self.session.post(
                'https://roblox-api.arkoselabs.com/fc/gt2/public_key/A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',

                data={
                    'public_key': 'A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',
                    'userbrowser': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
                    'rnd': f'0.{random.randint(1000, 10000000)}',
                    'data[blob]': self.blob,
                    'language': 'en'
                }
            ).json()['token']
            if tokpost:
                self.Token = tokpost
                self.TokenDetails = self.Token.split('|')
                self.TokenID = self.TokenDetails[0]
                self.location = self.TokenDetails[1]
                self.StartSession()
                return self.Token
            else:
                print("Failed to get captcha TOKEN")
        except Exception as error:
            print(error)
            return error
    def StartSession(self):
        global t
        if self.TokenDetails:
            solver_url = f'https://roblox-api.arkoselabs.com/fc/gc/?token={self.TokenID}&{self.location}&lang=en&pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F&cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc'
            #print(
                #f'- Received Captcha Details!\n\n\nCaptchaId : {self.ID}\nCaptchaBlob : {self.blob}\nLocation : {self.location}\ntoken : {self.TokenID}\n\n\n(Starting selenium browser to solve the captcha)..\n\n\n')
            print("[INFO] Starting Web browser to solve the captcha.")
            time.sleep(1)
            WEB.open(solver_url)
            time.sleep(1)

            input("[ENTER] Please press Enter (return) after completing the captcha...")
            #input()
            #print("Finished")
            self.data.update({'captchaId': self.ID,
        "captchaProvider": "PROVIDER_ARKOSE_LABS",
        "captchaToken": str(self.Token)})
            print(self.data)
            time.sleep(self.Seconds)
            a = self.MakePost()
            return a
            #print(a.json())
            #input('')
    def StartSessionFromDetails(self,TokenId,Location):
        global t
        if TokenId:
            solver_url = f'https://roblox-api.arkoselabs.com/fc/gc/?token={TokenId}&{Location}&lang=en&pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F&cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc'
            #print(
               # f'- Received Captcha Details!\n\n\nCaptchaId : {ID}\nCaptchaBlob : {blob}\nLocation : {Location}\ntoken : {TokenId}\n\n\n(Starting selenium browser to solve the captcha)..\n\n\n')
            print("[INFO] Starting Web browser to solve the captcha.")
            time.sleep(1)
            WEB.open(solver_url)
            input('[ENTER] Please press Enter (return) after completing the captcha...')
            #input()
            #print("Finished")
            self.data.update({'captchaId': self.ID,
        "captchaProvider": "PROVIDER_ARKOSE_LABS",
        "captchaToken": str(self.Token)})
            print(self.data)
            time.sleep(self.Seconds)
            a = self.MakePost()
            return a
            #print(a.json())
            #input('')

