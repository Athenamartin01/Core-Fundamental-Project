# Core-Fundamental-Project

<!-- Project Title and Description:
Provide a clear and concise title for your project. Follow it up with a brief description that explains what your project does and its key features. -->

This is Athena's Core Fundamental project. 
The project consists of a flask web application, which contains all of the neccesary files to runs a fully functional online poker store.

## Table of contents

-   [Technology](#Technology)
    -   [HTML & CSS](#HTML&CSS)
    -   [MySQL](#MySQL)
    -   [Python](#Python)
    -   [Jenkins](#Jenkins)
-   [Testing](#Testing)
-   [Furute Updates](#Future-Updates)
### Technology
In this project, I have used the following programming languages, software and libraries to create this project:

- HTML
- CSS
- MySQL
- Python
    - Flask
        - Flask-bcrypt
        - Flask-testing
        - Flask-sqlalchemy
        - Flask-Wtforms
    - Wtforms
    - Sqlalchemy
    - Pytest
    - Jinja2
- Jenkins
- Github

I will explain how each of these have been sued to create the final product.

### HTML&CSS
I have used HTML to create the elements for each of the webpages, these files are all stored in the 'Templates' folder. The HTML files have had some python integration using jinja2 to allow for some python functionality within the html scripts and to allow for a overall template which is used for every page of the website, this is known under Layout.html, which includes the navbar.

The HTML webpages all incorperate the CSS and images in the 'static' folder. all of the CSS stylings are stored into one css file, latout.css

### MySQL
I have used MySQL to store the database created from the SQLAlchemy library, the database is stored under the title apdb and consists of 4 tables, Customer, Order, Product and Order_Product. 

- Customer:

    Customer is used to hold all the information about the customer, and incorperates some bcrypt functionality to hash some of the more personal data. The Customer table is linked to the Order table via a one to many relation.

- Order:

    Order is used to keep track of if the order's have been completed and which customer has placed the order. This table is linked to the Order_Product table via a one to many relation.

- Product:

    The Product table holds all the information about a Product, including it's name, price, stock and image filename. This allows for easier creation and manipulation of the product pages, as a system doesn't have to be used for the iamge filenames and can instead be linked directly.
    The Product table has a one to many relation with the Order_Product table.

- Order_Product:

    The order product table is used to negate the many to many relationship which would occur between Order and Product. it is used to store the amount of each Product that occurs in each Order.

For more clarification on how each of the tables interlink, please check out the ERD.drawio file. to reset or create the database, please use the create.py file located in the application folder.

### Python 

Python is used to complete all of the back-end functionality of the website. 

Flask has been used to setup the application, including all of the routes to each of the various webpages and the links between them. A few submodules of flask have been used to handle database creation and manipulation, handling of data stored into html forms, hashing of sensitive data, webpage testing and allowing python functionality within the html scripts to allow for the items and form to be displayed in some of the webpages dynamically.

The best example to see the majority of these flask features in action would be the cart page, which uses all of the functionality except for bcrypt.

Pytest has been used for the coverage reports which have been stored into a html format. Currently the test coverage meets 92%.

### Jenkins

Jenkins has been used to attempt to run the application, and all create coverage reports for the application when a new buidl is introduced on github, this will be done using webhooks, and creating a link between the repo and the jenkins build.
However, currently I have had to install jenkins via windows, and unfortatly I have not been able to get my build up and running. 
 
due to my computer having the processing power of a potato and the file organisation of a toddlers play room.

## Testing

I have started the tests off by creating a testing database and including all the neccesary data to be implemented into the tables. 

In regards to testing, I have created tests to ensure each of the webpages handle GET requests, and allow for a functional build. I have also create some POST request tests to see how each of the webpages handle inputted data from the user, and to see if the functionality between the forms and the database functions as expected.

## Future Updates

In future versions, It is planned to include the following features:

-   A much better design of the homepage (which is currently a barren wasteland of nothingness except for the navbar).
-   Hopefully a functional jenkins build.
-   Form input rescrictions, to be implemented via wtform validators.
-   A customer login page, so a new customer doesn't have to be created each time.
-   Some better CSS styling and and html elements to create a more of a unique look to the webpages.










