# Hair-Hotty-PP5
![Hair Hotty website preview](https://res.cloudinary.com/dzesjeplp/image/upload/v1733263099/READMEPP5/Multi-Device-Website-Mockup-Generator-12-03-2024_01_11_PM_qpgaq1.png)

[Link to deployed site](https://app-hairhotty-9ddf6a2299e6.herokuapp.com/)

# Introduction
Hair Hotty is an online hair shop, built using Python, Django, HTML, CSS, JavaScript, Amazon S3 and Stripe. 
If you wish to make a test purchase, you can use the following [Stripe Dummy Card](https://stripe.com/docs/testing) details:

- Success Card Number: 4242424242424242
- 3D Secure Auth Number: 4000 0027 6000 3184
- Exp Date: Any date in the future using the format MM/YY
- CVN: any 3 digit number
- Postcode: any 5 numerals  

Any payments made using a valid debit/credit card will not be processed and the card will not be charged. No orders made will be fulfilled.

For full Admin access to Django Admin panel with relevant sign-in credentials (supplied to the evaluator only): [Hair Hotty Admin](https://app-hairhotty-9ddf6a2299e6.herokuapp.com/admin/)

# Table of content
- [Introduction](#introduction)
   * [Overview](#overview)
- [UX/UI - User Experience/User Interface](#uxui-user-experienceuser-interface)
   * [Design Inspiration](#design-inspiration)
- [Project Planning](#project-planning)
   * [Strategy Plane](#strategy-plane)
      + [Site Goals](#site-goals)
      + [Scope](#scope)
   * [Design](#design)
      + [Colour Scheme](#colour-scheme)
      + [Database Schema](#database-schema)
      + [Fonts](#fonts)
   * [Agile Methodologies](#agile-methodologies)
      + [MoSCoW Prioritization](#moscow-prioritization)
      + [Sprints](#sprints)
   * [User Stories](#user-stories)
      + [Epic 1: Initial Setup, Backend, User Authentication, Frontend and Test Deployments ](#epic-1-initial-setup-backend-user-authentication-frontend-and-test-deployments)
      + [Epic 2: Implementing Product Management and User Cart Functionality](#epic-2-implementing-product-management-and-user-cart-functionality)
      + [Epic 3: Implementing Stripe Checkout Functionality](#epic-3-implementing-stripe-checkout-functionality)
      + [Epic 4: Implementing Admin Dashboard & User Profile Functionality](#epic-4-implementing-admin-dashboard-user-profile-functionality)
      + [Epic 5: Enhanced Interactivity and Robust Validation](#epic-5-enhanced-interactivity-and-robust-validation)
      + [Epic 6: Feature Completion and User Engagement Boosters](#epic-6-feature-completion-and-user-engagement-boosters)
      + [Epic 7: UI/UX Optimization Sprint](#epic-7-uiux-optimization-sprint)
      + [Epic 8: Test Deployment and Project Completion](#epic-8-test-deployment-and-project-completion)
      + [Epic 9: Code Validation, Documentation, and Refinement](#epic-9-code-validation-documentation-and-refinement)
         - [GitHub Projects](#github-projects)
   * [Features](#features)
   * [Header](#header)
         - [Navbar](#navbar)
      + [Toasts](#toasts)
         - [Footer](#footer)
         - [Newsletter](#newsletter)
      + [Mailchimp Dashboard](#mailchimp-dashboard)
      + [Home Page](#home-page)
         - [Hero Section](#hero-section)
         - [Trust Badges](#trust-badges)
      + [Products Page](#products-page)
      + [Products Card](#products-card)
      + [Products-Detail Page](#products-detail-page)
      + [Edit review page](#edit-review-page)
      + [Delete review confirmation](#delete-review-confirmation)
      + [Blog](#blog)
      + [Contact Page](#contact-page)
      + [FAQ Page](#faq-page)
      + [Privacy Policy Page](#privacy-policy-page)
      + [About Us Page](#about-us-page)
      + [Return Page](#return-page)
      + [Customer-Service Page](#customer-service-page)
      + [Event Page](#event-page)
      + [My Profile Page](#my-profile-page)
         - [Profile](#profile)
         - [Order History](#order-history)
         - [My Wishlist](#my-wishlist)
         - [My Posts](#my-posts)
      + [Admin CRUD Functionality:](#admin-crud-functionality)
         - [Add Products](#add-products)
         - [Edit Product](#edit-product)
         - [Delete Product](#delete-product)
      + [Shopping bag](#shopping-bag)
      + [Checkout](#checkout)
      + [Order confirmation page](#order-confirmation-page)
      + [Confirmation email](#confirmation-email)
      + [User Authentication](#user-authentication)
   * [Future Features](#future-features)
   * [Search Engine Optimization SEO and Marketing](#search-engine-optimization-seo-and-marketing)
      + [Business Model](#business-model)
      + [SEO](#seo)
      + [Marketing](#marketing)
   * [Testing](#testing)
   * [Bugs](#bugs)
   * [Technologies And Languages](#technologies-and-languages)
      + [Languages Used](#languages-used)
      + [Python Modules](#python-modules)
      + [Technologies and programs](#technologies-and-programs)
   * [Deployment](#deployment)
      + [Before Deployment](#before-deployment)
      + [Stripe setup](#stripe-setup)
      + [AWS setup](#aws-setup)
      + [Deployment on Heroku](#deployment-on-heroku)
      + [Creating a fork](#creating-a-fork)
      + [Cloning Repository](#cloning-repository)
   * [Credits](#credits)
      + [Media](#media)
      + [Code and Content](#code-and-content)
      + [Acknowledgements](#acknowledgements)
      + [Comments](#comments)

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

![Hair Hotty logo as Favicon](https://res.cloudinary.com/dzesjeplp/image/upload/v1733263959/READMEPP5/h-Logo-12-03-2024_03_05_PM_cdh37l.png)  
*Hair Hotty logo*

![Hair Hotty logo for the website heading](https://res.cloudinary.com/dzesjeplp/image/upload/v1733263006/READMEPP5/readme/Untitled-design-422-_-80px-12-03-2024_03_07_PM_hrfxas.png)  
*Hair Hotty logo for heading*

The images for the Hero Carousel were created using AI [Leonardo.io](https://leonardo.ai/), with the first image edited in canva as well, to highlight Halloween and discounts as this is a very good season for customers to purchase wigs. 

![First Hero Images for the Carousel](./static/images/hero-banner1.png)
- *First Hero image*

![First Hero Images for the Carousel](./static/images/hero-banner2.jpg)
- *Second Hero image*

![First Hero Images for the Carousel](./static/images/hero-banner3.jpg)
- *Third Hero image*

Product images are kept clean with no backgrounds so that focus is on the product itself. Feedback is continuously provided to the user via the website's header which displays whether the user is logged in and how many items are in their bag. Message 'toasts' are also visible upon user actions to display further information. Buttons are kept similar for continuity.

![Header Feedback](https://res.cloudinary.com/dzesjeplp/image/upload/v1733263001/READMEPP5/readme/headerfeedback_kznyiz.png)  
*Header feedback is kept clean and intuitive*


# Project Planning
## Strategy Plane

The primary objective was to create an e-commerce store that satisfied the assessment criteria of the Code Institute's Project 5: E-Commerce Module. The store must provide the expected functions of a responsive e-commerce store using Stripe as a payment system, user/guest views for authentication and store features, some extra features of my choosing, wishlist and Ratings/Reviews, and demonstration of some marketing/SEO skills. The User, whether paying customer or just browsing, must receive the best in UX and feel that Hair Hotty is relatable and trust-worthy. A blog with CRUD functionality for registered users was added. Some marketing techniques with links to relevant sites were addes as well as links to the Hair Hotty store.

The site's design and graphic assets were collected through various copyright-free image websites. The products images were gotten from a another hair website [Her Given Hair](https://www.hergivenhair.com/). The hero-images on the home page was created by AI on [Leonardo AI](https://leonardo.ai/). Bootstrap and Crispy Forms were used for the project's frontend to speed up the process and to keep the templates consistent. Further customisation to the buttons, forms, modals, toasts and user feedback processes were added to the project's CSS files. 

### Site Goals
1. To provide users with a place to purchase hair products.
2. To provide the users the ability to search and browse hair wigs, hair extensions, hair products and utensils.
3. To provide the users with the ability to save products to their wishlist
4. To provide the users with the ability to check their order history.
5. To provide the users with the ability to leave a feedback for products.
6. To provide the users with the ability to read through a blog and comment, like and write posts with full CRUD functionality.

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
 - View blog with CRUD functionality for comments and liking the posts. 
 - As a registered User you can write a post and send it to the admin for review.
 - As a registered user you can view, edit and delete your posts from your profile links.

<a href="#top">Back to the top.</a>

Key Features:

1. Initial Project Setup:
- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.
2. Products:
- Users can view products for sale and refine them by category.
- Users can sort products by price and rating.
- Users can view details about each product including image, description, price and reviews and review count.
- Search products by title or description.
- Registered users can leave reviews and ratings.
3. User Authentication:
- Users can register an account, allowing them access to all of the website's functionality.
- Registered users can login and access wishlist, reviews, past orders, thier written blog posts and saving personal details.
- Users can reset their password.
- Users can add or remove items from their wishlist.
- Registered users have CRUD functionality for thier reviews and ratings.
4. Orders and checkout:
- Users can add items to their shopping bag.
- Users can update the quantity of the items in their shopping bag.
- Users can remove products from their shopping bag.
- Users can use secure checkout functionality to pay for their items.
5. Admin functionality:
The functionality in this section is limited to superusers or admins.
- Admins can add products for sale.
- Admins can delete products from the system.
- Admins can edit products.
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

![Colour Scheme](https://res.cloudinary.com/dzesjeplp/image/upload/v1733263097/READMEPP5/Create-a-Palette-Coolors-12-03-2024_01_25_PM_zoe2ak.png)

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

1. User:
The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, hence why changes directly to this model are not advisory. The User model is connected to the UserProfile model with one to one relationship.

2. UserProfile:
The UserProfile model is a custom-created model to handle the user profile details.

3. PrimaryCategory
This model was created for the purpose of defining a primary category for the products. All products should have a singel primary category (Foreignkey relationship).

4. SpecialCategory
This model was created so that products can have one or many special categories or none (manytomany relationship).

5. Product
This is a custom product model. It is connected to the PrimaryCategory as a foreign key and SpecialCategory (manytomany relationship). 

6. Wishlist
This model stores products to a wishlist for authenticated users. It is connected to UserProfile and Product models as a ForeignKey

7. Review 
This model stores the user's reviews for a product. It is connected to the UserProfile and the Product models as a ForeignKey

8. Order 
This model holds all the information of the user's order. It is connected to the UserProfile as a ForeignKey.

9. OrderLineItem
This model is connected to the Order and Product as a ForeignKey. It is created for each item in the order




### Fonts
In addition to Bootstrap 5 built-in font family the below two fonts were used throughout the application
1. Poppins

![Poppins](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264757/Poppins-Google-Fonts-12-03-2024_01_36_PM_sjyzlq.png)

2. Libre Baskerville

![Libre Baskerville](https://res.cloudinary.com/dzesjeplp/image/upload/v1733263002/READMEPP5/readme/Libre-Baskerville-Google-Fonts-12-03-2024_01_38_PM_zataal.png)

<a href="#top">Back to the top.</a>

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

### Epic 1: Initial Setup, Backend, User Authentication, Frontend and Test Deployments 

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a developer, I want to initialize a new project repository so that we have a centralized location for code storage and version control| **MUST HAVE** |
| As a developer, I want to set up a development environment so that the team has a standardized and functional workspace | **MUST HAVE** |
| As a developer, I want to make the initial commit to populate the repository with a basic project skeleton | **MUST HAVE** |
| As a developer, I want to set up a Kanban board to manage the project’s tasks and workflow efficiently | **MUST HAVE** |
| As a developer, I want to create a frontend project skeleton so that i have a structured starting point for frontend development|**MUST HAVE**|
| As a developer, I want to implement the main layout and UI components so that the frontend has a consistent look and feel.|**MUST HAVE**|
| As a developer, I want to integrate Django Allauth into the project so that we can leverage its authentication capabilities.|**MUST HAVE**|
| As a user, I want to be able to register for an account so that I can access the application's features.|**MUST HAVE**|
| As a user, I want to be able to log in so that I can access my account and use the application.|**MUST HAVE**|
| As a user, I want to verify my email address so that my account is more secure.|**MUST HAVE**|


### Epic 2: Implementing Product Management and User Cart Functionality

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|    
| As a developer, I want to design and implement data models for all products so that product information can be effectively stored and retrieved. | **MUST HAVE** |
| As a developer, I want to create API endpoints for product management so that product data can be manipulated via the API.| **MUST HAVE** |
| As a user, I want to easily find and view products that interest me through a frontend interface complete with a filtering system into categories.| **MUST HAVE** |
| As a user, I want to add products to a cart before finalizing my shopping, and I want to include specific contexts like selected sizes and colours.| **MUST HAVE** |

### Epic 3: Implementing Stripe Checkout Functionality

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a developer, I want to set up a Stripe account and retrieve API keys so that I can integrate Stripe into the application.| **MUST HAVE** |
| As a developer, I want to integrate the Stripe API into the backend so that payments can be processed securely. | **MUST HAVE** |
| As a developer, I want to integrate Stripe's frontend library to capture user payment details securely.| **MUST HAVE** |
| As a user, I want a seamless checkout process that includes reviewing my cart, entering payment details, and receiving confirmation so that I can finalize my shopping 
| with confidence.| **MUST HAVE** |
| As a developer, I want to thoroughly test the Stripe payment process to ensure it's secure and reliable. | **MUST HAVE** |
| As a developer, I want to set up and handle Stripe webhooks so that the backend can receive real-time notifications about payment events and update the application state accordingly. | **MUST HAVE** |

  
### Epic 4: Implementing Admin Dashboard & User Profile Functionality

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a user, I want to read and write reviews for purchased products so that I can make more informed decisions later on and share my experiences.| **MUST HAVE** |
| As a user, I want to mark products as favorites so that I can easily find them again inmy wish list in the future. | **MUST HAVE** |
| As a user, I want a search function to find products based on keywords so that I can more easily find products that interest me. | **COULD HAVE** |
| As a user, I want a profile page where I can view and edit my personal information, my wish list and reviews, see my past purchases and request refunds. | **MUST HAVE** |

### Epic 5: Enhanced Interactivity and Robust Validation

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a user, I want to receive real-time feedback when filling out forms, so that I can correct errors before submission. | **MUST HAVE** |
| As a user, I want to see toast notifications after certain actions, so I'm assured that my action was successful. | **SHOULD HAVE** |
| As a user, I want to receive email notifications for essential activities like registration, password reset, and order confirmation, so I can stay informed.| **SHOULD HAVE** |
| As a User or Visitor I want to be able to navigate to the About Us and Contact Pages to get information about the site.| **SHOULD HAVE** |
| As a User I want to be able to navigate to the privacy policy page to learn about the policies of the site. | **COULD HAVE** |
| As a User I want to be able to read frequently asked questions to get information about questions I might have. | **COULD HAVE** |
| As a User I want to get information about how to return my product incase it is not what I want or I want another product. | **COULD HAVE** |
| As a User I would like to make use of discount codes if they are provided to enjoy the discounted sales price.|**SHOULD HAVE**|
| As a User I want to be informed of price reduction of products or products that are on sale so that I can make an informed purchase.
As an Admin I want to be able to set some of the products in the store on sale and to reverse this condition as well.|**COULD HAVE**|
| As a user, I want to reset my password in case I forget it, so that I can recover access to my account.|**SHOULD HAVE**|
| As a user I can filter to see the products in thier primary categories and also filter them with thier secondary categories.
As an admin I can edit the categories of the products.|**SHOULD HAVE**|
| As a User I want to be notified of how many items of the product that interests me to buy are in stock so that I can make an informed purchase.|**COULD HAVE**|


### Epic 6: Feature Completion and User Engagement Boosters

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a developer, I want to install and configure PostgreSQL so that the application has a scalable and cloud-based database. | **MUST HAVE** |
| As a developer, I want to create AWS S3 buckets so that we have a dedicated place to store static and media files. | **MUST HAVE** |
| As a developer, I want to configure Django to use AWS S3 so that static and media files are served from S3. | **MUST HAVE** |
| As a developer, I want to prepare the codebase for Heroku deployment to ensure that it meets Heroku's requirements. | **MUST HAVE** |
| As a developer, I want to deploy a test version of the application to Heroku to validate that it runs as expected in a cloud environment.| **MUST HAVE** |
| As a developer, I want to validate that all functionalities work as expected in the Heroku test environment.| **SHOULD HAVE** |
| As a user, I want to see carousels showcasing products categories and top products on the home page so that I can discover new and interesting products| **COULD HAVE**|
| As a developer, I want the README file to be comprehensive and up-to-date, so that anyone engaging with the project can have a full understanding of its scope, features, and strategies.| **MUST HAVE**|
| As a developer, I want to set up a custom domain for my application hosted on Heroku, so that it can be accessed via a more professional and memorable URL.| **WONT HAVE**|


### Epic 7: UI/UX Optimization Sprint

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a user, I want the design elements to be consistent across all pages so that the website feels cohesive and professional. |**MUST HAVE**|
| As a user, I want the website to be fully responsive so that I can have an optimal viewing experience on different devices.|**MUST HAVE**|
| As a user, I want immediate feedback for my interactions, like button clicks and form submissions, so that I know my actions have been acknowledged. |**SHOULD HAVE**|
| As a user, I want an intuitive navigation system so that I can easily find what I'm looking for. |**COULD HAVE**|
| As a user, I want the website to be accessible so that people with disabilities can also use it effectively. |**SHOULD HAVE**|
| As a user, I want the website to load quickly so that I don't have to wait to access content. |**COULD HAVE**|
| As a developer, I want to conduct a final UX audit to ensure that all UI/UX improvements have been effectively implemented. |**COULD HAVE**|
| As a developer, I want to review the project's current status and set up the Kanban board for the final phases, focusing on finalizing the project with tasks like UX/UI improvements, code refactoring, bug fixes, further testing, and documentation. I also want to consider potential future features. |**SHOULD HAVE**|


### Epic 8: Test Deployment and Project Completion

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a developer, I want to deploy the latest build of the project to an existing Heroku test environment. The goal is to verify that AWS services, the database, and all styling, static, and media files are functioning as expected. This will allow the team to validate the project's performance, functionality, and reliability under real-world conditions.|**MUST HAVE**|
| As a developer, I want to thoroughly test the checkout workflow, including the sending of confirmation emails and the operation of webhooks, to ensure that users experience a seamless and reliable checkout process. |**MUST HAVE**|
| As a developer, I want to identify and fix all critical and non-critical bugs so that users have a smooth experience. |**MUST HAVE**|
| As a developer, I want to finalize all features, optimizations, and tasks so that the project is ready for launch. |**SHOULD HAVE**|

<a href="#top">Back to the top.</a>

### Epic 9: Code Validation, Documentation, and Refinement

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a developer, I want to update the project documentation to reflect detailed descriptions of features, outline possible future enhancements for academic purposes, and enumerate the technologies used, to provide clear project understanding for evaluators and for my personal portfolio. |**MUST HAVE**|
| As a developer, I want to conduct thorough manual testing and write automated tests using Python's unittest framework to ensure the application functions correctly, aiming for a high-quality application. |**SHOULD HAVE**|
| As a developer, I want to validate my Python and JavaScript code to ensure there are no issues, and confirm that HTML and CSS are compliant with W3C standards, to ensure a high-quality, standards-compliant project. |**MUST HAVE**|
| As a developer, I want to use the WAVE tool to evaluate and enhance the accessibility of the web application, ensuring it is usable by people with various disabilities and complies with web accessibility standards. |**COULD HAVE**|
| As a developer, I want to utilize Google's PageSpeed Insights to analyze and enhance the performance of the web application, aiming to improve load times, efficiency, and overall user experience. |**COULD HAVE**|
| As a developer, I want to thoroughly review and clean up the project's codebase, removing any unnecessary commented code, redundant files, and ensuring overall code quality, to finalize the project with a clean, efficient, and maintainable codebase. |**MUST HAVE**|


#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In progress, Done, Won´t do and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow.

![Project](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264653/READMEPP5/Backlog-_-hairhotty-pp5-12-03-2024_04_34_PM_gagg4r.png)

## Features
## Header
The header section has the banner with information about a halloween sale going on and the discount code for a 55% reduction. This is a feature that will be implemented in the future. The banner messages scroll horizontally across the screen to catch the attension of a visitor immediatly. 
Then there is the logo, a serach bar and the account and bag icons. Below that are the links and dropdown menus of the different pages of the website.

![Header feedback](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264658/READMEPP5/headerfeedback_gxrccu.png)

#### Navbar
The navbar was built using bootstrap 5 and it is fully responsive. The search bar allows the users to search for products by keywords from any page of the website. The My Account drop down gives the user the option to log in or register. If the user is authenticated additional menu options are displayed like my profile and Product Managements (if the user is a superuser). The shopping bag icon is a link to the shopping bag and it also displays the total of the items in the bag.
The nav links allow the user to refine the products by category, special offers (both are dropsdwon menus) or to browse through the FAQ and contact us pages. There is a dropdown for special offers which allows the user to see the new arrivals, deals and best collections.

![navbar desktop](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264663/READMEPP5/navbardesktop_exgult.png)

![navbar mobile](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264665/READMEPP5/navbarmobile_byj4wg.png)

![navbar mobile with dropdown](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264664/READMEPP5/navbardropdownonmobile_jk1xxg.png)

![All products dropdown menu](https://res.cloudinary.com/dzesjeplp/image/upload/v1733268723/allproductsdropdownmenu_bynd0c.png)

![Special offers dropdown](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264677/READMEPP5/specialoffersdropdownmenu_f8n5tm.png)

### Toasts
Toasts from Bootstrap were implemented to provide customers with feedback regarding their actions on the website.

![toasts](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264678/READMEPP5/toasterror_qpo6zx.png)


#### Footer
The footer was built as an example model featured on the bootstrap webseite consisting of lists of the different pages of the site and links to social media.

![footer](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264656/READMEPP5/footer_n9kv4t.png)

#### Newsletter
Part of the footer is a newsletter, which asks users to subscribe by applying thier emails addresses to receive the most recent offers and discount codes. The form was integrated using MailChimp.

![newsletter](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264666/READMEPP5/newsletter_scietk.png)

### Mailchimp Dashboard
Mailchimp was implemented as a marketing tool to gather email addresses of users to use for email marketing.

![Mailchimp Dashboard](https://res.cloudinary.com/dzesjeplp/image/upload/v1733345637/Contacts-Mailchimp-11-28-2024_07_00_PM_uzsz2d.png)

### Home Page
#### Hero Section
The hero section is the beginning of the whole customer's journey. That is why I made it a priority to create an appealing hero section with a carousel, featuring the highlights of certain seasons, like halloween. Other seasons like black friday or christmas sales can be easily implemented. 
All three hero section images were designed using an AI photo creation site ![Leonardo.ai](https://app.leonardo.ai/). Using Canva the first image was eidted with text. 
All three images have a call-to-action button Shop Now which invites the user to browse through the available products.

![hero section](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264660/READMEPP5/herosection_nui3mx.png)

#### Trust Badges
The trust badges serve as visual indicators to reassure the visitors about specific aspects of the services available.

![trust badges](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264679/READMEPP5/trustbadges_aigkhv.png)


### Products Page
The all products page renders all products to the user. They have the option to sort the products by price or rating. This page also displays the number of the products available depending on which category is chosen to be displayed. At the end of the products result there is pagination to help the user navigate easily through multiple pages of products.
![all products](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264652/READMEPP5/allproductssortedwithhighprice_zzjlji.png)

![pagination](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264668/READMEPP5/paginationallproducts_welpwd.png)

<a href="#top">Back to the top.</a>

### Products Card
The product card consist of an image of the product, title, price, number of reviews, category links, discount percentage and an add to Bag button. A flipping heart draws the user´s iattention to click it and not registered user´s get the promnt to register so that they can add the product to thier wishlist. Registered users can add the product to thie wishlist by clicking the heart. If the product is on sale, then the old price will be displayed with a line through, followed by the new price and a little label at the top of the image showing the percentage of the discount.

![product card](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264672/READMEPP5/productscardwithoutsale_s1ytdx.png)

![product card sale](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264671/READMEPP5/productscard_qfln7n.png)

### Products-Detail Page
On the page's left side, a product image is displayed. On the right side, the most important information about the product is displayed. This includes the title, number of reviews, price, stock levels, add to wishlist icon, sizes with dropdown list of sizes if the product has sizes, a quantitiy choice form, an add to bag button and return to shop button, returning the user to the all products page. 
Below the top section, there is a section with tabs allowing the user to switch between description and reviews. 
The reviews section allows an authenticated user to submit a review for a product. The overall rating is calculated and the number of stars are displayed in the top section of the page. Authenticated users can edit and delete their reviews from the same tab. 
The description tab includes a short description of the product which helps the users in making informed decision if they wish to purchase the product.


![product detail page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733437832/productdetailpageafterfix_fhxyad.png)

The reviews section allows the user to rate the product choosing from 5 stars and then writing a review for the product.These two aspects are stored together and have to be completed together.

![reviews](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264676/READMEPP5/reviewssection_kz3fit.png)

This is a flipping heart to catch the attention of the user so that they can click on the heart and add the product to thier wishlist, after which the heart displays as a solid crimson heart.
![add to wishlist](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264651/READMEPP5/addingtowishlist_mrypjp.png)

### Edit review page
This page allows the user to edit their review in the event they changed their mind. It renders prefilled with the original data. The rating with stars is also in this section for the users to edit.

![edit-review](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264655/READMEPP5/editreview_r2egsd.png)

### Delete review confirmation
This page asks the user for confirmation if they wish to delete their review

![delete-review](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264654/READMEPP5/deletereview_wxevmv.png)

### Blog

The Blog page consists of 6 blogs per page when the link is clicked from the navbar. Each Blog card has a link via the title to the detail blog post. The name of the author, the number of likes and comments are on the index page of the blog. 

![blog all posts](https://res.cloudinary.com/dzesjeplp/image/upload/v1733401931/postindexwithlikedandunlikedheart_dnvnb0.png)

On the detail page of each blog post, the user is invited to leave a comment, but can only do that if they are registered. Registered users can write, edit and delete thier comments. They can also like and unlike the post. 

![detail blog post](https://res.cloudinary.com/dzesjeplp/image/upload/v1733401930/postdetailview_sergjr.png)

Registered users can write a post for the blog. When they click the account icon on the navbar, a dropdown menu appears with thier profile and an Add a post link. Once clicked a form appears where they can write thier text using summernote for a good UX experience, add images and submit the post. In thier profile section under the tab my-posts they can view all thier posts irrespective of publish status and edit and delete thier posts.

![Add a post](https://res.cloudinary.com/dzesjeplp/image/upload/v1733401928/addpost_pym7jv.png)

![Edit a post](https://res.cloudinary.com/dzesjeplp/image/upload/v1733401928/editpost_eo0xau.png) 

![delete a post](https://res.cloudinary.com/dzesjeplp/image/upload/v1733401928/deletepostmodal_gcavou.png)

### Contact Page

The Contact page consists of all the contact methods with links where appicable, like email, phone number and physical address. There is also a contact form for all users to use, not only registered users. 

![contact-us-page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733266188/contactus_ke9qgv.png)

<a href="#top">Back to the top.</a>

### FAQ Page
The FAQ page consists of the most frequently asked questions.If the user clicks a question, a dropdown appears with the answer. 

![faq-page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733266189/FAQ_yuv25z.png)

### Privacy Policy Page
The Privacy Policy page was generated using ![Privacy Policy Generator](https://www.termsfeed.com/privacy-policy-generator/) and displays the privacy policy of the business for all users to access.

![privacy-policy-page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733266683/privacypolicy_gfcjxf.png)


### About Us Page
The About us page tells the user about the business and the background story and philosphy behind the brand. There are links to the social media sites to give more information to the users. Through this the user feels more connected to the brand.

![About-Us-page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733266682/aboutus_vpklny.png)

### Return Page
The Return page consists of the most frequently asked questions about returning a product.

![Return-page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733266190/returns_etgzot.png)

### Customer-Service Page
The Customer service page is the same link to the contact-us page, just incase users or customers are specifically searching for customer services.

### Event Page
The Event page consists of an advertisement of future planned online events with hair stylists, influencers from the social medial networks. There is the invitation to join the newsletter again explicitly to be informed when this event will take place.

![Event-page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733340614/eventpage_gkxdjn.png)

### My Profile Page
This section is accessible only to authenticated users.
This section contains three pages - my profile, my orders, and my wishlist

#### Profile
This page renders a form for the user's address and phone number. If the user has any details saved, it renders prefilled.

![profile](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264675/READMEPP5/profile_teosyb.png)

#### Order History
This page displays the past orders of this user.

![orders](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264667/READMEPP5/orderhistory_rcwuk0.png)

#### My Wishlist
This page displays the items in the wishlist. It uses the same pagination functionality of 6 products per page like the all products page.

![wishlist](https://res.cloudinary.com/dzesjeplp/image/upload/v1733267067/mywishlist_b3l6bc.png)

#### My Posts
This page displays the posts a registered user has written so that they can edit, delete or view them. The published status is also visible to the user so they know if the status is still in a draft status or published status and therefore visible for all. 

![my posts](https://res.cloudinary.com/dzesjeplp/image/upload/v1733423784/POSTS_m1c7jo.png)

After pressing the edit button the use is taken to the Add a Post page with the prefilled postform with the content of thier post. They can edit it and resubmit, whereby the status will change from published to draft again if it was formerly published or remain in the draft status if that was the former status.

When users choose to delete their post they are asked through a modal if they are sure they want to delete thier post as this step can not be reversed.
![my posts delete ](https://res.cloudinary.com/dzesjeplp/image/upload/v1733423784/deletmodelposts_j0ea1e.png)

### Admin CRUD Functionality:
The admin has the chance while logged on the site on the frontend to carry out CRUD functionality for the products.

#### Add Products
This page renders the product creation form and all required fields to add an item to the database. Admins can add products on sale by checking the on-sale box and adding the sale price or discount. If the on_sale box is not checked the product will display with the original price.

![add products](https://res.cloudinary.com/dzesjeplp/image/upload/v1733346711/addproductadmin_sh6rex.png)

#### Edit Product
This page renders the product form prefilled with the existing data in the database. It allows the admin to modify all details about the product.

![edit product](https://res.cloudinary.com/dzesjeplp/image/upload/v1733346711/editproductadmin_b41bar.png)

The admin receives an update success message after succesfully updating the product.

![edit product success message](https://res.cloudinary.com/dzesjeplp/image/upload/v1733346711/editedimagewithtoastsuccessmessage_hiapba.png)

#### Delete Product
This delete process does not come with a modal asking if the admin is sure they want to delete the product. The admin receives a success message after the deletion is complete. In the future a delete modal will be implemented to ask the admin if they really want to delete the product, as the delete button is very small and it could be clicked by accident and then a product will be deleted that the admin doesn´t want to delete.

![delete product](https://res.cloudinary.com/dzesjeplp/image/upload/v1733346711/deletedproductsuccess_y91igc.png)

### Shopping bag
The shopping bag can be accessed from the main nav menu. The shopping bag table section provides a clear and organized representation of the items added to the shopping bag. Each item has a small image, product name, price, quantity, and subtotal. The users can upgrade the quantity or delete items from the bag with the help of the buttons provided.
On the right side bottom side of the page the users can view their subtotal, delivery charges, and total on medium screens and above. 

![shopping bag](https://res.cloudinary.com/dzesjeplp/image/upload/v1733353289/shoppingbag_tbfquk.png)

On mobile screen the information of the Grandtotal and checkout buttons appear on the top of the screen with the rest of the details for the shopping bag appearing below.

![shopping bag o nmobile](https://res.cloudinary.com/dzesjeplp/image/upload/v1733353375/shoppingbagonmobile_dmdhhf.png)

If there are no products in the shopping bag there is a view for that with a link to invite users to keep shopping.

![shopping bag empty](https://res.cloudinary.com/dzesjeplp/image/upload/v1733353288/emptyshoppingbag_qbabdi.png)


### Checkout
This page contains a form for the user's delivery and payment information and a summary of the user's order. If the user has an account, they can save their delivery information on their profile to automatically be filled in the checkout process.
- The checkout Form
In the checkout form the user can add their details and if they're logged in, can check the box to save their details for future transactions. Users must enter their payment information before completing the checkout and all payments are handled via Stripe. If there is an error with the creditcard details, stripe will handle the process and the user gets an error message and the checkout is stalled. 

![checkouterror](https://res.cloudinary.com/dzesjeplp/image/upload/v1733348064/ccdateexpired_dgk9og.png)

![checkouterror](https://res.cloudinary.com/dzesjeplp/image/upload/v1733348064/ccinvalidnumber_talxsl.png)

![checkouterror](https://res.cloudinary.com/dzesjeplp/image/upload/v1733348064/ccpostalcodeerror_k1lsvh.png)


- Order summary
A final summary of the user's order is shown containing all the user's bag items, quantity and subtotal for each item. The user can also see their order total, delivery costs, any discounts that have been applied and the grand total in the summary.

![checkout](https://res.cloudinary.com/dzesjeplp/image/upload/v1733347563/checkout_dbhwn8.png)

 A vibrant pink spinner engages the user while stripe processes thier payment intent.

![spinner](https://res.cloudinary.com/dzesjeplp/image/upload/v1733347563/spinner_ncjp8t.png)

### Order confirmation page
After the order has been completed, the user is redirected to a confirmation page containing a final rundown of the order and what the user purchased. This page can be accessed again from the user's profile if they have an account on the site by clicking the order number from the list of past orders.

![order confirmation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733347563/checkoutsuccess_jfrriv.png)

### Confirmation email
Once the order is processed and payment has been received, the user will receive an email with the order details.

![email confirmation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733345352/Hair-Hotty-Confirmation-for-Order-Number-angela-anjorin-gmail-com-Gmail-12-04-2024_09_48_PM_v4it14.png)

### User Authentication
The website uses django allauth's built in functionality which allows the users to register and log in securely. There is also a reset password functionality which allows the user to input their email address and receive a link where they can securely reset their password.

## Future Features
- Add Stock amount for products with and without sizes.
- Add different wig hair lenghts and colours. This will cause every product to have many variations and the management of the complexity will be a challenge to master.
- Add a pop up with the current discount code which can be updated by the admin. Or allow the admin access to the edit the banner with new discount codes like the one displayed for the halloween season. 
- CRUD functionality to update the carousel images with new catching edited images depending on the shopping season, exeample the black friday sales, or upcoming christmas sales.
- Add an event section to host a live online hair bazaar, with vendors, hair stylists and have a lottery with special prizes. Customers can buy the tickets to the lottery online and it will be stored on thier profile and they will be notified per email if they win.
- Allow different user profiles, like hair stylists can have a unique customizable profile to highlight thier business and make this accessible to other users so that they can get potential customers. 
- For the online hair bazaar, you can have many different user profiles, like for vendors, hairstylists or moderators of the event.
- Allow admin to update only stock level fields as a quicker option to restock items. 
- On the frontend provide the admin with a good overall view of the stocks of the products, so that they can be easily updated. Allow the admin a good overview and management of orders and returns.
- Allow the management of discount codes by the admin.
- Have a return section on the user´s profile so that they can monitor thier returns. 
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

![Hair Hotty Facebook Business Page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733264650/READMEPP5/-20-Hairhotty-Facebook-12-03-2024_04_23_PM_f4rqhi.png)
*Hair Hotty Facebook Business Page*


## Testing
Testing documentation can be found here: [TESTING.md](TESTING.md)

## Bugs
Detail Bugs and thier fixes can be found here: [TESTING.md](TESTING.md)
 
<a href="#top">Back to the top.</a>

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

<a href="#top">Back to the top.</a>

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

<a href="#top">Back to the top.</a>

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
- [Carousel images](https://app.leonardo.ai/)
- [Logo](https://canva.com/)


### Code and Content
* Boutique Ado Walkthrough was used for the base of this project
* Images for the shop are from Her Given Hair <a href="https://www.hergivenhair.com/" target="_blank"><strong>Her Given Hair</strong></a>
* Images and content for the blog section of site are from Black Curl Magic <a href="https://www.blackcurlmagic.com/blog/" target="_blank"><strong>Black Curl Magic</strong></a>
* I got additional inspiration from the following :
    1. [Portfolio Project 5 by Dayana_N](https://github.com/Dayana-N/Book-Heaven-PP5)
    2. [Portfolio Project 5 Emma Hewson](https://github.com/emmahewson/island-bees)
    3. [Portfolio Project 5 Amy Richardson](https://github.com/amylour/everneed), especially for the testing and readme section of the project.
    4. [Portfolio Project 4 Angela Anjorin](https://github.com/angelaanjorin/travel-doc), I used a lot of my own code from my Project 4 for the blog section of the project.
    5. [Eleganz Hair](https://www.elegance-hair.de/index.php?lang=0&)
* [Styling django all auth pages](https://builtwithdjango.com/blog/styling-authentication-pages)
* [The right way to use Many To Many Field](https://www.reddit.com/r/django/comments/l937f1/the_right_way_to_use_a_manytomanyfield_in_django/)
* [Looping through integer in templates](https://copyprogramming.com/howto/how-do-i-loop-a-intergerfield-in-django-templates#how-do-i-loop-a-intergerfield-in-django-templates)
* [Product Card](https://bestjquery.com/tutorial/product-grid/demo199/) - the product cards were modified to suit the project
* [How to create automated tests](https://learndjango.com/tutorials/django-testing-tutorial)

### Acknowledgements
- Huge thank you to my mentor Gareth McGirr for all the help and resources.
- The Slack community and tutor support were very helpful.

### Comments
I wouldn´t have started without the urging and help of my partner Eric Jones with this training for full-stack developers from Code Institute. And it was a very rewarding journey, and I thank him wholeheartedly. I want to thank my children Lucas and Gabriel for thier patience and understanding throughout my training. Thank you to my parents and siblings for thier support.

<a href="#top">Back to the top.</a>