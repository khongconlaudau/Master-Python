class Text(str):
    def duplicate(self):
        return self + self

class TrackableList(list):
    def append(self, item):
        print("Append called")
        super().append(item)


text = Text("Python")
print(text.duplicate())

list = TrackableList()
list.append(text)