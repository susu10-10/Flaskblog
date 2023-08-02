from flaskr import app

print("flask app is running on port 5003")
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int("5003"))
