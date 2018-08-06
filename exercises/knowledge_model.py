from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'Knowledge'
    t_id = Column(Integer, primary_key=True)
    topic= Column(String)
    title= Column(String)
    rating=Column(Integer)


    def __repr__(self):
		if self.rating>6:
	   		return ("id: {}\n"
				   	"if you want to learn about: {}\n"
			  		"you should look at the Wikipedia article called: {} \n"
			   		"We gave this article a rating of {}").format(
						self.t_id, self.topic, self.title, self.rating)
		else:
			return ("id: {}\n"
					"if you want to learn about: {}\n"
					"you should look at the Wikipedia article called: {} \n"
					"We gave this article a rating of {}\n " 
					"unfortunatly , this article does not have a better rating. Maybe, this is an article that should be replaced soon").format(
						self.t_id, self.topic, self.title, self.rating)

x=Knowledge(t_id=1 , topic="sport" , title="real", rating=6)
print(x)
