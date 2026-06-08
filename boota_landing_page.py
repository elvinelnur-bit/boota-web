import streamlit as st
import os
import base64

_LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Boota Logo.png")
_FAVICON_16 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon-16x16.png")
_FAVICON_32 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon-32x32.png")
_FAVICON_48 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon-48x48.png")
_FAVICON_ICO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.ico")
_FAVICON_VERSION = 2


def _extract_logo_symbol(logo):
    """Extract only the stylized B mark — exclude Boota.az wordmark and infinity loop."""
    width, height = logo.size
    left = int(width * 0.075)
    right = int(width * 0.322)
    top = int(height * 0.28)
    bottom = int(height * 0.67)
    symbol = logo.crop((left, top, right, bottom))
    bbox = symbol.getbbox()
    return symbol.crop(bbox) if bbox else symbol


def _square_favicon_canvas(symbol, padding_ratio=0.1):
    """Center the mark on a square canvas with safe-zone padding for tab display."""
    from PIL import Image

    sym_w, sym_h = symbol.size
    inner = max(sym_w, sym_h)
    side = max(int(inner * (1 + 2 * padding_ratio)), 1)
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(symbol, ((side - sym_w) // 2, (side - sym_h) // 2), symbol)
    return canvas


def _ensure_favicons():
    """Generate optimized favicons from Boota Logo.png (B symbol only)."""
    if not os.path.exists(_LOGO_PATH):
        return _LOGO_PATH

    from PIL import Image

    stamp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".favicon-version")
    logo_mtime = os.path.getmtime(_LOGO_PATH)
    favicon_paths = (_FAVICON_16, _FAVICON_32, _FAVICON_48, _FAVICON_ICO)
    stamp_ok = (
            os.path.exists(stamp_path)
            and open(stamp_path).read().strip() == str(_FAVICON_VERSION)
    )
    if stamp_ok and all(os.path.exists(p) and os.path.getmtime(p) >= logo_mtime for p in favicon_paths):
        return _FAVICON_32

    logo = Image.open(_LOGO_PATH).convert("RGBA")
    canvas = _square_favicon_canvas(_extract_logo_symbol(logo))

    icon_16 = canvas.resize((16, 16), Image.Resampling.LANCZOS)
    icon_32 = canvas.resize((32, 32), Image.Resampling.LANCZOS)
    icon_48 = canvas.resize((48, 48), Image.Resampling.LANCZOS)
    icon_16.save(_FAVICON_16, format="PNG", optimize=True)
    icon_32.save(_FAVICON_32, format="PNG", optimize=True)
    icon_48.save(_FAVICON_48, format="PNG", optimize=True)
    icon_48.save(
        _FAVICON_ICO,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=[icon_32, icon_16],
    )
    with open(stamp_path, "w") as stamp_file:
        stamp_file.write(str(_FAVICON_VERSION))
    return _FAVICON_32


_PAGE_ICON = _ensure_favicons()

st.set_page_config(
    page_title="BOOTA | Azərbaycanın Yeni Nəqliyyat və Enerji Arteriyası",
    page_icon=_PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Dil seçimi üçün state yaradırıq (Defolt: AZ)
if 'lang' not in st.session_state:
    st.session_state.lang = 'AZ'


def toggle_language():
    st.session_state.lang = 'EN' if st.session_state.lang == 'AZ' else 'AZ'


# Tərcümə lüğəti (Bütün mətnlər burada saxlanılır)
translations = {
    'AZ': {
        'about_us': 'Haqqımızda',
        'mission': 'MİSSİYAMIZ',
        'hero_title': 'Təbiətin Gücünü Gələcəyə Yönəldirik!',
        'hero_sub': 'Azərbaycanın Yeni Nəqliyyat və Enerji Arteriyası. Hibrid Elektrik Doldurma Stansiyalarının (HEDS) Strateji Quruculuq Konsepsiyası.',
        'hero_btn': 'Layihə ilə Tanış Ol',
        'feat_title': 'Kompleks Yaşıl Enerji Həlləri',
        'feat_sub': 'Bərpa olunan enerji mənbəli Hibrid Elektrik Doldurma Stansiyalarının (HEDS) Strateji Quruculuq Konsepsiyası',
        'sun_title': 'Günəş Enerjisi',
        'sun_text': 'Lokal generasiya ilə təmiz enerji istehsalı.',
        'wind_title': 'Külək Enerjisi',
        'wind_text': 'Hava şəraitinə uyğunlaşan əlavə güc.',
        'ev_title': 'EV Doldurma',
        'ev_text': 'Ultra-sürətli universal hibrid şarj stansiyaları.',
        'future_title': 'Təmiz Gələcək',
        'future_text': 'Sıfır emissiya və tam karbon neytrallığı.',
        'badge1': 'Dayanıqlı Həllər',
        'badge1_desc': 'Uzunmüddətli, ekoloji cəhətdən məsul infrastruktur və enerji sistemləri.',
        'badge2': 'İnnovativ Yanaşma',
        'badge2_desc': 'Qabaqcıl texnologiya və strateji mühəndislik həlləri ilə gələcəyə investisiya.',
        'badge3': 'Etibarlı və Səmərəli',
        'badge3_desc': 'Məlumat əsaslı əməliyyatlar və beynəlxalq standartlara uyğun icra.',
        'badge4': 'Birlikdə Daha Yaşıl Gələcək',
        'badge4_desc': 'Dövlət, biznes və ictimaiyyət arasında strateji tərəfdaşlıq.',
        'team_header': 'İCRA LİDERLİYİ',
        'team_sub': 'İnnovasiya, idarəetmə və davamlı inkişafın mühərriki.',
        'ceo': 'Qlobal Strateq, İdeya Müəllifi və İdarəetmə Qurucusu.',
        'cbdo': 'Texniki/Elmi İşlər və Beynəlxalq Tərəfdaşlıqlar Rəhbəri.',
        'clo': 'Hüquqi Arxitektura və Korporativ Təhlükəsizlik.',
        'coo': 'Daxili Əməliyyatlar, Rəqəmsal Sistemlər və İcra Rəhbəri.',
        'cfo': 'Maliyyə, İqtisadiyyat və Resursların İdarəedilməsi.',
        'crio': 'Tədqiqat, innovasiya strategiyası, yeni texnologiyalar və gələcək biznes imkanları.',
        'cto': 'Texnologiya arxitekturası, rəqəmsal platformalar, kibertəhlükəsizlik və texniki mükəmməllik.',
        'footer_slogan': 'Bu gün təmiz enerjiyə keçid edək, sabaha yaşıl dünya quraq!',
        'footer_sub': 'Layihə barədə ətraflı məlumat və rəsmi tərəfdaşlıq üçün bizimlə əlaqə saxlayın.',
        'rights': '© 2026 Boota.az - Yaşıl Şəbəkə. Bütün hüquqlar qorunur.'
    },
    'EN': {
        'about_us': 'About Us',
        'mission': 'OUR MISSION',
        'hero_title': 'Directing the Power of Nature to the Future!',
        'hero_sub': "Azerbaijan's New Transport and Energy Artery. Strategic Construction Concept of Hybrid Electric Vehicle Charging Stations (HEVCS).",
        'hero_btn': 'Discover the Project',
        'feat_title': 'Comprehensive Green Energy Solutions',
        'feat_sub': 'Strategic Construction Concept of Hybrid Electric Vehicle Charging Stations (HEVCS) powered by renewable energy',
        'sun_title': 'Solar Energy',
        'sun_text': 'Clean energy production via local generation.',
        'wind_title': 'Wind Energy',
        'wind_text': 'Additional power adapting to weather conditions.',
        'ev_title': 'EV Charging',
        'ev_text': 'Ultra-fast universal hybrid charging stations.',
        'future_title': 'Clean Future',
        'future_text': 'Zero emissions and complete carbon neutrality.',
        'badge1': 'Sustainable Solutions',
        'badge1_desc': 'Long-term, environmentally responsible infrastructure and energy systems.',
        'badge2': 'Innovative Approach',
        'badge2_desc': 'Investing in the future through advanced technology and strategic engineering.',
        'badge3': 'Reliable & Efficient',
        'badge3_desc': 'Data-driven operations aligned with international standards of excellence.',
        'badge4': 'Greener Future Together',
        'badge4_desc': 'Strategic partnership across government, business, and communities.',
        'team_header': 'EXECUTIVE LEADERSHIP',
        'team_sub': 'Driving innovation, governance and sustainable growth.',
        'ceo': 'Global Strategist, Idea Author & Management Founder.',
        'cbdo': 'Head of Technical/Scientific Affairs & International Partnerships.',
        'clo': 'Legal Architecture & Corporate Security.',
        'coo': 'Internal Operations, Digital Systems & Execution Lead.',
        'cfo': 'Finance, Economics & Resource Management.',
        'crio': 'Research, innovation strategy, emerging technologies, and future business opportunities.',
        'cto': 'Technology architecture, digital platforms, cybersecurity, and technical excellence.',
        'footer_slogan': "Let's transition to clean energy today, and build a green world for tomorrow!",
        'footer_sub': 'Contact us for detailed information about the project and official partnerships.',
        'rights': '© 2026 Boota.az - Green Network. All rights reserved.'
    }
}

t = translations[st.session_state.lang]

EXECUTIVES = [
    {'name': 'Elnur Ağayev', 'title': 'Chief Executive Officer (CEO)', 'desc_key': 'ceo', 'row': 'ceo'},
    {'name': 'Elvin Rzayev', 'title': 'Chief Operating Officer (COO)', 'desc_key': 'coo', 'row': 'duo'},
    {'name': 'Mahir İmanov', 'title': 'Chief Financial Officer (CFO)', 'desc_key': 'cfo', 'row': 'duo'},
    {'name': 'Cavid Məmmədli', 'title': 'Chief Business Development Officer (CBDO)', 'desc_key': 'cbdo', 'row': 'duo2'},
    {'name': 'Vüqar Şəfiyev', 'title': 'Chief Legal Officer (CLO)', 'desc_key': 'clo', 'row': 'duo2'},
    {'name': 'Rauf Nəsirli', 'title': 'Chief Research & Innovation Officer (CRIO)', 'desc_key': 'crio', 'row': 'duo3'},
    {'name': 'Seymur Əliyev', 'title': 'Chief Technology Officer (CTO)', 'desc_key': 'cto', 'row': 'duo3'},
]


def get_executive_initials(name):
    parts = name.replace('ə', 'e').replace('ı', 'i').replace('ş', 's').replace('ğ', 'g').replace('ü', 'u').replace('ö',
                                                                                                                   'o').replace(
        'ç', 'c').split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    return name[:2].upper()


def build_exec_card(exec_data, translations_dict, delay=0, is_ceo=False):
    initials = get_executive_initials(exec_data['name'])
    ceo_class = ' exec-card-ceo' if is_ceo else ''
    desc = translations_dict[exec_data['desc_key']]
    return (
        f'<div class="exec-card{ceo_class}" data-delay="{delay}">'
        f'<div class="exec-card-glow"></div>'
        f'<div class="exec-card-border"></div>'
        f'<div class="exec-card-inner">'
        f'<div class="exec-avatar-wrap">'
        f'<div class="exec-avatar-ring"></div>'
        f'<div class="exec-avatar"><span class="exec-initials">{initials}</span></div>'
        f'</div>'
        f'<div class="exec-accent-line"></div>'
        f'<h3 class="exec-name">{exec_data["name"]}</h3>'
        f'<p class="exec-title">{exec_data["title"]}</p>'
        f'<p class="exec-desc">{desc}</p>'
        f'</div></div>'
    )


def build_executive_board_html(translations_dict):
    particles_html = ''.join(
        f'<div class="executive-particle" style="left:{i * 7.3 % 100:.1f}%;'
        f'animation-duration:{12 + (i % 8) * 2}s;animation-delay:{i * 0.4}s;"></div>'
        for i in range(30)
    )
    ceo_card = build_exec_card(EXECUTIVES[0], translations_dict, delay=0, is_ceo=True)
    coo_card = build_exec_card(EXECUTIVES[1], translations_dict, delay=1)
    cfo_card = build_exec_card(EXECUTIVES[2], translations_dict, delay=2)
    cbdo_card = build_exec_card(EXECUTIVES[3], translations_dict, delay=3)
    clo_card = build_exec_card(EXECUTIVES[4], translations_dict, delay=4)
    crio_card = build_exec_card(EXECUTIVES[5], translations_dict, delay=5)
    cto_card = build_exec_card(EXECUTIVES[6], translations_dict, delay=6)
    return (
        f'<div class="executive-section" id="executive-board">'
        f'<div class="executive-spotlight executive-spotlight-1"></div>'
        f'<div class="executive-spotlight executive-spotlight-2"></div>'
        f'<div class="executive-spotlight executive-spotlight-3"></div>'
        f'<div class="executive-particles">{particles_html}</div>'
        f'<div class="executive-header">'
        f'<div class="executive-eyebrow">{translations_dict["team_header"]}</div>'
        f'<p class="executive-subtitle">{translations_dict["team_sub"]}</p>'
        f'</div>'
        f'<div class="executive-grid">'
        f'<div class="exec-row exec-row-ceo">{ceo_card}</div>'
        f'<div class="exec-row exec-row-duo">{coo_card}{cfo_card}</div>'
        f'<div class="exec-row exec-row-duo">{cbdo_card}{clo_card}</div>'
        f'<div class="exec-row exec-row-duo">{crio_card}{cto_card}</div>'
        f'</div></div>'
    )


def build_corporate_values_html(translations_dict):
    pillars = []
    for i in range(1, 5):
        pillars.append(
            f'<div class="value-pillar">'
            f'<div class="value-pillar-accent"></div>'
            f'<span class="value-pillar-index">0{i}</span>'
            f'<h3 class="value-pillar-title">{translations_dict[f"badge{i}"]}</h3>'
            f'<p class="value-pillar-desc">{translations_dict[f"badge{i}_desc"]}</p>'
            f'</div>'
        )
    return (
        f'<div class="corporate-values-section">'
        f'<div class="values-bg-glow values-bg-glow-left"></div>'
        f'<div class="values-bg-glow values-bg-glow-right"></div>'
        f'<div class="corporate-values-inner">'
        f'<div class="values-panel">{"".join(pillars)}</div>'
        f'</div></div>'
    )


def get_image_as_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None


# Fayl adları (Sizin qovluqdakı adlar)
IMG_DIR = "."
LOGO_FILENAME = os.path.join(IMG_DIR, "Boota Logo.png")
HERO_BG_FILENAME = os.path.join(IMG_DIR, "131232.jpg")
SUN_FILENAME = os.path.join(IMG_DIR, "sun.jpg")
WIND_FILENAME = os.path.join(IMG_DIR, "wind.jpg")
EV_FILENAME = os.path.join(IMG_DIR, "ev.jpg")
FUTURE_FILENAME = os.path.join(IMG_DIR, "future.jpg")

# Şəkillərin oxunması
logo_base64 = get_image_as_base64(LOGO_FILENAME)
logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="boota-logo">' if logo_base64 else '<h1 class="boota-text-logo">Boota.az</h1>'

hero_bg_base64 = get_image_as_base64(HERO_BG_FILENAME)
hero_bg_url = f"data:image/jpeg;base64,{hero_bg_base64}" if hero_bg_base64 else "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"

sun_base64 = get_image_as_base64(SUN_FILENAME)
wind_base64 = get_image_as_base64(WIND_FILENAME)
ev_base64 = get_image_as_base64(EV_FILENAME)
future_base64 = get_image_as_base64(FUTURE_FILENAME)

# Tesla-stil düymə əlavə edirik (Yuxarı sağda üzən - floating button)
btn_label = "🌐 EN" if st.session_state.lang == 'AZ' else "🌐 AZ"
st.button(btn_label, on_click=toggle_language)

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Standart elementləri gizlədirik */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {{ display: none !important; }}

    .block-container {{padding: 0rem !important; max-width: 100% !important; overflow-x: hidden;}}
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], section.main {{
        overflow-x: hidden !important;
        max-width: 100vw;
    }}
    *, *::before, *::after {{
        box-sizing: border-box;
    }}

    /* Xüsusiyyətlər kartları qutusu */
    .features-cards-wrap {{
        padding: 0 10%;
        margin-top: -120px;
        max-width: 100%;
        overflow-x: hidden;
    }}
    .features-cards-wrap [data-testid="stHorizontalBlock"] {{
        gap: 1.5rem;
        flex-wrap: wrap !important;
    }}
    .features-cards-wrap [data-testid="column"] {{
        min-width: 0 !important;
    }}

    /* DİL DÜYMƏSİNİN XÜSUSİ DİZAYNI (Top Right) */
    div[data-testid="stElementContainer"]:has(> div[data-testid="stButton"]),
    div[data-testid="stButton"] {{
        position: fixed;
        top: 35px;
        right: 5%;
        left: auto;
        z-index: 1000;
        width: auto;
    }}
    div[data-testid="stButton"] button {{
        background: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 5px 20px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: auto !important;
        min-height: 44px;
        min-width: 44px;
        -webkit-tap-highlight-color: transparent;
    }}
    div[data-testid="stButton"] button:hover {{
        background: rgba(255, 255, 255, 0.3) !important;
        border-color: #16a34a !important;
        transform: scale(1.05) !important;
    }}

    /* Loqo Qutusu və Haqqımızda Düyməsi */
    .logo-container {{
        position: absolute;
        top: 35px;
        left: 5%;
        z-index: 999;
        display: flex;
        align-items: center;
    }}

    .nav-about-btn {{
        color: white;
        text-decoration: none;
        font-size: 0.95rem;
        font-weight: 600;
        padding: 5px 20px;
        min-height: 44px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 50px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        margin-left: 20px;
        box-sizing: border-box;
    }}

    .nav-about-btn:hover {{
        background: rgba(255, 255, 255, 0.3);
        border-color: #16a34a;
        transform: scale(1.05);
        color: white;
    }}

    /* Loqo Glassmorphism (Şüşə) effekti */
    .boota-logo {{
        height: 80px; 
        width: auto;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px); 
        padding: 10px 25px; 
        border-radius: 50px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
        border: 1px solid rgba(255, 255, 255, 0.4); 
        transition: all 0.3s ease;
    }}
    .boota-logo:hover {{
        transform: translateY(-3px) scale(1.02);
        background: rgba(255, 255, 255, 0.85);
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }}

    .boota-text-logo {{
            font-size: 1.75rem;
    }}
    .nav-about-btn {{
            font-size: 0.875rem;
            padding: 8px 16px;
            margin-left: 16px;
            min-height: auto;
    }}

    /* Qəhrəman (Hero) Bölməsi */
    .content-section-hero {{
        background-image: linear-gradient(rgba(10, 40, 20, 0.3), rgba(10, 40, 20, 0.6)), url('{hero_bg_url}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
        padding: 0 10%;
        position: relative;
    }}
     .boota-logo {{
            height: 48px;
            padding: 6px 12px;
    }}
    .nav-about-btn {{
            padding: 6px 14px;
            font-size: 0.8rem;
            margin-left: 12px;
    }}

    .hero-title {{
        font-size: clamp(1.85rem, 5.5vw, 4rem);
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 20px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
        max-width: 900px;
        overflow-wrap: break-word;
        word-wrap: break-word;
    }}

    .hero-subtitle {{
        font-size: clamp(1rem, 2.5vw, 1.25rem);
        font-weight: 300;
        max-width: 750px;
        margin-bottom: 40px;
        color: #f1f5f9;
        line-height: 1.6;
        overflow-wrap: break-word;
    }}

    .hero-mission {{
        color: #4ade80;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 15px;
        font-size: clamp(0.7rem, 2vw, 0.875rem);
    }}

    .hero-btn {{
        background-color: #16a34a;
        color: white !important;
        padding: 16px 50px;
        border-radius: 50px;
        font-size: clamp(0.95rem, 2.5vw, 1.1rem);
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 10px 25px rgba(22, 163, 74, 0.4);
        display: inline-block;
        min-height: 48px;
        line-height: 1.2;
        -webkit-tap-highlight-color: transparent;
    }}
    .hero-btn:hover {{
        background-color: #15803d;
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(22, 163, 74, 0.5);
    }}

    /* Xüsusiyyətlər (Features) Bölməsi */
    .features-section {{
        padding: 120px 10%;
        background-color: #0f172a; 
        color: white;
    }}

    .section-title {{
        font-size: clamp(1.65rem, 4.5vw, 2.8rem);
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
        color: white;
        overflow-wrap: break-word;
        padding: 0 4px;
    }}

    .section-subheader {{
        text-align: center;
        color: #94a3b8;
        font-size: clamp(1rem, 2.5vw, 1.2rem);
        max-width: 700px;
        margin: 0 auto 80px auto;
        line-height: 1.6;
        overflow-wrap: break-word;
        padding: 0 4px;
    }}

    /* Dəyərlər (Values) Kartları - İNTERAKTİV DİZAYN */
    .value-card {{
        background-color: #1e293b;
        padding: 0; 
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        text-align: center;
        height: 100%;
        transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
        border: 2px solid transparent; 
        border-bottom: 5px solid #16a34a;
        overflow: hidden; 
        display: flex;
        flex-direction: column;
        cursor: pointer;
    }}
    .value-card:hover {{
        transform: translateY(-15px);
        box-shadow: 0 20px 45px rgba(22, 163, 74, 0.25);
        border-color: rgba(74, 222, 128, 0.4); 
    }}

    .img-wrapper {{
        width: 100%;
        height: 180px;
        overflow: hidden; 
    }}

    .value-image {{
        width: 100%;
        height: 100%;
        max-width: 100%;
        object-fit: cover;
        transition: transform 0.7s ease; 
        border-bottom: 4px solid #16a34a;
    }}

    .value-card:hover .value-image {{
        transform: scale(1.15); 
    }}

    .card-content {{
        padding: 30px 20px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}

    .value-title {{
        font-size: clamp(1.15rem, 3vw, 1.4rem);
        font-weight: 700;
        margin-bottom: 15px;
        color: white;
        overflow-wrap: break-word;
    }}
    .value-text {{
        color: #cbd5e1;
        font-size: clamp(0.9rem, 2.2vw, 1rem);
        line-height: 1.6;
        overflow-wrap: break-word;
    }}

    /* Korporativ Dəyərlər Bölməsi */
    .corporate-values-section {{
        position: relative;
        padding: 64px 6% 80px;
        background: linear-gradient(180deg,
            #0f172a 0%,
            #0e1a2e 12%,
            #0b1726 35%,
            #081420 58%,
            #060e18 78%,
            #040a12 92%,
            #030712 100%);
        overflow: hidden;
    }}
    .values-bg-glow {{
        position: absolute;
        border-radius: 50%;
        filter: blur(100px);
        pointer-events: none;
        opacity: 0.35;
    }}
    .values-bg-glow-left {{
        width: 480px;
        height: 480px;
        top: 10%;
        left: -8%;
        background: radial-gradient(circle, rgba(22, 163, 74, 0.18) 0%, transparent 70%);
    }}
    .values-bg-glow-right {{
        width: 420px;
        height: 420px;
        bottom: 0%;
        right: -6%;
        background: radial-gradient(circle, rgba(14, 165, 233, 0.14) 0%, transparent 70%);
    }}
    .corporate-values-inner {{
        position: relative;
        z-index: 2;
        max-width: 1320px;
        margin: 0 auto;
    }}
    .values-panel {{
        display: flex;
        align-items: stretch;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.72) 0%, rgba(10, 20, 35, 0.85) 100%);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 2px;
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.35),
                    0 0 0 1px rgba(74, 222, 128, 0.04) inset,
                    0 1px 0 rgba(255, 255, 255, 0.06) inset;
    }}
    .value-pillar {{
        flex: 1;
        text-align: left;
        padding: 44px 36px 48px;
        position: relative;
        transition: background 0.4s ease;
    }}
    .value-pillar:hover {{
        background: rgba(255, 255, 255, 0.02);
    }}
    .value-pillar-accent {{
        width: 32px;
        height: 3px;
        background: linear-gradient(90deg, #4ade80, #0ea5e9);
        margin-bottom: 22px;
        border-radius: 2px;
        box-shadow: 0 0 12px rgba(74, 222, 128, 0.35);
        transition: width 0.4s ease, box-shadow 0.4s ease;
    }}
    .value-pillar:hover .value-pillar-accent {{
        width: 48px;
        box-shadow: 0 0 18px rgba(74, 222, 128, 0.5);
    }}
    .value-pillar-index {{
        display: block;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.28em;
        color: #4ade80;
        margin-bottom: 14px;
        opacity: 0.85;
    }}
    .value-pillar-title {{
        font-size: 1.35rem;
        font-weight: 700;
        color: #f8fafc;
        margin: 0 0 16px;
        letter-spacing: -0.01em;
        line-height: 1.35;
        overflow-wrap: break-word;
    }}
    .value-pillar-desc {{
        font-size: 1.02rem;
        font-weight: 400;
        color: #94a3b8;
        margin: 0;
        line-height: 1.65;
        letter-spacing: 0.01em;
        overflow-wrap: break-word;
    }}
    .value-pillar:hover .value-pillar-desc {{
        color: #b0bec9;
    }}
    .value-pillar:not(:last-child)::after {{
        content: '';
        position: absolute;
        right: 0;
        top: 12%;
        height: 76%;
        width: 1px;
        background: linear-gradient(180deg,
            transparent 0%,
            rgba(74, 222, 128, 0.14) 20%,
            rgba(14, 165, 233, 0.12) 50%,
            rgba(74, 222, 128, 0.14) 80%,
            transparent 100%);
    }}
    @media (max-width: 1100px) {{
        .values-panel {{
            display: grid;
            grid-template-columns: 1fr 1fr;
        }}
        .value-pillar {{
            padding: 36px 32px 40px;
        }}
        .value-pillar:nth-child(1),
        .value-pillar:nth-child(2) {{
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }}
        .value-pillar:nth-child(odd):not(:last-child)::after {{
            display: block;
        }}
        .value-pillar:nth-child(even)::after {{
            display: none;
        }}
    }}
    @media (max-width: 640px) {{
        .corporate-values-section {{
            padding: 48px 5% 64px;
        }}
        .values-panel {{
            grid-template-columns: 1fr;
        }}
        .value-pillar {{
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            padding: 32px 24px 36px;
        }}
        .value-pillar:last-child {{
            border-bottom: none;
        }}
        .value-pillar::after {{
            display: none !important;
        }}
        .value-pillar-title {{
            font-size: 1.22rem;
        }}
        .value-pillar-desc {{
            font-size: 0.98rem;
        }}
    }}

    /* Executive Leadership Board */
    .executive-section {{
        position: relative;
        padding: 140px 8% 160px;
        background: #030712;
        color: #f8fafc;
        overflow: hidden;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    .executive-spotlight {{
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        pointer-events: none;
        opacity: 0.45;
    }}
    .executive-spotlight-1 {{
        width: 600px; height: 600px;
        top: -10%; left: 15%;
        background: radial-gradient(circle, rgba(22, 163, 74, 0.35) 0%, transparent 70%);
        animation: spotlight-drift-1 18s ease-in-out infinite;
    }}
    .executive-spotlight-2 {{
        width: 500px; height: 500px;
        bottom: 5%; right: 10%;
        background: radial-gradient(circle, rgba(14, 165, 233, 0.25) 0%, transparent 70%);
        animation: spotlight-drift-2 22s ease-in-out infinite;
    }}
    .executive-spotlight-3 {{
        width: 400px; height: 400px;
        top: 40%; left: 50%;
        transform: translateX(-50%);
        background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, transparent 70%);
        animation: spotlight-drift-3 20s ease-in-out infinite;
    }}

    @keyframes spotlight-drift-1 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(60px, 40px); }}
    }}
    @keyframes spotlight-drift-2 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(-50px, -30px); }}
    }}
    @keyframes spotlight-drift-3 {{
        0%, 100% {{ transform: translate(-50%, 0); opacity: 0.3; }}
        50% {{ transform: translate(-50%, -20px); opacity: 0.5; }}
    }}

    .executive-particles {{
        position: absolute;
        inset: 0;
        overflow: hidden;
        pointer-events: none;
    }}
    .executive-particle {{
        position: absolute;
        width: 2px;
        height: 2px;
        background: rgba(74, 222, 128, 0.6);
        border-radius: 50%;
        animation: particle-float linear infinite;
    }}

    @keyframes particle-float {{
        0% {{ transform: translateY(100vh) scale(0); opacity: 0; }}
        10% {{ opacity: 1; }}
        90% {{ opacity: 1; }}
        100% {{ transform: translateY(-20px) scale(1); opacity: 0; }}
    }}

    .executive-header {{
        position: relative;
        z-index: 2;
        text-align: center;
        margin-bottom: 90px;
    }}
    .executive-eyebrow {{
        display: inline-block;
        color: #4ade80;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.35em;
        text-transform: uppercase;
        margin-bottom: 24px;
        padding: 8px 24px;
        border: 1px solid rgba(74, 222, 128, 0.25);
        border-radius: 50px;
        background: rgba(74, 222, 128, 0.05);
        backdrop-filter: blur(8px);
    }}
    .executive-subtitle {{
        color: #94a3b8;
        font-size: 1.25rem;
        font-weight: 300;
        max-width: 620px;
        margin: 0 auto;
        line-height: 1.7;
        letter-spacing: 0.01em;
    }}

    .executive-grid {{
        position: relative;
        z-index: 2;
        max-width: 1100px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        gap: 32px;
    }}

    .exec-row {{
        display: flex;
        justify-content: center;
        gap: 32px;
        flex-wrap: wrap;
    }}
    .exec-row-ceo {{
        margin-bottom: 8px;
    }}
    .exec-row-duo .exec-card {{
        flex: 1;
        min-width: 280px;
        max-width: 480px;
    }}

    @keyframes exec-reveal {{
        from {{ opacity: 0; transform: translateY(48px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    .exec-card {{
        position: relative;
        flex: 1;
        min-width: 280px;
        max-width: 480px;
        border-radius: 24px;
        opacity: 0;
        animation: exec-reveal 0.9s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        transition: transform 0.55s cubic-bezier(0.22, 1, 0.36, 1),
                    box-shadow 0.55s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .exec-card[data-delay="0"] {{ animation-delay: 0.1s; }}
    .exec-card[data-delay="1"] {{ animation-delay: 0.25s; }}
    .exec-card[data-delay="2"] {{ animation-delay: 0.4s; }}
    .exec-card[data-delay="3"] {{ animation-delay: 0.55s; }}
    .exec-card[data-delay="4"] {{ animation-delay: 0.7s; }}
    .exec-card[data-delay="5"] {{ animation-delay: 0.85s; }}
    .exec-card[data-delay="6"] {{ animation-delay: 1s; }}

    @supports (animation-timeline: view()) {{
        .exec-card {{
            animation: exec-reveal linear both;
            animation-timeline: view();
            animation-range: entry 0% cover 25%;
        }}
        .exec-card[data-delay="0"] {{ animation-delay: 0s; }}
        .exec-card[data-delay="1"] {{ animation-delay: 0.08s; }}
        .exec-card[data-delay="2"] {{ animation-delay: 0.16s; }}
        .exec-card[data-delay="3"] {{ animation-delay: 0.24s; }}
        .exec-card[data-delay="4"] {{ animation-delay: 0.32s; }}
        .exec-card[data-delay="5"] {{ animation-delay: 0.4s; }}
        .exec-card[data-delay="6"] {{ animation-delay: 0.48s; }}
    }}
    .exec-card-ceo {{
        max-width: 520px;
        width: 100%;
    }}

    .exec-card-glow {{
        position: absolute;
        inset: -1px;
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(22, 163, 74, 0.4), rgba(14, 165, 233, 0.3), rgba(139, 92, 246, 0.3));
        opacity: 0;
        filter: blur(20px);
        transition: opacity 0.55s ease;
        z-index: 0;
    }}
    .exec-card:hover .exec-card-glow {{
        opacity: 0.7;
    }}

    .exec-card-border {{
        position: absolute;
        inset: 0;
        border-radius: 24px;
        padding: 1px;
        background: linear-gradient(135deg, rgba(74, 222, 128, 0.15), rgba(14, 165, 233, 0.1), rgba(139, 92, 246, 0.1), rgba(74, 222, 128, 0.15));
        background-size: 300% 300%;
        animation: border-shimmer 6s ease infinite;
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        z-index: 1;
        transition: background 0.55s ease;
    }}
    .exec-card:hover .exec-card-border {{
        background: linear-gradient(135deg, rgba(74, 222, 128, 0.6), rgba(14, 165, 233, 0.5), rgba(139, 92, 246, 0.5), rgba(74, 222, 128, 0.6));
        background-size: 300% 300%;
        animation: border-shimmer 2s ease infinite;
    }}

    @keyframes border-shimmer {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .exec-card-inner {{
        position: relative;
        z-index: 2;
        padding: 40px 36px 36px;
        border-radius: 23px;
        background: rgba(15, 23, 42, 0.55);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        text-align: center;
        transition: background 0.55s cubic-bezier(0.22, 1, 0.36, 1),
                    border-color 0.55s ease;
    }}
    .exec-card:hover {{
        transform: translateY(-14px);
    }}
    .exec-card:hover .exec-card-inner {{
        background: rgba(15, 23, 42, 0.75);
        border-color: rgba(74, 222, 128, 0.15);
    }}
    .exec-card-ceo .exec-card-inner {{
        padding: 48px 40px 40px;
    }}

    .exec-avatar-wrap {{
        position: relative;
        width: 100px;
        height: 100px;
        margin: 0 auto 28px;
    }}
    .exec-card-ceo .exec-avatar-wrap {{
        width: 120px;
        height: 120px;
        margin-bottom: 32px;
    }}

    .exec-avatar-ring {{
        position: absolute;
        inset: -6px;
        border-radius: 50%;
        background: conic-gradient(from 0deg, #16a34a, #0ea5e9, #8b5cf6, #16a34a);
        animation: avatar-ring-spin 8s linear infinite;
        opacity: 0.7;
        transition: opacity 0.4s ease, inset 0.4s ease;
    }}
    .exec-card:hover .exec-avatar-ring {{
        opacity: 1;
        inset: -8px;
        animation-duration: 3s;
    }}

    @keyframes avatar-ring-spin {{
        to {{ transform: rotate(360deg); }}
    }}

    .exec-avatar {{
        position: relative;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: linear-gradient(145deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: inset 0 2px 12px rgba(255,255,255,0.08),
                    0 8px 32px rgba(0,0,0,0.4);
        overflow: hidden;
    }}
    .exec-avatar::before {{
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(22, 163, 74, 0.35), rgba(14, 165, 233, 0.25), rgba(139, 92, 246, 0.2));
        opacity: 0.85;
    }}
    .exec-initials {{
        position: relative;
        z-index: 1;
        font-size: 1.75rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        background: linear-gradient(135deg, #ffffff 0%, #4ade80 50%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none;
        transition: transform 0.4s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .exec-card-ceo .exec-initials {{
        font-size: 2.1rem;
    }}
    .exec-card:hover .exec-initials {{
        transform: scale(1.08);
    }}

    .exec-accent-line {{
        width: 48px;
        height: 2px;
        margin: 0 auto 22px;
        background: linear-gradient(90deg, transparent, #4ade80, #0ea5e9, transparent);
        border-radius: 2px;
        transition: width 0.55s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .exec-card:hover .exec-accent-line {{
        width: 100%;
    }}

    .exec-name {{
        font-size: 1.45rem;
        font-weight: 700;
        color: #f8fafc;
        margin: 0 0 8px;
        letter-spacing: -0.01em;
        line-height: 1.3;
    }}
    .exec-card-ceo .exec-name {{
        font-size: 1.65rem;
    }}

    .exec-title {{
        font-size: 0.82rem;
        font-weight: 600;
        color: #4ade80;
        margin: 0 0 16px;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }}

    .exec-desc {{
        font-size: 0.95rem;
        color: #94a3b8;
        line-height: 1.65;
        margin: 0;
        font-weight: 400;
    }}

    /* Footer */
    .footer {{
        background-color: #020617;
        color: white;
        text-align: center;
        padding: 80px 10%;
    }}
    .footer-slogan {{
        font-size: clamp(1.35rem, 4vw, 2rem);
        font-weight: 700;
        margin-bottom: 30px;
        color: #4ade80;
        overflow-wrap: break-word;
    }}
    .footer a {{
        -webkit-tap-highlight-color: transparent;
        min-height: 48px;
        max-width: 100%;
        overflow-wrap: break-word;
    }}
    .footer-subtitle {{
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 50px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }}

    /* ===== MOBİL RESPONSİV ===== */

    /* Planşet (768px – 1024px) */
    @media (max-width: 1024px) {{
        .features-section {{
            padding: 90px 6% 100px;
        }}
        .features-cards-wrap [data-testid="column"] {{
            flex: 1 1 calc(50% - 0.75rem) !important;
            width: calc(50% - 0.75rem) !important;
        }}
        .section-subheader {{
            margin-bottom: 60px;
        }}
        .exec-row-duo .exec-card {{
            min-width: 0;
        }}
    }}

    /* Mobil (≤768px) */
    @media (max-width: 768px) {{
        div[data-testid="stElementContainer"]:has(> div[data-testid="stButton"]),
        div[data-testid="stButton"] {{
            top: max(16px, env(safe-area-inset-top, 16px));
            right: max(16px, env(safe-area-inset-right, 16px));
        }}
        div[data-testid="stButton"] button {{
            padding: 8px 16px !important;
            font-size: 0.875rem !important;
        }}

        .logo-container {{
            top: max(16px, env(safe-area-inset-top, 16px));
            left: max(16px, env(safe-area-inset-left, 16px));
            max-width: calc(100% - 110px);
            flex-wrap: wrap;
        }}
        .boota-logo {{
            height: 56px;
            padding: 8px 16px;
        }}
        .boota-text-logo {{
            font-size: 1.75rem;
        }}
        .nav-about-btn {{
            font-size: 0.8rem;
            padding: 8px 16px;
            margin-left: 12px;
        }}

        .content-section-hero {{
            background-attachment: scroll;
            min-height: 100svh;
            padding: 120px 6% 48px;
            justify-content: center;
        }}

        .hero-btn {{
            padding: 14px 36px;
            width: auto;
            max-width: 100%;
        }}

        .features-section {{
            padding: 72px 5% 80px;
        }}
        .features-cards-wrap {{
            margin-top: -48px;
            padding: 0 5%;
        }}
        .features-cards-wrap [data-testid="stHorizontalBlock"] {{
            flex-direction: column !important;
            gap: 1.25rem;
        }}
        .features-cards-wrap [data-testid="column"] {{
            width: 100% !important;
            flex: 1 1 100% !important;
        }}
        .value-card:hover {{
            transform: translateY(-6px);
        }}
        .img-wrapper {{
            height: 160px;
        }}
        .card-content {{
            padding: 24px 18px;
        }}

        .executive-section {{
            padding: 80px 5% 100px;
        }}
        .executive-header {{
            margin-bottom: 48px;
        }}
        .executive-eyebrow {{
            font-size: 0.68rem;
            letter-spacing: 0.2em;
            padding: 8px 16px;
            max-width: 100%;
            overflow-wrap: break-word;
        }}
        .executive-subtitle {{
            font-size: 1rem;
            padding: 0 8px;
        }}
        .exec-row {{
            flex-direction: column;
            align-items: stretch;
            gap: 20px;
        }}
        .exec-row-duo .exec-card,
        .exec-card,
        .exec-card-ceo {{
            max-width: 100%;
            width: 100%;
            min-width: 0;
        }}
        .exec-card-inner {{
            padding: 32px 20px 28px;
        }}
        .exec-card-ceo .exec-card-inner {{
            padding: 36px 20px 32px;
        }}
        .exec-name {{
            font-size: 1.3rem;
            overflow-wrap: break-word;
        }}
        .exec-card-ceo .exec-name {{
            font-size: 1.4rem;
        }}
        .exec-title {{
            font-size: 0.75rem;
            overflow-wrap: break-word;
        }}
        .exec-desc {{
            font-size: 0.92rem;
        }}

        .footer {{
            padding: 60px 6%;
        }}
        .footer-subtitle {{
            font-size: 1rem;
            padding: 0 4px;
        }}
    }}

    /* Kiçik telefonlar – iPhone SE, Galaxy S (≤480px) */
    @media (max-width: 480px) {{
        div[data-testid="stButton"] button {{
            padding: 10px 14px !important;
            font-size: 0.8rem !important;
        }}
        .logo-container {{
            max-width: calc(100% - 96px);
        }}
        .boota-logo {{
            height: 48px;
            padding: 6px 12px;
        }}
        .nav-about-btn {{
            padding: 6px 12px;
            font-size: 0.75rem;
            margin-left: 10px;
        }}

        .content-section-hero {{
            padding: 108px 5% 40px;
        }}
        .hero-btn {{
            padding: 14px 28px;
            display: block;
            text-align: center;
            max-width: 280px;
            margin: 0 auto;
        }}

        .features-section {{
            padding: 56px 4% 64px;
        }}
        .features-cards-wrap {{
            margin-top: -32px;
            padding: 0 4%;
        }}
        .section-subheader {{
            margin-bottom: 40px;
        }}

        .value-pillar-title {{
            font-size: 1.15rem;
        }}
        .value-pillar-desc {{
            font-size: 0.92rem;
        }}

        .executive-spotlight-1,
        .executive-spotlight-2,
        .executive-spotlight-3 {{
            opacity: 0.25;
        }}
        .exec-avatar-wrap {{
            width: 88px;
            height: 88px;
        }}
        .exec-card-ceo .exec-avatar-wrap {{
            width: 100px;
            height: 100px;
        }}
        .exec-initials {{
            font-size: 1.5rem;
        }}
        .exec-card-ceo .exec-initials {{
            font-size: 1.75rem;
        }}
    }}

    /* iPhone SE və çox kiçik ekranlar (≤375px) */
    @media (max-width: 375px) {{
        .hero-mission {{
            letter-spacing: 2px;
        }}
        .executive-eyebrow {{
            letter-spacing: 0.14em;
            font-size: 0.62rem;
        }}
        .value-pillar {{
            padding: 28px 18px 32px;
        }}
    }}

    /* Touch cihazlar – hover effektlərini azalt */
    @media (hover: none) and (pointer: coarse) {{
        .value-card:hover {{
            transform: none;
        }}
        .value-card:hover .value-image {{
            transform: none;
        }}
        .exec-card:hover {{
            transform: none;
        }}
        div[data-testid="stButton"] button:hover {{
            transform: none !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="content-section-hero">
    <div class="logo-container">
        {logo_html}
        <a href="/about_boota" target="_self" class="nav-about-btn">{t['about_us']}</a>
    </div>
    <div class="hero-mission">{t['mission']}</div>
    <div class="hero-title">{t['hero_title']}</div>
    <div class="hero-subtitle">{t['hero_sub']}</div>
    <a href="#kesf-et" class="hero-btn">{t['hero_btn']}</a>
</div>
<div id="kesf-et"></div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="features-section">
    <div class="section-title">{t['feat_title']}</div>
    <div class="section-subheader">{t['feat_sub']}</div>
</div>
""", unsafe_allow_html=True)

# 4 Sütunlu Xüsusiyyətlər
st.write("<div class='features-cards-wrap'>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    sun_img_html = f'<img src="data:image/jpeg;base64,{sun_base64}" class="value-image">' if sun_base64 else '<div class="value-image" style="background: #16a34a; display: flex; align-items: center; justify-content: center; font-size: 3rem;">☀️</div>'
    st.markdown(f"""
    <div class="value-card">
        <div class="img-wrapper">{sun_img_html}</div>
        <div class="card-content">
            <div class="value-title">{t['sun_title']}</div>
            <div class="value-text">{t['sun_text']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    wind_img_html = f'<img src="data:image/jpeg;base64,{wind_base64}" class="value-image">' if wind_base64 else '<div class="value-image" style="background: #0d47a1; display: flex; align-items: center; justify-content: center; font-size: 3rem;">🌬️</div>'
    st.markdown(f"""
    <div class="value-card">
        <div class="img-wrapper">{wind_img_html}</div>
        <div class="card-content">
            <div class="value-title">{t['wind_title']}</div>
            <div class="value-text">{t['wind_text']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    ev_img_html = f'<img src="data:image/jpeg;base64,{ev_base64}" class="value-image">' if ev_base64 else '<div class="value-image" style="background: #f59e0b; display: flex; align-items: center; justify-content: center; font-size: 3rem;">⚡</div>'
    st.markdown(f"""
    <div class="value-card">
        <div class="img-wrapper">{ev_img_html}</div>
        <div class="card-content">
            <div class="value-title">{t['ev_title']}</div>
            <div class="value-text">{t['ev_text']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    future_img_html = f'<img src="data:image/jpeg;base64,{future_base64}" class="value-image">' if future_base64 else '<div class="value-image" style="background: #334155; display: flex; align-items: center; justify-content: center; font-size: 3rem;">🌱</div>'
    st.markdown(f"""
    <div class="value-card">
        <div class="img-wrapper">{future_img_html}</div>
        <div class="card-content">
            <div class="value-title">{t['future_title']}</div>
            <div class="value-text">{t['future_text']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("</div>", unsafe_allow_html=True)

st.markdown(build_corporate_values_html(t), unsafe_allow_html=True)

st.markdown(build_executive_board_html(t), unsafe_allow_html=True)

st.markdown(f"""
<div class="footer">
    <div class="footer-slogan">{t['footer_slogan']}</div>
    <div class="footer-subtitle">{t['footer_sub']}</div>
    <a href="mailto:info@boota.az" style="display: inline-block; padding: 12px 35px; background-color: transparent; color: #4ade80; border: 2px solid #4ade80; border-radius: 50px; font-size: 1.1rem; transition: all 0.3s;">📩 info@boota.az</a>
    <p style="margin-top: 50px; color: #475569; font-size: 0.9rem;">{t['rights']}</p>
</div>
""", unsafe_allow_html=True)