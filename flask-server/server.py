from flask import Flask 

app = Flask(__name__)

# Members of API route 
@app.route("/members")

def members():
    return {"members": ["Mem1", "Mem2", "Mem3"]}

if __name__ == '__main__':
    app.run(debug=True)
