from hoso import application_control

def test_login():
    pass

def test_login_wronguser():
    pass

def test_login_wrongpass():
    pass

def test_register():
    pass

def test_register_existing_user():
    pass

def test_get_all_channels():
    pass

def test_select_channels():
    pass

def test_view_selected_channels():
    application_control.selected_channels = ['Twitter','Facebook']
    view_channels = application_control.view_selected_channels()
    assert application_control.selected_channels == view_channels

def test_deselect():
    selected_channels = ['Twitter', 'Facebook', 'Mail']
    application_control.selected_channels = ['Twitter', 'Facebook', 'Mail']
    application_control.deselect('Mail')
    selected_channels.remove('Mail')
    assert application_control.selected_channels == selected_channels
    

def test_deselect_notesxisting():
    pass
