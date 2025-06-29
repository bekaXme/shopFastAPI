from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    address = Column(String)
    status = Column(String, default="yangi")  # yangi, tayyorlanmoqda, jo‘natildi, yetkazildi
    payment_status = Column(String, default="kutmoqda")  # to‘landi, kutmoqda
