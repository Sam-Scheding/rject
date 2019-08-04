import os, re
from .packed import compile, Component

class Rject():

    def __init__(self, src, dest='fe/rject/compiled_app/', title='Rject'):
        self.src = src
        self.dest = dest
        self.title = title

    def render(self):
        # from packed
        compile(self.src, self.dest) # Creates a compiled app, which we can now import
        from .compiled_app.App import app
        content = app()
        return self.render_template(self.title, content)

    def render_template(self, title, content):

        with open(os.path.join('fe', 'rject', 'templates', 'index.html')) as f:
            template = ''.join(f.readlines())
            template = re.sub('{{ *title *}}', title, template, flags=re.MULTILINE)
            template = re.sub('{{ *content *}}', content, template, flags=re.MULTILINE)
            return template
