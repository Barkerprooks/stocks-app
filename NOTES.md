# Classes
## the blueprints of code
We have talked about variables, which are like nouns. They are things. Functions are like verbs, they do things.

Somtimes its useful to group a bunch of variables and functions in order to represent something greater

This is why we have classes
```python

name_jeff = 'jeff'
sid_jeff = '111223'
color_jeff = 'blue'

name_sue = 'sue'
sid_sue = '111224'
color_sue = 'pink'

# we can create a blueprint for the pattern above
class Student:

    # the init method is responsible
    # for setting up a new class OBJECT
    def __init__(self, name, sid, color):
        self.name = name
        self.sid = sid
        self.color = color

    def show_fav_color(self):
        print(self.color)

# create a new object like so:
student = Student('bob', 'blue')
student.show_fav_color()
```

# SQL
```sql
-- creates a table called 'users', gives them
-- two fields "username" and "md5sum" which are
-- both strings
CREATE TABLE users (username TEXT, md5sum TEXT); 

-- inserts data into the table as rows
INSERT INTO users VALUES ('username', 'password');
```