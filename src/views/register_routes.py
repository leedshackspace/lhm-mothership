from views.openbot import EntryView


def register_routes(app):
    app.add_url_rule("/openbot/entry", view_func=EntryView.as_view("Entry"))
    return app
