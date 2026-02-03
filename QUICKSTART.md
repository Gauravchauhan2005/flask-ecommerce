# Quick Start Guide

## 🚀 Fast Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Database
Edit `config.py` and update MySQL credentials:
```python
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DATABASE = 'ecommerce_db'
```

### 3. Create Database
```bash
mysql -u root -p
CREATE DATABASE ecommerce_db;
EXIT;
```

### 4. Initialize Database
```bash
python init_db.py
```

### 5. Run Application
```bash
python app.py
```

### 6. Access the Website
- Open browser: http://localhost:5000
- **Admin Login**: admin@ecommerce.com / admin123
- **Customer Login**: customer@example.com / customer123

## ✅ That's it! You're ready to go!

## 📝 Next Steps

1. **Browse Products**: Visit homepage to see featured products
2. **Create Account**: Sign up as a new customer
3. **Add to Cart**: Login and add products to cart
4. **Place Order**: Complete checkout process
5. **Admin Panel**: Login as admin to manage products and orders

## 🐛 Troubleshooting

**Database Connection Error?**
- Check MySQL is running: `mysql -u root -p`
- Verify credentials in `config.py`
- Ensure database exists: `SHOW DATABASES;`

**Import Errors?**
- Activate virtual environment
- Reinstall: `pip install -r requirements.txt`

**Port Already in Use?**
- Change port in `app.py` line 39: `port=5001`

## 📚 Full Documentation

See `README.md` for complete documentation.
