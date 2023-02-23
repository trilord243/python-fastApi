from fastapi import Depends, FastAPI,Body, HTTPException,Query,Path,Request
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,Field
from typing import Optional,List
from jwt_manager import generate_token,validate_token
from fastapi.security import HTTPBearer


app= FastAPI()
app.title="Mi app es muy basada"
app.version="69.420"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth =await super().__call__(request)
        data=validate_token(auth.credentials)
        if data["email"]!="admin@example.com":
            raise HTTPException(status_code=403,detail="CREDENTIALS INVALID")



        
        
    

class User(BaseModel):
    email:str
    password:str

class Movie(BaseModel):
    id: Optional[int] = None
    title:str=Field(default="Bolas de toro",min_length=5, max_length=15)
    overview:str
    year:int =Field(Le=2022)
    rating:float
    category:str





        #Valores por defecto 
    class Config:
        schema_extra = {
            
            
            "example":{
                
                "id": 1,
                "title": "Avatar",
                "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
                "year": 2009,
                "rating": 7.8,
                "category": "Comedia"

            }
         }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } , 
    {
        'id': 2,
        'title': 'Hola',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'drama'    
    } , {
        'id': 3,
        'title': 'BOLAS',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'drama'    
    } ,
]

@app.get("/",tags=["Home"])

def message():
    return HTMLResponse("<h1>Bienvenido a mi app</h1>")

@app.post("/login",tags=["Login"],status_code=200)

def login(user:User) :
    if user.email == "admin@example.com" and user.password == "12":
        token:str=generate_token(user.dict())
    
        return JSONResponse(status_code=200,content=token)
    else:
        return JSONResponse(status_code=401,content={"message":"Usuario o contraseña incorrect"} )
    




@app.get("/movies", tags=["Movies"],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer())])



def get_movies()->List[Movie]:

    return JSONResponse(status_code=200,content=movies)

@app.get("/movies/{id}", tags=["Movies"],response_model=List[Movie])

def get_movie(id:int=Path(ge=1,le=2000)) ->Movie:

    for item in movies:
        if item['id'] == id:
            return JSONResponse(content=item)

    return JSONResponse(status_code=404,content={"message":"Movie not found"})


@app.get("/movies/",tags=["Movies"])

def get_movies_by_category(category: str):
    
    category_movies = [i for i in movies if i['category'] == category]
    return JSONResponse(content=category_movies)




@app.post("/movies", tags=["Movies"],status_code=201)

def create_movie(movie: Movie):

    movies.append(movie)
    return JSONResponse(status_code=201,content={"message":"Movie created"})


@app.put("/movies/{id}", tags=["Movies"],status_code=200)

def update_movie(id: int, movie: Movie):

    for i in movies:
        if i["id"]==id:
            i["title"]=movie.title
            i["overview"]=movie.overview
            i["year"]=movie.year
            i["rating"]=movie.rating
            i["category"]=movie.category
    return JSONResponse(status_code=200,content={"message":"Movie updated"})



        
@app.delete("/movies/{id}", tags=["Movies"],status_code=200)

def delete_movie(id: int):
     for i in movies:
        if i[id]==movies[id]:
           movies.remove(i)
        return JSONResponse(status_code=200,content={"message":"Movie deleted"})
           


     

    
    
   
       


