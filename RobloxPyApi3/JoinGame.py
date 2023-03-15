from RobloxPyApi3 import Client
import subprocess
from .Errors import JoinGameFailed,NoRobloxProcessFound
import random
import RobloxPyApi3
import psutil
def FindRobloxLauncherProcess():
    processName = "RobloxPlayerBeta"

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess) as a:
            raise NoRobloxProcessFound("RobloxPlayerBeta")
    return False;
def JoinGame(cookie, gameId=int, showErrors=bool):
    try:
        x_csrf_token = RobloxPyApi3.Get_Authentication_ticket(cookie=cookie,gameid=gameId,showErrors=showErrors)
        browserId = random.randint(1000000, 10000000)
        #os.chdir("C:\\Program Files (x86)\\Roblox\\Versions")
        subprocess.run(f'start roblox-player:1+launchmode:play+gameinfo:{x_csrf_token}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:',shell=True)
        return 200
    except Exception as error:
        if showErrors:
            raise JoinGameFailed(f"During the command execution, an error has been accrued, Exception: {error} ")
        else:
            return

def JoinServerWithLocateName(cookie, gameId=int, showErrors=bool):
    try:
        x_csrf_token = RobloxPyApi3.Get_Authentication_ticket(cookie=cookie,gameid=gameId,showErrors=showErrors)
        browserId = random.randint(1000000, 10000000)
        #os.chdir("C:\\Program Files (x86)\\Roblox\\Versions")
        subprocess.run(f'start roblox-player:1+launchmode:play+gameinfo:{x_csrf_token}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:',shell=True)
        return 200
    except Exception as error:
        if showErrors:
            raise JoinGameFailed(f"During the command execution, an error has been accrued, Exception: {error} ")
        else:
            return

