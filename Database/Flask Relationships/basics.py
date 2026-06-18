from models import db, Puppy, Owner, Toy, app

with app.app_context():

    # run once
    # db.create_all()

    z = Puppy("z")
    chester = Puppy("chester")

    db.session.add_all([z,chester])
    db.session.commit()

    print(Puppy.query.all())

    z = Puppy.query.filter_by(name="z").first()

    jr = Owner("jr", z.id)

    # give toys

    toy1 = Toy("Chew Toy", z.id)
    toy2 = Toy("Ball", z.id)

    db.session.add_all([jr,toy1, toy2])

    db.session.commit()

    z = Puppy.query.filter_by(name="z").first()

    print(z.report_toys())