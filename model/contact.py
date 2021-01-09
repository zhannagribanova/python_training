from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None,
                 company=None, address_company=None, telephone_home=None, telephone_mobile=None, telephone_work=None,
                 fax=None, email1=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None,
                 aday=None, amonth=None, ayear=None, home_address=None, telephone_secondary=None, notes=None,
                 identifier=None, all_phones_from_home_page=None, all_email_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address_company = address_company
        self.telephone_home = telephone_home
        self.telephone_mobile = telephone_mobile
        self.telephone_work = telephone_work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.home_address = home_address
        self.telephone_secondary = telephone_secondary
        self.notes = notes
        self.identifier = identifier
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.identifier, self.firstname, self.middlename)

    def __eq__(self, other):
        return (self.identifier is None or other.identifier is None or self.identifier == other.identifier) \
               and self.firstname == other.firstname and self.middlename == other.middlename

    def id_or_max(self):
        if self.identifier:
            return int(self.identifier)
        else:
            return maxsize
