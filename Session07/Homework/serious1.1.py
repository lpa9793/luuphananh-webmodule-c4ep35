from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def bmi_calculation(weight,height):
    bmi=weight/((height/100)**2)
    if bmi<16:
        return 'BMI = ' + str(bmi) + ': Severely underweight'
    elif bmi<18.5:
        return 'BMI = ' + str(bmi) + ': Underweight'
    elif bmi<25:
        return 'BMI = ' + str(bmi) + ': Normal'
    elif bmi<30:
        return 'BMI = ' + str(bmi) + ': Overweight'
    else:
        return 'BMI = ' + str(bmi) + ': Obese'

if __name__ == '__main__':
    app.run(debug=True)