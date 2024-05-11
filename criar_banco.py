from fakepinterest import database, app


from fakepinterest.models import Photo, Usuario



with app.app_context():
    database.create_all()
#database.drop_all()