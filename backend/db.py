import motor.motor_asyncio
from decouple import config

client = motor.motor_asyncio.AsyncIOMotorClient(config('MONGODB_URL'))
db = client.get_database("social_media")

user_collection = db.get_collection("users")
post_collection = db.get_collection("posts")