import logging

SECRET_KEY = "09027e5d4c40783326cef1ee95c179c7dcaa4c92e90844c1c1958b027546d240"
REFRESH_SECRET_KEY = "b92bb176d0c75d87efce31a3f4c472b3648d6e63d4b6a349802f712ba4422489"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24*7 # 1 day
REFRESH_TOKEN_EXPIRE_DAYS = 60*24*7 # 7 days


# Set up basic logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
