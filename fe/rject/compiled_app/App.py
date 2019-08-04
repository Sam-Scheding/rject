from rject.packed import Component, Elem, packed

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
                        'div',
                        {
                            'class': 'form-group mb-6',
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
                                'class': 'form-control-plaintext',
                                'placeholder': 'Enter a to do',
                            },
                        ),
                        ' ',
                    ),
                    ' ',
                    Elem(
                        'button',
                        {
                            'type': 'submit',
                            'class': 'btn btn-primary mb-2',
                        },
                        'Submit',
                    ),
                    ' ',
                ),
                ' ',
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

    def render(self):
        to_do_items = ['to do 1', 'to do 2', 'to do 3']

        if to_do_items:
            todos = list(map(self.to_link, to_do_items))
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

    def to_link(self, to_do_item):

        return (Elem(
            ToDoItem,
            {
                'item': to_do_item,
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
            )
        )
