<img src="https://raw.githubusercontent.com/Wonka86/foyle-valley-farms/master/media/tractor-banner.png" style="margin: 0;">

# Foyle Valley Farms

Live Website can be visited <a href="https://foyle-valley-farms.herokuapp.com/" target="_blank">Here</a>

Conceived from a love of fresh locally sourced food, Foyle Valley Farms  has become a hub for top notch produce.The online farming co-op plan is to serve people in the north-west region with freshly supplied produce from farms that specialise in different types of farming.

This project is used to showcase the use of Fullstack skills in the production of a farm shop to supply fresh produce in the local vicinity with the idea of creating a viable product that users and producers woould what to use to buy and sell on. 

## UX

### Target audience

- People who want to shop local but find it difficult to shop in person (for any reason)
- People who are not sure were to start when shopping fresh 
- People who are curious about what sort of products a grown locally
- People who are looking for an alternative choice
- People who are interested in sustainable farming practises and enviornment

### User Stories

### New User

- I expect to easily navigate the website, so that I can quickly find what I'm looking for.
- I want to be able to learn more about Foyle Valley farms and what makes them different.
- I expect to access the website from any device, so that I can use the website anytime and anywhere.
- I want to be able to easily contact the owner/manager of the company, so that I can write an additional query or ask a question.
- I expect to be able to easily register for an account so that I can see and save my personal details for quicker ordering in the future.

### Returning user

- I want to be able to easily log in and out of my account so that I can access my personal information and order history.
- I expect to be able to reset/ change my password if I forgot it, so that I can get access to my profile again.
- I want to be able to have my delivery details prefilled so that I can save time.

### Website User

- I expect to be able to add/delete products from my cart so that I can update the products I would like to purchase
- I want to be able to see a list of products and easily break them down to different categories.
- I expect to be able to click on a product and see it in more detail.
- I want to be able to receive an order confirmation so that I can be sure my order has gone through.

### Website Owner

- I expect to be able to Sell products securely to customers
- I want to have convenient admin interface to be able to add, remove and update products.


## Wireframes

The following wire frame was used as the base design for thw website

