
from schemas.movie import Movie

from models.movie import Movie as Movie_Model



class MovieService(object):
    def __init__(self,db) :
        self.db = db

    
    def get_movies(self):
         result= self.db.query(Movie_Model).all()
         return result
     
    def get_movie(self,id):
         result= self.db.query(Movie_Model).filter(Movie_Model.id==id).first()
         
         return result
    
    def get_movie_category(self,category):
        result= self.db.query(Movie_Model).filter(Movie_Model.category==category).all()
        return result
    
    def create_movie(self,movie:Movie):
        new_movie =Movie_Model(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def update_movie(self,id:int,data:Movie):

        movie=self.db.query(Movie_Model).filter(Movie_Model.id==id).first()
        
        movie.title=data.title
        movie.overview=data.overview
        movie.year=data.year
        movie.rating=data.rating
        movie.category=data.category
        self.db.commit()
        return 
    def delete_movie(self, id: int):
        result = self.db.query(Movie_Model).filter(Movie_Model.id == id).first()
        self.db.delete(result)
        self.db.commit()



        
        


    
    
