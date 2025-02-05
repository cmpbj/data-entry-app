from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import Column, String, Text, Integer
import streamlit as st

POSTGRES_DATABASE_URL = "postgresql://myuser:mypassword@postgres/mydatabase"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def main():
    st.title('Data Entry App')
    Base.metadata.create_all(engine)

    data = st.text_input(label='Insert your data here', max_chars=100)
    buttom = st.button(label='Submit')

    if buttom:
        if data is not None:
            db = next(get_db())
            insert_message(db=db, message=data)
            all_messages = get_message(db=db)
            for message in all_messages:
                st.write(message.message)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class MessageModel(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(Text)

def insert_message(db: Session, message: str):
    new_message = MessageModel(message=message)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)

def get_message(db: Session):
    return db.query(MessageModel).all()


if __name__ == "__main__":
    main()