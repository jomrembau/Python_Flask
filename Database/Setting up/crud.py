from main import app,db, Puppy

## CRUD

with app.app_context():

    ## Create
    my_puppy = Puppy("Rufus", 5)
    db.session.add(my_puppy)
    db.session.commit()

    ## Read

    all_puppies = Puppy.query.all()
    print(all_puppies)

    # Select by ID
    puppy_one = db.session.get(Puppy,1)
    print(puppy_one.name)

    #FILTERS
    puppy_frank = Puppy.query.filter_by(name="Frankie")
    print(puppy_frank.all())

    # UPDATE
    first_puppy = db.session.get(Puppy,1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    # Delete
    puppy_delete = db.session.query(Puppy).filter_by(name="Rufus").all()

    for puppy in puppy_delete:
        db.session.delete(puppy)

    db.session.commit()

    # Print all
    all_puppies = Puppy.query.all()
    print(all_puppies)