from beanie import init_beanie
import asyncio
import motor.motor_asyncio
from authx import Authentication, MongoDBBackend

from server.models.user import User
from server.models.review import ProductReview

from decouple import config


DATABASE_URL = config("DATABASE_URL")

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
    db_name = client['foodreviewapp']

    await init_beanie(database=db_name, document_models=[User, ProductReview])

