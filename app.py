from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"