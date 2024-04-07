from datetime import datetime
from typing import List, Union
from unittest.mock import Base

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str 


external_data = {
    'id': '123',
    'signup_ts': '2017-06-01 12:22',
    'friends': [1, '2', b'3'], 
}
