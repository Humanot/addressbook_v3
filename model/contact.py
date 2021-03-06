from sys import maxsize

class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None,
                 company=None, address=None, homephone=None, mobile=None,
                 workphone=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, group=None, address2=None, homephone2=None,
                 notes=None, all_phones_from_homepage=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.group = group
        self.address2 = address2
        self.homephone2 = homephone2
        self.notes = notes
        self.all_phones_from_homepage = all_phones_from_homepage

    def __repr__(self):
        return f'<{self.id}:{self.firstname}, {self.lastname}>'

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize