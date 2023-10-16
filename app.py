from flask import Flask, render_template

app = Flask(__name__)


@app.route('/fizzbuzz')
def fizzbuzz():
    fizzbuzz_list = []
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            fizzbuzz_list.append('fizzbuzz')
        elif number % 3 == 0:
            fizzbuzz_list.append('fizz')
        elif number % 5 == 0:
            fizzbuzz_list.append('buzz')
        else:
            fizzbuzz_list.append(str(number))
        

    return render_template('fizzbuzz.html', fizzbuzz_list = fizzbuzz_list)

