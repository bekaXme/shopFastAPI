from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.cart import CartItem
from app.schemas.cart import CartItemCreate, CartItemOut
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/v1/cart", tags=["Cart"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CartItemOut)
def add_to_cart(item: CartItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cart_item = CartItem(user_id=current_user.id, product_id=item.product_id, quantity=item.quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.get("/", response_model=list[CartItemOut])
def view_cart(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(CartItem).filter(CartItem.user_id == current_user.id).all()

