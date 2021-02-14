import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(identifier=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, home, mobile, work, phone2, email, email2, "
                           "email3, address from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, home, mobile, work, phone2, email, email2, email3, address) = row
                list.append(Contact(identifier=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    telephone_home=home, telephone_mobile=mobile, telephone_work=work,
                                    telephone_secondary=phone2, email1=email, email2=email2, email3=email3,
                                    address_company=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
