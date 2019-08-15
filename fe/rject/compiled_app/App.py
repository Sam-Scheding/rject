from rject.packed import Component, Elem, packed
import requests, json

BASE_URL = "http://localhost:8000/api/todo"

@packed
def app():
    return(
        Elem(
            'div',
            {
                'class': 'container-fluid',
            },
            ' ',
            Elem(
                'div',
                {
                    'class': 'row',
                },
                ' ',
                Elem(ToDoForm),
                ' ',
                Elem(ToDoContainer),
                ' ',
                Elem(PrintButton),
                ' ',
                Elem(GETButton),
                ' ',
            ),
            ' ',
        )
    )

class ToDoForm(Component):

    def render(self):
        return(
            Elem(
                'div',
                {
                    'class': 'col-md-6',
                },
                ' ',
                Elem(
                    'form',
                    {
                        'class': 'form-inline',
                    },
                    ' ',
                    Elem(
                        'label',
                        {
                            'class': 'sr-only',
                        },
                        'Email',
                    ),
                    ' ',
                    Elem(
                        'input',
                        {
                            'type': 'text',
                            'id': 'form_text_input',
                            'class': 'form-control-plaintext',
                            'placeholder': 'Enter a to do',
                        },
                    ),
                    ' ',
                    Elem(SubmitButton),
                    ' ',
                ),
                ' ',
            )
        )

class SubmitButton(Component):

    def render(self):
        return(
            Elem(
                'input',
                {
                    'type': 'button',
                    'id': 'form_submit',
                    'class': 'btn btn-primary mb-2',
                    'value': 'Add',
                },
            )
        )

class ToDoContainer(Component):

    def render(self):
        return(
            Elem(
                'div',
                {
                    'class': 'col-md-6',
                },
                ' ',
                Elem(ToDoList),
                ' ',
            )
        )


class ToDoList(Component):

    to_do_items = []

    # Populate the todo array with items from the api
    def prerender(self):
        r = requests.get(BASE_URL)
        todos = json.loads(r.content)
        self.to_do_items += todos

    def render(self):
        self.prerender()

        if self.to_do_items:
            todos = list(map(self.to_link, self.to_do_items))

            return(
                Elem(
                    'ul',
                    {
                        'class': 'list-group',
                    },
                    ' ',
                    todos,
                    ' ',
                )
            )
        return(Elem('ul'))

    def to_link(self, to_do_item):

        return (Elem(
            ToDoItem,
            {
                'item': to_do_item['text'],
            },
        ) )

class ToDoItem(Component):

    def render(self):

        item = self.props['item']
        return (
            Elem(
                'li',
                {
                    'class': 'list-group-item',
                },
                ' ',
                item,
                ' ',
                Elem(
                    'input',
                    {
                        'type': 'button',
                        'id': 'delete_button',
                        'class': 'btn btn-primary mb-2',
                        'value': 'Delete',
                    },
                ),
                ' ',
            )
        )

#################################
#
#    Below are some examples that I thought were interesting
#
#################################
class GETButton(Component):

    def render(self):
        return(
            Elem(
                'input',
                {
                    'type': 'button',
                    'id': 'GET_button',
                    'class': 'btn btn-primary mb-2',
                    'value': 'GET',
                },
            )
        )

class PrintButton(Component):

    def render(self):
        return(
            Elem(
                'input',
                {
                    'type': 'button',
                    'onclick': 'print()',
                    'id': 'print_button',
                    'class': 'btn btn-primary mb-2',
                    'value': 'Print',
                },
            )
        )
