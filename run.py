from app import app,db, manager
import os
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    # manager.run()
    app.run(debug=true)
