from app import db


class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    login = db.Column(db.String())
    password = db.Column(db.String())
    my_donations = db.relationship('DonationObject', backref='person', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name

        }


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    # one-many-relationship
    donation_objects = db.relationship('DonationObject', backref='category', lazy=True)

    def __init__(self, name, description):
        self.description = description
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description

        }


class DonationObject(db.Model):
    __tablename__ = 'donation_objects'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    quantity = db.Column(db.Integer())

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),
                            nullable=False)

    person = db.relationship('Person', backref='donation_objectgory', lazy=True)


    def __init__(self, description, quantity, category_id):
        self.description = description
        self.quantity = quantity
        self.category_id = category_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'quantity': self.quantity,
            'category_id': self.category_id

        }


class States(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


myDonations = db.Table('my_donations',
                       db.Column('persons_id', db.Integer, db.ForeignKey('persons.id'), primary_key=True),
                       db.Column('donations_objects.id', db.Integer, db.ForeignKey('donation_objects.id')))

donationState = db.Table('donation_sate',
                        db.Column('donations_objects.id', db.Integer, db.ForeignKey('donation_objects.id')),
                        db.Column('states_id', db.Integer, db.ForeignKey('states.id')),
                        db.Column('date_change', db.DateTime(), ))
