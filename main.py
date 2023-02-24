from fastapi import  FastAPI
from fastapi.responses import HTMLResponse



from routers.movie import movie_router
from routers.users import user_router


from config.database import engine,Base



from middlewares.error_handler import ErrorHandler




app= FastAPI()
app.title="Inventario de peliculas"
app.version="1.0"


app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)




@app.get("/",tags=["Home"])

def message():
    return HTMLResponse("<h1>Bienvenido a mi app</h1>")





     

    
    
   
       


