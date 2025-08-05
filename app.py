from flask import Flask, render_template, request, redirect, Response, flash, session
import csv, sqlite3


def init_db():
    conn=sqlite3.connect('database.db')
    cursor=conn.cursor()
    cursor.execute('''
                   create table if not exists feedback(
                   id integer primary key autoincrement,
                   name text not null,
                   email text not null,
                   rating integer not null,
                   comments text,
                   date_submitted timetamp default current_timestamp
                   )'''
                   )
    conn.commit()
    conn.close()


app=Flask(__name__)

app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-feedback', methods=['GET','POST'])
def submit_form():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['mail']
        rating=request.form['rating']
        comments=request.form['comments']
        conn=sqlite3.connect('database.db')
        cursor=conn.cursor()
        cursor.execute('''
                    insert into feedback(name,email,rating,comments)
                   values(?,?,?,?)''',(name,email,rating,comments))
        conn.commit()
        conn.close()
        
        flash("Feedback submitted successfully!", "success")

        return redirect('/')
    else:
        return render_template('index.html')





@app.route('/admin-dashboard')
def admin_dashboard():
    if not session.get('admin'):
        return redirect('/admin-login')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM feedback ORDER BY date_submitted DESC')
    feedback_list = cursor.fetchall()

    rating_count = {}
    for i in range(1, 6):
        cursor.execute("SELECT COUNT(*) FROM feedback WHERE rating=?", (i,))
        count = cursor.fetchone()[0]
        rating_count[i] = count

    cursor.execute("SELECT AVG(rating) FROM feedback")
    avg_rating = cursor.fetchone()[0]

    rating_counts = {str(k): v for k, v in rating_count.items()}
    conn.close()

    return render_template('admin.html',
                           feedback_list=feedback_list,
                           avg_rating=avg_rating,
                           rating_count=rating_count,
                           rating_counts=rating_counts)






@app.route('/export_csv')
def export_csv():
    conn = sqlite3.connect('database.db')  # your DB name
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM feedback")  # table name must match
    rows = cursor.fetchall()

    # Column names
    column_names = [description[0] for description in cursor.description]

    # CSV response
    def generate():
        data = [column_names] + rows
        for row in data:
            yield ','.join(str(item) for item in row) + '\n'

    return Response(generate(), mimetype='text/csv',
                    headers={"Content-Disposition": "attachment; filename=feedback.csv"})


ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect('/admin-dashboard')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')


    


if __name__=='__main__':
    init_db()
    app.run(debug=True)