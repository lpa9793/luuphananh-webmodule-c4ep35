from flask import Flask, render_template
app = Flask(__name__)

user_list = {
    'phananh': {
        'Name': 'Luu Phan Anh',
        'Age': '22',
        'Gender': 'Female',
        'Hobby': 'Listening to music'
        },
    'truong': {
        'Name': 'Nguyen Hung Truong',
        'Age': '25',
        'Gender': 'Male',
        'Hobby': 'Playing games'
        },
    'hieu': {
        'Name': 'Trinh Thanh Hieu',
        'Age': '26',
        'Gender': 'Male',
        'Hobby': 'Reading books'
        }
}

@app.route('/user/<username>')
def user_details(username):
    if username not in user_list:
        return 'User not found'
    user = user_list[username]
    return render_template('user_details.html',USER=user)

if __name__ == '__main__':
    app.run(debug=True)