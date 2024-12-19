from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('childcare.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS vaccines
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         name TEXT, 
                         date TEXT,  -- Changed to TEXT
                         dose INTEGER,
                         height REAL,  -- Changed to REAL
                         weight REAL,  -- Changed to REAL
                         aftereffects TEXT)''')

@app.route('/')
def home():
    with sqlite3.connect('childcare.db') as conn:
        vaccines = conn.execute('SELECT * FROM vaccines').fetchall()
    return render_template('vaccine.html', vaccines=vaccines)

@app.route('/add', methods=['POST'])
def add_vaccine():
    try:
        name = request.form['name']
        date = request.form['date']
        dose = int(request.form['dose'])
        height = float(request.form['height'])  
        weight = float(request.form['weight'])  
        aftereffects = request.form.get('aftereffects', 'Null')  
        with sqlite3.connect('childcare.db') as conn:
            conn.execute('INSERT INTO vaccines (name, date, dose, height, weight, aftereffects) VALUES (?, ?, ?, ?, ?, ?)', 
                         (name, date, dose, height, weight, aftereffects))
        return 'Vaccine details recorded successfully!'
    except Exception as e:
        return f'Error recording vaccine details: {e}', 400

@app.route('/update', methods=['POST'])
def update_vaccine():
    try:
        vaccine_id = int(request.form['id'])
        name = request.form['name']
        date = request.form['date']  
        dose = int(request.form['dose'])
        height = float(request.form['height'])  
        weight = float(request.form['weight'])  
        aftereffects = request.form['aftereffects']
        with sqlite3.connect('childcare.db') as conn:
            conn.execute('UPDATE vaccines SET name = ?, date = ?, dose = ?, height = ?, weight = ?, aftereffects = ? WHERE id = ?', 
                         (name, date, dose, height, weight, aftereffects, vaccine_id))
        return 'Vaccine details updated successfully!'
    except Exception as e:
        return f'Error updating vaccine details: {e}', 400

@app.route('/delete', methods=['POST'])
def delete_vaccine():
    try:
        vaccine_id = int(request.form['id'])
        with sqlite3.connect('childcare.db') as conn:
            conn.execute('DELETE FROM vaccines WHERE id = ?', (vaccine_id,))
        return 'Vaccine record deleted successfully!'
    except Exception as e:
        return f'Error deleting vaccine record: {e}', 400

@app.route('/search', methods=['GET'])
def search_vaccine():
    search_query = request.args.get('query', '')
    with sqlite3.connect('childcare.db') as conn:
        results = conn.execute('SELECT * FROM vaccines WHERE name LIKE ? OR date LIKE ?', 
                               (f'%{search_query}%', f'%{search_query}%')).fetchall()
    return jsonify(results)

if __name__ == '__main__':
    init_db()
    app.run(port=9001)
