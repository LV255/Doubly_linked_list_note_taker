# create the node class
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    # next node
    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    # previous node
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    # value
    def get_value(self):
        return self.value


# create the doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node == None:
            self.head_node = new_tail

    def delete_note(self, note_to_remove):
        global currently_viewed

        if (note_to_remove == self.head_node) and (note_to_remove == self.tail_node):
            print("removing head and tail")
            self.head_node = None
            self.tail_node = None
            currently_viewed = None

        elif note_to_remove == self.head_node:
            print("delete head note")
            removed_node = self.head_node
            self.head_node = removed_node.get_next_node()

            if self.head_node != None:
                self.head_node.set_prev_node(None)

            currently_viewed = self.head_node

        elif note_to_remove == self.tail_node:
            print("delete tail note")

            removed_node = self.tail_node
            self.tail_node = removed_node.get_prev_node()

            if self.head_node != None:
                self.tail_node.set_next_node(None)

            currently_viewed = self.tail_node

        else:
            print("delete middle node")

            next_node = note_to_remove.get_next_node()
            prev_node = note_to_remove.get_prev_node()

            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

            currently_viewed = prev_node


# create notes list
notes = DoublyLinkedList()

# organise currently viewed note
currently_viewed = None

# view next node
def change_viewing_note():
    global currently_viewed
    if currently_viewed.get_next_node() != None:
        currently_viewed = currently_viewed.get_next_node()
    else:
        print()
        print("No more notes")

# view previous node
def change_viewing_note2():
    global currently_viewed
    if currently_viewed.get_prev_node() != None:
        currently_viewed = currently_viewed.get_prev_node()
    else:
        print()
        print("No more notes")

# add a new note
def add_new_note():
    global currently_viewed
    print()
    x = input("Please enter text: ")
    notes.add_to_head(x)
    if currently_viewed == None:
        currently_viewed = notes.head_node


# main program loop
program_running = True

while program_running == True:

    if notes.head_node != None and currently_viewed != None:
        print()
        print(" ### Note viewer ### ")
        print()
        print(currently_viewed.value)
        print()

    if notes.head_node == None:
        print()
        print("Welcome to note taker")
        print()
        print("Please add your first note")
        add_new_note()
    else:
        print("Options: write a new note(w), delete current note(d), view next note(n), view previous note(p), exit(x)")
        choice = input("Type a letter and press enter: ")
        if choice.lower().strip() == "w":
            add_new_note()
        if choice.lower().strip() == "d":
           notes.delete_note(currently_viewed)
        if choice.lower().strip() == "n":
            change_viewing_note2()
        if choice.lower().strip() == "p":
            change_viewing_note()
        if choice.lower().strip() == "x":
            program_running = False





