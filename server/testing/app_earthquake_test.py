import unittest
from server.app import app, db
from server.models import Earthquake

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Create the database and tables
        with app.app_context():  # Add this line to push app context
            db.create_all()

            # Seed the database with an earthquake record
            earthquake = Earthquake(id=1, magnitude=6.5, location="California", year=2020)
            db.session.add(earthquake)
            db.session.commit()

    def tearDown(self):
        with app.app_context():  # Add this line to push app context
            db.session.remove()
            db.drop_all()

    def test_earthquake_found_route(self):
        with self.app:  # Use the app context here
            response = self.app.get('/earthquakes/1')
            print("Response Status Code:", response.status_code)  # Debug print
            print("Response Data:", response.get_data(as_text=True))  # Debug print
            self.assertEqual(response.status_code, 200)

    def test_earthquake_not_found_route(self):
        with self.app:  # Use the app context here
            response = self.app.get('/earthquakes/999')
            self.assertEqual(response.status_code, 404)

    def test_earthquakes_found_response(self):
        with self.app:  # Use the app context here
            response = self.app.get('/earthquakes/1')
            data = response.get_json()
            print("Response Data:", data)  # Debug print
            self.assertIn('id', data)
            self.assertIn('magnitude', data)
            self.assertIn('location', data)
            self.assertIn('year', data)

if __name__ == '__main__':
    unittest.main()
