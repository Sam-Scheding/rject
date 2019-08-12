from rject.packed import Component, Elem, packed
import requests, json

BASE_URL = "http://localhost:8000/api/todo"

@packed
def app():
    return(
        <div class="container-fluid">
            <div class="row">
                <ToDoForm />
                <ToDoContainer />
                <PrintButton />
                <GETButton />
            </div>
        </div>
    )

class ToDoForm(Component):

    def render(self):
        return(
            <div class="col-md-6">
                <form class="form-inline">
                    <label class="sr-only">Email</label>
                    <input type="text" id="form_text_input" class="form-control-plaintext" placeholder="Enter a to do" />
                    <SubmitButton />
                </form>
            </div>
        )

class SubmitButton(Component):

    def render(self):
        return(
            <input type="button" id="form_submit" class="btn btn-primary mb-2" value="Add" />
        )

class ToDoContainer(Component):

    def render(self):
        return(
            <div class="col-md-6">
                <ToDoList />
            </div>
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
                <ul class="list-group">
                    {todos}
                </ul>
            )
        return(<ul></ul>)

    def to_link(self, to_do_item):

        return (<ToDoItem item={to_do_item['text']} /> )

class ToDoItem(Component):

    def render(self):

        item = self.props['item']
        return (
            <li class="list-group-item">
                {item}
            </li>
        )

#################################
#
#    Below are some examples that I thought were interesting
#
#################################
class GETButton(Component):

    def render(self):
        return(
            <input type="button" id="GET_button" class="btn btn-primary mb-2" value="GET" />
        )

class PrintButton(Component):

    def render(self):
        return(
            <input type="button" onclick="print()" id="print_button" class="btn btn-primary mb-2" value="Print" />
        )
