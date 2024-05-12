# Python E-Commerce Website

## Description
This repository contains the source code for a Python-based e-commerce website. The project aims to develop a fully functional online store with user authentication, product browsing, shopping cart management, and order processing features.

## Features
- User Authentication: Allow users to register, login, and manage their accounts.
- Product Browsing: Browse through available products with detailed descriptions and images.
- Shopping Cart Management: Add products to a shopping cart, update quantities, and remove items.
- Order Processing: Checkout process for users to place orders and complete transactions.
- Product Search: Implement a search functionality to allow users to quickly find products by name, category, or other attributes.
- Product Sorting and Filtering: Add options for users to sort and filter product listings based on criteria such as price, popularity, or category.
- Product Reviews and Ratings: Allow users to leave reviews and ratings for products, providing valuable feedback for other users and enhancing trust in your platform.
- Wishlist: Enable users to create and manage a wishlist of products they're interested in, making it easier for them to save items for later purchase.
- Order History: Provide users with a history of their past orders, including details such as order status, items purchased, and order total.
- Promotional Banners: Include banners or sliders on your website to promote special offers, discounts, or featured products.
- Contact Form: Include a contact form or live chat feature to allow users to reach out to customer support or ask questions about products or orders.
- Order Tracking: Implement a tracking system that allows users to track the status of their orders in real-time, providing transparency and peace of mind.

## To get started with this repo, follow these steps:

1. **Clone the Repository:**
   
   ```bash
   git clone https://github.com/mgnegrete/python-ecommerce-project.git

1. **Virtual Environment**
    
    Navigate into the cloned repository directory:
    
    ```bash
    cd python-ecommerce-project
    ```
    
    Create Virtual Environment:

    ```bash
    python3 -m venv env  # For venv
    ```    
    or
    
    ```bash
    virtualenv env       # For virtualenv
    ```    
    Activate Virtual Environment:

    ```bash
    source env/bin/activate  # For Unix/Linux
    ```    
    or

    ```bash    
    .\env\Scripts\activate   # For Windows
    ```

1. **Install Dependencies**
    
    ```bash
    pip install -r requirements.txt
    ```    
    or

    ```bash
    pip3 install -r requirements.txt
    ```
1. **Run the Project:**
    After installing the dependencies, navigate into the project directory and perform database migrations:

   ```bash
   python manage.py migrate
    ```
   or
   
   ```bash
   python3 manage.py migrate
    ```
   ## Once the migrations are applied, you can start the development server:
    
    ```bash
    python manage.py runserver
    ```    
    or

    ```bash
    python3 manage.py runserver
    ```


