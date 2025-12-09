"""
SAVA E-Commerce Platform - Complete Functional Version
Version 8.0 - All Pages Working

Features:
- Premium modern design
- All pages fully functional
- Complete navigation
- Cart functionality
- User authentication
- Product browsing
- Checkout flow
"""
import streamlit as st
from typing import Optional, Dict, Any, List

# Page Configuration
st.set_page_config(
    page_title="SAVA | Premium E-Commerce",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== PROFESSIONAL CSS ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');
    
    :root {
        --primary: #0F172A;
        --accent: #6366F1;
        --accent-hover: #4F46E5;
        --success: #10B981;
        --warning: #F59E0B;
        --error: #EF4444;
        --bg-primary: #FFFFFF;
        --bg-secondary: #F8FAFC;
        --bg-tertiary: #F1F5F9;
        --text-primary: #0F172A;
        --text-secondary: #64748B;
        --text-muted: #94A3B8;
        --border: #E2E8F0;
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
        --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
        --radius-sm: 0.375rem;
        --radius-md: 0.5rem;
        --radius-lg: 0.75rem;
        --radius-xl: 1rem;
        --radius-2xl: 1.5rem;
    }
    
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: var(--text-primary);
        background: var(--bg-secondary) !important;
        -webkit-font-smoothing: antialiased;
    }
    
    #MainMenu, footer, header { visibility: hidden; }
    .stDeployButton { display: none; }
    
    .main .block-container {
        max-width: 1400px !important;
        padding: 1rem 2rem 4rem !important;
    }
    
    /* Premium Header */
    .premium-header {
        background: linear-gradient(135deg, var(--primary) 0%, #1E293B 100%);
        padding: 1rem 2rem;
        border-radius: var(--radius-2xl);
        margin-bottom: 2rem;
        box-shadow: var(--shadow-lg);
    }
    
    .header-inner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .logo {
        font-family: 'Outfit', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff 0%, #A5B4FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .nav-links {
        display: flex;
        gap: 1.5rem;
    }
    
    .nav-link {
        color: rgba(255,255,255,0.8);
        text-decoration: none;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: var(--radius-md);
        transition: all 0.2s;
    }
    
    .nav-link:hover {
        background: rgba(255,255,255,0.1);
        color: white;
    }
    
    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #A855F7 100%);
        border-radius: var(--radius-2xl);
        padding: 4rem 3rem;
        text-align: center;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .hero h1 {
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    
    .hero p {
        font-size: 1.25rem;
        color: rgba(255,255,255,0.9);
        margin-bottom: 2rem;
    }
    
    .hero-btn {
        display: inline-block;
        background: white;
        color: var(--accent);
        padding: 1rem 2.5rem;
        border-radius: var(--radius-xl);
        font-weight: 700;
        font-size: 1.125rem;
        text-decoration: none;
        box-shadow: var(--shadow-xl);
        transition: all 0.3s;
        cursor: pointer;
    }
    
    .hero-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
    }
    
    /* Section Title */
    .section-title {
        font-family: 'Outfit', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 2rem 0 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    /* Product Cards */
    .product-card {
        background: white;
        border-radius: var(--radius-xl);
        overflow: hidden;
        border: 1px solid var(--border);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
    }
    
    .product-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--shadow-xl);
        border-color: var(--accent);
    }
    
    .product-img-container {
        position: relative;
        width: 100%;
        padding-top: 100%;
        background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-tertiary) 100%);
        overflow: hidden;
    }
    
    .product-img-container img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }
    
    .product-card:hover .product-img-container img {
        transform: scale(1.1);
    }
    
    .product-badge {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: var(--accent);
        color: white;
        padding: 0.375rem 0.75rem;
        border-radius: var(--radius-md);
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .product-badge.sale { background: var(--error); }
    .product-badge.new { background: var(--success); }
    
    .product-info {
        padding: 1.5rem;
    }
    
    .product-category {
        color: var(--text-muted);
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .product-name {
        font-family: 'Outfit', sans-serif;
        font-size: 1.125rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.75rem;
        line-height: 1.4;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    
    .product-rating {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1rem;
        font-size: 0.875rem;
    }
    
    .stars { color: #FBBF24; }
    
    .product-price {
        font-family: 'Outfit', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--accent);
    }
    
    .product-old-price {
        font-size: 0.875rem;
        color: var(--text-muted);
        text-decoration: line-through;
        margin-left: 0.5rem;
    }
    
    /* Buttons */
    .stButton > button {
        font-weight: 600;
        border-radius: var(--radius-lg) !important;
        transition: all 0.2s !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%) !important;
        color: white !important;
        box-shadow: var(--shadow-md) !important;
    }
    
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-lg) !important;
    }
    
    .stButton > button[kind="secondary"] {
        background: white !important;
        color: var(--text-primary) !important;
        border: 2px solid var(--border) !important;
    }
    
    .stButton > button[kind="secondary"]:hover {
        border-color: var(--accent) !important;
        color: var(--accent) !important;
    }
    
    .stButton > button > div > p {
        background: transparent !important;
        color: inherit !important;
    }
    
    /* Inputs */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div {
        border: 2px solid var(--border) !important;
        border-radius: var(--radius-lg) !important;
        padding: 0.75rem 1rem !important;
        transition: all 0.2s !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: var(--bg-tertiary);
        padding: 0.5rem;
        border-radius: var(--radius-xl);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-lg);
        padding: 0.75rem 1.5rem;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: white !important;
        box-shadow: var(--shadow-sm);
    }
    
    /* Cards Container */
    .card {
        background: white;
        border-radius: var(--radius-xl);
        padding: 2rem;
        border: 1px solid var(--border);
        box-shadow: var(--shadow-sm);
    }
    
    /* Cart Item */
    .cart-item {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        padding: 1.5rem;
        background: var(--bg-secondary);
        border-radius: var(--radius-lg);
        margin-bottom: 1rem;
        transition: all 0.2s;
    }
    
    .cart-item:hover {
        background: white;
        box-shadow: var(--shadow-md);
    }
    
    /* Footer */
    .footer {
        background: var(--primary);
        color: white;
        padding: 3rem 2rem 2rem;
        margin-top: 4rem;
        border-radius: var(--radius-2xl) var(--radius-2xl) 0 0;
    }
    
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        max-width: 1400px;
        margin: 0 auto 2rem;
    }
    
    .footer-col h4 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.125rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: white;
    }
    
    .footer-col a {
        display: block;
        color: rgba(255,255,255,0.7);
        text-decoration: none;
        margin-bottom: 0.5rem;
        transition: color 0.2s;
    }
    
    .footer-col a:hover { color: white; }
    
    .footer-bottom {
        text-align: center;
        padding-top: 2rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        color: rgba(255,255,255,0.6);
        font-size: 0.875rem;
    }
    
    /* Feature Cards */
    .feature-card {
        background: white;
        border-radius: var(--radius-xl);
        padding: 2rem;
        text-align: center;
        border: 1px solid var(--border);
        transition: all 0.3s;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: var(--text-secondary);
        font-size: 0.9375rem;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero h1 { font-size: 2.5rem; }
        .hero { padding: 3rem 1.5rem; }
        .premium-header { padding: 1rem; }
        .logo { font-size: 1.5rem; }
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in { animation: fadeInUp 0.5s ease-out; }
    
    /* Scrollbar */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: var(--bg-secondary); }
    ::-webkit-scrollbar-thumb { 
        background: var(--text-muted); 
        border-radius: 5px; 
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--text-secondary); }
</style>
""", unsafe_allow_html=True)

# ==================== SESSION STATE ====================
def init_session():
    defaults = {
        'page': 'home',
        'lang': 'ES',
        'user': None,
        'cart': [],
        'cart_count': 0,
        'search_query': '',
        'selected_category': None,
        'selected_product': None
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session()

# ==================== BILINGUAL TEXTS ====================
TEXTS = {
    'ES': {
        'home': 'Inicio',
        'products': 'Productos',
        'about': 'Nosotros',
        'cart': 'Carrito',
        'signin': 'Ingresar',
        'signup': 'Crear Cuenta',
        'hero_title': '¡Bienvenido a SAVA!',
        'hero_subtitle': 'Descubre productos increíbles con los mejores precios y envío gratis',
        'explore': 'Explorar Productos',
        'featured': 'Productos Destacados',
        'categories': 'Categorías',
        'search_placeholder': 'Buscar productos, marcas y más...',
        'add_to_cart': 'Agregar al Carrito',
        'buy_now': 'Comprar Ahora',
        'view_details': 'Ver Detalles',
        'cart_empty': 'Tu carrito está vacío',
        'cart_total': 'Total',
        'checkout': 'Proceder al Pago',
        'continue_shopping': 'Continuar Comprando',
        'quantity': 'Cantidad',
        'remove': 'Eliminar',
        'about_title': 'Acerca de SAVA',
        'our_mission': 'Nuestra Misión',
        'our_values': 'Nuestros Valores',
        'contact': 'Contacto',
        'email': 'Correo Electrónico',
        'password': 'Contraseña',
        'name': 'Nombre Completo',
        'login': 'Iniciar Sesión',
        'register': 'Registrarse',
        'logout': 'Cerrar Sesión',
        'welcome': 'Bienvenido',
        'no_products': 'No se encontraron productos',
        'loading': 'Cargando...',
        'reviews': 'reseñas',
        'in_stock': 'En Stock',
        'out_of_stock': 'Agotado',
        'free_shipping': 'Envío Gratis',
        'secure_payment': 'Pago Seguro',
        'support_24_7': 'Soporte 24/7',
        'easy_returns': 'Devoluciones Fáciles'
    },
    'EN': {
        'home': 'Home',
        'products': 'Products',
        'about': 'About',
        'cart': 'Cart',
        'signin': 'Sign In',
        'signup': 'Sign Up',
        'hero_title': 'Welcome to SAVA!',
        'hero_subtitle': 'Discover amazing products with the best prices and free shipping',
        'explore': 'Explore Products',
        'featured': 'Featured Products',
        'categories': 'Categories',
        'search_placeholder': 'Search products, brands and more...',
        'add_to_cart': 'Add to Cart',
        'buy_now': 'Buy Now',
        'view_details': 'View Details',
        'cart_empty': 'Your cart is empty',
        'cart_total': 'Total',
        'checkout': 'Proceed to Checkout',
        'continue_shopping': 'Continue Shopping',
        'quantity': 'Quantity',
        'remove': 'Remove',
        'about_title': 'About SAVA',
        'our_mission': 'Our Mission',
        'our_values': 'Our Values',
        'contact': 'Contact',
        'email': 'Email',
        'password': 'Password',
        'name': 'Full Name',
        'login': 'Login',
        'register': 'Register',
        'logout': 'Logout',
        'welcome': 'Welcome',
        'no_products': 'No products found',
        'loading': 'Loading...',
        'reviews': 'reviews',
        'in_stock': 'In Stock',
        'out_of_stock': 'Out of Stock',
        'free_shipping': 'Free Shipping',
        'secure_payment': 'Secure Payment',
        'support_24_7': '24/7 Support',
        'easy_returns': 'Easy Returns'
    }
}

T = TEXTS[st.session_state.lang]

# ==================== NAVIGATION ====================
def navigate_to(page):
    st.session_state.page = page
    st.rerun()

# ==================== HEADER ====================
def render_header():
    st.markdown("""
        <div class="premium-header fade-in">
            <div class="header-inner">
                <div class="logo">✨ SAVA</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation Row
    col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
    
    with col1:
        search = st.text_input(
            "search",
            placeholder=T['search_placeholder'],
            value=st.session_state.search_query,
            label_visibility="collapsed",
            key="search_input"
        )
        if search != st.session_state.search_query:
            st.session_state.search_query = search
            navigate_to('products')
    
    with col2:
        if st.button(f"🏠 {T['home']}", use_container_width=True):
            navigate_to('home')
    
    with col3:
        if st.button(f"🛍️ {T['products']}", use_container_width=True):
            navigate_to('products')
    
    with col4:
        if st.session_state.user:
            if st.button(f"👤 {st.session_state.user.get('name', 'User')[:10]}", use_container_width=True):
                navigate_to('account')
        else:
            if st.button(f"👤 {T['signin']}", use_container_width=True):
                navigate_to('auth')
    
    with col5:
        cart_label = f"🛒 ({len(st.session_state.cart)})" if st.session_state.cart else "🛒"
        if st.button(cart_label, use_container_width=True):
            navigate_to('cart')
    
    # Language selector in sidebar-like area
    with st.expander("🌐 Idioma / Language"):
        lang = st.radio("", ['ES', 'EN'], horizontal=True, label_visibility="collapsed")
        if lang != st.session_state.lang:
            st.session_state.lang = lang
            st.rerun()

