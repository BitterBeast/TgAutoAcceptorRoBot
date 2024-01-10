from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "26182452"))
    API_HASH = getenv("API_HASH", "8fb0a5ecb53e81c7ab9198475658ca43")
    BOT_TOKEN = getenv("BOT_TOKEN", "6612576433:AAGmRGoCGG-YdWlMc_BuB03lmIV4IP1HYf0")
    FSUB = getenv("FSUB", "ZiB_BoTs")
    CHID = int(getenv("CHID", "-1001839696032"))
    SUDO = list(map(int, getenv("SUDO", "5343462550").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://A1:A1@cluster0.z34eekf.mongodb.net/?retryWrites=tue&w=majority")
    
cfg = Config()
