from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return('''
        <div>
            <p> hello </p>
        </div>
           
           ''')
    
if __name__ == "__main__":
    app.run(port=4800, host="0.0.0.0", debug=True)