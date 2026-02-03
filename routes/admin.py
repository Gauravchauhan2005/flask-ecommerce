"""
Admin Routes
Handles admin dashboard, product management, and order management
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from functools import wraps
from models import db, Product, Order, User
from werkzeug.utils import secure_filename
import os

admin_bp = Blueprint('admin', __name__)

def admin_required(f):
    """Decorator to require admin role"""
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if current_user.role != 'admin':
            flash('Access denied. Admin privileges required.', 'error')
            return redirect(url_for('user.home'))
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route('/admin/dashboard')
@admin_required
def dashboard():
    """Admin dashboard"""
    total_products = Product.query.count()
    total_orders = Order.query.count()
    total_users = User.query.filter_by(role='customer').count()
    pending_orders = Order.query.filter_by(status='pending').count()
    
    recent_orders = Order.query.order_by(Order.order_date.desc()).limit(10).all()
    
    return render_template('admin/dashboard.html',
                         total_products=total_products,
                         total_orders=total_orders,
                         total_users=total_users,
                         pending_orders=pending_orders,
                         recent_orders=recent_orders)


@admin_bp.route('/admin/products')
@admin_required
def products():
    """Admin product management page"""
    category = request.args.get('category', '')
    query = Product.query
    
    if category:
        query = query.filter_by(category=category)
    
    products = query.order_by(Product.created_at.desc()).all()
    return render_template('admin/products.html', products=products, category=category)


@admin_bp.route('/admin/product/add', methods=['GET', 'POST'])
@admin_required
def add_product():
    """Add new product"""
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        price = float(request.form.get('price'))
        description = request.form.get('description')
        stock = int(request.form.get('stock', 100))
        image = request.form.get('image', '')  # For demo, using URL
        
        if not all([name, category, price]):
            flash('Please fill in all required fields', 'error')
            return render_template('admin/add_product.html')
        
        product = Product(
            name=name,
            category=category,
            price=price,
            description=description,
            stock=stock,
            image=image
        )
        
        try:
            db.session.add(product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('admin.products'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding product', 'error')
    
    return render_template('admin/add_product.html')


@admin_bp.route('/admin/product/edit/<int:product_id>', methods=['GET', 'POST'])
@admin_required
def edit_product(product_id):
    """Edit existing product"""
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.category = request.form.get('category')
        product.price = float(request.form.get('price'))
        product.description = request.form.get('description')
        product.stock = int(request.form.get('stock', 100))
        product.image = request.form.get('image', product.image)
        
        try:
            db.session.commit()
            flash('Product updated successfully!', 'success')
            return redirect(url_for('admin.products'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating product', 'error')
    
    return render_template('admin/edit_product.html', product=product)


@admin_bp.route('/admin/product/delete/<int:product_id>')
@admin_required
def delete_product(product_id):
    """Delete product"""
    product = Product.query.get_or_404(product_id)
    
    try:
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting product', 'error')
    
    return redirect(url_for('admin.products'))


@admin_bp.route('/admin/orders')
@admin_required
def orders():
    """Admin order management page"""
    status = request.args.get('status', '')
    query = Order.query
    
    if status:
        query = query.filter_by(status=status)
    
    orders = query.order_by(Order.order_date.desc()).all()
    return render_template('admin/orders.html', orders=orders, status=status)


@admin_bp.route('/admin/order/<int:order_id>')
@admin_required
def order_detail(order_id):
    """Admin order detail page"""
    order = Order.query.get_or_404(order_id)
    return render_template('admin/order_detail.html', order=order)


@admin_bp.route('/admin/order/update-status', methods=['POST'])
@admin_required
def update_order_status():
    """Update order status"""
    order_id = request.form.get('order_id')
    status = request.form.get('status')
    
    order = Order.query.get_or_404(order_id)
    order.status = status
    
    try:
        db.session.commit()
        flash('Order status updated!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error updating order status', 'error')
    
    return redirect(url_for('admin.order_detail', order_id=order_id))
