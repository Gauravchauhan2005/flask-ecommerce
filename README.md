# E-Commerce Website - Food, Flowers & Heritage Products

A full-stack multi-category e-commerce website built with Flask (Python) and MySQL, featuring food delivery, flower delivery, and heritage/handicraft products.

## 🚀 Features

### Customer Features
- **Homepage** with three main categories: Food, Flowers, Heritage
- **Product Listing** with category filters and search functionality
- **Product Detail** pages with full descriptions
- **Shopping Cart** with quantity updates and item removal
- **Checkout** with Cash on Delivery and Online Payment (demo) options
- **User Authentication** - Login and Signup with secure password hashing
- **Order Management** - View order history and order confirmation
- **Responsive Design** - Works seamlessly on mobile and desktop

### Admin Features
- **Admin Dashboard** with statistics and overview
- **Product Management** - Add, edit, and delete products
- **Category Management** - Organize products by category
- **Order Management** - View and update order statuses
- **Customer Orders** - Track all customer orders

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Backend**: Python Flask
- **Database**: MySQL
- **Architecture**: MVC (Model-View-Controller) pattern
- **Authentication**: Flask-Login with secure password hashing (Werkzeug)

## 📁 Project Structure

```
ecommerce-store/
│
├── app.py                 # Main Flask application entry point
├── config.py              # Configuration settings
├── models.py              # Database models (User, Product, Cart, Order)
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── routes/               # Route handlers (MVC Controllers)
│   ├── auth.py          # Authentication routes (login, signup, logout)
│   ├── user.py          # User-facing routes (home, products, cart, checkout)
│   └── admin.py         # Admin routes (dashboard, product/order management)
│
├── templates/            # HTML templates (MVC Views)
│   ├── base.html        # Base template with navigation and footer
│   ├── auth/           # Authentication templates
│   │   ├── login.html
│   │   └── signup.html
│   ├── user/           # User-facing templates
│   │   ├── home.html
│   │   ├── products.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── order_confirmation.html
│   │   └── my_orders.html
│   └── admin/          # Admin templates
│       ├── dashboard.html
│       ├── products.html
│       ├── add_product.html
│       ├── edit_product.html
│       ├── orders.html
│       └── order_detail.html
│
├── static/             # Static files
│   ├── css/
│   │   └── style.css   # Custom styles
│   └── js/
│       └── main.js     # JavaScript functionality
│
└── database/           # Database files
    └── schema.sql      # Database schema and sample data
```

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- MySQL Server 5.7 or higher
- pip (Python package manager)

## 🔧 Installation & Setup

### Step 1: Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd ecommerce-store
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up MySQL Database

1. **Start MySQL Server** (if not already running)

2. **Create Database**:
   ```bash
   # Login to MySQL
   mysql -u root -p
   
   # Create database
   CREATE DATABASE ecommerce_db;
   EXIT;
   ```

3. **Update Database Configuration** in `config.py`:
   ```python
   MYSQL_HOST = 'localhost'
   MYSQL_USER = 'root'
   MYSQL_PASSWORD = 'your_password'
   MYSQL_DATABASE = 'ecommerce_db'
   ```

4. **Initialize Database with Sample Data**:
   ```bash
   python init_db.py
   ```
   
   This script will:
   - Create all database tables
   - Create admin and sample customer accounts with properly hashed passwords
   - Add sample products (food, flowers, heritage)

### Step 5: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 👤 Default Accounts

### Admin Account
- **Email**: admin@ecommerce.com
- **Password**: admin123

### Customer Account (Sample)
- **Email**: customer@example.com
- **Password**: customer123

> **Note**: For security, change these passwords after first login in production!

## 🗄️ Database Schema

### Tables

1. **users** - User accounts (customers and admins)
   - user_id, name, email, password, role, created_at

2. **products** - Product catalog
   - product_id, name, category, price, description, image, stock, created_at

3. **cart** - Shopping cart items
   - cart_id, user_id, product_id, quantity, created_at

4. **orders** - Customer orders
   - order_id, user_id, total_amount, order_date, status, payment_method, shipping_address, phone

5. **order_items** - Items in each order
   - order_item_id, order_id, product_id, quantity, price

## 🎯 Usage Guide

### For Customers

1. **Browse Products**: Visit the homepage or navigate to "All Products"
2. **Filter by Category**: Use category buttons to filter Food, Flowers, or Heritage products
3. **View Product Details**: Click on any product to see full details
4. **Add to Cart**: Login and add products to your cart
5. **Checkout**: Review cart, enter shipping details, and place order
6. **Track Orders**: View order history in "My Orders"

### For Admins

1. **Login**: Use admin credentials to access admin panel
2. **Dashboard**: View statistics and recent orders
3. **Manage Products**: Add, edit, or delete products
4. **Manage Orders**: View orders and update their status
5. **Categories**: Products are automatically organized by category

## 🔒 Security Features

- **Password Hashing**: Uses Werkzeug's secure password hashing (PBKDF2)
- **Session Management**: Flask-Login for secure session handling
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **Role-Based Access**: Admin routes protected with decorators
- **Input Validation**: Form validation on both client and server side

## 🎨 UI/UX Features

- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI**: Clean, professional design with smooth transitions
- **User Feedback**: Flash messages for actions and errors
- **Intuitive Navigation**: Easy-to-use navigation and category filters
- **Product Images**: Support for product images (URL-based for demo)

## 🚧 Future Enhancements

- Image upload functionality for products
- Payment gateway integration (Stripe, PayPal)
- Email notifications for orders
- Product reviews and ratings
- Wishlist functionality
- Advanced search and filtering
- Order tracking with status updates
- Multi-language support

## 🐛 Troubleshooting

### Database Connection Issues
- Ensure MySQL server is running
- Verify database credentials in `config.py`
- Check if database `ecommerce_db` exists

### Import Errors
- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

### Port Already in Use
- Change port in `app.py`: `app.run(debug=True, port=5001)`

## 📝 Notes

- This is a demo application. For production use:
  - Change the SECRET_KEY in `config.py`
  - Use environment variables for sensitive data
  - Implement proper error handling
  - Add logging
  - Set up HTTPS
  - Use a production WSGI server (Gunicorn, uWSGI)

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as a full-stack e-commerce solution demonstration.

---

**Happy Shopping! 🛒**
