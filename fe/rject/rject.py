import os, re
from .packed import compile, Component

class Rject():

    def __init__(self, src, dest='fe/rject/compiled_app/'):
        self.src = src
        self.dest = dest

    def render(self):
        # from packed
        compile(self.src, self.dest) # Creates a compiled app, which we can now import
        from .compiled_app.App import app
        content = app()
        return content
