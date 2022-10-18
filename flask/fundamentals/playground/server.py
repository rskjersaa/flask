from flask import Flask, render_template
# Import Flask to allow us to create our app
app = Flask(__name__)  
# Create a new instance of the Flask class called "app"
# @app.route('/')  
# def hello_world():
#     return render_template('index.html')  # Return the string 'Hello World!' as a response  
# # The "@" decorator associates this route with the function immediately following

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return 'Sorry! No response. Try again.'

@app.route('/play')
def play():
    return render_template ("index.html", num=3, color="lightblue")

@app.route('/play/<int:num>')
def play_2(num):
    return render_template("index.html", num=num, color="lightblue")

@app.route('/play/<int:num>/<string:color>')
def play_3(num, color):
    return render_template("index.html", num=num, color=color)


    
# @app.route('/say/<name>')
# def say (name):
#     return f"Hi {name}!"

# @app.route('/repeat/<name>/<int:num>')
# def repeat(name,num):
#     return render_template("hello.html", name=name, num=num)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5500)    # Run the app in debug mode.
