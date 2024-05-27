from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
import os
from flask_mail import Mail, Message
from config import Config
import google.generativeai as genai

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Helper function to generate content
def generate_content(input_text):
    model = genai.GenerativeModel(model_name="gemini-pro")
    response = model.generate_content(input_text)
    return response.text

# Rendering loader page
@app.route("/", methods=['GET', 'POST'])
def load():
    return render_template("loader.html")

# Rendering home page
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

# Rendering about page
@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")

# Rendering contact page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

# Endpoint to handle text and store it in the session
@app.route("/gemini", methods=['GET', 'POST'])
def text():
    data = session.get('data', [])

    if request.method == "POST":
        input_text = request.form.get("text")
        if input_text:
            try:
                text_result = generate_content(input_text)
                data.append({'input': input_text, 'result': text_result})
                session['data'] = data
                return redirect(url_for('text'))
            except Exception as e:
                flash(f"Error generating content: {str(e)}", "error")
        else:
            flash("Please provide a valid input!", "error")

    return render_template("index.html", data=data[::-1])

@app.route("/logout")
def logout():
    session.pop('data', None)
    return redirect(url_for('load'))

# Endpoint to handle form submission for sending an email
@app.route('/send-mail', methods=['POST'])
def send_email():
    subject = request.form['text']
    mail_address = request.form['mail']
    message_content = request.form['text_area']

    if subject and mail_address and message_content:
        try:
            msg = Message(subject, sender=mail_address, recipients=['a.dizdar00@gmail.com'])
            html_content = render_template('mail.html', subject=subject, mail_address=mail_address, content=message_content)
            msg.html = html_content
            mail.send(msg)
            flash("Email sent!", "success")
        except Exception as e:
            flash(f"Error sending email: {str(e)}", "error")
    else:
        flash("All fields are required!", "error")

    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
