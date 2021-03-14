from app import app, db
from data.act_data import act_list
from data.user_data import user_list
from data.fb_data import fb_list
from data.order_data import order_list
import json

def login(client):
    login_data = {"password": "test", "email": "test@test.com"}
    login_response = client.post(
        "/api/login", data=json.dumps(login_data), content_type="application/json"
    )
    assert len(login_response.json["token"]) != 0
    return login_response.json["token"]

def setup_db():
    with app.app_context():

        try:
            db.drop_all()

            db.create_all()

            db.session.add_all(user_list)

            db.session.commit()

            db.session.add_all(act_list)

            db.session.commit()

            db.session.add_all(fb_list)

            db.session.commit()

            db.session.add_all(order_list)

            db.session.commit()
    
            print("🎤 You rock at testing 🎤")

        except Exception as e:
            print("🚨 Uh-Oh 🚨")
            print(e)