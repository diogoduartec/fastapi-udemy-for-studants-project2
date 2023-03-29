from fastapi import FastAPI
from app.routes.category_routes import router as category_routes
from app.routes.product_routes import router as product_routes
from app.routes.user_routes import router as user_routes
from app.routes.poc import router as poc_routes


app = FastAPI()
@app.get('/health-check')
def health_check():
    return True

app.include_router(category_routes)
app.include_router(product_routes)
app.include_router(user_routes)
app.include_router(poc_routes)
