from app import app, db
with app.app_context():
    # Create database tables
    db.create_all()
app.run(debug=True)
