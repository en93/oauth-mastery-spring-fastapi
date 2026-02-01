import uvicorn
import os
from pathlib import Path

if __name__ == "__main__":
    # Force the working directory to be the folder containing this script
    os.chdir(Path(__file__).resolve().parent)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
