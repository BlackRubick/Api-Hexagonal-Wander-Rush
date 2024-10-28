from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from infrastructure.db.database import engine, Base
from core.models.user import User
from core.routes import user_routes  # Asegúrate de que `user_routes` está bien importado

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar esto según el dominio permitido en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creación de tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inclusión de rutas de usuario
app.include_router(user_routes.router)

# Manejo de excepciones genéricas
@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": str(exc)})

# Ruta básica de prueba
@app.get("/")
async def read_root():
    return {"message": "API está funcionando correctamente"}
