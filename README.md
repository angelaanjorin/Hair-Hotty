# Hair-Hotty-PP5
![Hair Hotty website preview](./assets/readme_images/Multi-Device-Website-Mockup-Generator-12-03-2024_01_11_PM.png)

[Link to deployed site](https://app-hairhotty-9ddf6a2299e6.herokuapp.com/)
Hair Hotty is an online hair shop, built using Python, Django, HTML, CSS, JavaScript, Amazon S3 and Stripe. 
If you wish to make a test purchase, you can use the following [Stripe Dummy Card](https://stripe.com/docs/testing) details:

- Success Card Number: 4242424242424242
- 3D Secure Auth Number: 4000 0027 6000 3184
- Exp Date: Any date in the future using the format MM/YY
- CVN: any 3 digit number
- Postcode: any 5 numerals  

Any payments made using a valid debit/credit card will not be processed and the card will not be charged. No orders made will be fulfilled.

For full Admin access to Django Admin panel with relevant sign-in credentials (supplied to the evaluator only): [Hair Hotty Admin](https://app-hairhotty-9ddf6a2299e6.herokuapp.com/admin/)


## Overview
Hair Hotty is a products store focusing on offering the best in sustainable, long-lasting products. Hair Hotty is accessible via all browsers with full responsiveness on different screen sizes. Users are invited to:

- View the store as Guests
- Register for an Account
- Use the stores Wishlist feature to record liked products
- Browse products by categories, ratings and price
- View, add and edit products in their bag
- As registered users, view past orders
- As registered users, view, add and edit thier reviews
- Sign up for a monthly newsletter featuring new products and developments

# UX/UI - User Experience/User Interface

## Design Inspiration
From the beginning of the project, I knew that the colour palette would have shades of purple acting as the primary colour with pops of color using shades of pink. The website is kept clean, with a good flow, using plenty of white space to draw attention to the products.


A simple logo, created using [Canva](https://www.canva.com/) and [Favicon.io](https://favicon.io/favicon-converter/)is used as a favicon. The logo depicts two "H" representing the two aspects of the brand name Hair Hotty. Another logo with the name Hari Hotty was also created using Canva for the heading of the website.

![Hair Hotty logo as Favicon](./assets/readme_images/h-Logo-12-03-2024_03_05_PM.png)  
*Hair Hotty logo*

![Hair Hotty logo for the website heading](./assets/readme_images/website-logo.png)  
*Hair Hotty logo for heading*

The images for the Hero Carousel were created using AI [Canva](https://www.canva.com/), with the first image edited in canva to highlight Halloween and discounts as this is a very good season for customers to purchase wigs. 

![First Hero Images for the Carousel](./static/images/hero-banner1.png)
- *First Hero image*

![First Hero Images for the Carousel](./static/images/hero-banner2.jpg)
- *Second Hero image*

![First Hero Images for the Carousel](./static/images/hero-banner3.jpg)
- *Third Hero image*

Product images are kept clean with no backgrounds so that focus is on the product itself. Feedback is continuously provided to the user via the website's header which displays whether the user is logged in and how many items are in their bag. Message 'toasts' are also visible upon user actions to display further information. Buttons are kept similar for continuity.

![Header Feedback](./assets/readme_images/headerfeedback.png)  
*Header feedback is kept clean and intuitive*


# Project Planning
## Strategy Plane

The primary objective was to create an e-commerce store that satisfied the assessment criteria of the Code Institute's Project 5: E-Commerce Module. The store must provide the expected functions of a responsive e-commerce store using Stripe as a payment system, user/guest views for authentication and store features, some extra features of my choosing, wishlist and Ratings/Reviews, and demonstration of some marketing/SEO skills. The User, whether paying customer or just browsing, must receive the best in UX and feel that Hair Hotty is relatable and trust-worthy. 

The site's design and graphic assets were collected through various copyright-free image websites. The products images were gotten from a another hair website [Her Given Hair](https://www.hergivenhair.com/). The hero-images on the home page was created by AI on [Leonardo AI](https://leonardo.ai/). Bootstrap and Crispy Forms were used for the project's frontend to speed up the process and to keep the templates consistent. Further customisation to the buttons, forms, modals, toasts and user feedback processes were added to the project's CSS files. 

### Site Goals
1. To provide users with a place to purchase hair products.
2. To provide the users the ability to search and browse hair wigs, hair extensions, hair products and utensils.
3. To provide the users with the ability to save products to their wishlist
4. To provide the users with the ability to check their order history.
5. To provide the users with the ability to leave a feedback for products.

### Scope
The project aims to develop an e-commerce website offering different hair products to customers. The website will be responsive and user-friendly, providing the user with the ability to:
 - Register and Login
 - Reset Password
 - Browse, search and find hair products for sale
 - Add products to thier shopping bag
 - View product stock levels
 - Add, edit and delete Reviews and Ratings
 - Update quantity in shopping bag
 - Delete items from shopping bag
 - Pay for items securely by using the integrated Stripe payment system
 - Save products to thier wishlist
 - Update personal information
 - View past orders

Key Features:

1. Initial Project Setup:
- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.
2. Products:
- Users can view products for sale and refine them by category
- Users can sort products by price and rating.
- Users can view details about each product including image, description, stock level and reviews and review count
- Search products by title or description
- Registered users can leave reviews and ratings.
3. User Authentication:
- Users can register an account, allowing them access to all of the website's functionality.
- Registered users can login and access wishlist, reviews, past orders and saving personal details.
- Users can reset their password
- Users can add or remove items from their wishlist
- Registered users have CRUD functionality for thier reviews and ratings
4. Orders and checkout:
- Users can add items to their shopping bag
- Users can update the quantity of the items in their shopping cbag
- Users can remove products from their shopping bag
- Users can use secure checkout functionality to pay for their items
5. Admin functionality:
The functionality in this section is limited to superusers or admins.
- Admins can add products for sale.
- Admins can delete products from the system.
- Admins can edit products and stock levels.
- Admins can access orders section in the backend.
6. Notification Messages:
Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.

Benefits:

1. User-Centric Experience: The platform focuses on the user's needs, allowing efficient browsing and product purchasing.
2. Efficient Navigation: Users can easily navigate through different sections of the website for seamless access.
4. Effective Communication: Sending emails and notification messages features, enhances user interaction.

## Design
### Colour Scheme
The website harmoniously blends warm tones of purple with accents of light gray and white, all anchored by a cool grey undertone. A hot pink was used to add a pop effect to highlight certain features as feedback to the users. This carefully curated color scheme establishes a sense of vibrancy and professionalism while ensuring a visually engaging experience for the users.
The main colours set as variables are

    --cordovan: #B00058;
    --licorice: #55002A;
    --hot-pink: #FF69B4;
    --pink:#FF439D;
    --old-lace: #FDF4E7;
    --white: #ffff;
    --dark: #140C00;
    --background: #ebeae5;
    --gray: #959595;
    --dark-gray:#6f6a6a;

![Colour Scheme](./assets/readme_images/Create-a-Palette-Coolors-12-03-2024_01_25_PM.png)

The below colours were used to compliment the main colours. Due to the fact that these colours have been used with very little repetition, there was no need to set them as variables
- #007bff
- #6c757d  
- #28a745 
- #dc3545 
- #ffc107 
- #17a2b8  
- #f8f9fa
- #343a40
- #333
- #eeebe3
- #97908e
- #8f8f8f
- #309e30
- #ff7a7a
- #cdc8c8
- #dc3545
- #gold



### Database Schema
![database schema]()

1. User:
The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, hence why changes directly to this model are not advisory. The User model is connected to the UserProfile model with one to one relationship.

2. UserProfile:
The UserProfile model is a custom-created model to handle the user profile details.

3. PrimaryCategory
This model was created for the purpose of defining a primary category for the products. All products should have a singel primary category (Foreignkey relationship).

4. SpecialCategory
This model was created so that products can have one or many special categories or none (manytomany relationship).

5. Product
This is a custom product model. It is connected to athe PrimaryCategory as a foreign key and SpecialCategory (manytomany relationship). In addition to that it has fields for handling stock. Stock_amount holds the integer value of the stock levels. In_stock is a Boolean field which sets the product to being in stock or not. A method called product_in_stock determines if a product is in stock based on the stock_amount value. The result of this method updates the in_stock boolean field. 

6. Wishlist
This model stores products to a wishlist for authenticated users. It is connected to UserProfile and Product models as a ForeignKey

7. Review 
This model stores the user's reviews for a product. It is connected to the UserProfile and the Product models as a ForeignKey

8. Order 
This model holds all the information of the user's order. It is connected to the UserProfile as a ForeignKey.

9. OrderLineItem
This model is connected to the Order and Product as a ForeignKey. It is created for each item in the order




### Fonts
In addition to Bootstrap 5 built in font family the below two fonts were used throughout the application
1. Poppins

![Poppins](./assets/readme_images/Poppins-Google-Fonts-12-03-2024_01_36_PM.png)

2. Libre Baskerville

![Libre Baskerville](./assets/readme_images/Libre-Baskerville-Google-Fonts-12-03-2024_01_38_PM.png)


## Agile Methodologies

Hair Hotty followed Agile planning methodologies to its completion. [GitHub Projects](https://github.com/users/angelaanjorin/projects/4) provided an ideal platform to create issues, boards and milestones for each of the project's Epics. Using labels I could easily identify my next task and organise them into the appropriate Milestones and Sprints. Keeping focused on individual sections as I built Hair Hotty reduced the number of bugs and human errors.

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Hair Hotty, identifying and labeling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project.
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release.

### Sprints

My Sprints were broken down into appropriately sized chunks from the beginning and I followed them to the best of my abilities. It is difficult to quantify the time taken exactly for each sprint as running a busy household outside of the course meant the hours the project was completed in hours outside of the normal working week. I have done my best to record them below. They are representative of a general timeframe of focus on the project areas.

| Sprint No. | Sprint Content |
|------------|----------------|
|    # 1     | Initial Setup, Backend, User Authentication, Frontend and Test Deployments |
|    # 2     | Implementing Product Management and User Cart Functionality |
|    # 3     | Implementing Stripe Checkout Functionality |
|    # 4     | Implementing Admin Dashboard & User Profile Functionality |
|    # 5     | Enhanced Interactivity and Robust Validation |
|    # 6     | Feature Completion and User Engagement Boosters |
|    # 7     | UI/UX Optimization Sprint  |
|    # 8     | Test Deployment and Project Completion |
|    # 9     | Code Validation, Documentation, and Refinement  |

## User Stories

User stories and features were recorded and managed on [GitHub Projects](https://github.com/users/angelaanjorin/projects/4)

#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In progress, Done, Won´t do and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow.

![Project](assets/readme_images/Backlog-·-hairhotty-pp5-12-03-2024_04_34_PM.png)

## Features
#### Navbar
The navbar was built using bootstrap 5 and it is fully responsive. The search bar allows the users to search for products by keywords from any page of the website. The My Account drop down gives the user the option to log in or register. If the user is authenticated additional menu options are displayed like my profile and admin (if the user is a superuser). The shopping bag icon is a link to the shopping bag and it also displays the total of the items in the bag.
The nav links allow the user to refine the products by category, special offers or to browse through the FAQ and contact us pages. There is a dropdown for special offers which allows the user to see the new arrivals and deals.

![navbar desktop]()

![navbar desktop]()

![navbar desktop]()

### Toasts
Toasts from Bootstrap were implemented to provide customers with feedback regarding their actions on the website.

![toasts]()


#### Footer
The footer was built as an example model featured on the bootstrap webseite consisting of lists of the different pages of the site and links to social media.

![footer](./assets/readme-images/features/footer.PNG)

#### Newsletter
Part of the footer is a newsletter, which asks users to subscribe to by applying thier emails addresses to recieve the most recent offers and discount codes. The form was integrated using MailChimp.

![newsletter]()


### Home Page
#### Hero Section
The hero section is the beginning of the whole customer's journey. That is why I made it a priority to create an appealing hero section with a carousel, featuring the highlights of certain seasons, like halloween. Other seasons like black friday or christmas sales can be easily implemented. 
All three hero section images were designed using an AI photo creation site (). Using Canva the first image was eidted with text. 
All three images have a call-to-action button Shop Now which invites the user to browse through the available products.

![hero section]()

#### Trust Badges
The trust badges serve as visual indicators to reassure the visitors about specific aspects of the services available.

![trust badges]()


### Products Page
The all products page renders all products to the user. They have the option to sort the products by title, price or category. This page also displays the number of the products available. The pages, which refine the products by category the same template as all products, prefilled with the relevant data.
At the end of the products result there is pagination to help the user navigate easily through multiple pages of products.

![pagination]()

![all products]()

### Products Card
The product card consist of an image of the product, title, price, number of reviews, category links, discount percentage and an add to Bag button. A flipping heart draws the user´s iattention to click it and not registered user´s get the promnt to register so that they can add the product to thier wishlist. Registered users can add the product to thie wishlist by clicking the heart. If the product is on sale, then the old price will be displayed with a line through, followed by the new price and a little label at the top of the image showing the percentage of the discount.

![product card]()

![product card sale]()

### Products-Detail Page
On the page's left side, a product image is displayed. On the right side, the most important information about the product is displayed. This includes the title, category link, number of reviews, price, stock levels, add to wishlist icon, sizes with dropdown list of sizes if the product has sizes, a quantitiy choice form, an add to bag button and return to shop button, returning the user to the all products page. 
Implementing stock levels in the product model, allowed for adding custom logic when it comes to adding items to the bag. The user should not be able to add to their bag a higher quantity than the stock levels and this logic also needs to account for items already in the bag. If the user tries to add more than what is in stock an error message appears to notify them that there is not enough stock to fulfill the order.
Below the top section, there is a section with tabs allowing the user to switch between description, details, and reviews. The reviews section allows an authenticated user to submit a review for a product. The overall rating is calculated and the number of stars are displayed in the top section of the page. Authenticated users can edit and delete their reviews from the same tab. 
The description tab includes a short description of the product which helps the users in making informed decision if they wish to purchase the product.
The details tab includes more specific information about the product, including materials used etc.

![product page]()

![reviews]()

![not enough stock]()

![add to wishlist]()

### Edit review page
This page allows the user to edit their review in the event they changed their mind. It renders prefilled with the original data. 

![edit-review]()

### Delete review confirmation
This page asks the user for confirmation if they wish to delete their review

![delete-review]()

### FAQ Page
The FAQ page consists of the most frequently asked questions.

![faq-page]()

### Privacy Policy Page
The Privacy Policy page was generated using () and displays the privacy policy of the business for all users to access.

![privacy-policy-page]()

### Contact Page
The Contact page consists of all the contact methods with links where appicable, like email, phone number and physical address. There is also a contact form for all users to use, not only registered users. 

![contact-us-page]()

### About Us Page
The About us page tells the user about the business and the background story and philosphy behind the brand. There are links to the social media sites to give more information to the users. Through this the user feels more connected to the brand.

![About-Us-page]()

### Return Page
The Return page consists of the most frequently asked questions about returning a product.

![Return-page]()

### Customer-Service Page
The Customer service page is the same link to the contact-us page, just incase users or customers are specifically searching for customer services.

![Customer-service-page]()


### My Profile Page
This section is accessible only to authenticated users.
This section contains three pages - my profile, my orders, and my wishlist

#### Profile
This page renders a form for the user's address and phone number. If the user has any details saved, it renders prefilled.

![profile]()

#### Order History
This page displays the past orders of this user.

![orders]()

#### My Wishlist
This page displays the items in the wishlist

![wishlist]()


### Admin CRUD Functionality:

![admin dashboard]()

Refine Products:
![refine products admin]()

#### Add Products
This page renders the product creation form and all required fields to add an item to the database. Admins can add products on sale by checking the on-sale box and adding the sale price. If the on_sale box is not checked the product will display with the original price. The Author field allows for multiple authors to be selected. If the author's name does not exist in the list, it can be added by clicking on the add author link

![add products]()

#### Edit Product
This page renders the product form prefilled with the existing data in the database. It allows the admin to modify the stock levels and any other details about the products.

![edit product]()

#### Delete Product
![delete product]()

#### Orders Admin
The orders page in the admin section provides a breakdown of the order stats based on status.
Below that there is a drop-down offering the ability to refine by order status. The options are In Progress, Completed, Cancelled, and All.
Below that the orders are displayed in a table with the order number, date, amount of items, order total, and status. The status field clearly indicates the status of the order. The used colours are red for canceled, green for completed, and blue for in progress. The admin can edit the order status by using the pencil icon on the side of each row.

Admin Orders;

![admin orders]()

Orders Refine:

![admin orders refine]()

#### Edit Order Status
This page renders a one-field form with a drop-down. It allows the admin the select from the available status choices.

![edit order status]()

#### Admin Discount Codes
This page has similar layout to the orders and dashboard. It presents the admin with a breakdown of the number of discount codes on the system by status.
There is a button to create code which opens a modal with the creation form. The discount code consist of the code, the amount of the discount in percentage and a checkbox to determine if the code is active or not.
The discount codes can be editted and deleted from this section without the need of using Django admin.

Admin Discounts

![admin codes]()

Admin Refine Codes

![admin refine codes]()

Admin Add Code

![admin add code]()

Admin Edit Code

![admin edit codes]()

Admin Delete Code

![admin delete codes]()

### Shopping bag
The shopping bag can be accessed from the main nav menu. The shopping bag table section provides a clear and organized representation of the items added to the shopping bag. Each item has a small image, title, author, price, quantity, and subtotal. The users can upgrade the quantity or delete items from the bag with the help of the buttons provided.
On the right side, there is a section allowing the user to input discount codes and view their subtotal, delivery charges, and total. 

![shopping bag]()
![shopping bag empty]()

##### Stock Quantity
Stock amounts have been implemented into the product model. Every time a user adds an item or updates quantity the shopping bag checks the quantity selected + the quantity of that item in the bag (if any) and compares it to the stock levels of the product. The user cannot add to the bag more items that there are in stock. 
In the event that another user purchases all units of a product while the product is sitting in another bag, when the user refreshes the page or continues to checkout, the item will be removed from their bag and an error message will be displayed letting them know that this item is not out of stock. In the event that 2 orders go through at the same time, the admin can cancel the status of the order and contact the customer for a refund. 

Trying to update quantity to levels above stock

![shopping bag no stock]()

##### Discount Codes
When an active discount code is applied, the subtotal is recalculated minus the percentage of the discount code. This excludes delivery fees. The discount amount is presented to the user and the total is updated. The code can be removed by clicking the remove button. A notification message is displayed to the user and the total price is adjusted accordingly.

![discount code success]()

The error messages recognise invalid and not active codes as well. 

![discount code invalid]()

![discount code inactive]()

### Checkout
This page contains a form for the user's delivery and payment information and a summary of the user's order. If the user has an account, they can save their delivery information on their profile to automatically be filled in the checkout.
- The checkout Form
In the checkout the user can add their details and if they're logged in, can check the box to save their details for future transactions. Users must enter their payment information before completing the checkout and all payments are handled via Stripe.

- Order summary
A final summary of the user's order is shown containing all the user's bag items, quantity and subtotal for each item. The user can also see their order total, delivery costs, any discounts that have been applied and the grand total in the summary.

![checkout]()

### Order confirmation page
After the order has been completed, the user is redirected to a confirmation page containing a final rundown of the order and what the user purchased. This page can be accessed again from the user's profile if they have an account on the site by clicking the order number from the list of past orders.

![order confirmation]()

### Confirmation email
Once the order is processed and payment has been received, the user will receive an email with the order details.

![email confirmation]()

### User Authentication
The website uses django allauth's built in functionality which allows the users to register and log in securely. There is also a reset password functionality which allows the user to input their email address and receive a link where they can securely reset their password.

## Future Features
- Add a pop up with the current discount code which can be updated by the admin.
- Add an event section to host a live online hair bazaar, with vendors, hair stylists and have a lottery with special prizes. Customers can buy the tickets to the lottery online and it will be stored on thier profile and they will be notified per email if they win.
- Allow admin to update only stock level fields as a quicker option to restock items. 
- Send email to customers when their order changes status.

## Search Engine Optimization SEO and Marketing

### Business Model
The B2C (Business-to-Consumer) ecommerce model for this online store operates as a platform catering to individual consumers looking to purchase a wide array of hair wigs, extension and utensils conveniently from their homes. This model revolves around offering a selection of different Hair wigs, extensions and accessories.

The target customers for this online store encompasses diverse demographics of women but mostly women of colour. 

### SEO
Within the head's meta tags of the base template are researched keywords and a description of Hair Hotty's goal as a business. These keywords have been researched using[Wordtracker](https://www.wordtracker.com/) to ensure that both short-tail and long-tail keywords are included. Keywords such as 'hairwig', 'black hair' and 'curly hair products' aim to reach most of the market, with additional descriptive key phrases such as 'buy human hair wigs for black women' and 'buy 
human hair half wigs for black women' to draw in users who know exactly what type of product they are looking for. Important keywords like 'human hair', 'full wigs' and 'half wigs' are present in the product names and descriptions in the hope to catch a chance to appear at the top of the customers' Google searches.

In addition to this, sitemap.xml and robots.txt files are included to increase the site's visibility. These files are essential for SEO (Search Engine Optimisation). The sitemap.xml was generated using [XML Sitemap](https://www.xml-sitemaps.com/) and included in the root folder of the project. A robots.txt file was created in the root folder to instruct search engine crawlers on how to access and crawl the site's pages.


### Marketing
- Using Mailchimp with thier embedded subscirption form that was customized and is included in the Footer, provides a possiblity for users to sign up for the monthly Newsletter. This section facilitates user engagement and promotes the e-commerce store through effective email marketing and social media presence.

- Facebook Page
A [Hair Hotty Facebook Page](https://www.facebook.com/people/Hairhotty/100064214191331/) that I have had for years was linked to this project to demonstrate promotion of the Hair Hotty store on social media. Posts informing customers of deals and new products are available on the page with the hopes of drawing in more revenue. Facebook provides an easy, minimal-step process to allow business owners to promote their business, with additional paid 'boost' features to further promote and spread the reach of the posts. Hair Hotty also offers a newsletter subscription service through MailChimp. The benefit of both of these services is that the customer is not forced to sign up to either and potentially worry that they will be spammed with an unnecessary amount of information. Hair Hotty avoids this in order to keep its brand clean and uphold its eco-friendly efforts.

![Hair Hotty Facebook Business Page](./assets/readme_images/-20-Hairhotty-Facebook-12-03-2024_04_23_PM.png)
*Hair Hotty Facebook Business Page*


## Testing
Testing documentation can be found [](TESTING.md)
## Bugs
|Bug|Status|
| ---| ---|
|[BUG: ]()|Closed|
|[BUG: ]()|Closed|
|[BUG: ]()|Closed|
|[BUG: ]()|Closed|
|[BUG: ]()|Closed|
|[BUG: ]()|Closed|
 


## Technologies And Languages

### Languages Used
- HTML
- CSS
- JavaScript
- jQuery
- Bootstrap
- Python
- Django

### Python Modules
- Boto3 is the Amazon Web Services (AWS) SDK for Python. It allows to interact with AWS services, such as S3

- dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.


- django-storages - Django Storages is a collection of custom storage backends for Django, including support for storing files on remote services like AWS S3.

- django-widget-tweaks - Django Widget Tweaks is a package that simplifies working with form widgets and templates in Django

- gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

- Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

- psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

- s3transfer - S3 Transfer is a library for managing file transfers to and from Amazon S3 storage.

- whitenoise - Whitenoise is a middleware for serving static files directly from your Django application.
### Technologies and programs
- [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate Favicon
- [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Photoshop](https://www.adobe.com/ie/products/photoshop.html) was used for creating the mockup images of the website during planning stage.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used during the testing of the website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [AWS](https://aws.amazon.com/) was used to store media files.
- [Stripe](https://stripe.com/en-ie) was integrated to handle payment processing in a secure and convenient way.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Online Convert](https://image.online-convert.com/convert-to-webp) used to convert images to webp format
- [Coolors.co](https://coolors.co/) was used to display the colour scheme.
- [Box Shadow Generator](https://cssgenerator.org/box-shadow-css-generator.html) was used to generate the shadows


## Deployment
### Before Deployment
To ensure the application is deployed correctly on Heroku it is mandatory to update the requirements.txt. This is a list of requirements that the application needs in order to run.

- To create the list of requirements we use the command pip3 freeze > requirements.txt. This will ensure the file with the requirements is updated.
- Then commit and push the changes to GitHub.

! Before pushing code to GitHub ensure all credentials are in an env.py file, which is included in the .gitignore file. This tells Git not to track this file which will prevent it from being added to Github and the credentials being exposed.

### Stripe setup
- Log in to [Stripe](https://stripe.com/en-ie)
- Navigate to developers section (link located at the top right)
- Go to API keys tab and copy the values of PUBLIC_KEY and SECRET_KEY and add them to your env.py file
- Navigate to the Webhooks page from the tab in the menu at the top and click on add endpoint.
- This section requires a link to the deployed application. The link should look like this https://your_website.herokuapp.com/checkout/wh/ 
- Choose the events the webhook should recieve and add endpoint.
- When the application is deployed, run a test transaction to ensure the webhooks are working. The events chan be checked in the webhooks page.

### AWS setup
- Log in to [AWS](https://aws.amazon.com/)
1. Create a new S3 bucket:
- Choose the closest AWS region.
- Add unique bucket name.
- Under Object Ownership select ACLs enabled to allow access to the objects in the bucket.
- Under Block Public Access settings unselect block all public access as the application will need access to the objects in the bucket.
- Click on create bucket.
2. Edit bucket settings.
- Bucket properties
  - Open the bucket page.
  - Go to properties tab and scroll down to website hosting and click on edit.
  - Enable static website hosting
  - Under the Hosting type section ensure Host a static website is selected.
  - Add Index.html to index document field and error.html to error document field and click save.
- Bucket permissions
    - Navigate and Click on the "Permissions" tab.
    - Scroll down to the "CORS configuration" section and click edit.
    - Enter the following snippet into the text box and click on save changes.

    ```
    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
    ```
    - Scroll to bucket policy section and click edit. Take note of the bucket arn (Example: arn:aws:s3:::test-bucket)
    - Click on policy generator and set the following settings:

        1. Select Type of Policy - S3 Bucket Policy
        2. Effect Allow
        3. Principal *
        4. AWS Service Amazon S3
        5. Actions: GetObject
        6. Amazon arn: your arn from the previous page

    - Click on add statement and then generate policy.Copy the policy
    - Paste the policy into the bucket policy editor.
    - Add "/*" to the end of the resource key to allow access to all resources in this bucket.
    - Navigate and Click Save changes.
    - For the Access control list (ACL) section, click edit and enable List for Everyone (public access) and accept the warning box. If the edit button is disabled, you need to change the Object Ownership section above to ACLs enabled (refer to Create Bucket section above).

3. Identify and Access Management (IAM)
- Create User group
    - In the search bar, search for IAM. 
    - On the IAM page select user groups in the menu on the left.
    - Click on create user group, add a name and click create group. The users and permission policies will be added later.
- Create Permissions policy for the user group
    - Go to Policies in the left-hand menu and click create policy
    - Click on actions and import policy.
    - Search for "AmazonS3FullAccess", select this policy, and click "Import".
    - Click "JSON" under "Policy Document" to see the imported policy
    - Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
    Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/*" to the end of the ARN to allow access to all resources in this bucket.

    ``````
        {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*",
                    "s3-object-lambda:*"
                ],
                "Resource": [
                    "arn:aws:s3:::your-project",
                    "arn:aws:s3:::your-project/*"
                ]
            }
        ]
    }

    ``````


    - On the next page add polcity name and description and click create policy.

- Attach Policy to User Group
    - Click on User Groups in the left-hand menu.
    - Click on the user group name created during the above step and select the permissions tab.
    - Click Attach Policy.
    - Search for the policy created during the above step, select it and click attach policy.

- Create User
    - Click on Users in the left-hand menu and click on add user.
    - Enter a User name .
    - Select Programmatic access and AWS Management Console access and click next.
    - Click on add user to group, select the user group created earlier and click create user.
    - Take note of the Access key ID and Secret access key as these will be needed to connect to the S3 bucket.
    - To save a copy of the credentials click Download .csv


### Deployment on Heroku
- To deploy the project on Heroku, first create an account.
- Once logged in, create a new app by clicking on the create app button
- Pick a unique name for the app, select a region, and click Create App.
- On the next page select the settings tab and scroll down to Config Vars. If there are any files that should be hidden like credentials and API keys they should be added here. In this project, there are credentials that need to be protected. This project requires credentials added for:

        1. Django's secret key
        2. Database Credentials
        3. AWS access key 
        3. AWS secret key
        4. Email host password.
        5. Stripe public key
        6. stripe secret key
        7. Stripe wh secret

- Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python
- From the tab above select the deploy section.
- The deployment method for this project is GitHub. Once selected, confirm that we want to connect to GitHub, search for the repository name, and click connect to connect the Heroku app to our GitHub code.
- Scroll further down to the deploy section where automatic deploys can be enabled, which means that the app will update every time code is pushed to GitHub. Click deploy and wait for the app to be built. Once this is done, a message should appear letting us know that the app was successfully deployed with a view button to see the app.
### Creating a fork
1. Navigate to the [repository](https://github.com/angelaanjorin/Hair-Hotty)
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description 
4. Choose to copy only the main branch or all branches to the new fork. 
5. Click Create a Fork. A repository should appear in your GitHub

### Cloning Repository
1. Navigate to the [repository](https://github.com/angelaanjorin/Hair-Hotty)
2. Click on the Code button on top of the repository and copy the link. 
3. Open Git Bash and change the working directory to the location where you want the cloned directory. 
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

## Credits
### Media
- [Defaut avatar image](https://www.pngwing.com/en/free-png-azzyd)
- [Default product image]()
- [Logo]()



### Code
- Boutique Ado Walkthrough was used for the base of this project
- [Styling django all auth pages](https://builtwithdjango.com/blog/styling-authentication-pages)
- [The right way to use Many To Many Field](https://www.reddit.com/r/django/comments/l937f1/the_right_way_to_use_a_manytomanyfield_in_django/)
- [Looping through integer in templates](https://copyprogramming.com/howto/how-do-i-loop-a-intergerfield-in-django-templates#how-do-i-loop-a-intergerfield-in-django-templates)
- [Product Card](https://bestjquery.com/tutorial/product-grid/demo199/) - the product cards were modified to suit the project
- [How to create automated tests](https://learndjango.com/tutorials/django-testing-tutorial)

### Acknowledgements
- Huge thank you to my mentor Gareth McGirr for all the help and resources.
- The Slack community and especially Indrek who listened to my struggles during development once again.
### Comments

