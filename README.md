### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) 
### General Assembly: Software Engineering Immersive

# Dreamland: festival app

## Overview
Dreamland is a full stack app built with Python, React JS, Flask, SQLAlchemy and Marshmallow interacting with a PostgreSQL database. It was created for attendees and event staff to use onsite across the live days of the event. Due to the presumed use case we decided on a mobile first design. Attendees can view the festival line up, create their personal schedule and place bar orders whilst event staff can view incoming orders and update collection status. 

Trello was used as a ticketing system and Balsamiq to wireframe the mobile design.

🔗 http://dreamland-festival-app.herokuapp.com/

## Demo

![dreamland](https://user-images.githubusercontent.com/68645584/122233228-cd136400-ceb3-11eb-9130-b3f9bd9a0398.gif)


## Brief & Timeframe:
* Build a full-stack application by making your own backend and your own front-end
* Use a Python Flask API using a Flask REST Framework to serve your data from a Postgres database
* Consume your API with a separate front-end built with React
* Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models
* Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut
* Be deployed online so it's publicly accessible
* Timeframe: 1week

### Team 🚀:
Lydia Wood : https://github.com/lydiarrrw
Fabien Depasse : https://github.com/fdepasse

## Technologies used
### Frontend:
* JavaScript (ES6)
* React JS
* SASS
* Babel
* Node.js
* React-Router
* Webpack
* Axios
* HTML5
* Bulma

### Backend:
* Python
* Flask
* SQL Alchemy
* Marshmallow
* PostgreSQL
* bcrypt
* jwt

### Testing:
* pytest

### Dev Tools
* GitHub
* Git --> branching
* Heroku
* VS Code
* Chrome developer tools
* Balsamiq
* Canva
* Trello
* Insomnia
* Quick Database Diagrams

## User journey 
### Homepage
![Screenshot 2021-04-26 at 14 37 42](https://user-images.githubusercontent.com/68645584/116091670-f75b5900-a69c-11eb-8b51-fde5a1ec8f47.png)

### Line Up
![Screenshot 2021-04-26 at 14 37 59](https://user-images.githubusercontent.com/68645584/116091701-0215ee00-a69d-11eb-9fb8-734ef77299c1.png)

* To save an act to their personal lineup, the user changes the toggle to "on" which triggers an async function, saveArtistToUser. Passing the bearer token and act id as parameters the function generates an Axios PUT request to the backend in order to save an act to a user. 
* If the act clashes with another in the users’ personal schedule this triggers an alert which pulls through a backend error message.
* Currently, this feature doesn’t account for users’ that aren’t logged in, to fix this I’d update the error messaging to prompt the user to sign up or log in. 
* In order to beautify the slider pretty checkbox library was installed with npm.  
 
### Artist Information
![Screenshot 2021-04-26 at 14 38 13](https://user-images.githubusercontent.com/68645584/116091729-093cfc00-a69d-11eb-8c19-3a7dd0603330.png)
### Sign Up
![Screenshot 2021-04-26 at 14 38 22](https://user-images.githubusercontent.com/68645584/116091758-0fcb7380-a69d-11eb-93f1-4e5d606ca426.png)
### Login
![Screenshot 2021-04-26 at 14 38 36](https://user-images.githubusercontent.com/68645584/116091789-178b1800-a69d-11eb-8c31-27e724f4b625.png)
### Menu 
![Screenshot 2021-04-26 at 14 38 57](https://user-images.githubusercontent.com/68645584/116091834-22de4380-a69d-11eb-8569-9509102a5c46.png)

### Admin

### User Profile 
![Screenshot 2021-04-26 at 14 39 09](https://user-images.githubusercontent.com/68645584/116091854-2a9de800-a69d-11eb-9f80-ba5e6d6acc5c.png)
* Users can view and amend their personal lineup and view more artist information. They can also view the status of any bar orders. 

### Functionality
The functionality is similar to other event mobile apps, users are able to:
* View live and upcoming acts.
* Post and delete reactions to current sets.
* Browse artists by stage and create a personal lineup.
* Sign up & login.
* View bar menu and submit an order.
* View collection status of food and drink orders.
* View and update collection status of incoming bar orders (with admin access). 
## Process
From the outset we decided to keep a high level of communication and had daily standups to discuss current tasks and blockers. We kept in touch via Zoom and  Slack which was handy for any quick debugging. Git and GitHub were used for version control and we decided to push/pull as a team to avoid any potential issues or merge conflicts.The workload was delegated evenly between ourselves using Trello to manage tickets. 
### Planning
We focused heavily on planning during initially, outlining user stories and product features in a white-boarding session. 
![Screenshot 2021-04-26 at 14 40 02](https://user-images.githubusercontent.com/68645584/116091968-4acda700-a69d-11eb-8521-c9ec72d0af50.png)

Using an Entity Relationship Diagram, we structured the database architecture: 
<img width="935" alt="Screenshot 2021-04-26 at 14 51 49" src="https://user-images.githubusercontent.com/68645584/116093849-ef9cb400-a69e-11eb-9a62-21ecce7ba93a.png">

For the frontend UI we produced a wireframe using Balsamiq which helped to cement our understanding of the app's functionality.
![Screenshot 2021-04-26 at 14 40 47](https://user-images.githubusercontent.com/68645584/116092067-65078500-a69d-11eb-8487-37a2005a80a1.png)

### Backend 

Using Trello to manage tickets we built the backend models, views and controllers over two days. I specifically built the act, product and order models which extended the base model using Python classes. 

The act model was used to produce artist information for the overall festival lineup and the personal user schedule, it also had one to many relationships with the order and reactions models. For example, whilst placing an order a user must select an act to determine pickup time/location. Also, many users can react to an act live on stage by tapping the heart emoji on the homepage. 
```javascript
from app import db
from models.base_model import BaseModel
from models.order_model import Order
from models.reaction_model import Reaction

class Act(db.Model, BaseModel):

    __tablename__ = "acts"

    stage_name = db.Column(db.String(40), nullable=False)
    set_time = db.Column(db.String(5), nullable=False)
    artist_name = db.Column(db.String(50), nullable=False, unique=True)
    image = db.Column(db.Text, nullable=False)
    official_website = db.Column(db.Text, nullable=False)
    genre = db.Column(db.String(40), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    
    #relationship 1 act to many orders
    orders = db.relationship("Order", backref="act", cascade="all, delete")

    #relationship 1 act to many reactions
    reactions = db.relationship("Reaction", backref="act", cascade="all, delete")
```

The order model was the basis for the food and beverage bar order system, it required one to many relationships with users and acts for pickup logistics. Due to the many-to-many relationship between products and orders it also links to the products_orders join table. 
```javascript
from app import db
from models.base_model import BaseModel
from models.product_model import Product
from models.products_orders_model import products_orders_join


class Order(db.Model, BaseModel):
    __tablename__ = "orders"

    ready_to_collect = db.Column(db.Boolean, nullable =True)

    #relationship 1 user to many orders
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))

    #relationship 1 act to many orders
    act_id = db.Column(db.Integer, db.ForeignKey("acts.id", ondelete="CASCADE"))

    #relationship many orders to many products
    products = db.relationship("Product", backref = "orders", secondary=products_orders_join)
```
TablePlus allowed us to visualise the PostGreSQL database. We tested the backend using Insomnia to make requests and ensured the expected JSON response was received.

### Frontend 
On day 4 we moved on to the frontend and laid out the main components focusing on functionality first. I built the line-up page, artist information modal, food and beverage menu page and order system. React Hooks were used throughout, specifically useState and useEffect. Axios was used to request relevant data from the backend to display on the frontend with JSX.

#### Line up page
```javascript
 async function getLineUp() {
    try {
      const { data } = await axios.get('/api/acts')
      updateActs(data)
    } catch (err) {
      console.log(err)
    }
  }
  useEffect(() => {
    getLineUp()
  }, [])

  function filterByStage() {
    return acts.filter(act => {
      return (act.stage_name === stage)
    })
  }
```
* Axios was used to GET act data from the backend which was then saved as an array of acts in state. To display the full lineup, the acts array was mapped over to render each artist as JSX. The filterByStage() function sorts acts by stage name when the user clicks a tab. 

#### Featured piece of code: order system 
To combat the problem of waiting in line and missing the show we created an order system for attendees to buy food and drinks using the app. React hooks were used to link up the backend and frontend functionalities, for example:
* Axios GET request retrieves the full menu data from backend, it's then mapped over and returns each product as a card in JSX. The filterByProduct function called on the array separates food and beverage items out on the front end. 
* To create an order the backend requires a logged-in user to submit an array of products and an act id (for pickup logistics).It was important to use the frontend UI to gather the necessary data to submit an order request to the backend, this happened in stages. 
** Each product has an ‘add to basket’ button, onClick the product is pushed to the products array (saved in state)

<img width="875" alt="Screenshot 2021-04-26 at 16 42 32" src="https://user-images.githubusercontent.com/68645584/116111279-69886980-a6ae-11eb-830f-8c16f3b0a3a7.png">

```javascript 
 const [products, updateProducts] = useState([])
 const [actID, updateActID] = useState('')
 const token = localStorage.getItem('token')
 const [basket, updateBasket] = useState([])
 const [modal, showModal] = useState(false)

  //function to add the selected products to products array 
  function addToProducts(productID) {
    const tempProductArr = [...products, productID]
    return updateProducts(tempProductArr)
  }
  
   //function to get the act id 
  function getActId(key) {
    const selectedAct = key.value
    updateActID(selectedAct)
  }
  
  //function to render products in basket and trigger basket modal
  function displayBasket() {
    const tempBasket = []
    products.forEach(product => {
      const itemToShow = menu.find(item => {
        return product === item.id
      })
      tempBasket.push(itemToShow)
      updateBasket(tempBasket)
    })
    showModal(!modal)
  }
  
  //function to create user order 
  async function submitUserOrder(token, actID, products) {
    try {
      await axios.post(`/api/order/${actID}`, { products: products }, {
        headers: { Authorization: `Bearer ${token}` }
      })
    } catch (err) {
      console.log(err)
    }
  }

```

### Styling 

A mixture of Bulma and standard css practises were used for styling. To keep with the festival theme we opted for a clean colour scheme with pops of bold colour and sans serif fonts.

### Known bugs and errors
* Food and Drinks menu: can currently add products without a collection point which triggers an empty basket modal. This is due to the backend logic requiring all fields to create an order. I'd fix this by adding an error message on the front end to remind the user to add a collection point prior to creating a basket.
* User Profile : display the personal lineup in order and render the most recent bar order once submitted.

### Wins:
* Simple and functional responsive design across mobile and desktop devices.
* This was my second full stack app so it was interesting to use an alternative tech stack and practice Python fundamentals like classes, list and dictionary methods, functions and control flow statements. 
* The team dynamic worked well throughout the project, we spoke regularly and had daily zoom standup to communicate any wins and blockers. In the case of the latter we discussed as a team and worked together to solve issues that arose.
### Key learnings:
* After making three react apps, React Hooks helped me to think about the project as a whole in order to link up backend and frontend functionality. 
* Although I enjoyed the challenge of this project, in future, I’d reduce the scale of the MVP to ensure there was enough time to build out functionality of the core features (including frontend permissions, error messages etc). 
* Creating a food/drink order was tricky
* It took some time to get the serializers and models working correctly to deal with the information as we intended
## Future Features
Some extra added functionality if there was more time:
* Build out the user types to include event organisers, they could amend the lineup to account for any program changes. For example, they could post/put/delete acts. This feature could notify attendees when new artists announced in the lead up to the festival to promote app engagement.
* Extend reactions feature to include a community social feed (display everything on Twitter with #dreamland2021). Give attendees a reason to use the app post event and notify them when dreamland2022 goes on sale!
* Add a festival site map for users to navigate and make the bar collection points clearer from a UX perspective.
