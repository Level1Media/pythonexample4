from app import app,db
import os
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)
