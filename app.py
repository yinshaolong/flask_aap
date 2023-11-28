from flask import Flask, render_template, request #request is variable
#__name__ refers to current file
#says turn thsi file into a flask application
app = Flask(__name__)

#decides what files going to be sent based on browser request
#use decorator to tell flask what url triggers what function
@app.route("/") #says what code wanted exucuted when user inputs /
def index(): #default of the site, but by convention, index.html
    return "hello, world"