import uvicorn
from app.config.db_config import settings


if __name__ == "__main__":
    uvicorn.run(app=settings.app_path, host=settings.app_host, port=settings.app_port, reload=settings.app_DEBUG)