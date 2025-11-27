#Aqui va el motor de datos -> SUPABASE
# Contiene:
# Configuración de conexión
# Inicialización del cliente
# Variables globales

from supabase import create_client
from app.core.config import SUPABASE_URL, SUPABASE_SERVICE_KEY

if not SUPABASE_SERVICE_KEY or not SUPABASE_URL:
  raise RuntimeError("Missing Supabase configuration in .env")

client_supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

