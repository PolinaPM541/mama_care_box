from app.dao.base import BaseDao
from models.user import User


class UsersDao(BaseDao):
    model = User