from flask import Flask
from flask import request
import gemini as g
import vonage_connection as v

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=False, port=443, host='0.0.0.0') 

@app.route("/inbound_message", methods=['POST','GET'])
def inbound_message():
    if request.method == 'POST':
        reply = g.send_text_prompt(request.form['text'])
        response = v.send_message(text=reply,to_number=request.form['from'])
    else:
        return "<p>200</p>" 
    
