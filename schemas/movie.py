
from pydantic import BaseModel
from typing import Optional




class Movie(BaseModel):
    id: Optional[int] = None
    title:str
    overview:str
    year:int 
    rating:float
    category:str





        #Valores por defecto 
    class Config:
        schema_extra = {
            
            
            "example":{
                "title": "Avatar33",
                "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...sdfsd",
                "year": 2009,
                "rating": 7.8,
                "category": "Comedia"

            }
         }
