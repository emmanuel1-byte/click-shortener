import dotenv
import jwt
import os
import datetime

dotenv.load_dotenv()


def create_access_token(userId):
    encoded = jwt.encode(
        {
            "sub": userId,
            "exp": datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(days=60),
        },
        os.getenv("JWT_SECRET"),
        algorithm="HS256",
    )
    return encoded
