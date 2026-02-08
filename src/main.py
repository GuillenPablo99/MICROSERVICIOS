import uvicorn
import threading
import sys
import os

# Asegurar que Python encuentre los módulos en la carpeta src
# Esto es vital para que los "import src..." no fallen
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from core.config import settings
from infraestructura.api.user_api import router as user_router
from infraestructura.api.pedido_api import router as pedido_router

# 1. Creamos las dos aplicaciones de FastAPI
app_usuarios = FastAPI(title="Microservicio de Usuarios")
app_pedidos = FastAPI(title="Microservicio de Pedidos")

# 2. IMPORTANTE: Conectar las rutas (routers) a sus aplicaciones correspondientes
app_usuarios.include_router(user_router)
app_pedidos.include_router(pedido_router)

# Función para lanzar el microservicio de Usuarios en el puerto 8001
def run_user_service():
    print(f"--- Servidor de Usuarios iniciado en http://localhost:{settings.user_service_port} ---")
    uvicorn.run(app_usuarios, host="0.0.0.0", port=settings.user_service_port)

# Función para lanzar el microservicio de Pedidos en el puerto 8002
def run_pedido_service():
    print(f"--- Servidor de Pedidos iniciado en http://localhost:{settings.pedido_service_port} ---")
    uvicorn.run(app_pedidos, host="0.0.0.0", port=settings.pedido_service_port)

if __name__ == "__main__":
    # Usamos hilos (threading) para correr ambos servidores al mismo tiempo
    # tal como se mostró en la clase para simular microservicios independientes
    thread_users = threading.Thread(target=run_user_service)
    thread_pedidos = threading.Thread(target=run_pedido_service)
    
    # Iniciamos ambos hilos
    thread_users.start()
    thread_pedidos.start()

    # Mantenemos el hilo principal vivo
    thread_users.join()
    thread_pedidos.join()