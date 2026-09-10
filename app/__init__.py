import os

from flask import Flask,request,jsonify,render_template
from flask_cors import CORS

from app.gmail import(
is_email_command,
extract_email,
create_gmail_url,
generate_email_with_gemini
)

from app:youtube import youtube_bp

def create_app():

    app=Flask(__name__)
    CORS(app)

#youtube
app.register_blueprint(
    youtube_bp,
    url_prefix="youtube"
)

@app.route("/")
def home():
    return render_template("index.html")

#html
@app.route("/html")
def html():
    return render_templates("index.html")

#health
@app.route("/health")
def health():
    return jsonify({
        "status":"ok",
        "service":"Nova AI Agent"
    })

#gmail AI Agent
@app.route("/agent",methods=["POST"])
def agent():

    try:
        data=request.get_json(silent=True) or {}
        command = dta.get("command","").strip()

if not command:
    return jsonify({
        "success":False,
        "message":"command is required"
    }),400

if not is_email_command(command):
    return jsonify({
        "success":False,
        "message":"please give a Gmail command."
    }),400

recipient = extract_email(command)

email = geneate_email_with_gemini(command)

return jsonify({
    "sucess": True,
    "Type": "email",
    "email_generated":True,
    "recipitent": recipient,
    "subject":email["subject"],
    "body":email["body"],
    "gmail_url": create_gmail_url(
        email["subject"],
        email["body"],
        recipient
    )
})
except exception as e:

return jsonify({
    "sucess":False,
    "message":str(e)
}),500
return app





    
