from rject.packed import Component, Elem, packed

class ToDoItem(Component):

   def render(self):
      return <li class={self.props['class']}>{self.props['text']}</li>

@packed
def todo_item(self):
    text = 'get milk'
    return <ToDoItem text={text} />
