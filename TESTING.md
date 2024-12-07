# Testing

This is the TESTING file for the [Hair Hotty](https://app-hairhotty-9ddf6a2299e6.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

# Table of content
- [Testing](#testing)
   * [Validation](#validation)
      + [HTML Validation](#html-validation)
      + [JavaScript Validation](#javascript-validation)
      + [Python Validation](#python-validation)
      + [CSS Validation](#css-validation)
      + [Lighthouse Scores](#lighthouse-scores)
      + [Lighthouse](#lighthouse)
            * [Desktop Results:](#desktop-results)
               + [Mobile Results:](#mobile-results)
      + [Wave Accessibility Score](#wave-accessibility-score)
   * [Manual Testing](#manual-testing)
      + [User Input/Form Validation](#user-inputform-validation)
      + [Backend/Admin Panel](#backendadmin-panel)
      + [Browser Compatibility](#browser-compatibility)
      + [Responsiveness](#responsiveness)
      + [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
   * [Bugs](#bugs)
   * [Fixed Bugs](#fixed-bugs)
   * [Unfixed Bugs](#unfixed-bugs)

## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
Via the deployed Heroku app link, I was able to carry out the validation using the url method.

![html validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/Showing-results-for-https-app-hairhotty-9ddf6a2299e6-herokuapp-com-Nu-Html-Checker-12-06-2024_03_05_PM_kzihnh.png)  

All HTML pages were validated and received a 'No errors or warning to show' result as shown above.

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript code added to the project. External JS, for Bootstrap, jQuery and Fontawesome purposes were not validated through JSHint.

| Page | Screenshot | Errors |
| ---- | ---------- | ------ |
| bag  | ![js from Bag page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500628/JSHint-bag_u7ggll.png) | none |
| blog - Comment js | ![js from post section](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500628/JSHint-comments-blog_blri1k.pngg) | none |
| Stripe JS | ![js from Stripe elements](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500628/JSHint-a-JavaScript-stripe_oyrfik.png) | none |
| Products Product quantitiyinput Script | ![js from product quantityinput script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-quantityinput_haelbp.png) | none (code has been highlighted red at the top of the code block but no errors returned from JSHint and code functions as intended. I could not get a definitive answer on why JSHint colours these lines red.) |
| Products  | ![js from sortproducts script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-sortproducts_houdhz.png) | none |
| Products Add and Edit Product Script | ![js from add and edit product page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500625/JSHint-a-JavaScript-add-products_vqifrh.png) | none |
| Products Productdetail Script | ![js from productdetail page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-productdetail_exlvow.png) | none |
| Profile| ![js myposts script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500625/JSHint-a-JavaScript-mypostsprofile_vkg0d9.png) | none |
| Review - Ratings Selector Script | ![js from ratings selector script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733545899/JSHint-a-JavaScript-ratinsselectreviews_wbu0jd.png) | none |
| Base Script | ![js Sort Selector Script script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-sortselectorproduct_mmq6xz.png) | none |
| Base Script | ![js mailchimp script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500625/JSHint-a-JavaScript-mailchimp_ddtl2s.png) | none |
| Base Script | ![js toast script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500628/JSHint-a-JavaScript-toast_bsjawq.png) | none |


<a href="#top">Back to the top.</a>

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files that were created or edited by myself. No issues presented and line lengths were double checked. I have included some screenshots with the results below. none = no issues present.

| Feature | admin | forms | models | urls | views | extra |
|---------|----------|----------|-----------|---------|----------|-------|
| bag  | n/a | n/a | n/a | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733510719/CI-Python-Linter-urlsbag_n6eg8u.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512156/CI-Python-Linter-bagviews_fknnha.png) | contexts ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733510719/CI-Python-Linter-bagcontexts_lx7vlb.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733510719/CI-Python-Linter-bagutils_gwbtlc.png) |
| blog | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512429/CI-Python-Linter-adminblog_pe1zxz.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512430/CI-Python-Linter-blogforms_mfq4kl.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512430/CI-Python-Linter-blogmodels_xhwggp.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512431/CI-Python-Linter-blogurls_kggm96.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733515136/CI-Python-Linter-blognewviews_xvwhsa.png) | n/a |
| Checkout | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512593/CI-Python-Linter-checkoutadmin_k7f4kw.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512594/CI-Python-Linter-checkoutforms_me2jcn.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512596/CI-Python-Linter-chheckoutmodels_tqugaf.png) | none | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512595/CI-Python-Linter-checkouturls_iqyzmb.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512596/CI-Python-Linter-checkoutviews_dbmaiy.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512595/CI-Python-Linter-checkoututility_ahxmqh.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512594/CI-Python-Linter-checkoutsignals_qfk07w.png)|
| Home | n/a | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512942/CI-Python-Linter-homeforms_ya81p7.png)| n/a |none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512942/CI-Python-Linter-homeurls_iedc23.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512942/CI-Python-Linter-homeviews_fv8q4z.png) | n/a |
| Products | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513124/CI-Python-Linter-productsadmin_fppzrq.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513125/CI-Python-Linter-productsforms_ucxbmh.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513125/CI-Python-Linter-productsmodel_oqvigt.png) | none![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513126/CI-Python-Linter-productsurls_fq70b0.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513127/CI-Python-Linter-productsviews_nqf0uf.png) | none |none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513126/CI-Python-Linter-productsutils_j09leh.png) | none |
| Profiles | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513347/CI-Python-Linter-profilesadmin_si7b2n.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513347/CI-Python-Linter-profilesforms_iezoxf.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513348/CI-Python-Linter-profilesmodels_pgkwob.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513349/CI-Python-Linter-profilesurls_aoeemv.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513349/CI-Python-Linter-profilesviews_kjqgqf.png) | n/a |
| Reviews | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513594/CI-Python-Linter-reviewsadmin_y4yotd.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513595/CI-Python-Linter-reviewsforms_yau10a.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513595/CI-Python-Linter-reviewsmodels_xmsmqh.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513596/CI-Python-Linter-reviewsurls_s1xag2.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513597/CI-Python-Linter-reviewsviews_rdtjiu.png) | n/a |

<a href="#top">Back to the top.</a>

### CSS Validation

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS files. External CSS for Bootstrap, provided by [CDN](https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css) was not tested.

I used the url of the deployed Heroku to carry out the validation. Results were good as shown below.
![css validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/W3C-CSS-Validator-results-for-https-app-hairhotty-9ddf6a2299e6-herokuapp-com-CSS-level-3-SVG--12-06-2024_03_07_PM_anlvsa.png)


### Lighthouse Scores

### Lighthouse
Lighthouse was used to test Performance, Best Practices, Accessibility, and SEO on Desktop.

##### Desktop Results:
![Lighthouse Desktop Result](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/Lighthouse-Report-Viewer-12-06-2024_02_14_PM_qgngib.png).

###### Mobile Results:
![Lighthouse Mobile Result](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/Lighthouse-Report-Viewer-12-06-2024_02_18_PM_m0ygdz.png).


### Wave Accessibility Score

Accessibility was included in every planning stage for Hair Hotty, through the use of the WAVE report tool I could ensure that any necessary changes were made to make the website as accessible as it could be. Only 2 issues persisted with form labels. Form label was assigned to the newsletter field with hidden visibility styling applied in the CSS file, as it affected the form field positioning, but error persisted. No other issues, contrast or structural issues.

![WAVE Report](https://res.cloudinary.com/dzesjeplp/image/upload/v1733498867/WAVE-Report-of-Hair-Hotty_o5azwo.png)  
*WAVE Report for Hair Hotty*

<a href="#top">Back to the top.</a>

## Manual Testing

### User Input/Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process appropriately.

| Feature                    | Tested?  | User Input Required | User Feedback Provided     | Pass/Fail | Fix |
|----------------------------|----------|---------------------|----------------------------|-----------|-----|
| Header Banner              | Yes      | None | Second below banner message moves horizontally across the screen | Pass | N/A |
| Navbar Logo and Icons      | Yes      | Click Links bring user to correct destination    | Text Colour Change/Icon Animation/Dropdowns | Pass | N/A |
| Home Page                  | Yes      | Hover/Click interactive features | Carousel moves| Pass | N/A |
| Home Page                  | Yes      | Hover/Click Shop button with interactive features | Button changes color vby hovering and takes the user to the all products shop page | Pass | N/A |
| Register Page              | Yes      | Text Input/Click Links | Form field highlight/Button animation/ change on hover/Toast message | Pass | N/A |
| Email Validate             | Yes      | Click Links | Button animation/Toast message | Pass | N/A |
| Forgot Password            | Yes      | Text Input/Click Links | Form field highlight/Button animation/Toast message | Pass | N/A |
| Log In Page                | Yes      | Text Input/Click Links | Form field highlight on hover/Button animation//Toast message | Pass | N/A |
| Log Out Page               | Yes      | Click Links bring user to correct destination | Button animation/Toast message | Pass | N/A |
| Account - My Profile       | Yes      | Text Input/Click to Save | Form field highlight/Button animation/Toast message | Pass | N/A |
| Account - My Orders        | Yes      | Click to view old orders | Text highlight/Button animation/Toast message | Pass | N/A |
| Account - My Wishlist      | Yes      | Click heart to remove from wishlist| Heart animation/Toast message | Pass | N/A |
| Account - My Posts         | Yes      | Click to delete or edit post | Delete modal/ Add post rendered with post/Button animation/Toast message | Pass | N/A |
| Search                     | Yes      | Text Input/Click to Search | Pop up Modal/Form field highlight/Button Animation | Pass | N/A |
| Events Page                | Yes      | Text Input/Click to Subscribe to Newsletter | Success Message from Mailchimp/Form field highlight/Button Animation | Pass | N/A |
| Contact Us Page            | Yes      | Text Input/Click to Save/ contact links | Pop up Modal/Form field highlight/Button animation/Toast message/contact links work | Pass | N/A |
| Blog index                 | Yes      | Click to open post detail page/click to view next pages| Post titel highlight/Button Animation | Pass | N/A |
| Blog detail                | Yes      | Text Input/Click heart to like | Pop up Modal/Form field highlight/Button Animation/Toast messages | Pass | N/A |
| Newsletter Sign Up         | Yes      | Text Input/ Click to Subscribe | Button animation/New tab subscription confirmation | Pass | N/A |
|  All Products page         | Yes      | Click product image brings user to product detail page/click heart/click pagination buttons/sorting section/primary category link | Pointer change on hover of category link/ product´s image, heart changes colour/Toast message, Navigation to next page/sorting works | Pass | N/A |
| Add Product(admin)         | Yes      | Navigated to Admin Dashboard, clicked on 'Product Management', Completed form, Form submits to display the product, but the image is not rendered. | Form field highlight/Button animation/Toast message, new product uploaded. | Fail | Fix the issue with crispy forms incompatibility for Bootstrap 5 and Media storage of images |
| Edit Product(admin)        | Yes      | Navigated to Product, clicked 'Edit', Completed form, Form submits correctly to display the edited product. | Form field highlight/Button animation/Toast message, product updated. | Pass | N/a |
| Delete Product(admin)      | Yes      | Navigated to Product, clicked 'delete'. |  Pass | N/a | |
| Add post                | Yes      | Navigated to Account for registered users, clicked 'Add post', Completed form, Form submits. | Form field highlight/Button animation/Toast message, new post in draft and accessible in my_posts for CRUD functionality. | Pass | N/A |
| Edit post               | Yes      | Navigated to Profile, my posts, clicked 'Edit post', Completed form, Form submits correctly to display the edited post. | Form field highlight/Button animation/Toast message, post edited and availabe in my-post until published by admin. | Pass | N/A |
| Product Detail - heart     | Yes      | Click the heart  | Adds the product to wishlist or removes it | Pass | N/A |
| Product Detail- Rating     | Yes      | None | Shows the correct average | Pass | N/A |
| Rating/Reviews Section     | Yes      | Click dropdown tab, click stars, write review | Pop up Modal/Form field highlight/Button animation/Toast message/ | Pass | N/A |
| Edit Review                | Yes      | Navigate to review section tab, click edit button, completed form appears on another page, Form submits correctly to display the edited product. | Form field highlight/Button animation/Toast message, review updated. | Pass | N/a |
| Delete Review              | Yes      | Navigated to review section, click 'delete button'| New page with delete or cancel buttons, button animation/Toast message, review deleted. | Pass | N/a |
| Privacy Policy             | Yes      | Click the links in text  | Opens all links on click | Pass | N/A |
| Product Quantity           | Yes      | Click increment/decrement | Colour change on hover/product quantity successfully changed | Pass | N/A |
| Product Sizes              | Yes      | Click dropdown/Click to select | Form field highlight/Size highlight | Pass | N/A |
| Checkout                   | Yes      | Click 'Secure Checkout', correct products in bag, entered delivery and payment details, submitted form to process payment. | Form field highlight/Button animation/Toast message, Loading spinner when processing order, order processed saved to account and email sent. | Pass | N/A |
| Footer                     | Yes      | Click Links brings user to all referenced Pages | Font colour change on hover | Pass | N/A |
| FAQ Page                   | Yes      | Click opens the dropdown answers to the FAQs | colour change on click | Pass | N/A |
| Returns Page               | Yes      | Click opens the dropdown answers to the Return Questions | colour change on click | Pass | N/A |
| About Us                   | Yes      | Click social media links | Opens the relevant links on click | Pass | N/A |
| Privacy Policy             | Yes      | Click the links in text  | Opens all links on click | Pass | N/A |

<a href="#top">Back to the top.</a>


### Backend/Admin Panel
* I have tested the Admin Panel repeatedly since the start of the project development. All the models are working without issues.  
  I have created, deleted, and updated data in all models without errors. The models have the behavior expected for what they were built for.
* Whenever a user submits a post the Superuser has to approve it before it will be displayed on the website. This functionality is working without issues. The comments to the posts are visible and editable as well.
* Through the admin I can add products and edit and delete them. 
* The orders are visible at the backend with CRUD functionality. 
* The reviews are visible with CRUD functionality.
* The wishlist is visible and the person it belongs to as well.
* The profile information of all the users are visible.
* The email addresses are also visible of all users.
* The users have a seperate section due to allauth, where the admin can give them differnt permissions to the site.


### Browser Compatibility

Hair Hotty was tested on the following browsers, purchases were made, post/products added/edited/deleted, error pages, all features were accessible and working as intended:

- Chrome v117.0.5938.92
- Firefox v114.0.2
- Edge v114.0.1823.79
- Safari v16.5.1

| Browser | Issue | Functionality |
|---------|-------|---------------|
| Firefox | None  | All Intact    |
| Edge    | None  | All Intact    |
| Safari (iPad Pro) | None | All Intact  |
| Chrome (Main browser used in development) | None | All Intact |

### Responsiveness

Using the Bootstrap framework allowed a more rapid development of a responsive website. Starting with mobile first, Hair Hotty was created to ensure the customer has an unhindered, positive experience when shopping. Hair Hotty was regularly tested during development using Dev Tools to check for display issues on iPhone4 -> iPhone 12/Samsung Galaxy S20, iPad/iPad Pro and laptop/desktop screen sizes. Once deployed to Heroku, Hair Hotty was tested on real world devices. No major issues were detected, changes were made to the my wishlist view to make the product cards responsive on all devices with a good layout. There were no major differences between desktop and tablet views thanks to the Bootstrap Grid system of columns. 

### Dev Tools/Real World Device Testing

Responsiveness testing was carried out using Google Dev Tools on the devices detailed within the below table. Responsiveness was evident on all features throughout all tested devices.

**Dev Tools Device Testing - all features tested, issues noted below**
| Device  | Feature    | Issue  | Fix  |
| ------- | ---------- | ------ |------|
| iPhone 4 | Order History table | Content overflow on y-axis | Separate media query created for screens max-width: 350px to cope with iPhone4 320px screen width, font-size reduced for order history table |
| iPhone12 Pro | All features | None | None  |
| Samsung Galaxy S20 | All features | None | None  |
| iPad Pro | All features | All features | None | None |

**Real World Device Testing**
| Device      | Feature    | Issue  | Fix  |
| ------------| ---------- | ------ |------|
| OPPO Reno 8 Lite |   All features    | No issues | None needed |
| iPhone XR | All features |  No issues  | None needed |
| iPhone 12  | All features | No issues | None needed |
| Samsung Galaxy S21 | All features | No issues | None needed |
| iPad Pro 2021 |    All features      |    No issues    |  None needed |
| Acer Aspire 3 2019 laptop | All features | No issues | None needed |

<a href="#top">Back to the top.</a>

## Bugs

## Fixed Bugs
* Initially I had problems at the with the webhook handler of my project. I could mke a payment intent but I was not receiving the feedback that stripe was sending back to my computer or project. At first I thought it was a firewire issue and I even downloaded a programm from stripe to set up a runs tests called cli. It runs on the terminal of the computer. It was able to receive the webhook handler or event as stripe has renamed it bit could also not send that same information to my program. It was with the help of tutor support that we figured out that stripe had made an update. To handle the payment intent with the webhook from Stripe  it was no more that the billing details were equal to (billing_details = intent.charges.data[0].billing_details) but (billing_details = stripe_charge.billing_detials) and the grand total was also different. See below code.
![webhook handler issue](https://res.cloudinary.com/dzesjeplp/image/upload/v1733539751/Dashboard-_-New-business-_-Stripe-Test--11-26-2024_07_58_PM_ngcjmw.png).

![webhook handler issue](https://res.cloudinary.com/dzesjeplp/image/upload/v1733539751/webhook_handler-py-Hair-Hotty-Gitpod-Code-11-26-2024_07_39_PM_vsriks.png).
* I had a lot of other smaller bugs along the way, like that the STATIC ROOT information to my settings.py file. 

<a href="#top">Back to the top.</a>

## Unfixed Bugs
![Add Product](https://res.cloudinary.com/dzesjeplp/image/upload/v1733537220/Hair-Hotty-Products-12-07-2024_02_49_AM_wb5cyj.png).
![Add Product](https://res.cloudinary.com/dzesjeplp/image/upload/v1733537137/DoesNotExist-at-products-delete-677913e5-f5c2-4500-bf44-7ad479e28551--12-07-2024_02_48_AM_wzfkkd.png).
![Add Product](https://res.cloudinary.com/dzesjeplp/image/upload/v1733538391/add_product-html-_-add_product-html-Hair-Hotty-Gitpod-Code-12-07-2024_03_26_AM_ixw6n5.png).
* I think the problem lies with Post method and that although the image is stored in the media directory, the product is not accessible because it is not saved in the databank. Trying to delete the image provides the error shown below.It could also lie with the issues I had been encountering with the AWS s3 storage system.

* I spent a considerable amount of time trying to add stock amount to the products. But ran into so many issues with the products with sizes. I tried using the instance or as I called it virtual shopping session and bag content to control the different quantity amounts of the different sizes. Initially I had the quantity input javascript file in my static directory and had it called in the base template which caused so many issues with both the product detail and shopping bag templates calling on the script. I had conficting and overriding functionality of the buttons and quantity field forms of both templates. 
* Due to time constraints I decided to delete this function and revert to following the Boutique Ado walkthrough project to have at least a functioning store. 
  
![Crispyforms](https://res.cloudinary.com/dzesjeplp/image/upload/v1733534294/crispyformsissue_ufccsa.png).
![Crispyforms](https://res.cloudinary.com/dzesjeplp/image/upload/v1733534294/crispyformsdetailsmyprofile_ybyphi.png).
![Crispyforms](https://res.cloudinary.com/dzesjeplp/image/upload/v1733534294/htmlineditproduct_vt2zay.png).
* I started off my project with Bootstrap 5 and due to the above problems with the stock and the fact that I had to revert a lot of my code, the crispy forms from the Boutique Ado project are designed to work with Bootstrap4. Due to this the labels of my forms were not being shown on the templates. The checkout template had placeholders based which I could not replicate for the other forms. Even on the my profile template where a user could edit thier name and addressI figured a walkaround for the add_post form by having a placeholder for the title and image and summernote for the textfield section. With more time I could have found a fix for this problem. 
* In the backend I had changed the description textinput section of the products to also have summornote like the content section of the blog app. This causes another problem on the frontend when the admin tries to edit a product cause the text is than rendered with HMTL tags. Due to how the template was written for the add and edit a post with a loop rendering the fields, I could not explicitly say crispy| safe for the description. 

<a href="#top">Back to the top.</a>