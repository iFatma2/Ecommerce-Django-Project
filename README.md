# Django Flower Shop

Welcome to the Django Flower Shop, an e-commerce platform built with Django for flower enthusiasts and gift shoppers. This project leverages Django's robust framework to provide a seamless shopping experience, from browsing to checkout.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Website Interface Previews](#Website Interface Previews)
- [Demo Video](#Demo Video)

## Introduction

The Django Flower Shop is designed to showcase the capabilities of the Django web framework in creating a fully functional e-commerce platform. This project is ideal for learners, developers, and anyone interested in understanding the intricacies of online store development using Django.

## Features

- **Product Catalog:** Browse a wide range of flowers and related products.
- **Shopping Cart:** Add items to your cart and manage them with ease.
- **User Authentication:** Secure sign-up and login functionality.
- **Order Management:** Place orders and track their status from payment to delivery.
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
![Home Page Sketch]("C:\Users\F\OneDrive - UMM AL-QURA UNIVERSITY\Documents\flower\Index.png")

### Shop Items
![Shop Items Sketch]("C:\Users\F\OneDrive - UMM AL-QURA UNIVERSITY\Documents\flower\ItemsShop.png")

### Item Details
![Item Details Sketch]("C:\Users\F\OneDrive - UMM AL-QURA UNIVERSITY\Documents\flower\ItemsDetails.png")

### Checkout
![Checkout Sketch]("C:\Users\F\OneDrive - UMM AL-QURA UNIVERSITY\Documents\flower\Checkout.png")

### Address Form
![Address Form Sketch]("C:\Users\F\OneDrive - UMM AL-QURA UNIVERSITY\Documents\flower\address.png")

### Payment Form
![Address Form Sketch]("C:\Users\F\OneDrive - UMM AL-QURA UNIVERSITY\Documents\flower\payment.png")

## Video Demonstration
For a full demonstration of the web application, check out this video:
[![Django Flower Shop Video Demo](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE "Django Flower Shop Video Demo")


## Demo Video

Watch a full demonstration of the Django Flower Shop in action:

[![Watch the demo](https://img.youtube.com/vi/your_video_id_here/maxresdefault.jpg)](https://youtu.be/your_video_id_here)



