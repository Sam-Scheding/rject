from rject.packed import Component, Elem, packed

class ToDoItem(Component):

   def render(self):
      return Elem(
        'li',
        {
            'class': self.props['class'],
        },
        self.props['text'],
    )

@packed
def todo_item(self):
    text = 'get milk'
    return Elem(
        ToDoItem,
        {
            'text': text,
        },
    )
