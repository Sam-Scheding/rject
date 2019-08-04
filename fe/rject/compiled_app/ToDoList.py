from rject.packed import Component, Elem, packed

class ToDoList(Component):

   def render(self):
      return Elem(
        'ul',
        {
            'className': self.props['className'],
        },
    )

@packed
def todo_list(self):
    className = 'todo_list'
    return Elem(
        ToDoList,
        {
            'className': className,
        },
    )
