# Setup Checklist

Use this checklist to ensure everything is set up correctly:

## ✅ Pre-Installation

- [ ] Python 3.8+ installed (`python --version`)
- [ ] MySQL Server installed and running
- [ ] pip package manager available (`pip --version`)

## ✅ Installation Steps

- [ ] Cloned/downloaded project files
- [ ] Created virtual environment (optional but recommended)
- [ ] Activated virtual environment
- [ ] Installed dependencies: `pip install -r requirements.txt`

## ✅ Database Setup

- [ ] MySQL server is running
- [ ] Created database: `CREATE DATABASE ecommerce_db;`
- [ ] Updated `config.py` with correct MySQL credentials:
  - [ ] MYSQL_HOST
  - [ ] MYSQL_USER
  - [ ] MYSQL_PASSWORD
  - [ ] MYSQL_DATABASE
- [ ] Ran initialization script: `python init_db.py`
- [ ] Verified tables were created
- [ ] Verified sample data was inserted

## ✅ Application Setup

- [ ] All files are in correct locations
- [ ] No import errors when running `python app.py`
- [ ] Application starts without errors
- [ ] Can access http://localhost:5000

## ✅ Testing

### Customer Features
- [ ] Homepage loads correctly
- [ ] Can browse products by category
- [ ] Can search for products
- [ ] Can view product details
- [ ] Can create customer account
- [ ] Can login as customer
- [ ] Can add products to cart
- [ ] Can update cart quantities
- [ ] Can remove items from cart
- [ ] Can proceed to checkout
- [ ] Can place order (Cash on Delivery)
- [ ] Can place order (Online Payment demo)
- [ ] Can view order confirmation
- [ ] Can view order history

### Admin Features
- [ ] Can login as admin (admin@ecommerce.com / admin123)
- [ ] Admin dashboard displays statistics
- [ ] Can view all products
- [ ] Can add new product
- [ ] Can edit existing product
- [ ] Can delete product
- [ ] Can filter products by category
- [ ] Can view all orders
- [ ] Can filter orders by status
- [ ] Can view order details
- [ ] Can update order status

## ✅ Responsive Design

- [ ] Website works on desktop browsers
- [ ] Website works on mobile devices
- [ ] Navigation menu works on mobile
- [ ] Forms are usable on mobile
- [ ] Images display correctly

## ✅ Security

- [ ] Passwords are hashed (check database)
- [ ] Admin routes require authentication
- [ ] Users can only access their own data
- [ ] SQL injection protection (using ORM)

## 🎉 All Done!

If all items are checked, your e-commerce website is ready to use!

## 🐛 Troubleshooting

**If something doesn't work:**

1. Check error messages in terminal
2. Verify database connection in `config.py`
3. Ensure MySQL is running
4. Check if port 5000 is available
5. Review README.md troubleshooting section
6. Check QUICKSTART.md for common issues
