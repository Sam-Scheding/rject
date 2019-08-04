from rject.packed import Component, Elem, packed

@packed
def app():
    return(
        <div class="container-fluid">
            <div class="row">
                <ToDoForm />
                <ToDoContainer />
            </div>
        </div>
    )

class ToDoForm(Component):

    def render(self):
        return(
            <div class="col-md-6">
                <form class="form-inline">
                  <div class="form-group mb-6">
                    <label class="sr-only">Email</label>
                    <input type="text" class="form-control-plaintext" placeholder="Enter a to do" />
                  </div>
                  <button type="submit" class="btn btn-primary mb-2">Submit</button>
                </form>
            </div>
        )

class ToDoContainer(Component):

    def render(self):
        return(
            <div class="col-md-6">
                <ToDoList />
            </div>
        )


class ToDoList(Component):

    def render(self):
        to_do_items = ['to do 1', 'to do 2', 'to do 3']

        if to_do_items:
            todos = list(map(self.to_link, to_do_items))
        return(
            <ul class="list-group">
                {todos}
            </ul>
        )

    def to_link(self, to_do_item):

        return (<ToDoItem item={to_do_item} /> )

class ToDoItem(Component):

    def render(self):

        item = self.props['item']
        return (
            <li class="list-group-item">
                {item}
            </li>
        )
