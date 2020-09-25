from sqlalchemy import Column, Integer, String

from run import db

class Document(db.Model):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String)
    text = Column(String, nullable=False)
    string = Column(String)