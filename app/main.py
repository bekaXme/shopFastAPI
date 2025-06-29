from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, product, cart, order,stats  # Make sure these files exist

app = FastAPI(title="ShopTime API")

Base.metadata.create_all(bind=engine)

app.include_router(stats.router)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(cart.router)
app.include_router(order.router)

@app.get("/")
def root():
    return {"message": "Welcome to ShopTime"}
