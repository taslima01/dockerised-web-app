from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

