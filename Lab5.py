import sqlite3
def print_table(cursor, table_name):
   try:
       print(f"\n\nShowing the table '{table_name}'\n")
       for row in cursor.execute(f'SELECT * FROM {table_name};'):
           print(row)
   except sqlite3.OperationalError as e:
       print(f"Error: {e}")
def main():
   try:
       con = sqlite3.connect("PostLab3_grp9.db")
       cur = con.cursor()
       table_names = ["GUIDE", "TRIP", "CUSTOMER", "RESERVATION"]
       for table_name in table_names:
           print_table(cur, table_name)
   except sqlite3.Error as e:
       print(f"Database error: {e}")
   finally:
       if con:
           con.close()
if __name__ == "__main__":
   main()
