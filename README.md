# Django Flower Shop

Welcome to the Django Flower Shop, an e-commerce platform built with Django for flower enthusiasts and gift shoppers. This project leverages Django's robust framework to provide a seamless shopping experience, from browsing to checkout.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Django Flower Shop UI Sketches Previews](#django-flower-shop-ui-sketches-previews)
- [Database Checking](#database-checking)
- [Demo Video](#Demo-video)

## Introduction

The Django Flower Shop is designed to showcase the capabilities of the Django web framework in creating a fully functional e-commerce platform. This project is ideal for learners, developers, and anyone interested in understanding the intricacies of online store development using Django.

## Features

- **Product Catalog:** Browse a wide range of flowers and related products.
- **Shopping Cart:** Add items to your cart.
- **User Authentication:** Secure sign-up and login functionality.
- **Order Management:** Place orders.
- **Admin Panel:** Manage products, orders, and users through the Django admin interface.

## Installation

To get the Django Flower Shop up and running on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/iFatma2/Ecommerce-Django-Project.git
   
2. Navigate to the project directory:
     ```bash
     cd Ecommerce-Django-Project

  
3. Run the migrations to set up your database:
     ```bash
     Database Connection

     pip install mysqlclient
     
     python manage.py makemigrations
     
     python manage.py migrate
     
  
4. Start the development server:
     ```bash
     py manage.py runserver 

5. Open your browser and go to http://127.0.0.1:8000 to view the app.

## Dependencies

This project requires the following major dependencies:

- **Python:** The core programming language used for this project. Ensure you have Python 3.8 or newer installed.
- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design. This project was built with Django 3.2.

## Configuration

Before running the Django Flower Shop application, ensure the database is properly configured. The project uses MySQL as its database. Update the `DATABASES` setting in your project's `settings.py` file as follows:

      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'shopping',
              'USER': 'root',
              'PASSWORD': '',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }

## Django Flower Shop UI Sketches Previews

Here's a sneak peek at Flower Shop Website:

### Home Page
![Index](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/a1555ff2-3392-4e6d-8a2a-0e4f5e60a33f)

### Shop Items
![Shop Items Sketch](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/9f6a0413-1f32-4a90-a9ad-7e5442f40e4e)

### Item Details
![Item Details Sketch](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/c354c51b-7dc3-4c79-8870-0847f3924546)


### Checkout
![CheckoutSketch](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/6f740015-4e46-40f7-8bc2-cc4494c702f9)

### Address Form
![AddresFormSketch](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/ae860f26-e48b-4672-8cd6-81f9d615257c)

### Payment Form
![AddressFormSketch](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/1e1fad96-a8df-4dfe-aa78-9b3334c5d276)

## Database Checking:
### Address Table:
![DBaddress](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/b0d9784e-07ef-4a4d-8323-44ef7798040c)

### Payment Table:
![DBpayment](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/21618008-9636-410f-b5fe-b05ad53255a1)


## Demo Video

Watch a full demonstration of the Django Flower Shop in action:
![FlowerShopDemo](https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/e1f530d4-6858-40d5-a792-a0810440e4a3)
https://github.com/iFatma2/Ecommerce-Django-Project/assets/139279448/e1f530d4-6858-40d5-a792-a0810440e4a3



