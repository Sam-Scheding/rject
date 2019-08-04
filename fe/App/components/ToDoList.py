from rject.packed import Component, Elem, packed

class ToDoList(Component):

   def render(self):
      return <ul className={self.props['className']}></ul>

@packed
def todo_list(self):
    className = 'todo_list'
    return <ToDoList className={className} />
