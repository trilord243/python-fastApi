from fastapi import APIRouter
from fastapi import Depends,Path
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,Field
from typing import Optional,List

from middlewares.jwt_bearer import JWTBearer


from config.database import Session
from models.movie import Movie as Movie_Model
from fastapi.encoders import jsonable_encoder
from services.movie import MovieService


from schemas.movie import Movie



movie_router = APIRouter()




@movie_router.get("/movies", tags=["Movies"],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer())])



def get_movies()->List[Movie]:
    db=Session()
    result=MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))
    

@movie_router.get("/movies/{id}", tags=["Movies"],response_model=List[Movie])

def get_movie(id:int=Path(ge=1,le=2000)) ->Movie:
    db=Session()
    result=MovieService(db).get_movie(id)

    return JSONResponse(content=jsonable_encoder(result))
    



@movie_router.get("/movies/",tags=["Movies"])

def get_movies_by_category(category: str):
    db=Session()
    result=MovieService(db).get_movie_category(category)
   
    return JSONResponse(content=jsonable_encoder(result))





@movie_router.post("/movies", tags=["Movies"],status_code=201)

def create_movie(movie: Movie):
    db=Session()
    MovieService(db).create_movie(movie)
    

    
    return JSONResponse(status_code=201,content={"message":"Movie created"})


@movie_router.put("/movies/{id}", tags=["Movies"],status_code=200)

def update_movie(id: int, movie: Movie):
    db=Session()
    result =MovieService(db).get_movie(id)
    if not result:
        JSONResponse(status_code=404,content={"message":"Movie not found"})

    MovieService(db).update_movie(id,movie)


    





        
@movie_router.delete("/movies/{id}", tags=["Movies"],status_code=200)

def delete_movie(id: int):
    db=Session()
    result=db.query(Movie_Model).filter(Movie_Model.id==id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message":"Movie not found"})
    result.delete(result)
    db.commit()
    
           