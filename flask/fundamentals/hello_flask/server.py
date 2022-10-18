from flask import Flask, render_template
# Import Flask to allow us to create our app
app = Flask(__name__)  
# Create a new instance of the Flask class called "app"
@app.route('/')  
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response  
# The "@" decorator associates this route with the function immediately following

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'



@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say (name):
    return f"Hi {name}!"

@app.route('/repeat/<name>/<int:num>')
def repeat(name,num):
    return render_template("hello.html", name=name, num=num)

@app.route('/lists')
def render_lists():
    student_info= [
        {'name': 'Michael','age': 35},
        {'name': 'John', 'age' : 30},
        {'name': 'Mark', 'age':25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students=student_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5500)    # Run the app in debug mode.

