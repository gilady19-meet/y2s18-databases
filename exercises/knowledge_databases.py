from knowledge_model import Base, Knowledge
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(title, topic, rating):
	article_object = Knowledge(
		title=title,
		topic=topic,
		rating=rating
		)
	session.add(article_object)
	session.commit()

add_article("real" , "sport" , 10)
add_article("spain" , "contries" , 7)

def query_all_articles():
   	article = session.query(
        Knowledge).all()
   	return article

print(query_all_articles())

def query_article_by_topic(topic):
   	article = session.query(Knowledge).filter_by(topic=topic).first()
   	return article


print(query_article_by_topic("contries"))

def query_article_by_rating(rating):
	article = session.query(Knowledge).filter_by(rating=rating).first()
   	return article

print(query_article_by_rating(10))

def query_article_by_primary_key(title):
	article = session.query(Knowledge).filter_by(title=title).first()
   	return article

print(query_article_by_primary_key("real"))


def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
