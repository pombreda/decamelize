from app import db

class Person(db.Model):
    """ 
    Any one person tracked by the system is a person. 
    But, a victim/aggressor are only stored in the database by the event, not as an actual state.
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
 

class PhoneNumber(db.Model):
    """
    USA specific phone number format.
    """
    __tablename__ = 'PhoneNumbers'

    id = db.Column(db.Integer, primary_key=True)
    areaCode = db.Column(db.String(3))
    actualNumber = db.Column(db.String(7)) 
    extension = db.Column(db.String(10))

    person = db.Column(db.Integer, db.ForeignKey('People.id'))

    def __repr__(self):
        return '<PhoneNumber: %s-%s x.%s>' %(self.areaCode, self.actualNumber, self.extension)


class Address(db.Model):
    __tablename__ = 'Addresses'

    id = db.Column(db.Integer, primary_key=True)
    # composite of the following?
    streetNumber = db.Column(db.Integer)
    streetNumberSuffix = db.Column(db.String(10))
    streetName = db.Column(db.String(100))
    streetType = db.Column(db.String(10))
    streetDirection = db.Column(db.String(10))
    addressType = db.Column(db.String(100))
    addressTypeIdentfier = db.Column(db.String(100))
    minorMunicipality = db.Column(db.String(100))
    majorMunicipality = db.Column(db.String(100))
    governingDistrict = db.Column(db.String(100))
    postalArea = db.Column(db.String(100))
    country = db.Column(db.String(100))
    
    #relations
    people = db.Column(db.Integer, db.ForeignKey('People.id'))

    def __repr__(self):
        return "<address: 1>" 
    

#class PoliceOfficer(db.Model):
#    __tablename__ = 'Addresses'
#    id = db.Column(db.Integer, primary_key=True)

#class Judge(db.Model):
#    """ Extend the people table """
#    __tablename__ = 'Judges'
#    id = db.Column(db.Integer, primary_key=True)

#class Counselor(db.Model):
#    __tablename__ = 'Counselors'
#    id = db.Column(db.Integer, primary_key=True)
    
