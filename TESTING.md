# Testing
- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [HTML Testing](#html-testing)
    - [Python Testing](#python-testing)
    - [JavaScript Validation](#javascript-validation)
    - [CSS Testing](#css-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Responsiveness Test](#responsiveness-test)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Additional Testing](#additional-testing)
    - [Lighthouse](#lighthouse)
    - [Results from Lighthouse](#results-from-lighthouse)
    - [User Stories Testing](#user-stories-testing)
    - [Manual Testing](#manual-testing)

## Code Validation

[Back to top](#testing)
### HTML Testing

I used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I followed a different approach for validating my HTML for this project as all of my pages contain Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication to avoid html validation errors. I followed the steps below:

- I gradually opened each html page on my heroku deployed app.
- I right clicked on the screen and chode 'View page source' towards the bottom of the menu.
- I copied the source code.
- I pasted the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- I checked for errors and warnings, fixed any issues, revalidated by following the above steps and recorded the results.

I would do html validation at different stages of the development to avoid being overwhelmed by multiple errors at the end of the project development.

All HTML pages were validated and received a 'No errors or warning to show' for code that I had written. The image was identical for all pages, so I'm including if here for illustration.

![html validation](./testing-images/html_no_errors.png)

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- |
| Home | 0 | 0 |
| All Books (including filtering and sorting) | 0 | 0 |
| Book Detail | 0 | 0 |
| Register | 0 | 0 |
| Log In | 0 | 0 |
| Logout| 0 | 0 |
| Profile | 0 | 0 |
| Admin Dashboard | 0 | 0 |
| Admin Add Product | 0 | 0 |
| Admin Edit Product | 0 | 0 |
| Admin Delete Product | n/a due to deletion modal | n/a |
| Admin Add Article | 0 | 0 |
| Admin Edit Article | 0 | 0 |
| Admin Delete Article | n/a due to deletion modal | n/a |
| Admin Add Enquiry | 0 | 0 |
| Admin Edit Enquiry | 0 | 0 |
| Admin Delete Enquiry | n/a due to deletion modal | n/a |
| Order History | 0 | 0 |
| Wishlist | 0 | 0 |
| Bag - Empty | 0 | 0 |
| Bag - Products | 0 | 0 |
| Checkout | 0 | 0 |
| All Articles | 0 | 0 |
| Article Detail | 0 | 0 |
| Contact Us | 0 | 0 |
| Enquiries | 0 | 0 |
| Newsletter | 0 | 0 |
| Error 403 | 0 | 0 |
| Error 404 | 0 | 0 |
| Error 500 | 0  | 0 |
| Footer | Privacy Policy | [multiple errors](./testing-images/html_privacy_policy_error.png) | x |
| Footer | Terms and Conditions | [multiple errors](./testing-images/html_terms_and_conditions_errors.png) | x |


There were multiple errors in both the Privacy Policy and the Terms and Conditions. Both of these html files were downloaded from termly.io. I didn't attempt to correct the errors as I feared that I would break the document and it would not render correctly. This is perhaps because the service was provided for free. For my future projects, I would look for a better source of these documents.

### Python Testing
[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files which were created or edited by me. I regularly checked my code in my environment and corrected mistakes as I went. I shortened the lines where possible, but in a few places I felt splitting the code would make it illegible. In such cases I used `# noqa` to ignore the length of the line.

| Feature | admin | forms | models | urls | views | extra |
|---------|----------|----------|-----------|---------|----------|-------|
| Article | none ![python validation](./testing-images/article_admin_py.png) | none ![python validation](./testing-images/article_forms_py.png) | none ![python validation](./testing-images/article_models_py.png) | none ![python validation](./testing-images/article_urls_py.png) | none ![python validation](./testing-images/article_views_py.png) | none ![python validation](./testing-images/article_widgets_py.png)  |
| Bag | n/a |n/a | n/a | none ![python validation](./testing-images/bag_urls_py.png) | none ![python validation](./testing-images/bag_views_py.png) | n/a  |
| Bookstore Managegement | n/a |n/a | n/a | none ![python validation](./testing-images/bs_urls_py.png) | none ![python validation](./testing-images/bs_views_py.png) | n/a  |
| Checkout | none ![python validation](./testing-images/checkout_admin_py.png) | none ![python validation](./testing-images/checkout_forms_py.png) | none ![python validation](./testing-images/checkout_models_py.png) | none ![python validation](./testing-images/checkout_urls_py.png) | none ![python validation](./testing-images/checkout_views_py.png) | none ![python validation](./testing-images/checkout_signals_py.png), none ![python validation](./testing-images/checkout_wh_py.png), none ![python validation](./testing-images/checkout_webhooks_py.png)  |
| Contact | n/a | none ![python validation](./testing-images/contact_forms_py.png) | n/a | none ![python validation](./testing-images/contact_urls_py.png) | none ![python validation](./testing-images/contact_views_py.png) | n/a  |
| Enquiry |  none ![python validation](./testing-images/enquiry_admin_py.png) | none ![python validation](./testing-images/enquiry_forms_py.png) | none ![python validation](./testing-images/enquiry_models_py.png) | none ![python validation](./testing-images/enquiry_urls_py.png) | none ![python validation](./testing-images/enquiry_views_py.png) | n/a |
| Home | n/a |n/a | n/a | none ![python validation](./testing-images/home_urls_py.png) | none ![python validation](./testing-images/home_views_py.png) | n/a  |
| Newsletter | n/a |n/a | n/a | none ![python validation](./testing-images/newsletter_urls_py.png) | none ![python validation](./testing-images/newsletter_views_py.png) | n/a  |
| Products | none ![python validation](./testing-images/product_admin_py.png) | none ![python validation](./testing-images/product_forms_py.png) | none ![python validation](./testing-images/product_models_py.png) | none ![python validation](./testing-images/product_urls_py.png) | none ![python validation](./testing-images/product_views_py.png) | none ![python validation](./testing-images/product_widgets_py.png)  |
| Profile |  n/a | none ![python validation](./testing-images/profile_forms_py.png) | none ![python validation](./testing-images/profile_models_py.png) | none ![python validation](./testing-images/profile_urls_py.png) | none ![python validation](./testing-images/profile_views_py.png) | n/a |
| Review |  none ![python validation](./testing-images/review_admin_py.png) | none ![python validation](./testing-images/review_forms_py.png) | none ![python validation](./testing-images/review_models_py.png) | none ![python validation](./testing-images/review_urls_py.png) | none ![python validation](./testing-images/review_views_py.png) | n/a |
| Wishlist | none ![python validation](./testing-images/wishlist_admin_py.png) | none ![python validation](wishlist./testing-images/wishlist_forms_py.png) | none ![python validation](./testing-images/wishlist_models_py.png) | none ![python validation](./testing-images/wishlist_urls_py.png) | none ![python validation](./testing-images/wishlist_views_py.png) | none ![python validation](./testing-images/wishlist_contexts_py.png)  |

[Back to top](#testing)

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript code added to the project. External JS, for Bootstrap, jQuery and Fontawesome purposes were not validated through JSHint.

| Page | Screenshot | Errors | Warnings |
|---------|----------|----------|-----------|
| Bag - Quantity Update/Remove Script | ![Bag update/remove js](./testing-images/bag_update_remove_js.png) | none | none |
| Checkout - Stripe Script | ![Stripe elements](./testing-images/stripe_element_js.png) | none | none |
| Products - Quantity Input Script | ![Product quantity script](./testing-images/product_quantity_input_script_js.png) | none  | none |
| Products - Sorting Script | ![Product sorting script](./testing-images/product_sorting_js.png) | none | none |
| Edit Product Image Script | ![Edit product image script](./testing-images/edit_product_image_js.png) | none | none |
| Profile - Country Field Script | ![Profile country field script](./testing-images/profile_country_field_js.png) | none | none |
| Back to Top Button | ![Back to top button script](./testing-images/back_to_top_js.png) | none | none |
### CSS Testing
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS files. External CSS for Bootstrap, provided by CDN was not tested. No errors were found.

To avoid cluttering my testing file with multiple identical images, I have not included every screenshot of the CSS validations, as they were all the same. 

![css validation](./testing-images/css_no_errors.png)

| CSS File | Errors | Warnings |
| ---- | ------ | -------- |
| Base CSS | 0 | 0 |
| bag | 0 | 0 |
| Checkout | 0 | 0 |
| Profiles | 0 | 0 |

## Browser Compatibility

The website was tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. There were no errors discovered in the functionality of the site or the individual features.

| App | Browser Compatibility |
| ---- | ---------- |
| Google Chrome | &check; |
| Safari | &check; |
| Microsoft Edge| &check; |
| Mozilla Firefox| &check; |

[Back to top](#testing)

## Responsiveness Test

Achieving responsiveness on this project was much easier and faster than before mainly due to the application of Bootstrap. I always strived to put mobile devices first and then I used medie queries for larger devices, as it is proven that majority of internet users are accessing web apps through their mobile phones.

Testing of responsive design was carried out manually by utilizing [Google Chrome DevTools](https://developer.chrome.com/docs/devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

|        | S Galaxy 5 | iPhone 6/6S/7 | iPad Mini | iPad Pro | Display <1200px | Display >1200px |
| ------ | ---------- | ------------- | --------- | -------- | --------------- | --------------- |
| Render | pass       | pass          | pass      | pass     | pass            | pass            |
| Images | pass       | pass          | pass      | pass     | pass            | pass            |

[Responsiveness test video](./readme-images/responsivness_test.webm)


[Back to top](#testing)

## Fixed Bugs

|                                        BUG                                       | WHERE |                                      HOW                                      |                   COMMIT                   |
|:--------------------------------------------------------------------------------:|:-----:|:-----------------------------------------------------------------------------:|:------------------------------------------:|
| The quantity of books in the shopping bag was not updating.| bag.html  | I had to take away the "href" element from the respective buttons.| [b3393b9](https://github.com/lucia2007/bookwormkid/commit/b3393b91866a5edf35f3e44bdd5cc408c3a815cb)  |
| The crispy_forms were not loading correctly | settings.py  | I had to correct a typo.| [af52cfe](https://github.com/lucia2007/bookwormkid/commit/af52cfe5f13c18af0ea7817c1164507551d9b475)  |
| The 404 page was not applying custom template | settings.py  | I had to move content from settings.py to urls.py| [af52cfe](https://github.com/lucia2007/bookwormkid/commit/f60afce6a6725faf30e0ae3b6ba7b95f1e5845df) and [3c048ce](https://github.com/lucia2007/bookwormkid/commit/3c048cebbd26b0f8a9c2ddeec379d0b1976da38c) |
| The 403 and 500 error pages were not applying custom template | views.py, urls.py  | I had made several messy commits trying to see if the error pages worked on the deployed app. In the end I reverted to the simplest option, just define error pages in the templates directory without any views.py or urls.py error code| [ and several previous commits](https://github.com/lucia2007/bookwormkid/commit/307f044cdbea30b665fed8fad6a2702213ab3aa5)
| My user registration and email sending for order confirmation stopped working | settings.py, gmail, heroku  | I'll provide a more detailed explanation below*. | [a960055](https://github.com/lucia2007/bookwormkid/commit/a960055f60ad0a04dc4192ae04a5a7e9c790ee9b) and [965c607](https://github.com/lucia2007/bookwormkid/commit/965c607c8a8115a25ff0d8d199aeccf2f7cf8f40)
| "Country" label was appearing twice in my checkout form | checkout/forms.py  | I had to correct the indentation error. | [1b653a2](https://github.com/lucia2007/bookwormkid/commit/1b653a2269432d69ce9bb975befc7c77253bb056)
| Wishlist items were rendering incorrectly | wishlist.html  | I had several indentation errors and wrong order of elements which I had to fix. | [d34b771](https://github.com/lucia2007/bookwormkid/commit/d34b7719ce77c698882f2e196511dd930ce3bb9c)
| My Wishlist context processor wasn't working due to inconsistencies in the code. | wishlist/contexts.py  | I had to correct the variable names in the file. | [81af4d7](https://github.com/lucia2007/bookwormkid/commit/81af4d793bc781c0e49183faaa7d9b322c0f5788)
| Noimage placeholder picture was not displaying for articles if no image provided. | article/models.py  | I had to get rid of default=placaholder for the image in the model. | [230333b](https://github.com/lucia2007/bookwormkid/commit/230333bfd2a23d9d75752c0d82a983e7785323ad) and [6a935d8](https://github.com/lucia2007/bookwormkid/commit/6a935d8f37bfcfdba8816842b5de491ed9f88f51)
| Adding a draft of an article would take me to a 404 page | article/views.py  | I had to update my views, espcially take away the status=1 condition from my detail views. | [692d357](https://github.com/lucia2007/bookwormkid/commit/692d357d724180422312cac204d2658e11846187)
| Article edit picture was not working - tip from tutor| article/views.py  | I had to add request.files to my view | [9728fc8](https://github.com/lucia2007/bookwormkid/commit/9728fc809f60383ea2b28eca683dde7bd342af25)
| Class "{%" duplicated| products.html  | products.html| I had change the place where I added the condition for filters** | [dccafb7](https://github.com/lucia2007/bookwormkid/commit/dccafb7b55aec72f89a381019eabd77c4caec305)
| Avoid anonymous user error for reviews  | product_detail.html, products/views.py| I had to switch the order of the conditions | [e9e9b23](https://github.com/lucia2007/bookwormkid/commit/e9e9b23a5b90202e3bc693b736833941e565847a)
| 'AnonymousUser' object is not iterable (max 1 review) and wrong rendering  | products.html, product_detail.html, products/views.py| I had to switch the order of the if conditions and add a @login_required decorator to my view| [59fc46d](https://github.com/lucia2007/bookwormkid/commit/59fc46daea23bf228de2c7288e244c4100fb96c6)
| Div not persmissible under small + extra space in tab= -1  | articles.html, article_detail.html, article_deletion.html | I had to change small to div and add classes, and delete an extra space in tabindex=" -1"| [2754559](https://github.com/lucia2007/bookwormkid/commit/2754559bd3b5a4a9f711a69e0f4a4f13d1dd2d61)
| Fix duplicate id="id_image" (I wasn't able to add an image to an article) | articles.html, add/edit_article.html, products.html, add/edit_product.html, custom_clearable_file_input.html | I had to get rid on id="new-image", as it was creating a duplicate id, and had to add/change js which worked with "new-image"| [6f0cf78](https://github.com/lucia2007/bookwormkid/commit/6f0cf78c2697b1de4f6a7c592ea235dc924ee49b)

* My registration and email confirmation for orders stopped working for all users but admin. This was partly due to the fact, that I attempted to use aws ses functionality for sending emails for my contact form. I later found out that aws ses in the basic version would allow sending emails only to verified email addresses, which couldn't be done when a new user was being created, as his email address was new and not verified. I found out that if I used a "helping email address" success@simulator.amazonses.com, everything worked fine. If I wanted aws ses to send emails to nonverified email address, I would have to ask for a personal approval from Amazon. As it was proving quite complicated, I opted to revert back to the previous smtp functionality. Neverthless, the problem persisted even after that. With tutor support we were able to discover that my "app password" in my gmail account got deleted (without any action on my side) and thus the email functionality stopped working. When I created a new app and reset the password in Heroku, everything started working again. I hope this problem doesn't happen again, as it's completely out of my control if Google decided to delete my "app password" for some reason.
[Error due to deleted app password](/testing_images/smtp_error.png)

** There are quite a few commits around my product filters and highlighting of the chosen age segment, as I was trying to figure out ways how to do it more efficiently and more simply. There was a lot of back and forth, and some unnecessary or duplicated commits, and even though I know the code could still be refactored, I feel that at the moment it is finally easily legible and understandable.
## Unfixed Bugs

There are no known unfixed bugs in the project.

[Back to top](#testing)

## Additional Testing
### Lighthouse

The application was also tested using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Developer Tools. The following aspects were tested:

- Performance - reveals how the site performs during loading
- Accessibility - shows if the site if accessible for all users and suggests ways to improve it
- Best Practices - indicates if the site conforms to industry best practices
- SEO - Search Engine Optimisation - shows if the site is optimised for search engine result rankings

### Results from Lighthouse
| Page | Validation Results |
| ---- | ---------- |
| Home | [Home Page Score](./testing-images/lighthouse_homepage.png) |
| Contact Us | [Contact Us Score](./testing-images/lighthouse_contactus.png) |
| Products | [Products Score](./testing-images/lighthouse_products.png) |
| Product Details | [Product Details](./testing-images/lighthouse_product_detail.png) |
| Admin Dashboard | [Admin Dashboard](./testing-images/lighthouse_admin_dashboard.png) |
| Shopping Bag | [Shopping Bag Score](./testing-images/lighthouse_shopping_bag.png) |
| Checkout | [Checkout Score](./testing-images/lighthouse_checkout.png) |
| Articles | [Articles Score](./testing-images/lighthouse_articles.png) |
| Article Details | [Article Details](./testing-images/lighthouse_article_detail.png) |
| Wishlist | [Wishlist Score](./testing-images/lighthouse_wishlist.png) |
| Profile | [Profile Score](./testing-images/lighthouse_profile.png) |
| Enquiries | [Enquiries Score](./testing-images/lighthouse_enquiries.png) |
| Sign In | [Sign In Score](./testing-images/lighthouse_login.png) |
| Sign Up | [Sign Up Score](./testing-images/lighthouse_signup.png) |
| Sign Out | [Sign Out Score](./testing-images/lighthouse_logout.png) |

I continuously worked on improving the individual scores and tried to reflect on the warnings in the Lighthouse which lead to the score increase. For increasing accessibility I had to change many button names as I was not using their explicit description and for performance I used [tiny png](tinypng.com) and [convertio](convertio.co) and [i love img](https://www.iloveimg.com/) to decrease their size and change them to webp where possible. However, I couldn't do this for all of my images, espcially for the book covers, as sometimes I was not able to find a large enough image of a book I needed.

All of my scores for all of the pages were above 90, often close to 100. On a couple of pages the "SEO" score is slightly lower. This is due to the presence of a "back to top" button which has no href value and thus is not crawlable. I also got a lower score on Best Practices, due to [issues](./testing-images/stripe_cookies.png) which were logged into the console and have to do with using stripe cookies. Sometimes my scores for performance differed, probably due to current connection speed.


### User Stories Testing
[Back to top](#testing)

### Manual Testing

**User Input/Form Validation**

I tested all Bookworm Kid features repeatedly throughout the development process and again at the end in the testing sprints. The final testing was carried out on the deployed version on Chrome on desktop. All features were tested for both guest and logged in user, but to avoid redundancy, I added only the extra features available to the logged in users in the respective section. Again, for the admin section, only new features were mentioned to avoid redundancy.

| Status | **Main Website - User Logged Out - Top Navigation**
|:-------:|:--------|
| &check; | The free shipping treshold corresponds to the value set in the settings.py file.
| &check; | Typing in a incorrect URL on the page loads the 404 error page.
| &check; | Pasting page that needs authentication opens the login page (e.g. clicking on a "add to wishlist" button if not signed in).
| &check; | Pasting page that is restricted to a logged in admin user, displays the login page first and either a forbidden 403 page for articles or a warning message for products. (This can be
achieved e.g. by pasting in an edit product or edit article url when signed in as a regular user.)
| &check; | Inputting an invalid query in the search box displays "Sorry, no books match your search" message.
| &check; | Clicking the Register link in the My Account menu loads the sign up page.
| &check; | Clicking the Login link in the My Account menu loads the login page.
| &check; | Clicking on the shopping bag link in the menu bar loads the shopping bag page.
| &check; | Inputting an empty query in the search box triggers an error messages and lists all products.


| Status | **Main Website - User Logged Out - Main Navigation**
|:-------:|:--------|
| &check; | The main navigation collapses into a hamburger on small screens. All links work properly.
| &check; | Clicking the nav logo loads the home page.
| &check; | Clicking the Home button on the nav bar loads the home page.
| &check; | Clicking the By Price link in the Products menu lists all products and sorts them by price taking the sales price into consideration if a product is on sale.
| &check; | Clicking the By Rating link in the Products menu lists all products and sorts them by rating.
| &check; | Clicking the By Name link in the Products menu lists all products and sorts them by name.
| &check; | Clicking the By Category link in the Products menu lists all products and sorts them by Category name.
| &check; | Clicking the All Products link in the Products menu lists all products.
| &check; | Clicking the Reluctant Reader link in the Categories menu lists all products within the Reluctant Reader category are displayed.
| &check; | Clicking the Keen Reader link in the Categories menu lists all products within the Keen Reader category are displayed.
| &check; | Clicking the Avid Reader link in the Categories menu lists all products within the Avid Reader category are displayed.
| &check; | Clicking the All Products link in the Skill Level menu lists all products.
| &check; | Clicking the New Arrivals link in the Special Offers menu lists all products with the tag new arrivals and displayes the correct icon.
| &check; | Clicking the Featured Books link in the Special Offers menu lists all products with the tag Featured Books and displayes the correct icon.
| &check; | Clicking the On Sale link in the Special Offers menu lists all products with the tag On Sale and displayes the correct icon.
| &check; | Clicking the Specialls link in the Special Offers menu lists all products with the tag New Arrival/Featured or On Sale and displayes the correct icons.
| &check; | Clicking the Articles link takes the user to all articles page, 4 articles are displayed.
| &check; | Clicking the Contact US link takes the user to a contact form which the user can fill in.


| Status | **Main Website - User Logged Out - Books**
|:-------:|:--------|
| &check; | Clicking the filtering links in the by skill or special offers, renders the correct subcategory name at the top of the page.
| &check; | Age segmentation buttons + all are present on all product pages.
| &check; | Clicking the chosen age link (6-8, 9-10, 11-12, all) displays products within that age group in the chosen subcategory (e.g. skill level or specials) and the correct age button choice is highlighted in dard blue.
| &check; | Sorting function below the product page headline sorts the products accordingly within the chosen subsegments.
| &check; | The correct image and information for each book is displayed.
| &check; | One piece of the chosen book is added to the shopping bag when "add to bag" button is clicked from the main products page.
page.
| &check; | If product is added to bag successfully, a toast with bag and delivery cost information is displayed in the top right corner, if total price is below €30 or without it delivery fee, if the total price is higher. The toast includes a link to the shopping bag.
| &check; | When the first products is added to the bag, the bag changes color to yellow.
| &check; | Clicking the "add to wishlist" button takes the user to the login page.
| &check; | Sales price is displayed in red if present.
| &check; | Products have correct specials icons if in new arrivals/featured or on sale.
| &check; | Back to top button is present in the right hand corner and takes the user to the top of the page.

| Status | **Main Website - User Logged Out - Books Details**
|:-------:|:--------|
| &check; | Clicking the book image on the product card, loads the product detail page.
| &check; | Clicking the book image on the product detail page displays a new page with the book image.
| &check; | Book details (title, author, category, age group, price, rating, description, quantity selection, keep shopping/add to bag buttons and a clickable number of reviews if present are displayed. If book is in specials category, a correct icon is present and all add to wishlist button.)
| &check; | Sales price is displayed in red if present.
| &check; | Clicking the read more button opens up the whole book description.
| &check; | Clicking the read less button closes the whole book description.
| &check; | Setting the quantity in the quantity selector and clicking "add to bag" button, adds the correct quantity in the bag (works for both mobile and larger screens).
| &check; | Trying a add a decimal number in the quantity selector renders a warning message about using whole numbers.
| &check; | If product is added to bag successfully, a toast with bag and delivery cost information is displayed in the top right corner, if total price is below €30 or without it delivery fee, if the total price is higher. The toast includes a link to the shopping bag.
| &check; | When the first products is added to the bag, the bag changes color to yellow.
| &check; | Keep shopping button takes the user back to all books.
| &check; | Clicking the "add to wishlist" button takes the user to the login page.
| &check; | If reviews are present, the reviews icon and their number is displayed. The user can click on the reviews button and see all the current reviews.

| Status | **Main Website - User Logged Out - Articles**
|:-------:|:--------|
| &check; | Clicking the article link, takes the user to all articles.
| &check; | The correct image and information for each article post is displayed.
| &check; | Currently 4 articles are present.
| &check; | A short excerpt of the article is shown.
| &check; | Newest articles are shown first.
| &check; | The number next to the heart, which is not clickable in this view, shows the number of likes.
| &check; | Clicking the article image or the article text takes the user to the article detail page.
| &check; | Back to top button is present in the right hand corner and takes the user to the top of the page.
| &check; | The search functionality is restricted to products only.

| Status | **Main Website - User Logged Out - Article Details**
|:-------:|:--------|
| &check; | Clicking the article image/text on the card, takes the user to the article detail page.
| &check; | The correct image and information for each article post is displayed.
| &check; | The article image, author, heading and text are present.
| &check; | At the bottom of the article, the source is present, which when clicked, opens a new tab with the original article.
| &check; | The number next to the heart, which is not clickable when not signed in, shows the number of likes.
| &check; | Clicking the article image takes the user to the detail or the article image.
| &check; | Back to top button is present in the right hand corner and takes the user to the top of the page.
| &check; | "Back to articles" button takes the user back to all articles.

| Status | **Main Website - User Logged Out - Shopping Bag**
|:-------:|:--------|
| &check; | The correct products, their titles, images, quantity, price and subtotal are displayed in the shopping bag.
| &check; | When changing the quantity and clicking update the quantity updates and the toast confirms this action. The quantity must be a whole number, otherwise a warning message is displayed and the form is not processed.
| &check; | When clicking the remove link, the product is removed from the shopping bag. If the bag remains empty after the removal, the user is informed about this.
| &check; | Clicking the Keep Shopping button on the shopping bag page, takes the user to all products.
| &check; | Clicking the Secure Checkout button on the shopping bag page, loads the secure checkout page.
| &check; | The shopping bag is yellow, if there are items present in it.

| Status | **Main Website - User Logged Out - Secure Checkout**
|:-------:|:--------|
| &check; | The correct products with images, quantity, subtotal and delivery amount (if below €30) are showing in the order summary.
| &check; | In the bottom of the form an option log in or sign up is visible.
| &check; | Clicking the "Adjust Bag" button loads the shopping bag page.
| &check; | Clicking the "Complete order" buttons lead to the order processing.
| &check; | The payment with card number is working correctly (tested with Stripe test numbers).
| &check; | The payment with card number that needs to be authenticated is working correctly (tested with Stripe test numbers). The authentication window is visible.
| &#10008; | The form validation works except that the Full Name field (which is empty) can include numbers and the phone number field can include text.
| &check; | The Success toast is displayed in the right hand corner with order number and information about confirmation email.

| Status | **Main Website - User Logged Out - Order Confirmation Page**
|:-------:|:--------|
| &check; | The correct products, information and delivery amount are showing in the order confirmation and an e-mail has been sent to the user e-mail used in the checkout form.
| &check; | Webhooks are working and are confirmed in Stripe developer dashboard.
| &check; | Clicking "Now Check out our special offers" button, the user is taken to all specials page.


| Status | **Main Website - User Logged Out - Contact Us Page**
|:-------:|:--------|
| &check; | The correct form is rendered when Contact Us link is clicked.
| &check; | Email has to be in a correct format. User is informed if they didn't use the correct form.
| &check; | An email with the enquiry is sent to the bookstore's email address.
| &check; | The user sees a success toast.
| &check; | The user is taken to the Thank you page and HOME button.


| Status | **Main Website - User Logged Out - Footer**
|:-------:|:--------|
| &check; | Clicking the Facebook link in the footer area opens store's Facebook page in a new window.
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window.
| &check; | Clicking the Pinterest link in the footer area opens Pinterest in a new window.
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window.
| &check; | Clicking the FAQ link in the footer area takes the user to freaquently asked questions.
| &check; | The search functionality is restricted to products only and does not comprise enquiries.
| &check; | Clicking the Privacy Policy link in the footer area takes the user to the Privacy Policy.
| &check; | Clicking the Terms of Use in the footer area takes the user to the Terms of Use.
| &check; | Clicking the Shipping Info in the footer area takes the user to the FAQ where they can find more information.
| &check; | Clicking the Home, Books, Articles and Contact us button in the footer area takes the user to the corresponding pages.
| &check; | Clicking the Home, Books, Articles and Contact us button in the footer area takes the user to the corresponding pages.
| &check; | Registering an invalid e-mail address in the newsletter signup in the footer triggers an error message.
| &check; | Registering a valid e-mail address in the newsletter signup in the footer triggers a confirmation message.
| &check; | Registering an already used valid e-mail address in the newsletter signup in the footer triggers a message about being registered already.
| &check; | Contact information is displayed in footer. Clicking on the envelope opens up an email draft.
| &check; | On small devices the footer is collapsed and some information is hidden under the HELP button. The links work correctly.

[Back to top](#testing)

| Status | **Main Website - User Logged In - Navigation** (Extra features)
|:-------:|:--------|
| &check; | Clicking the My Profile icon the main navigatin menu, loads My profile page.
| &check; | Under My profile, user can see their delivery information if previously saved and their order history ordered from the newest to the oldest. Order history is clickable to display order details.
| &check; | Update button lets the user update their default delivery information.
| &check; | A heart icon is present in the main navbar. It is blue, if wishlist is empty and yellow, if there is at least one item in the wishlist. Clicking the heart, takes the user to My Wishlist page.

| Status | **Main Website - User Logged In - Article Detail**
|:-------:|:--------|
| &check; | Clicking the heart icon at the bottom of the article detail page, lets the user like/unlike the article. The change in the number of likes is reflected both on the detail and all article pages.


| Status | **Main Website - User Logged In - Products**
|:-------:|:--------|
| &check; | User can click on a link in their order history and a review window is present on the respective product's detail page if they had bought the product and had not previously reviewed it.
| &check; | User can add a review and wait for the admin's approval. After approval, the review is added and the number of reviews is updated.
| &check; | The review form is also available for the user who had bought the product previously and had not availed of the review opportunity yet. They can see the form to add review under the books they had bought and not reviewed yet without having to click on the link in their order confirmation.

| Status | **Main Website - User Logged In - Checkout**
|:-------:|:--------|
| &check; | It the user has updated the profile information previously, the information is prefilled in the form.
| &check; | In the bottom of the form an option to save the delivery information to their profile is visible.

| Status | **Main Website - User Logged In - Order Confirmation Page**
|:-------:|:--------|
| &check; | Clickable past orders are displayed under My Profile for each user.
| &check; | Orders contain a link to the bought products to leave a review. The review form is available only if the product had not been reviewed previously.

| Status | **Main Website - User Logged In - Wishlist**
|:-------:|:--------|
| &check; | When a user adds a product to their wishlist, they are taken to their wishlist page. The "add to wishlist" button changes to "remove from wishlist" button and the heart is full.
| &check; | Also on all products page, if the signed in user already has a book in their wishlist, they see a "remove from wishlist" button instead of "add to wishlist button" with an empty heart.
| &check; | If the user tries to add a product to the wishlist and is not signed in, they are taken to the sign in page first. If they are accidently trying to add a product to their wishlist which they had added previously, they are warned about the product being present in their wishlist already.
| &check; | "Add to bag" button is present on the wishlist page and addes one piece of the chosen product to the shopping bag.

[Back to top](#testing)

| Status | **Main Website - Admin Logged In - Navigation**
|:-------:|:--------|
| &check; | Under the Profile Icon, the Bookstore Management link is present. When clicked, it takes the admin to a bookstore management page, where they can add/edit/delete products, articles and enquiries.


| Status | **Main Website - Admin Logged In - Products/Product Detail Page**
|:-------:|:--------|
| &check; | When an admin is logged in, they can see an edit/delete button on each product card both on all products and product details pages.
| &check; | The edit button takes them to the product's edit page, where they can update the product details.
| &check; | The update button leads to saving the updated information and takes the user to the product detail page.
| &check; | The admin can add a product with no image. In this case a placeholder images is displayed.
| &check; | Before the admin can delete a chosen product from the store, they have to confirm their deletion choice.

| Status | **Main Website - Admin Logged In - Book Management - Add Book**
|:-------:|:--------|
| &check; | The form validation is working and does not accept negative numbers on the price, sales price, number of pages and rating fields.
| &check; | When no image is provided, a placeholder image is used.
| &check; | When clicking the Add Product button, the user is taken to product detail page.
| &check; | When clicking the Cancel button, the user is taken to All products page.

| Status | **Main Website - Admin Logged In - Book Management - Edit/Delete Book**
|:-------:|:--------|
| &check; | When clicking the Edit button the form is prefilled with the product information and the action is changed to 'You are editing this product'.
| &check; | When clicking the Delete Product button a warning modal is loaded for deletion confirmation. After deletion, the user is taken to all products page.
| &check; | Clicking on Cancel button, the user is taken back to all products view.
| &check; | When clicking the Update button, the user is taken back to the product detail page with the updated information.

| Status | **Main Website - Admin Logged In - Articles/Article Detail Page**
|:-------:|:--------|
| &check; | When an admin is logged in, they can see an edit/delete button on each article card both on all articles and article details pages.
| &check; | The edit button takes them to the article's edit page, where they can update the article's details.
| &check; | The update button leads to saving the updated information and takes the user to the article detail page.
| &check; | The admin can add an article with no image. In this case a placeholder images is displayed.
| &check; | The admin can save an article as a draft. In this case only admin can see this article in all articles.
| &check; | Before the admin can delete a chosen article, they have to confirm their deletion choice.

| Status | **Main Website - Admin Logged In - Article Management - Add Article**
|:-------:|:--------|
| &check; | The form validation is working and article has to have a unique name.
| &check; | When no image is provided, a placeholder image is used.
| &check; | When clicking the Add Article button, the user is taken to article detail page.
| &check; | When clicking the Cancel button, the user is taken to all articles page.

| Status | **Main Website - Admin Logged In - Article Management - Edit/Delete Article**
|:-------:|:--------|
| &check; | When clicking the Edit button the form is prefilled with the article information.
| &check; | When clicking the Delete article button a warning modal is loaded for deletion confirmation. After deletion, the user is taken to all articles page.
| &check; | Clicking on Cancel button, the user is taken back to all articles view.
| &check; | When clicking the Update button, the user is taken back to the article detail page with the updated information.

| Status | **Main Website - Admin Logged In - Enquiries Page**
|:-------:|:--------|
| &check; | When an admin is logged in, they can see an edit/delete button on each enquiry card both on all enquiries page.
| &check; | The edit button takes them to the enquiry edit page, where they can update the enquiry's details.
| &check; | The update button leads to saving the updated information and takes the user to all enquiries.
| &check; | The admin can save an enquiry as a draft. In this case only admin can see this enquiry in all enquiries.
| &check; | Before the admin can delete a chosen enquiry, they have to confirm their deletion choice.

| Status | **Main Website - Admin Logged In - FAQ Management - Add FAQ**
|:-------:|:--------|
| &check; | When clicking the Add Enquiry button, the user is taken to all FAQ page.
| &check; | When clicking the Cancel button, the user is taken to all articlesFAQ page.

| Status | **Main Website - Admin Logged In - FAQ Management - Edit/Delete FAQ**
|:-------:|:--------|
| &check; | When clicking the Edit button the form is prefilled with the FAQ information.
| &check; | When clicking the Delete article button a warning modal is loaded for deletion confirmation. After deletion, the user is taken to all FAQs page.
| &check; | Clicking on Cancel button, the user is taken back to all FAQs view.
| &check; | When clicking the Update button, the user is taken back to all FAQs.

[Back to top](#testing)