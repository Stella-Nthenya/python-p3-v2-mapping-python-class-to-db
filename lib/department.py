from __init__ import CURSOR, CONN
#we have just imported there two objects


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        # we have just assigned a multiline string to the variable `sql`. 
        # The string contains the SQL code for creating a table named "departments".
        CURSOR.execute(sql) #executes the above sql command stored in sql variable. Using CURSOR object we have sent that to the db for execution

        CONN.commit() #the changes are not permanent so you must commit them in order to be saved permanently to the db.

#the code below drops/deletes the table if it exists in the db
    @classmethod
    def drop_table(cls): 
        # an sql command
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS departments;
            # if exists ensures that the command does not prod error if the table does not exist
        """
        CURSOR.execute(sql)
        CONN.commit()

    #inserts a new row into the departments table in our db
    def save(self):
        # a docstring explaining whats going to happen
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        """
        # sql variable stores the multiline string
        # the sql query inserts a new row with name and loc data into the dept table
        sql = """
            INSERT INTO departments (name, location)
            # below is a placeholder for preventing injection attacks
            VALUES (?, ?)
        """
        # this line executes the SQL query stored in the sql var above and passed two values as parameters to replace the placeholders in the query
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()


        # retrieves the id of the last inserted row from the database and updates the id attribute of the current Department instance with that value.
        # CURSOR.lastrowid is an attribute of the cursor object (CURSOR) that holds the value of the primary key (id in this case) of the last row inserted, if the database supports it.
        self.id = CURSOR.lastrowid


    @classmethod
    def create(cls, name, location):
        """ Initialize a new Department instance and save the object to the database """
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Update the table row corresponding to the current Department instance."""
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Department instance"""
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
