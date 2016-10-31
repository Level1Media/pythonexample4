from app import app
import os
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))