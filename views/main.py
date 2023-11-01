from .IndexView import IndexView


class View:
    def __init__(self):
        self.current_view = None
        self.views = {
            'index': IndexView()
        }

    def bind(self, controller):
        self.views['index'].bind(controller)

    def ui(self, name: str):
        return self.views[name].ui

    def switch(self, name, hide=False):
        new_view = self.views[name]

        if self.current_view is not None:
            if hide:
                self.current_view.hide()
            else:
                self.current_view.destroy()

        self.current_view = new_view
        self.current_view.show()

    def start(self):
        self.switch('index')
