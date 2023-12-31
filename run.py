import os
import uvicorn
from main import app
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    port = int(os.getenv("PORT", 5050))
    uvicorn.run(app, port=port)
