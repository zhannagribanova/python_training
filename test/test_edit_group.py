from random import randint
from model.group import Group
from random import randrange
import allure


def test_edit_some_group_name(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(name='Test'))
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        index = randrange(len(old_groups))
    group = Group(name="New group "+str(randint(1, 1000)))
    # remember the identifier
    group.identifier = old_groups[index].identifier
    with allure.step('When I edit the group %s from the list' % group):
        app.group.edit_group_by_id(group.identifier, group)
    with allure.step('Then the new list of groups is equal to the old list with the replacement of the edited group'):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        # replace
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


"""
def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="New footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""