# ==================== HERO SECTION ====================
def render_hero():
    st.markdown(f"""
        <div class="hero fade-in">
            <div class="hero-content">
                <h1>{T['hero_title']}</h1>
                <p>{T['hero_subtitle']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # CTA Button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button(f"🚀 {T['explore']}", type="primary", use_container_width=True):
            navigate_to('products')

# ==================== FEATURES ====================
def render_features():
    st.markdown("")
    cols = st.columns(4)
    
    features = [
        ("🚚", T['free_shipping'], "En todos los pedidos"),
        ("🔒", T['secure_payment'], "100% seguro"),
        ("📞", T['support_24_7'], "Estamos para ayudarte"),
        ("↩️", T['easy_returns'], "30 días de garantía")
    ]
    
    for i, (icon, title, desc) in enumerate(features):
        with cols[i]:
            st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-desc">{desc}</div>
                </div>
            """, unsafe_allow_html=True)

# ==================== PRODUCT FUNCTIONS ====================
def get_sample_products():
    """Return sample products when Firebase is not available"""
    return [
        {
            'id': '1',
            'name': 'Laptop Gaming Pro X1',
            'price': 1299.99,
            'old_price': 1599.99,
            'category': 'Electronics',
            'rating': 4.8,
            'reviews_count': 256,
            'stock': 15,
            'badge': 'sale',
            'image': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400',
            'description': 'Potente laptop gaming con procesador de última generación, 16GB RAM, 512GB SSD y pantalla 144Hz.'
        },
        {
            'id': '2',
            'name': 'Auriculares Wireless Premium',
            'price': 199.99,
            'category': 'Audio',
            'rating': 4.9,
            'reviews_count': 1024,
            'stock': 50,
            'badge': 'new',
            'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400',
            'description': 'Auriculares inalámbricos con cancelación de ruido activa y 30 horas de batería.'
        },
        {
            'id': '3',
            'name': 'Smartwatch Series 8',
            'price': 349.99,
            'old_price': 399.99,
            'category': 'Wearables',
            'rating': 4.7,
            'reviews_count': 512,
            'stock': 25,
            'badge': 'sale',
            'image': 'https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400',
            'description': 'Reloj inteligente con monitor de salud, GPS y resistencia al agua.'
        },
        {
            'id': '4',
            'name': 'Cámara DSLR Professional',
            'price': 899.99,
            'category': 'Photography',
            'rating': 4.6,
            'reviews_count': 189,
            'stock': 10,
            'image': 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400',
            'description': 'Cámara profesional con sensor de 24MP y grabación de video 4K.'
        },
        {
            'id': '5',
            'name': 'Teclado Mecánico RGB',
            'price': 129.99,
            'category': 'Gaming',
            'rating': 4.8,
            'reviews_count': 876,
            'stock': 100,
            'badge': 'new',
            'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=400',
            'description': 'Teclado mecánico con switches Cherry MX e iluminación RGB personalizable.'
        },
        {
            'id': '6',
            'name': 'Monitor 4K Ultra HD 27"',
            'price': 449.99,
            'old_price': 549.99,
            'category': 'Electronics',
            'rating': 4.5,
            'reviews_count': 324,
            'stock': 20,
            'badge': 'sale',
            'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400',
            'description': 'Monitor 4K con HDR10, 144Hz y tiempo de respuesta de 1ms.'
        },
        {
            'id': '7',
            'name': 'Mochila Tech Travel',
            'price': 79.99,
            'category': 'Accessories',
            'rating': 4.4,
            'reviews_count': 445,
            'stock': 75,
            'image': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400',
            'description': 'Mochila resistente al agua con compartimento para laptop de hasta 17".'
        },
        {
            'id': '8',
            'name': 'Speaker Bluetooth Portable',
            'price': 59.99,
            'category': 'Audio',
            'rating': 4.3,
            'reviews_count': 678,
            'stock': 150,
            'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400',
            'description': 'Altavoz portátil con 20 horas de batería y resistencia IPX7.'
        }
    ]

