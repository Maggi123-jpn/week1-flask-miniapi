from backend.main import db, app

# Jalankan dalam application context
with app.app_context():
    db.create_all()
    print("Database tables created.")