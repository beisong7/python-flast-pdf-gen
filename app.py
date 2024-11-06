from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv("FLASK_PORT", 5000)) 
    app.run(debug=True, port=port, host="0.0.0.0")