from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user import delete_user
from app.database import get_db


router = APIRouter()
# Ruta Health para verificar si el microservicio está activo
@router.get("/health")
def health_check():
    return {"status": "Microservice Users is up and running"}


# Ruta para actualizar un usuario
@router.delete("/users/{user_id}")
def delete_user_endpoint(user_id: str, db: Session = Depends(get_db)):
    success = delete_user(db, user_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}