- [Wireframe](https://github.com/Wonka86/foyle-valley-farms/tree/master/wireframes)

There have been some changes from the orginal design due to aesthetic appeal not feeling quite right on production.

[wireframe](https://wireframe.cc/) tool was used to create the wireframes for the project

## Design

- I used Bootstrap framework for ease of use and ability to be easily customized. It is used for creating features such as navbar, cards, forms, as well as for the layout.
- JQuery is used for initializing some Bootstrap components.
- I used FontAwesome across the project for social media links, forms, cart, search and user icons in navigation.

## Website Features

Foyle valley farms contain the following applications: home, about, blog, bag, checkout, contact, products and profiles.

### Existing Website Features

- Navigation Bar:  Main nav bar is fixed at the top throughout all pages on desktop and mobile screen. The logo placed on the left hand side, search option, accounts and shopping cart moving left to right.  This allows for ease of navigation in finding products, login/ register and items bought so far.


- Navigation : secondary nav allows for accesing shop, reading information about shop, contact and blog. This collapses on small screen to a burger menu.

- Footer: Contains social media link and home logo/button comes in two forms one for desktop and mobile.

- Home page: The home page serves to draw in users to the business and give an idea of what is expected from the website. 
**Hero Image** section is what users see first. The idea behind this is to give an impression of wholsome hard working local farmers producing what we need with a button to take you directly to the products.
**Quotes** sections are there to give short sharpe emphasis on what standards that the company look for **sustainability** and **Quality**.
**short statement** section is to build on the eye catching quotes and fill the user in more.

- About Page: The about page continues to give more information on foyle valley farms and its main focus and ideas

- Contact Page: Offers a contact form to fill out with name, email and message if a user has any questions or queries. The real email will be sent to the admin of the website. Contact details of where the main office is to be found, ways in which it can be contacted and opening hours are also made avaiable.

- Blog: This section offeres another form of interaction with users and a larger scope for engagement. If there are any events or further background information it can be posted here and users can comment.

- Products pages: (includes Butchery and groceries) Displays product cards with following information - img, name, category, rating and price. All cards are clickable and send the user to individual product detail page. Depending on weather the user has superuser privilege they will be able to edit and delete products on this page with the edit button directing them to product management page and the delete button deleting the product. Users of all levels also have the ability to filter products.

- Product details page: This page offers more information to the user on the specific item showing same informtaion that was in products page along with a detailed paragraph on the item. Here the user can select how many of a particular item they would like to buy with item quantity buttons. The user can then proceed to add to bag and either keep shopping or proceed to bag by clicking on the pop up that says item is added to bag or by clicking the trolly icon item on top right.

- Bag page: The user can evalulate what the have added and make adjustments. They have options to increase or decrease the quantity of the items they would like, see a total of how much everything costs and either keep shopping which return the user to the products page or head to payment by clicking the secure checkout button.

- Checkout Page:  The checkout page has a brief summary of what is being bought displaying quantities names and totals. The page also contains a form which if the user is logged in will be prefilled and all the user will have to complete will be the card payments. when the user can then complete or or adjust bag. adjust bag will go back to the bag section and complete order will go to checkout success page and put order through stripe payment.Since the website is made for educational purposes only and the Stripe functionality is only for testing, only 4242 4242 4242 4242 card number will lead to the successfull payment.

- Checkout success: A display message will thank you saying email confirmation. Information about the order is also displayed.

- Profile page: Available only for authenticated users it contains personal information shipping details and order history.

- Product Admin: Available only for authenticated superusers it contains the ability to add new products by filling out a form. If valid the form/new product is added to the products page.

- Django-allauth features: inlcude sign up ( allows a user to create a new account), Login (allows registered users to log into their account), Forgot password ( allows user to reset password), Logout (renders logout page that gices user option to continue logout)


### Features to add in the future:

- Social account login: This feature would allow an ease of use by connecting accounts such as facebook or google and enhance user experience.

- Defensive delete button: Currently, the Delete button to delete a product has no defence to stop it being automatically pressed. A confirmation of delete should be added.

- Reviews products section: Reading reviews are a great way to help users decide to purchase a product.

## Technologies Used

Languages

[HTML5](https://en.wikipedia.org/wiki/HTML5) 

[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) 

[JavaScript](https://en.wikipedia.org/wiki/JavaScript) 

[Python](https://www.python.org/)

Libraries and Frameworks

[Django](https://www.djangoproject.com/)

[Bootstrap](https://www.bootstrapcdn.com/)

[stripe](https://stripe.com/gb)

[Fontawesome](https://fontawesome.com/)

[Gunicorn ](https://pypi.org/project/gunicorn/)

[Google Fonts](https://fonts.google.com/)

Tools

[AWS](https://aws.amazon.com/)

[GitHub](https://en.wikipedia.org/wiki/GitHub) 

[Heroku](https://www.heroku.com/what)

[GitPod ](https://www.gitpod.io/)

[wireframe](https://wireframe.cc/) 

Databases

[SQlite3](https://www.sqlite.org/index.html)

[PostgreSQL](https://www.postgresql.org/)

## Testing

## Deployment

Foyle-valley-farms was developed on gitpod and deployed on Heroku.

Heroku deployment process

- [requirements.txt](https://github.com/Wonka86/foyle-valley-farms/blob/master/requirements.txt) is needed as it contains a list of dependencies and created by pip3 freeze > requirements.txt in gitpod console.
- [Procfile](https://github.com/Wonka86/foyle-valley-farms/blob/master/Procfile) is needed in order to tell heroku how to run project.
- On [Heroku](https://dashboard.heroku.com/apps) go to create a new app, assign a name and closest region and click create app.
- In Heroku  resources tab go to Heroku Postgres select hobby dev and click provision button to add project.
- In Heroku settings tab click on reveal config vars and set the following - 
  - AWS_ACCESS_KEY_ID <your aws access key>
  - AWS_SECRET_ACCESS_KEY <your aws secret access key>
  - DATABASE_URL <your postgres database url>
  - EMAIL_HOST_PASS <your email password(generated by Gmail)>
  - EMAIL_HOST_USER <your email address>  
  - SECRET_KEY <your secret key>
  - STRIPE_PUBLIC_KEY <your stripe public key>
  - STRIPE_SECRET_KEY <your stripe secret key>
  - STRIPE_WH_SECRET <your stripe wh key>
  - USE_AWS	<True>
- Temporary set up (do not push) - Copy DATABASE_URL's value(Postrgres database URL) from the Convig Vars and paste it into the default database in settings.py.
- Migrate the database models to the Postgres database using the following commands in the terminal - python3 manage.py makemigrations and python3 manage.py migrate
- Load the data fixtures - python3 manage.py loaddata <fixture_name>
- Create a superuser for the Postgres database - python3 manage.py createsuperuser
- Remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.
- Add your Heroku app URL to ALLOWED_HOSTS in the settings.py file
- Automatically deploy each time you push to GitHub by going to heroku 
  - Deploy section -> Deployment method -> select GitHub
  - link the Heroku app to your GitHub repository for this project
  - click Enable Automatic Deploys in the Automatic Deployment section
  - Run git push command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.
- on successful deployment you can view your app by clicking Open App on Heroku
- Verify email by logging on with superuser login on app address/admin

## Local Deployment

For local deployment the user can download the git repository by clicking 'download.zip' button at the top of the page and extracting the zip file to your chosen folder or clone the repository by following what is outlined here: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository.

- Install the required dependencies with the following command: pip3 install -r requirements.txt

- Create an env.py file and add the following with your own values:
  - import os  
  - os.environ["DEVELOPMENT"] = "True"    
  - os.environ["SECRET_KEY"] = "<your value>"    
  - os.environ["STRIPE_PUBLIC_KEY"] = "<your value>"    
  - os.environ["STRIPE_SECRET_KEY"] = "<your value>"    
  - os.environ["STRIPE_WH_SECRET"] = "<your value>" 
  - os.environ["EMAIL_USER"] = "<your value>"
  - os.environ["EMAIL_PASS"] = "<your value>"

- Create a .gitignore and add these files so that they are not published at any stage. This is to keep the secret keys and values safe.

- You need to make migrations to set up the SQLite3 tables. You can do that by: python3 manage.py makemigrations, python3 manage.py migrate

- Create a superuser for your project by using the following command: python3 manage.py createsuperuser

- Run locally by the following command: python3 manage.py runserver


## Credits

- Code

- Content

- Media

- Acknowledgements

