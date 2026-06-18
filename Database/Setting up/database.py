from main import app,db, Puppy

with app.app_context():
    db.create_all()

    sam = Puppy("Sammy", 3)
    frank = Puppy("Frankie", 4)

    # add all
    db.session.add_all([sam, frank])

    # add individually
    # db.session.add(sam)
    # db.session.add(frank)

    db.session.commit()

    print(sam.id)
    print(frank.id)