from flask import Flask, render_template, redirect
app = Flask(__name__)

info_me = {
    'Name': 'Phan Anh',
    'Age': '22',
    'School': 'Foreign Trade University',
    'Hobbies': 'Listening to music',
    'Pet': 'Micky'
}

@app.route('/about-me')
def about_me():
    return render_template('info_me.html',INFO=info_me)

@app.route('/school')
def school():
    return redirect('http://techkids.vn')


if __name__ == '__main__':
    app.run(debug=True)