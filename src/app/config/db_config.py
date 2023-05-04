
# old confid for db
# import urllib
# USERNAME = urllib.parse.quote("st_admin")
# PASSWORD = urllib.parse.quote("Bvk@$*26t4sA9NT%")
# MONGODB_URI = "mongodb://"+USERNAME+":"+PASSWORD+"@3.110.249.2:27017"
# CYBER_INTEL_DB = "cyber_intel"

# new config for db

import os
from urllib.parse import quote_plus

from pydantic import BaseSettings, Field,  SecretStr

# 
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))

class Settings(BaseSettings):
    mongodb_username : str = Field(..., env="MONGODB_USERNAME")
    mongodb_password : SecretStr = Field(..., env="MONGODB_PASSWORD")
    mongodb_hostname : str = Field(..., env="MONGODB_HOST")
    mongodb_port : str = Field(..., env="MONGODB_PORT")
    mongodb_auth_source : SecretStr = Field(..., env="MONGODB_AUTH_SOURCE")
    
    app_path : str = Field(..., env="APPPATH")
    app_host : str = Field(..., env="APPHOST")
    app_port : int = Field(..., env="APPPORT")
    app_DEBUG : bool = Field(..., env="APPDEBUG")
    
    class Config:
        env_file = os.path.join(ROOT_DIR, '.env')
        env_prefix = ""
        case_sentive = False
        env_encoding = 'utf-8'
        

# PATHS
       
settings = Settings()

MONGODB_URI = f"mongodb://{settings.mongodb_username}:{quote_plus(settings.mongodb_password.get_secret_value())}@{settings.mongodb_hostname}:{settings.mongodb_port}/?authSource={settings.mongodb_auth_source.get_secret_value()}&readPreference=primary&directConnection=true&tls=false"
CYBER_INTEL_DB = "cyber_intel"

if __name__ == "__main__":
    print(ROOT_DIR)
    settings = Settings()
    print(settings.mongodb_hostname)
    print(settings.mongodb_port)
    mongodb_url = f"mongodb://{settings.mongodb_username}:{settings.mongodb_password.get_secret_value()}@{settings.mongodb_hostname}:{settings.mongodb_port}/?authSource={settings.mongodb_auth_source.get_secret_value()}&readPreference=primary&directConnection=true&tls=false"
    print(mongodb_url)