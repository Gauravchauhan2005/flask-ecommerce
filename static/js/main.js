// Main JavaScript file for E-Commerce Store

document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // Quantity input validation
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');
    quantityInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            const value = parseInt(this.value);
            const max = parseInt(this.max);
            const min = parseInt(this.min);
            
            if (value > max) {
                this.value = max;
                alert('Maximum quantity available: ' + max);
            }
            if (value < min) {
                this.value = min;
            }
        });
    });
    
    // Confirm delete actions
    const deleteLinks = document.querySelectorAll('a[onclick*="confirm"]');
    deleteLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
});

// Update cart count (if needed for AJAX updates)
function updateCartCount(count) {
    const cartCount = document.getElementById('cart-count');
    if (cartCount) {
        cartCount.textContent = count;
    }
}

// Format currency
const CURRENCY_SYMBOL = "₹";

function formatCurrency(amount) {
    return CURRENCY_SYMBOL+ parseFloat(amount).toFixed(2);
}

// Calculate total
function calculateTotal() {
    const items = document.querySelectorAll('.cart-item');
    let total = 0;
    
    items.forEach(function(item) {
        const price = parseFloat(item.querySelector('.item-price').textContent.replace( '₹', ''));
        const quantity = parseInt(item.querySelector('.item-quantity').value);
        total += price * quantity;
    });
    
    return total;
}
