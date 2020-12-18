<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

## Bonjovi
This site is dedicated to the Band's fans and offers them the ability to access their music, most updated articles
and above all the ability to purchase their merchandise.
The site color has been chosen in line with the latest album called '2020' which gives a strong impact as it is mainly 
black however the grey/red used throughout the site is reflecting the logo palette.


## Site Structure
The menu of the site is quite simple with a navigation focused first on the band's social media and fans account.
It gives the fans the ability to reach out to their favourite band but also getting info on their tour dates, listen to their
music, purchase their merchandise by categories, and be part of the jbj xp. 

The top navigation provides:
--links to the band's official social media accounts
--the users' account: provides the ability to login to an existing account, create an account by registering, upon registration, it
offers a link to their profile and the option to logout, and if the user is a super user there is a product management link added
to either add a new product, edit, update or delete an existing one.
--view of their current shopping bag.

The menu is as follow:
--Home -- the logo also brings you back to the homepage
--JBJ Boutique -- offers a dropdown by category
--Tour -- gives information on the band next tour appereances
--Music -- provides the user with a large selection of the band's albums and ability to either buy or stream them

Toast messages have been put in place to accompany the users throughout their interactions in the site, whether it is when registering
purchasing a product, logging in, logging out...

The homepage is a generic page where the user can get familiar with the jbj experience, which are products subscriptions to the band's3
inside stories. it also gives the user a view of the latest album and then can also read the latest articles written.

The JBJ Boutique is the ecommerce part of the site where users/visitors can see all the items displayed by categories.
Upon surfing on this page, the users can sort the products as well as make a search to find their favourite items.

The Tour page will send the users to the upcoming tours events the bands organised, currently none is set.

The Music page gives the users the ability to chcek every album and presented in a flip card, the album title and tracks as well as an option
that directs them to the official channels to buy or stream online their songs.

## User stories
As a user I would like to feel close to the band, I would want a site that is easy to use, easy to navigate and gets me to sign up
and eventually purchase some items.
For that reason, the use of impactful images of the band is important. I am happy seeing the band and having the ability to 
be part of the jbj experience gives a sense of closeness to them.
As a user being able to register by providing a simple email and password to the 'fan club' is bringing me closer to the band. 
When navigation through the boutique, being able to see the products by category helps me as a user filter what I am looking for, and if 
I am interested in the cheapest product for example I can use the sort out option provided. 
Once the product selected, the toast message gives me an indication that it has been added to my basket which is a nice update to have as it also provides me with the 
option to either checkout ie purchase or continue shopping.
As a user if I want to checkout and find out on the page that I can benefit from free delivery it will entice me to purchase some more,
which I can do by choosing the go back to shopping option.
As a user it is also important for me to know that the purchases are secure. So after purchasing, an order number is displayed and a confirmation email will be sent.
If as a user I have an account, my order history will be displayed in my profile as a nice reminder and also to avoid purchasing the same products or simply as a folow up if 
there are delivery issues.
As a user having the option to purchase without registering is great. 
However any fan would want to register and have a profile so as a user I am happy to find that option on display on the top navigation.
When looking at the music page, as a user it shows me what are the latest albums but giving the option to buy or stream enhance my will to listen to the track without worrying about
the legality of it.

As a superuser, it is important for me to know that I am the only person whom can be in charge of the Boutique's product management.
Once logged in as a superuser, I will be interested in adding a product, editing an existing one, updating and deleting if products are out of stock.
and also making sure all the images load properly before logging out safely.

## Wireframes

## Features
**Branded design and easy navigation:** the jbj boutique is easy to navigate to, the products are displayed in cards where all details ie price are
available, when a user click on the product image, it brings them to an individual product detail page they can select the size when appropriate, the quantities and 
more importantly they can purchase.
**User-focused order functionality:** Once the user select the product he/she wants to purchase and they want to complete their order, by clicking on secure checkout on either the toast message 
or the actual checkout page, it directs them to a secure checkout where they are asked to fill up their order details ie name, email, address before submitting their card details.
**Social media:** as we are in difficult time it is important to give the users the ability to stay connected with the band in all means especially through their active social media platforms.
**Music buying and streaming:** With all the legality involved around music, it is important to provide the user with the right channels.


## Features for the future
**Social media integration:** giving the ability to user to sign up with facebook 
**Youtube livestream:** with what is happening today, most gatherings such as concerts have been cancelled, a user will definetly enjoy the band's future live streaming online through youtube
**Tour dates:** as soon as the concerts are back on, add the ability to purchase/book tickets online

## technologies used
**HTML**: for site layout
**CSS**: content structure and layout
**:Javascript/jquery:** used to add some animations
**Python:** programming language
**Github and gitpod**
**Fontawesome:** for icons
****

# Heroku deployment

Once the jbj site was set I have deployed with Heroku.

**deployment steps:**
First create a new app on heroku site by clicking new and create new app, I gave it the next available but close to my gitpod project name: jbonjovi.
then I chose europe as a region. On the resources tab, I provisioned a new Postgres database.
then installed dj_database_url, and psycopg2 in gitpod so to be able to use the postgres with accordingly pip3 install dj_database_url and pip3 install psycopg2-binary
then I froze the requirements with pip3 freeze > requirements.txt
To set up the new database I imported dj_database_url, commented out the default configuration and replaced the default database with a call to dj_database_url.parse, adding the url databse data from heroku
After that I ran the migrations with Python 3 manage.py migrate.
Followed by loading the fixtures, first categories python3 manage.py load data categories, then products with  python3 manage.py loaddata products
After that I have created with python3 manage.py create superuser.
Before commiting these changes I have uncommented the database default config.
At this stage I have added a piece of code on the app settings so that I can open my app either with heroku or on localhost.
The next step, I installed gunicorn with pip3 install gunicorn, created a Procfile and disabled collectstatic as I want this to be stored in S3 service from AWS.
this required to add the hostname into the app settings.py
I then initialised heroku remote in gitpod, logged in heroku through gitpod and pushed the code.
After that I realised my secret keys were bare so created a env.py and stored my secret keys in there and also added the secret keys in settings tab reveal var in heroku too.
My next step was to set up the automatic deployment on the heroku site simply by linking my repository through heroku and chosing the automatic deploy otpion offered on the page.

PS: STEPS TO SET UP AN ENV.PY:
    --Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
    --If you don't have one already, create a file named .gitignore  in the root directory of your project.
    --Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore  file add the following text to it: env.py 
    --At the top of your env.py  file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os” underneath you can assign your environment variables using the following syntax: 
    --os.environ["Variable Name Here"] = "Value of Variable Goes Here" 
    --Example: os.environ["SECRET_KEY"] = "ohsosecret" 
    --Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project or settings.py file for Django project. Add this under your other imports at the top of the file. 
    import os
    if os.path.exists("env.py"):
    import env 