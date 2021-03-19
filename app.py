from flask import Flask, render_template
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # data
    mars_info = mongo.db.mars_info.find_one()

    # return template
    return render_template("index.html", mars_info=mars_info)



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars_info = mongo.db.mars_info
    
    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page????
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)




