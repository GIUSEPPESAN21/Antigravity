"""
SAVA E-Commerce Platform - Modern Professional UI
Version 7.0 - Complete Redesign

Features:
- Premium modern design with sleek aesthetics
- Gradient accents and glassmorphism
- Smooth animations and transitions
- Fully responsive layout
- Clean, minimalist interface
"""
import streamlit as st
from typing import Optional, Dict, Any

# Page Configuration
st.set_page_config(
    page_title="SAVA E-Commerce | Premium Shopping Experience",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== PROFESSIONAL UI DESIGN SYSTEM ==========
st.markdown("""
<style>
    /* Import Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');
    
    /* Design Tokens */
    :root {
        /* Colors */
        --primary: #0F172A;
        --primary-rgb: 15, 23, 42;
        --accent: #3B82F6;
        --accent-hover: #2563EB;
        --success: #10B981;
        --warning: #F59E0B;
        --error: #EF4444;
        
        /* Backgrounds */
        --bg-primary: #FFFFFF;
        --bg-secondary: #F8FAFC;
        --bg-tertiary: #F1F5F9;
        
        /* Text */
        --text-primary: #0F172A;
        --text-secondary: #64748B;
        --text-muted: #94A3B8;
        
        /* Borders */
        --border: #E2E8F0;
        
        /* Shadows */
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
        --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
        
        /* Border Radius */
        --radius-sm: 0.375rem;
        --radius-md: 0.5rem;
        --radius-lg: 0.75rem;
        --radius-xl: 1rem;
        --radius-2xl: 1.5rem;
        
        /* Spacing */
        --space-2: 0.5rem;
        --space-3: 0.75rem;
        --space-4: 1rem;
        --space-6: 1.5rem;
        --space-8: 2rem;
        --space-12: 3rem;
        --space-16: 4rem;
    }
    
    /* Global Reset */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Base Styles */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: var(--text-primary);
        background: var(--bg-secondary);
        -webkit-font-smoothing: antialiased;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Main Container */
    .main .block-container {
        max-width: 1400px !important;
        padding: 0 var(--space-6) var(--space-12);
    }
    
    /* ===== PREMIUM HEADER ===== */
    .premium-header {
        position: sticky;
        top: 0;
        z-index: 1000;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid var(--border);
        box-shadow: var(--shadow-sm);
        padding: var(--space-4) 0;
        margin: 0 0 var(--space-8);
    }
    
    .header-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 var(--space-6);
        display: flex;
        align-items: center;
        gap: var(--space-8);
    }
    
    .logo-section {
        display: flex;
        align-items: center;
        gap: var(--space-3);
    }
    
    .logo-text {
        font-family: 'Outfit', sans-serif;
        font-size: 1.75rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .search-bar {
        flex: 1;
        max-width: 600px;
    }
    
    .search-bar input {
        width: 100%;
        padding: var(--space-3) var(--space-6);
        border: 2px solid var(--border);
        border-radius: var(--radius-lg);
        font-size: 0.9375rem;
        transition: all 0.2s;
    }
    
    .search-bar input:focus {
        outline: none;
        border-color: var(--accent);
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
    }
    
    .nav-actions {
        display: flex;
        align-items: center;
        gap: var(--space-4);
    }
    
    /* ===== HERO SECTION ===== */
    .hero-section {
        position: relative;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: var(--radius-2xl);
        padding: var(--space-16) var(--space-12);
        text-align: center;
        overflow: hidden;
        margin-bottom: var(--space-12);
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 50%, rgba(255,255,255,0.15) 0%, transparent 60%);
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .hero-title {
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: var(--space-4);
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: rgba(255,255,255,0.9);
        margin-bottom: var(--space-8);
    }
    
    .hero-cta {
        display: inline-flex;
        align-items: center;
        gap: var(--space-2);
        background: white;
        color: var(--primary);
        padding: var(--space-4) var(--space-8);
        border-radius: var(--radius-xl);
        font-weight: 600;
        font-size: 1.125rem;
        box-shadow: var(--shadow-xl);
        transition: transform 0.2s;
    }
    
    .hero-cta:hover {
        transform: translateY(-2px);
    }
    
    /* ===== PRODUCT CARDS - PREMIUM ===== */
    .products-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: var(--space-8);
        margin: var(--space-8) 0;
    }
    
    .product-card {
        background: var(--bg-primary);
        border-radius: var(--radius-xl);
        overflow: hidden;
        border: 1px solid var(--border);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }
    
    .product-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--shadow-xl);
        border-color: var(--accent);
    }
    
    .product-image {
        position: relative;
        width: 100%;
        padding-top: 100%;
        background: var(--bg-secondary);
        overflow: hidden;
    }
    
    .product-image img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }
    
    .product-card:hover .product-image img {
        transform: scale(1.1);
    }
    
    .product-badge {
        position: absolute;
        top: var(--space-3);
        right: var(--space-3);
        background: var(--accent);
        color: white;
        padding: var(--space-2) var(--space-3);
        border-radius: var(--radius-md);
        font-size: 0.75rem;
        font-weight: 600;
        box-shadow: var(--shadow-md);
    }
    
    .product-info {
        padding: var(--space-6);
    }
    
    .product-category {
        color: var(--text-muted);
        font-size: 0.8125rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: var(--space-2);
    }
    
    .product-name {
        font-family: 'Outfit', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: var(--space-3);
        line-height: 1.3;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    
    .product-rating {
        display: flex;
        align-items: center;
        gap: var(--space-2);
        margin-bottom: var(--space-4);
        font-size: 0.875rem;
        color: var(--text-secondary);
    }
    
    .star-rating {
        color: #FBBF24;
    }
    
    .product-price-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    .product-price {
        font-family: 'Outfit', sans-serif;
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--primary);
    }
    
    .product-old-price {
        font-size: 1rem;
        color: var(--text-muted);
        text-decoration: line-through;
    }
    
    /* ===== BUTTONS ===== */
    .stButton > button {
        font-weight: 600;
        border-radius: var(--radius-lg);
        transition: all 0.2s;
        border: none;
        padding: var(--space-3) var(--space-6);
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%);
        color: white !important;
        box-shadow: var(--shadow-md);
    }
    
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
    }
    
    .stButton > button > div > p {
        background: transparent !important;
        color: inherit !important;
    }
    
    /* ===== INPUTS ===== */
    .stTextInput > div > div > input {
        border: 2px solid var(--border);
        border-radius: var(--radius-md);
        padding: var(--space-3) var(--space-4);
        transition: all 0.2s;
    }
    
    .stTextInput > div > div > input:focus {
        outline: none;
        border-color: var(--accent);
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
    }
    
    /* ===== FOOTER ===== */
    .premium-footer {
        background: var(--primary);
        color: white;
        padding: var(--space-12) 0;
        margin-top: var(--space-16);
        border-radius: var(--radius-2xl) var(--radius-2xl) 0 0;
    }
    
    .footer-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 var(--space-6);
    }
    
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: var(--space-8);
        margin-bottom: var(--space-8);
    }
    
    .footer-col h4 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: var(--space-4);
    }
    
    .footer-col a {
        color: rgba(255,255,255,0.7);
        text-decoration: none;
        display: block;
        margin-bottom: var(--space-2);
        transition: color 0.2s;
    }
    
    .footer-col a:hover {
        color: white;
    }
    
    .footer-bottom {
        padding-top: var(--space-8);
        border-top: 1px solid rgba(255,255,255,0.1);
        text-align: center;
        color: rgba(255,255,255,0.6);
    }
    
    /* =====  ANIMATIONS ===== */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .products-grid {
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: var(--space-4);
        }
        
        .header-container {
            flex-direction: column;
            gap: var(--space-4);
        }
        
        .search-bar {
            width: 100%;
            max-width: none;
        }
    }
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--text-muted);
        border-radius: 6px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--text-secondary);
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'search_query' not in st.session_state:
    st.session_state.search_query = ''
if 'user' not in st.session_state:
    st.session_state.user = None
if 'cart_count' not in st.session_state:
    st.session_state.cart_count = 0

# Bilingual Text
TEXTS = {
    'ES': {
        'title': 'Compra Lo Que Amas',
        'subtitle': 'Descubre productos increíbles con envío gratis',
        'cta': 'Explorar Productos',
        'search_placeholder': 'Buscar productos...',
        'categories': 'Categorías',
        'about': 'Acerca de',
        'signin': 'Ingresar',
        'signup': 'Crear Cuenta',
        'cart': 'Carrito',
        'no_products': 'No se encontraron productos',
        'featured': 'Productos Destacados'
    },
    'EN': {
        'title': 'Shop What You Love',
        'subtitle': 'Discover amazing products with free shipping',
        'cta': 'Explore Products',
        'search_placeholder': 'Search products...',
        'categories': 'Categories',
        'about': 'About',
        'signin': 'Sign In',
        'signup': 'Sign Up',
        'cart': 'Cart',
        'no_products': 'No products found',
        'featured': 'Featured Products'
    }
}

lang = st.session_state.get('lang', 'ES')
T = TEXTS[lang]

# ========== PREMIUM HEADER ==========
def render_premium_header():
    st.markdown(
        f"""
        <div class="premium-header fade-in">
            <div class="header-container">
                <div class="logo-section">
                    <div class="logo-text">✨ SAVA</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([2, 4, 2])
    
    with col1:
        st.write("")  # Spacing
    
    with col2:
        search = st.text_input(
            "Search",
            placeholder=T['search_placeholder'],
            label_visibility="collapsed",
            key="global_search"
        )
    
    with col3:
        cols = st.columns(4)
        with cols[0]:
            if st.button("🗂️"):
                st.session_state.page = 'products'
        with cols[1]:
            if st.button("ℹ️"):
                st.session_state.page = 'about'
        with cols[2]:
            if st.button("👤"):
                st.session_state.page = 'auth'
        with cols[3]:
            if st.button("🛒"):
                st.session_state.page = 'cart'

# ========== HERO SECTION ==========
def render_hero():
    st.markdown(
        f"""
        <div class="hero-section fade-in">
            <div class="hero-content">
                <h1 class="hero-title">{T['title']}</h1>
                <p class="hero-subtitle">{T['subtitle']}</p>
                <div class="hero-cta">
                    {T['cta']} →
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ========== HOME PAGE ==========
def render_home():
    render_hero()
    
    st.markdown(f"## {T['featured']}")
    
    try:
        from services.firebase_service import FirebaseService
        firebase = FirebaseService()
        products = firebase.get_products(limit=8)
        
        if products:
            cols = st.columns(4)
            for idx, product in enumerate(products):
                with cols[idx % 4]:
                    render_product_card(product)
        else:
            st.info(T['no_products'])
    except:
        st.warning("Cargando productos...")

# ========== PRODUCT CARD ==========
def render_product_card(product):
    name = product.get('name', 'Product')
    price = product.get('price', 0)
    image = product.get('images', [{}])[0].get('url', 'https://placehold.co/400x400/E2E8F0/64748B?text=No+Image')
    rating = product.get('rating', 0)
    reviews = product.get('reviews_count', 0)
    
    st.markdown(
        f"""
        <div class="product-card fade-in">
            <div class="product-image">
                <img src="{image}" alt="{name}" />
                <div class="product-badge">NEW</div>
            </div>
            <div class="product-info">
                <div class="product-category">ELECTRONICS</div>
                <div class="product-name">{name}</div>
                <div class="product-rating">
                    <span class="star-rating">{'⭐' * int(rating)}</span>
                    <span>({reviews})</span>
                </div>
                <div class="product-price-row">
                    <div class="product-price">${price:,.0f}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ========== FOOTER ==========
def render_footer():
    st.markdown(
        """
        <div class="premium-footer">
            <div class="footer-container">
                <div class="footer-grid">
                    <div class="footer-col">
                        <h4>Compañía</h4>
                        <a href="#">Acerca de Nosotros</a>
                        <a href="#">Carreras</a>
                        <a href="#">Blog</a>
                    </div>
                    <div class="footer-col">
                        <h4>Ayuda</h4>
                        <a href="#">Centro de Ayuda</a>
                        <a href="#">Envíos</a>
                        <a href="#">Devoluciones</a>
                    </div>
                    <div class="footer-col">
                        <h4>Legal</h4>
                        <a href="#">Privacidad</a>
                        <a href="#">Términos</a>
                        <a href="#">Cookies</a>
                    </div>
                    <div class="footer-col">
                        <h4>Síguenos</h4>
                        <a href="https://github.com/GIUSEPPESAN21">GitHub</a>
                        <a href="https://linkedin.com/in/joseph-javier-sánchez-acuña-150410275">LinkedIn</a>
                    </div>
                </div>
                <div class="footer-bottom">
                    © 2025 SAVA Software for Engineering. Todos los derechos reservados.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ========== MAIN ==========
def main():
    render_premium_header()
    
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'products':
        st.title("Productos")
        st.info("Página de productos en construcción")
    elif st.session_state.page == 'about':
        st.title("Acerca de")
        st.info("Página en construcción")
    elif st.session_state.page == 'auth':
        st.title("Iniciar Sesión")
        st.info("Página en construcción")
    elif st.session_state.page == 'cart':
        st.title("Carrito")
        st.info("Página en construcción")
    
    render_footer()

if __name__ == "__main__":
    main()
