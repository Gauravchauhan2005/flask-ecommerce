"""
User Routes
Handles homepage, products, cart, checkout, and orders
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models import db, Product, Cart, Order, OrderItem
from sqlalchemy import func

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def home():
    """Homepage with categories"""
    # Get featured products from each category
    food_products = Product.query.filter_by(category='food').limit(4).all()
    flower_products = Product.query.filter_by(category='flowers').limit(4).all()
    heritage_products = Product.query.filter_by(category='heritage').limit(4).all()
    
    return render_template('user/home.html', 
                         food_products=food_products,
                         flower_products=flower_products,
                         heritage_products=heritage_products)


@user_bp.route('/products')
def products():
    """Product listing page with filters"""
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    
    query = Product.query
    
    if category:
        query = query.filter_by(category=category)
    
    if search:
        query = query.filter(Product.name.like(f'%{search}%'))
    
    products = query.all()
    
    return render_template('user/products.html', products=products, category=category, search=search)


@user_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    """Product detail page"""
    product = Product.query.get_or_404(product_id)
    return render_template('user/product_detail.html', product=product)


@user_bp.route('/add-to-cart', methods=['POST'])
@login_required
def add_to_cart():
    """Add product to cart"""
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 1))
    
    product = Product.query.get_or_404(product_id)
    
    # Check if item already in cart
    cart_item = Cart.query.filter_by(user_id=current_user.user_id, product_id=product_id).first()
    
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=current_user.user_id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    
    db.session.commit()
    flash(f'{product.name} added to cart!', 'success')
    return redirect(request.referrer or url_for('user.products'))


@user_bp.route('/cart')
@login_required
def cart():
    """Shopping cart page"""
    cart_items = Cart.query.filter_by(user_id=current_user.user_id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    return render_template('user/cart.html', cart_items=cart_items, total=total)


@user_bp.route('/update-cart', methods=['POST'])
@login_required
def update_cart():
    """Update cart item quantity"""
    cart_id = request.form.get('cart_id')
    quantity = int(request.form.get('quantity', 1))
    
    cart_item = Cart.query.get_or_404(cart_id)
    
    if cart_item.user_id != current_user.user_id:
        flash('Unauthorized access', 'error')
        return redirect(url_for('user.cart'))
    
    if quantity <= 0:
        db.session.delete(cart_item)
    else:
        cart_item.quantity = quantity
    
    db.session.commit()
    flash('Cart updated!', 'success')
    return redirect(url_for('user.cart'))


@user_bp.route('/remove-from-cart/<int:cart_id>')
@login_required
def remove_from_cart(cart_id):
    """Remove item from cart"""
    cart_item = Cart.query.get_or_404(cart_id)
    
    if cart_item.user_id != current_user.user_id:
        flash('Unauthorized access', 'error')
        return redirect(url_for('user.cart'))
    
    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart', 'success')
    return redirect(url_for('user.cart'))


@user_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    """Checkout page"""
    cart_items = Cart.query.filter_by(user_id=current_user.user_id).all()
    
    if not cart_items:
        flash('Your cart is empty', 'error')
        return redirect(url_for('user.cart'))
    
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    if request.method == 'POST':
        payment_method = request.form.get('payment_method')
        shipping_address = request.form.get('shipping_address')
        phone = request.form.get('phone')
        
        if not all([payment_method, shipping_address, phone]):
            flash('Please fill in all fields', 'error')
            return render_template('user/checkout.html', cart_items=cart_items, total=total)
        
        # Create order
        order = Order(
            user_id=current_user.user_id,
            total_amount=total,
            payment_method=payment_method,
            shipping_address=shipping_address,
            phone=phone,
            status='pending'
        )
        db.session.add(order)
        db.session.flush()  # Get order_id
        
        # Create order items
        for cart_item in cart_items:
            order_item = OrderItem(
                order_id=order.order_id,
                product_id=cart_item.product_id,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )
            db.session.add(order_item)
        
        # Clear cart
        Cart.query.filter_by(user_id=current_user.user_id).delete()
        
        db.session.commit()
        
        return redirect(url_for('user.order_confirmation', order_id=order.order_id))
    
    return render_template('user/checkout.html', cart_items=cart_items, total=total)


@user_bp.route('/order-confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    """Order confirmation page"""
    order = Order.query.get_or_404(order_id)
    
    if order.user_id != current_user.user_id:
        flash('Unauthorized access', 'error')
        return redirect(url_for('user.home'))
    
    return render_template('user/order_confirmation.html', order=order)


@user_bp.route('/my-orders')
@login_required
def my_orders():
    """User's order history"""
    orders = Order.query.filter_by(user_id=current_user.user_id).order_by(Order.order_date.desc()).all()
    return render_template('user/my_orders.html', orders=orders)
