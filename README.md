# Online Marketplace API

This project is an online marketplace API built using Django and Django Rest Framework. It allows users to buy and sell products, manage user accounts, and track purchases.

## Features
- User Management: Create accounts, authenticate users using JWT tokens.
- Product Management: Add products for sale with details such as name, description, price, and image.
- Purchase Handling: Track purchases in a database, recording product details, seller's username, buyer's username, and purchase price.
- Product Listing: View a list of all products for sale, including details such as name, description, price, and image.

## Requirements
- Python 3.8+
- Django 4.2+
- Django Rest Framework 3.14+
- Pillow 10.2+

## Setup
1. Clone the repository:

   git clone https://github.com/litshivang/online-ecommerce.git
   cd https://github.com/litshivang/online-ecommerce.git

2. Install dependencies:
   
   pip install -r requirements.txt
   

3. Configure Django settings:
   - Set up database settings in `settings.py`.
   - Configure email settings for email notifications (optional).

4. Migrate database:

   python manage.py migrate

5. Create a superuser (admin):
   
   python manage.py createsuperuser
   

6. Run the development server:
   
   python manage.py runserver
   

7. Access the API at `http://localhost:8000/api/`.

## API Endpoints
- User Management:
  - GET /api/users/ - List all users
  - POST /api/users/ - Create a new user
  - GET /api/users/<int:pk>/ - Retrieve a specific user
  - PUT /api/users/<int:pk>/ - Update a specific user
  - DELETE /api/users/<int:pk>/ - Delete a specific user
  - POST /api/login/ - User login

- Product Management:
  - GET /api/products/ - List all products
  - POST /api/products/ - Create a new product
  - POST /api/products/purchase/ - Purchase a product
  - GET /api/products/list/ - List all products with filtering and sorting options

## Testing
- Run tests:
  
  python manage.py test
  

## Contributors
- Shivang (GitHub: [@litshivang](https://github.com/litshivang))

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


