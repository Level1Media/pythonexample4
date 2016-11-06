from app import app,db, manager,sess
import os

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    sess.init_app(app)
    app.debug = True
    app.run()