from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import events

app = FastAPI(
    title="Events Map Visualizer API",
    description="API для додавання, перегляду і візуалізації подій на мапі",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events.router, prefix="/api/events", tags=["events"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)