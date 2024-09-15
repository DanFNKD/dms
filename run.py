import os
from taskmanager import app

print(f"App object: {app}")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )