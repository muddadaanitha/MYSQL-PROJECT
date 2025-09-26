import mysql.connector as connector

class DBHelper:
    def __init__(self):
        try:
            self.con = connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='Anitha@123',
                database='TestPython'
            )
            self.cursor = self.con.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS user (
                userid INT PRIMARY KEY,
                username VARCHAR(100),
                phone VARCHAR(20)
            )
            """
            self.cursor.execute(query)
            print("Table 'user' created or already exists.")
        except connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            raise

    def insert_user(self, userid, username, phone):
        try:
            query = "INSERT INTO user (userid, username, phone) VALUES (%s, %s, %s)"
            values = (userid, username, phone)
            self.cursor.execute(query, values)
            self.con.commit()
            print("User saved successfully.")
        except connector.Error as err:
            print(f"Error inserting user: {err}")
            self.con.rollback()

    def fetch_all_users(self):
        try:
            query = "SELECT userid, username, phone FROM user"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            
            if not rows:
                print("No users found in the database.")
                return

            print("--- Users in the database ---")
            for row in rows:
                print(f"User ID: {row[0]}")
                print(f"User Name: {row[1]}")
                print(f"Phone No.: {row[2]}")
                print("-" * 25)
                
        except connector.Error as err:
            print(f"Error fetching users: {err}")

    def delete_user(self, userid):
        try:
            query = "DELETE FROM user WHERE userid = %s"
            self.cursor.execute(query, (userid,))
            self.con.commit()
            print(f"User with ID {userid} deleted successfully.")
        except connector.Error as err:
            print(f"Error deleting user: {err}")
            self.con.rollback()

    def update_user(self, userid, new_name, new_phone):
        try:
            query = "UPDATE user SET username = %s, phone = %s WHERE userid = %s"
            values = (new_name, new_phone, userid)
            self.cursor.execute(query, values)
            self.con.commit()
            print(f"User with ID {userid} updated successfully.")
        except connector.Error as err:
            print(f"Error updating user: {err}")
            self.con.rollback()

def main():
    db = DBHelper()
    while True:
        print("****WELCOME****")
        print("PRESS 1 TO INSERT NEW USER:")
        print("PRESS 2 TO DISPLAY ALL USERS:")
        print("PRESS 3 TO DELETE A USER:")
        print("PRESS 4 TO UPDATE A USER:")
        print("PRESS 5 TO EXIT PROGRAM:")
        print("-" * 25)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                userid = int(input("Enter User ID: "))
                username = input("Enter User Name: ")
                phone = input("Enter User Phone: ")
                db.insert_user(userid, username, phone)
            
            elif choice == 2:
                db.fetch_all_users()

            elif choice == 3:
                userid = int(input("Enter User ID to delete: "))
                db.delete_user(userid)
                
            elif choice == 4:
                userid = int(input("Enter User ID to update: "))
                new_username = input("Enter new User Name: ")
                new_phone = input("Enter new User Phone: ")
                db.update_user(userid, new_username, new_phone)
                
            elif choice == 5:
                print("Exiting program. Goodbye!")
                break
            
            else:
                print("Invalid Input... Please enter a number from 1 to 5.")
                
        except ValueError:
            print("Invalid Input... Please enter a number for the choice and ID.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()