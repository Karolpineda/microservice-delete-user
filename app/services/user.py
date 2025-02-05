# app/services/user.py
from sqlalchemy.orm import Session
from app.models.user import User


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

# Función para actualizar un usuario
def delete_user(db: Session, user_id: str):
    # Buscar el usuario en la base de datos por su ID
    user = db.query(User).filter(User.id == user_id).first()
    
    if user:
        db.delete(user)  # Eliminar el usuario
        db.commit()  # Guardar los cambios
        return True
    return False