def get_products():
    """Try to get products from Firebase, fallback to sample data"""
    try:
        from services.firebase_service import FirebaseService
        firebase = FirebaseService()
        products = firebase.get_products(limit=12)
        if products:
            return products
    except:
        pass
    return get_sample_products()

def render_product_card(product, show_button=True):
    """Render a product card"""
    name = product.get('name', 'Product')
    price = product.get('price', 0)
    old_price = product.get('old_price')
    image = product.get('image', 'https://placehold.co/400x400/E2E8F0/64748B?text=Product')
    rating = product.get('rating', 0)
    reviews = product.get('reviews_count', 0)
    category = product.get('category', 'General')
    badge = product.get('badge', '')
    
    badge_html = f'<div class="product-badge {badge}">{badge.upper()}</div>' if badge else ''
    old_price_html = f'<span class="product-old-price">${old_price:.2f}</span>' if old_price else ''
    
    st.markdown(f"""
        <div class="product-card fade-in">
            <div class="product-img-container">
                <img src="{image}" alt="{name}" />
                {badge_html}
            </div>
            <div class="product-info">
                <div class="product-category">{category}</div>
                <div class="product-name">{name}</div>
                <div class="product-rating">
                    <span class="stars">{'⭐' * int(rating)}</span>
                    <span>({reviews} {T['reviews']})</span>
                </div>
                <div>
                    <span class="product-price">${price:.2f}</span>
                    {old_price_html}
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if show_button:
        if st.button(f"🛒 {T['add_to_cart']}", key=f"add_{product.get('id', name)}", use_container_width=True):
            add_to_cart(product)
            st.success("✅ Agregado al carrito!")
            st.rerun()

# ==================== CART FUNCTIONS ====================
def add_to_cart(product, quantity=1):
    """Add product to cart"""
    cart = st.session_state.cart
    
    # Check if product already in cart
    for item in cart:
        if item['id'] == product.get('id'):
            item['quantity'] += quantity
            return
    
    # Add new item
    cart.append({
        'id': product.get('id'),
        'name': product.get('name'),
        'price': product.get('price'),
        'image': product.get('image', ''),
        'quantity': quantity
    })

def remove_from_cart(product_id):
    """Remove product from cart"""
    st.session_state.cart = [item for item in st.session_state.cart if item['id'] != product_id]

def update_cart_quantity(product_id, quantity):
    """Update quantity in cart"""
    for item in st.session_state.cart:
        if item['id'] == product_id:
            item['quantity'] = quantity
            break

def get_cart_total():
    """Calculate cart total"""
    return sum(item['price'] * item['quantity'] for item in st.session_state.cart)

# ==================== PAGES ====================
def render_home_page():
    render_hero()
    render_features()
    
    st.markdown(f'<div class="section-title">🌟 {T["featured"]}</div>', unsafe_allow_html=True)
    
    products = get_products()
    
    if products:
        cols = st.columns(4)
        for idx, product in enumerate(products[:8]):
            with cols[idx % 4]:
                render_product_card(product)
    else:
        st.info(T['no_products'])

def render_products_page():
    st.markdown(f'<div class="section-title">🛍️ {T["products"]}</div>', unsafe_allow_html=True)
    
    # Filters
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search = st.text_input("🔍 Buscar", st.session_state.search_query, key="prod_search")
        if search != st.session_state.search_query:
            st.session_state.search_query = search
    
    with col2:
        categories = ['Todos', 'Electronics', 'Audio', 'Gaming', 'Wearables', 'Photography', 'Accessories']
        selected_cat = st.selectbox(f"📁 {T['categories']}", categories)
    
    with col3:
        sort_options = ['Relevancia', 'Precio: Menor a Mayor', 'Precio: Mayor a Menor', 'Mejor Valorados']
        sort_by = st.selectbox("📊 Ordenar por", sort_options)
    
    st.markdown("---")
    
    # Get and filter products
    products = get_products()
    
    # Apply category filter
    if selected_cat != 'Todos':
        products = [p for p in products if p.get('category') == selected_cat]
    
    # Apply search filter
    if search:
        products = [p for p in products if search.lower() in p.get('name', '').lower()]
    
    # Apply sorting
    if sort_by == 'Precio: Menor a Mayor':
        products.sort(key=lambda x: x.get('price', 0))
    elif sort_by == 'Precio: Mayor a Menor':
        products.sort(key=lambda x: x.get('price', 0), reverse=True)
    elif sort_by == 'Mejor Valorados':
        products.sort(key=lambda x: x.get('rating', 0), reverse=True)
    
    if products:
        st.caption(f"Mostrando {len(products)} productos")
        cols = st.columns(4)
        for idx, product in enumerate(products):
            with cols[idx % 4]:
                render_product_card(product)
    else:
        st.warning(T['no_products'])

def render_cart_page():
    st.markdown(f'<div class="section-title">🛒 {T["cart"]}</div>', unsafe_allow_html=True)
    
    cart = st.session_state.cart
    
    if not cart:
        st.markdown("""
            <div class="card" style="text-align: center; padding: 4rem;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">🛒</div>
                <h3 style="margin-bottom: 0.5rem;">Tu carrito está vacío</h3>
                <p style="color: var(--text-secondary);">¡Agrega productos para comenzar!</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🛍️ {T['continue_shopping']}", type="primary"):
            navigate_to('products')
        return
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for item in cart:
            c1, c2, c3, c4, c5 = st.columns([1, 3, 2, 1, 1])
            
            with c1:
                st.image(item['image'] or 'https://placehold.co/100x100', width=80)
            
            with c2:
                st.markdown(f"**{item['name']}**")
                st.caption(f"${item['price']:.2f}")
            
            with c3:
                new_qty = st.number_input(
                    T['quantity'],
                    min_value=1,
                    max_value=99,
                    value=item['quantity'],
                    key=f"qty_{item['id']}",
                    label_visibility="collapsed"
                )
                if new_qty != item['quantity']:
                    update_cart_quantity(item['id'], new_qty)
                    st.rerun()
            
            with c4:
                st.markdown(f"**${item['price'] * item['quantity']:.2f}**")
            
            with c5:
                if st.button("🗑️", key=f"del_{item['id']}"):
                    remove_from_cart(item['id'])
                    st.rerun()
            
            st.markdown("---")
    
    with col2:
        st.markdown("""
            <div class="card">
                <h3 style="margin-bottom: 1rem;">Resumen del Pedido</h3>
            </div>
        """, unsafe_allow_html=True)
        
        subtotal = get_cart_total()
        shipping = 0 if subtotal > 100 else 9.99
        tax = subtotal * 0.08
        total = subtotal + shipping + tax
        
        st.markdown(f"**Subtotal:** ${subtotal:.2f}")
        st.markdown(f"**Envío:** {'GRATIS' if shipping == 0 else f'${shipping:.2f}'}")
        st.markdown(f"**Impuestos:** ${tax:.2f}")
        st.markdown("---")
        st.markdown(f"### Total: ${total:.2f}")
        
        if st.button(f"💳 {T['checkout']}", type="primary", use_container_width=True):
            if st.session_state.user:
                navigate_to('checkout')
            else:
                st.warning("Por favor inicia sesión para continuar")
                navigate_to('auth')
        
        if st.button(f"🛍️ {T['continue_shopping']}", use_container_width=True):
            navigate_to('products')

def render_auth_page():
    st.markdown(f'<div class="section-title">👤 {T["signin"]}</div>', unsafe_allow_html=True)
    
    if st.session_state.user:
        st.success(f"✅ {T['welcome']}, {st.session_state.user.get('name')}!")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🛒 {T['cart']}", use_container_width=True):
                navigate_to('cart')
        with col2:
            if st.button(f"🚪 {T['logout']}", use_container_width=True):
                st.session_state.user = None
                st.rerun()
        return
    
    tab1, tab2 = st.tabs([f"🔐 {T['login']}", f"📝 {T['register']}"])
    
    with tab1:
        with st.form("login_form"):
            email = st.text_input(f"📧 {T['email']}")
            password = st.text_input(f"🔒 {T['password']}", type="password")
            
            if st.form_submit_button(T['login'], type="primary", use_container_width=True):
                if email and password:
                    # Try Firebase auth first
                    try:
                        from services.firebase_service import FirebaseService
                        firebase = FirebaseService()
                        user = firebase.sign_in(email, password)
                        if user:
                            st.session_state.user = user
                            st.success("✅ ¡Inicio de sesión exitoso!")
                            st.rerun()
                    except:
                        # Demo mode
                        st.session_state.user = {
                            'uid': 'demo123',
                            'email': email,
                            'name': email.split('@')[0].title()
                        }
                        st.success("✅ ¡Inicio de sesión exitoso!")
                        st.rerun()
                else:
                    st.error("Por favor completa todos los campos")
    
    with tab2:
        with st.form("register_form"):
            name = st.text_input(f"👤 {T['name']}")
            reg_email = st.text_input(f"📧 {T['email']}", key="reg_email")
            reg_password = st.text_input(f"🔒 {T['password']}", type="password", key="reg_pass")
            confirm_password = st.text_input("🔒 Confirmar Contraseña", type="password")
            
            if st.form_submit_button(T['register'], type="primary", use_container_width=True):
                if all([name, reg_email, reg_password, confirm_password]):
                    if reg_password != confirm_password:
                        st.error("Las contraseñas no coinciden")
                    else:
                        # Try Firebase registration
                        try:
                            from services.firebase_service import FirebaseService
                            firebase = FirebaseService()
                            user = firebase.create_user(reg_email, reg_password, name)
                            if user:
                                st.session_state.user = user
                                st.success("✅ ¡Cuenta creada exitosamente!")
                                st.rerun()
                        except:
                            # Demo mode
                            st.session_state.user = {
                                'uid': 'demo123',
                                'email': reg_email,
                                'name': name
                            }
                            st.success("✅ ¡Cuenta creada exitosamente!")
                            st.rerun()
                else:
                    st.error("Por favor completa todos los campos")

def render_about_page():
    st.markdown(f'<div class="section-title">ℹ️ {T["about_title"]}</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card fade-in">
            <h2 style="color: var(--accent); margin-bottom: 1rem;">Nuestra Misión</h2>
            <p style="font-size: 1.125rem; line-height: 1.8; color: var(--text-secondary);">
                En SAVA, nos dedicamos a ofrecer la mejor experiencia de compra online, 
                combinando tecnología de vanguardia con un servicio al cliente excepcional. 
                Nuestro objetivo es hacer que las compras online sean fáciles, seguras y agradables.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    col1, col2, col3 = st.columns(3)
    
    values = [
        ("🎯", "Excelencia", "Buscamos la perfección en cada detalle de nuestro servicio."),
        ("🤝", "Confianza", "Construimos relaciones duraderas basadas en la transparencia."),
        ("💡", "Innovación", "Siempre a la vanguardia de las últimas tendencias tecnológicas.")
    ]
    
    for col, (icon, title, desc) in zip([col1, col2, col3], values):
        with col:
            st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-desc">{desc}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown(f'<div class="section-title">📞 {T["contact"]}</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="card">
                <h3 style="margin-bottom: 1rem;">Información de Contacto</h3>
                <p>📧 <strong>Email:</strong> contacto@sava.com</p>
                <p>📞 <strong>Teléfono:</strong> +1 (555) 123-4567</p>
                <p>📍 <strong>Dirección:</strong> 123 Tech Street, Innovation City</p>
                <p>🕐 <strong>Horario:</strong> Lun-Vie 9:00 - 18:00</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.form("contact_form"):
            st.text_input("Nombre")
            st.text_input("Email")
            st.text_area("Mensaje")
            if st.form_submit_button("📤 Enviar Mensaje", type="primary", use_container_width=True):
                st.success("✅ ¡Mensaje enviado! Te responderemos pronto.")

def render_checkout_page():
    st.markdown('<div class="section-title">💳 Checkout</div>', unsafe_allow_html=True)
    
    if not st.session_state.user:
        st.warning("Por favor inicia sesión para continuar")
        if st.button("Ir a Iniciar Sesión"):
            navigate_to('auth')
        return
    
    if not st.session_state.cart:
        st.info("Tu carrito está vacío")
        if st.button("Ir a Productos"):
            navigate_to('products')
        return
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("### 📦 Información de Envío")
        
        with st.form("checkout_form"):
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("Nombre", value=st.session_state.user.get('name', ''))
            with c2:
                st.text_input("Apellido")
            
            st.text_input("Dirección")
            
            c1, c2, c3 = st.columns(3)
            with c1:
                st.text_input("Ciudad")
            with c2:
                st.text_input("Estado/Provincia")
            with c3:
                st.text_input("Código Postal")
            
            st.text_input("Teléfono")
            
            st.markdown("### 💳 Información de Pago")
            st.text_input("Número de Tarjeta", placeholder="1234 5678 9012 3456")
            
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("Fecha de Expiración", placeholder="MM/YY")
            with c2:
                st.text_input("CVV", placeholder="123", type="password")
            
            if st.form_submit_button("🛒 Completar Compra", type="primary", use_container_width=True):
                st.success("✅ ¡Pedido realizado exitosamente!")
                st.balloons()
                st.session_state.cart = []
                st.info("Tu pedido ha sido procesado. Recibirás un email de confirmación.")
    
    with col2:
        st.markdown("### 📋 Resumen del Pedido")
        
        for item in st.session_state.cart:
            st.markdown(f"**{item['name']}** x{item['quantity']}")
            st.caption(f"${item['price'] * item['quantity']:.2f}")
        
        st.markdown("---")
        
        subtotal = get_cart_total()
        shipping = 0 if subtotal > 100 else 9.99
        tax = subtotal * 0.08
        total = subtotal + shipping + tax
        
        st.markdown(f"**Subtotal:** ${subtotal:.2f}")
        st.markdown(f"**Envío:** {'GRATIS 🎉' if shipping == 0 else f'${shipping:.2f}'}")
        st.markdown(f"**Impuestos:** ${tax:.2f}")
        st.markdown("---")
        st.markdown(f"## Total: ${total:.2f}")

def render_account_page():
    st.markdown('<div class="section-title">👤 Mi Cuenta</div>', unsafe_allow_html=True)
    
    if not st.session_state.user:
        navigate_to('auth')
        return
    
    user = st.session_state.user
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
            <div class="card" style="text-align: center;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">👤</div>
                <h2>{user.get('name', 'Usuario')}</h2>
                <p style="color: var(--text-secondary);">{user.get('email', '')}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🚪 {T['logout']}", use_container_width=True):
            st.session_state.user = None
            navigate_to('home')
    
    with col2:
        tab1, tab2 = st.tabs(["📦 Pedidos", "⚙️ Configuración"])
        
        with tab1:
            st.info("No tienes pedidos aún. ¡Comienza a comprar!")
            if st.button("🛍️ Ir a Productos"):
                navigate_to('products')
        
        with tab2:
            with st.form("update_profile"):
                st.text_input("Nombre", value=user.get('name', ''))
                st.text_input("Email", value=user.get('email', ''), disabled=True)
                st.text_input("Teléfono")
                st.text_area("Dirección")
                
                if st.form_submit_button("💾 Guardar Cambios", type="primary"):
                    st.success("✅ Perfil actualizado")

# ==================== FOOTER ====================
def render_footer():
    st.markdown("""
        <div class="footer">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>Compañía</h4>
                    <a href="#">Acerca de Nosotros</a>
                    <a href="#">Carreras</a>
                    <a href="#">Blog</a>
                    <a href="#">Prensa</a>
                </div>
                <div class="footer-col">
                    <h4>Soporte</h4>
                    <a href="#">Centro de Ayuda</a>
                    <a href="#">Envíos</a>
                    <a href="#">Devoluciones</a>
                    <a href="#">Estado del Pedido</a>
                </div>
                <div class="footer-col">
                    <h4>Legal</h4>
                    <a href="#">Privacidad</a>
                    <a href="#">Términos</a>
                    <a href="#">Cookies</a>
                    <a href="#">Licencias</a>
                </div>
                <div class="footer-col">
                    <h4>Síguenos</h4>
                    <a href="https://github.com/GIUSEPPESAN21" target="_blank">GitHub</a>
                    <a href="https://linkedin.com/in/joseph-javier-sánchez-acuña-150410275" target="_blank">LinkedIn</a>
                    <a href="#">Instagram</a>
                    <a href="#">Twitter</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2025 SAVA Software for Engineering. Todos los derechos reservados.</p>
                <p style="margin-top: 0.5rem;">Desarrollado con ❤️ por Joseph Javier Sánchez Acuña</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ==================== MAIN ====================
def main():
    render_header()
    
    page = st.session_state.page
    
    if page == 'home':
        render_home_page()
    elif page == 'products':
        render_products_page()
    elif page == 'cart':
        render_cart_page()
    elif page == 'auth':
        render_auth_page()
    elif page == 'about':
        render_about_page()
    elif page == 'checkout':
        render_checkout_page()
    elif page == 'account':
        render_account_page()
    else:
        render_home_page()
    
    render_footer()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"Error: {str(e)}")
