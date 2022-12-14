from flask import Flask, render_template

app = Flask(__name__)  
# Create a new instance of the Flask class called "app"
# @app.route('/')  
# def hello_world():
#     return render_template('index.html')  # Return the string 'Hello World!' as a response  
# # The "@" decorator associates this route with the function immediately following

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'

@app.route('/lists')
def list():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template("index.html", users=users)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5500)    # Run the app in debug mode.