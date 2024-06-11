from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Database credentials and connection string
server = 'demodbone.database.windows.net'
username = 'rakshit'
password = 'Canada@90'
database = 'firstdatabase'
driver = '{ODBC Driver 18 for SQL Server}'

def get_data():
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 * FROM Persons")  # Adjust query as needed
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    cursor.close()
    conn.close()
    # Return both rows and their corresponding column names
    return [dict(zip(columns, row)) for row in rows]

@app.route('/')
def index():
    data = get_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
