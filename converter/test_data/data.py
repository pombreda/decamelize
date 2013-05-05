
class Person(db.Model):
    """ 
    Any one person tracked by the system is a person. 
    But, a victim/aggressor are only stored in the database by the event, not
    as an actual state.
    """
    __tablename__ = 'People'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    middleName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    email = db.Column(db.String(100))

    addresses = db.relationship('Address', backref='address', lazy='dynamic')
    phoneNumbers = db.relationship('PhoneNumber', backref='address', lazy='dynamic')

    def __repr__(self):
        return '<Person: %s %s>' %(self.firstName, self.lastName)
   
