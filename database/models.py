from sqlalchemy import Column, Integer, String, Text
from database.base import Base

class UserResponse(Base):
    __tablename__ = 'user_responses'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=True)
    phone = Column(String(30), nullable=True)
    source = Column(String(50), nullable=True)
    concern = Column(Text, nullable=True)
    desired_activity = Column(String(50), nullable=True)
    gemini_recommendation = Column(Text, nullable=True)
    best_direction = Column(String(50), nullable=True)

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # Reference to the user
    amount = Column(Integer, nullable=False)  # Payment amount
    status = Column(String(20), nullable=False)  # Payment status (e.g., pending, completed)

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # Reference to the user
    date_time = Column(String(50), nullable=False)  # Appointment date and time
    confirmation_status = Column(String(20), nullable=False)  # Confirmation status (e.g., confirmed, pending)