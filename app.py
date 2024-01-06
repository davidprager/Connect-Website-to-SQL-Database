from flask import Flask, render_template, request, redirect, url_for, make_response
import mysql.connector


# instantiate the app
app = Flask(__name__)

# Connect to the database

# Retrieve all the categories from the database

# Fetch all the rows in a list of tuples called categories



# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template()

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable

    # Retrieve the books from the database that are associated with the selected categoryId

    # Fetch all the rows in a list of tuples called books.

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
