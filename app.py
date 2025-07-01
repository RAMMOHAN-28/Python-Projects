from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Contact Page (GET + POST)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print("Form Submitted!")
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return render_template('success.html', name=name)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
