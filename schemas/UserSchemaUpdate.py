from pydantic import BaseModel
from typing import  Optional

class User(BaseModel):
     
      nameUser: str

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        "nameUser": "Oscar Lopez"
                        }
                  ]
            }
      }