# Welcome to GreatKart Django Web application.

## Explanation
GreatKart is an eCommerce application built with Python Django Framework. Some of the features of this project includes custom user model, categories and products, Carts, Incrementing, Decrementing and removing car items, Unlimited Product image gallery, Orders, Payments, after-order functionalities such as reduce the quantify of sold products, send the order received email, clearing the cart, Order completion page as well as generating an invoice for the order. Also we have a Review and Rating system with the interactive rating stars that even allows you to rate a half-star rating. My account functionalities for the customer who can easily edit his profile, profile pictures, change his account password, and also manage his orders and much more.

- Django Custom User Model, Category & Media Files
- Working with Products
- Context Processors & Product Details
- Carts Functionality
- Add to Cart using Session Keys, Increment/decrement/remove Cart Items
- Fixing Cart Bugs & Context Processor for Cart Item Counter
- Paginator & Search
- Product Variations & Variation Manager
- Adding the Variation in Cart, Grouping Cart Item Variations
- Registration, Login with Token Based Verification & Message Alerts
- User Account Activation & Activation Link Expiry
- Forgot Password with Secure Validation Links
- Cart Checkout, automatically assign the Cart Items to Logged-in User
- Orders & Order Number Generation
- Payment Gateway Integration & Place Order
- After Order Functionalities
- Review and Rating System
- Two Factor Checks for Submitting Reviews (Login check & Product purchase check)
- Rating Average & Review Count Calculation
- My Account Functionalities
- Product Gallery with Unlimited Images
- Django Security Measures


![1](https://github.com/samsorrahman/greatkart-django/assets/112087807/37459455-a09d-447d-8e06-f029fc286efb)


![2](https://github.com/samsorrahman/greatkart-django/assets/112087807/9822865f-1bf7-476c-bf21-18f649a1ec22)

![3](https://github.com/samsorrahman/greatkart-django/assets/112087807/a048c702-6c9e-49b7-ac56-01a866516737)

![4](https://github.com/samsorrahman/greatkart-django/assets/112087807/46e1fa89-db4c-4341-aeef-a381fe3af4b4)
<br>
![5](https://github.com/samsorrahman/greatkart-django/assets/112087807/e27ad8ad-e3e8-4442-933b-16ab763b83ed)
![6](https://github.com/samsorrahman/greatkart-django/assets/112087807/09f8958a-0f8b-491b-84a8-b34bcd48f360)



Clone the repository git clone https://github.com/samsorrahman/greatkart-django.git

Navigrate to the working directory

Open the project from the code editor code . or atom .

Create virtual environment python -m venv env

Activate the virtual environment source env/Scripts/activate

Install required packages to run the project pip install -r requirements.txt

Rename .env-sample to .env

Fill up the environment variables: Generate your own Secret key using this tool https://djecrety.ir/, copy and paste the secret key in the SECRET_KEY field.

Your configuration should look something like this:

SECRET_KEY=47d)n05#ei0rg4#)*@fuhc%$5+0n(t%jgxg$)!1pkegsi*l4c%
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=youremailaddress@gmail.com
EMAIL_HOST_PASSWORD=yourStrongPassword
EMAIL_USE_TLS=True

9. Create database tables
python manage.py migrate

10. Create a super user
python manage.py createsuperuser

11. Run server
python manage.py runserver

12. Login to admin panel - (http://127.0.0.1:8000/securelogin/)
13. Add categories, products, add variations, register user, login, place orders and EXPLORE SO MANY FEATURES
