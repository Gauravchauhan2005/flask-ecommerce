"""
Database Initialization Script
Run this script to set up the database with sample data and proper password hashing
"""
from app import app, db
from models import User, Product
from werkzeug.security import generate_password_hash

def init_database():
    """Initialize database with tables and sample data"""
    with app.app_context():
        # Create all tables
        print("Creating database tables...")
        db.create_all()
        print("✓ Tables created successfully!")
        
        # Check if admin user exists
        admin = User.query.filter_by(email='admin@ecommerce.com').first()
        if not admin:
            print("\nCreating admin user...")
            admin = User(
                name='Admin User',
                email='admin@ecommerce.com',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            print("✓ Admin user created!")
            print("  Email: admin@ecommerce.com")
            print("  Password: admin123")
        else:
            print("\nAdmin user already exists.")
        
        # Check if sample customer exists
        customer = User.query.filter_by(email='customer@example.com').first()
        if not customer:
            print("\nCreating sample customer...")
            customer = User(
                name='John Doe',
                email='customer@example.com',
                role='customer'
            )
            customer.set_password('customer123')
            db.session.add(customer)
            print("✓ Sample customer created!")
            print("  Email: customer@example.com")
            print("  Password: customer123")
        else:
            print("\nSample customer already exists.")
        
        # Add sample products if they don't exist
        if Product.query.count() == 0:
            print("\nAdding sample products...")
            
            # Food products
            food_products = [
                Product(name='Margherita Pizza', category='food', price=12.99,
                       description='Classic Italian pizza with fresh tomatoes, mozzarella, and basil',
                       image='https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400', stock=50),
                Product(name='Chicken Biryani', category='food', price=15.99,
                       description='Fragrant basmati rice cooked with tender chicken and aromatic spices',
                       image='https://images.unsplash.com/photo-1563379091339-03246963d4c9?w=400', stock=30),
                Product(name='Chocolate Cake', category='food', price=8.99,
                       description='Rich and moist chocolate cake with creamy frosting',
                       image='https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400', stock=25),
                Product(name='Caesar Salad', category='food', price=9.99,
                       description='Fresh romaine lettuce with caesar dressing, croutons, and parmesan',
                       image='https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400', stock=40),
                Product(name='Sushi Platter', category='food', price=18.99,
                       description='Assorted fresh sushi rolls with soy sauce and wasabi',
                       image='https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=400', stock=20),
                Product(name='Burger Combo', category='food', price=11.99,
                       description='Juicy beef burger with fries and soft drink',
                       image='https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400', stock=35),
            ]
            
            # Flower products
            flower_products = [
                Product(name='Red Roses Bouquet', category='flowers', price=29.99,
                       description='A dozen beautiful red roses arranged in an elegant bouquet',
                       image='https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=400', stock=15),
                Product(name='Sunflower Arrangement', category='flowers', price=24.99,
                       description='Bright and cheerful sunflowers in a decorative vase',
                       image='https://images.unsplash.com/photo-1597848212624-e593beb5e0e1?w=400', stock=20),
                Product(name='Lily Bouquet', category='flowers', price=32.99,
                       description='Elegant white lilies with green foliage',
                       image='https://images.unsplash.com/photo-1520763185298-1b434c919102?w=400', stock=12),
                Product(name='Mixed Spring Flowers', category='flowers', price=27.99,
                       description='Colorful mix of seasonal spring flowers',
                       image='https://images.unsplash.com/photo-1490750967868-88c44860c1d1?w=400', stock=18),
                Product(name='Orchid Plant', category='flowers', price=35.99,
                       description='Exotic purple orchid plant in decorative pot',
                       image='https://images.unsplash.com/photo-1462275646964-a0e3386b89fa?w=400', stock=10),
                Product(name='Tulip Bouquet', category='flowers', price=22.99,
                       description='Fresh tulips in various colors',
                       image='https://images.unsplash.com/photo-1520763185298-1b434c919102?w=400', stock=25),
            ]
            
            # Heritage products
            heritage_products = [
                Product(name='Handwoven Silk Scarf', category='heritage', price=45.99,
                       description='Traditional handwoven silk scarf with intricate patterns',
                       image='https://images.unsplash.com/photo-1586075010923-2dd4570fb338?w=400', stock=15),
                Product(name='Ceramic Pottery Set', category='heritage', price=89.99,
                       description='Handcrafted ceramic pottery set with traditional designs',
                       image='https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', stock=8),
                Product(name='Wooden Carved Statue', category='heritage', price=125.99,
                       description='Beautifully carved wooden statue showcasing traditional craftsmanship',
                       image='https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', stock=5),
                Product(name='Embroidered Cushion Cover', category='heritage', price=34.99,
                       description='Hand-embroidered cushion cover with traditional motifs',
                       image='https://images.unsplash.com/photo-1586075010923-2dd4570fb338?w=400', stock=20),
                Product(name='Brass Decorative Bowl', category='heritage', price=55.99,
                       description='Handcrafted brass bowl with intricate engravings',
                       image='https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', stock=12),
                Product(name='Traditional Jewelry Box', category='heritage', price=67.99,
                       description='Ornate wooden jewelry box with traditional carvings',
                       image='https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', stock=10),
            ]
            
            all_products = food_products + flower_products + heritage_products
            for product in all_products:
                db.session.add(product)
            
            print(f"✓ Added {len(all_products)} sample products!")
        else:
            print(f"\nDatabase already contains {Product.query.count()} products.")
        
        # Commit all changes
        db.session.commit()
        print("\n" + "="*50)
        print("Database initialization completed successfully!")
        print("="*50)
        print("\nYou can now run the application with: python app.py")
        print("\nDefault Login Credentials:")
        print("  Admin: admin@ecommerce.com / admin123")
        print("  Customer: customer@example.com / customer123")

if __name__ == '__main__':
    init_database()
