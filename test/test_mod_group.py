from model.group import Group


def test_modification_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Edit_New_group", header="Edit_Logo", footer="Edit_Comment"))
    app.session.logout()