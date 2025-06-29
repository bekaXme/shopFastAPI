from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderOut, OrderStatusUpdate
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/v1/order", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from app.dependencies import get_current_admin

@router.get("/admin", response_model=list[OrderOut])
def get_all_orders_admin(db: Session = Depends(get_db), _: User = Depends(get_current_admin)):
    return db.query(Order).all()

@router.patch("/admin/{order_id}/status", response_model=OrderOut)
def update_order_status(order_id: int, status_data: OrderStatusUpdate,
                        db: Session = Depends(get_db), _: User = Depends(get_current_admin)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = status_data.status
    db.commit()
    db.refresh(order)
    return order


@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_order = Order(user_id=current_user.id, address=order.address)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/", response_model=list[OrderOut])
def get_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Order).filter(Order.user_id == current_user.id).all()

