import uvicorn
import threading
import sys
import os
from fastapi import FastAPI


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir) 

from core.config import settings
from infraestructura.api.user_api import router as user_router
from infraestructura.api.pedido_api import router as pedido_router

app_usuarios = FastAPI(title="Microservicio de Usuarios")
app_pedidos = FastAPI(title="Microservicio de Pedidos")

app_usuarios.include_router(user_router)
app_pedidos.include_router(pedido_router)

def run_user_service():
    print(f"--- Servidor de Usuarios iniciado en http://localhost:{settings.user_service_port} ---")
    uvicorn.run(app_usuarios, host="0.0.0.0", port=settings.user_service_port)

def run_pedido_service():
    print(f"--- Servidor de Pedidos iniciado en http://localhost:{settings.pedido_service_port} ---")
    uvicorn.run(app_pedidos, host="0.0.0.0", port=settings.pedido_service_port)

if __name__ == "__main__":
  
    thread_users = threading.Thread(target=run_user_service)
    thread_pedidos = threading.Thread(target=run_pedido_service)
    
    thread_users.start()
    thread_pedidos.start()

    thread_users.join()
    thread_pedidos.join()