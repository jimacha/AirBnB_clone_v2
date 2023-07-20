from flask import Flask, render_template
from models import storage

app = Flask(name)
app.url_map.strict_slashes = False


@app.route('/hbnb', methods=['GET'])
def hbnb():
    """Logic to load data from storage (FileStorage or DBStorage) and sort by name (A->Z)
    Replace this with your actual implementation"""
    states = storage.all("State")
    cities = storage.all("City")
    amenities = storage.all("Amenity")
    places = storage.all("Place")

    return render_template('2-hbnb.html', states=states, cities=cities,
            amenities=amenities, places=places)


    @app.teardown_appcontext
    def teardown_db(exception):
        storage.close()


    if name == 'main':
        app.run(host='0.0.0.0', port=5000)
