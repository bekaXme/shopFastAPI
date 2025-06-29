from pydantic import BaseModel

class OrderCreate(BaseModel):
    address: str
    
class OrderStatusUpdate(BaseModel):
    status: str  # yangi, tayyorlanmoqda, jo‘natildi, yetkazildi


class OrderOut(OrderCreate):
    id: int
    user_id: int
    status: str
    payment_status: str

    class Config:
        from_attributes = True
