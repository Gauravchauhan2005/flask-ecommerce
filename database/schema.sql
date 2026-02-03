-- E-Commerce Database Schema
-- Database: ecommerce_db
-- Created for: Food, Flowers, and Heritage Products E-Commerce Store

-- Create database
CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'customer' NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    image VARCHAR(255),
    stock INT DEFAULT 100 NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Cart table
CREATE TABLE IF NOT EXISTS cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT DEFAULT 1 NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    status VARCHAR(50) DEFAULT 'pending' NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    shipping_address TEXT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Order items table
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Note: User accounts should be created through the application or init_db.py script
-- to ensure proper password hashing. Sample users will be created by init_db.py

-- Insert sample food products
INSERT INTO products (name, category, price, description, image, stock) VALUES
('Margherita Pizza', 'food', 12.99, 'Classic Italian pizza with fresh tomatoes, mozzarella, and basil', 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400', 50),
('Chicken Biryani', 'food', 15.99, 'Fragrant basmati rice cooked with tender chicken and aromatic spices', 'https://images.unsplash.com/photo-1563379091339-03246963d4c9?w=400', 30),
('Chocolate Cake', 'food', 8.99, 'Rich and moist chocolate cake with creamy frosting', 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400', 25),
('Caesar Salad', 'food', 9.99, 'Fresh romaine lettuce with caesar dressing, croutons, and parmesan', 'https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400', 40),
('Sushi Platter', 'food', 18.99, 'Assorted fresh sushi rolls with soy sauce and wasabi', 'https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=400', 20),
('Burger Combo', 'food', 11.99, 'Juicy beef burger with fries and soft drink', 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400', 35)
ON DUPLICATE KEY UPDATE name=name;

-- Insert sample flower products
INSERT INTO products (name, category, price, description, image, stock) VALUES
('Red Roses Bouquet', 'flowers', 29.99, 'A dozen beautiful red roses arranged in an elegant bouquet', 'https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=400', 15),
('Sunflower Arrangement', 'flowers', 24.99, 'Bright and cheerful sunflowers in a decorative vase', 'https://images.unsplash.com/photo-1597848212624-e593beb5e0e1?w=400', 20),
('Lily Bouquet', 'flowers', 32.99, 'Elegant white lilies with green foliage', 'https://images.unsplash.com/photo-1520763185298-1b434c919102?w=400', 12),
('Mixed Spring Flowers', 'flowers', 27.99, 'Colorful mix of seasonal spring flowers', 'https://images.unsplash.com/photo-1490750967868-88c44860c1d1?w=400', 18),
('Orchid Plant', 'flowers', 35.99, 'Exotic purple orchid plant in decorative pot', 'https://images.unsplash.com/photo-1462275646964-a0e3386b89fa?w=400', 10),
('Tulip Bouquet', 'flowers', 22.99, 'Fresh tulips in various colors', 'https://images.unsplash.com/photo-1520763185298-1b434c919102?w=400', 25)
ON DUPLICATE KEY UPDATE name=name;

-- Insert sample heritage/handicraft products
INSERT INTO products (name, category, price, description, image, stock) VALUES
('Handwoven Silk Scarf', 'heritage', 45.99, 'Traditional handwoven silk scarf with intricate patterns', 'https://images.unsplash.com/photo-1586075010923-2dd4570fb338?w=400', 15),
('Ceramic Pottery Set', 'heritage', 89.99, 'Handcrafted ceramic pottery set with traditional designs', 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', 8),
('Wooden Carved Statue', 'heritage', 125.99, 'Beautifully carved wooden statue showcasing traditional craftsmanship', 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', 5),
('Embroidered Cushion Cover', 'heritage', 34.99, 'Hand-embroidered cushion cover with traditional motifs', 'https://images.unsplash.com/photo-1586075010923-2dd4570fb338?w=400', 20),
('Brass Decorative Bowl', 'heritage', 55.99, 'Handcrafted brass bowl with intricate engravings', 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', 12),
('Traditional Jewelry Box', 'heritage', 67.99, 'Ornate wooden jewelry box with traditional carvings', 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400', 10)
ON DUPLICATE KEY UPDATE name=name;

-- Create indexes for better performance
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_product_category ON products(category);
CREATE INDEX idx_cart_user ON cart(user_id);
CREATE INDEX idx_order_user ON orders(user_id);
CREATE INDEX idx_order_status ON orders(status);
CREATE INDEX idx_order_date ON orders(order_date);
