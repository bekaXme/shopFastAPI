from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from datetime import date
from app.database import SessionLocal
from app.dependencies import get_current_admin
from app.models.order import Order
from app.models.user import User

router = APIRouter(prefix="/api/v1/stats", tags=["Stats"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_statistics(db: Session = Depends(get_db), _: User = Depends(get_current_admin)):
    total_orders = db.query(Order).count()
    paid_orders = db.query(Order).filter(Order.payment_status == "to‘landi").count()
    total_revenue = db.query(func.count(Order.id) * 100000).scalar()  # if each order = 100k so‘m (mock)

    today_orders = db.query(Order).filter(func.date(Order.id) == date.today()).count()

    top_users = (
        db.query(Order.user_id, func.count(Order.id).label("order_count"))
        .group_by(Order.user_id)
        .order_by(desc("order_count"))
        .limit(3)
        .all()
    )

    return {
        "total_orders": total_orders,
        "paid_orders": paid_orders,
        "total_revenue": total_revenue,
        "today_orders": today_orders,
        "top_users": [{"user_id": u[0], "order_count": u[1]} for u in top_users]
    }
