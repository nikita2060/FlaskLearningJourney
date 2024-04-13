import nullable
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///HamroBazaar.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class HamroBazaar(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Product_id = db.Column(db.Integer)
    Product_name = db.Column(db.String(200), nullable=True)
    Price = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.Product_name}"


with app.app_context():
    # Create the database tables based on the defined models
    db.create_all()


@app.route('/')
def hello_world():
    hamrobazaar = HamroBazaar(Product_id="224", Product_name="Shirt", Price="2000")
    db.session.add(hamrobazaar)
    db.session.commit()
    allProduct = HamroBazaar.query.all()

    return render_template("home.html", allProduct=allProduct)
    # return 'Hello, World!'


@app.route('/newendpoint')
def create_new_endpoint():
    return 'I created new endpoint by making new function in app.route'


if __name__ == "__main__":
    app.run(debug=True)
