import streamlit as st
import os
import base64

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_LOGO_PATH = os.path.join(_BASE_DIR, "Boota Logo.png")
_FAVICON_32 = os.path.join(_BASE_DIR, "favicon-32x32.png")
_HERO_BG = os.path.join(_BASE_DIR, "131232.jpg")

_PAGE_ICON = _FAVICON_32 if os.path.exists(_FAVICON_32) else _LOGO_PATH

st.set_page_config(
    page_title="About BOOTA | Azərbaycanın Yeni Nəqliyyat və Enerji Arteriyası",
    page_icon=_PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "lang" not in st.session_state:
    st.session_state.lang = "AZ"


def toggle_language():
    st.session_state.lang = "EN" if st.session_state.lang == "AZ" else "AZ"


def get_image_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


CONTENT = {
    "AZ": {
        "nav_home": "Ana Səhifə",
        "hero_eyebrow": "KORPORATİV PROFİL",
        "hero_title": "Haqqımızda",
        "hero_sub": "Azərbaycanın Davamlı Nəqliyyat və Enerji İnfrastrukturu Gələcəyinə Vizyon",
        "who_eyebrow": "BİZ KİMİK",
        "who_title": "Milli İnfrastruktur və Enerji Keçidinin Strateji Təşəbbüsü",
        "who_lead": (
            "BOOTA, Hibrid Elektrik Nəqliyyat Vasitələrinin Doldurma Stansiyaları (HEVCS) "
            "şəbəkəsinin və davamlı enerji infrastrukturunun ölkə miqyasında inkişafına "
            "yönəlmiş strateji təşəbbüsdür."
        ),
        "who_cards": [
            ("İnnovasiya", "Qabaqcıl texnologiya və mühəndislik yanaşmaları ilə enerji və mobillik sistemlərinin inteqrasiyası."),
            ("Davamlılıq", "Bərpa olunan enerji mənbələri əsasında uzunmüddətli ekoloji və iqtisadi dəyər."),
            ("İnfrastruktur", "Milli miqyasda miqyaslana bilən, etibarlı və inteqrasiya olunmuş enerji arteriyaları."),
            ("Enerji Keçidi", "Azərbaycanın yaşıl iqtisadiyyat və təmiz nəqliyyat gündəminin strateji dəstəyi."),
            ("Milli Dəyər", "Gələcək nəsillər üçün dayanıqlı inkişaf və rəqabət qabiliyyətinin gücləndirilməsi."),
        ],
        "vision_eyebrow": "VİZYONUMUZ",
        "vision_quote": "Azərbaycanın gələcək davamlı nəqliyyat və təmiz enerji ekosisteminin onurğa sütunu olmaq.",
        "mission_eyebrow": "MİSSİYAMIZ",
        "mission_quote": "Təbiətin gücünü gələcəyə yönəldirik.",
        "mission_body": (
            "BOOTA təbiətin bərpa olunan enerji potensialını müasir infrastrukturla birləşdirərək "
            "ölkənin enerji və nəqliyyat sistemlərində strateji transformasiyanı sürətləndirir."
        ),
        "pillars_eyebrow": "STRATEJİ SÜTUNLAR",
        "pillars_title": "Davamlı İnkişafın Struktur Prinsipləri",
        "pillars": [
            ("Davamlı Enerji", "Günəş, külək və hibrid enerji həlləri ilə təmiz enerji istehsalı və paylanması."),
            ("Ağıllı İnfrastruktur", "Rəqəmsal idarəetmə, monitorinq və miqyaslana bilən şəbəkə arxitekturası."),
            ("İnnovasiya və Texnologiya", "Tədqiqat, yeni texnologiyalar və gələcək biznes imkanlarının inkişafı."),
            ("Uzunmüddətli Milli Təsir", "İqtisadi artım, enerji təhlükəsizliyi və strateji rəqabət üstünlüyü."),
        ],
        "why_eyebrow": "NİYƏ BOOTA",
        "why_title": "Strateji İnvestisiya və Milli Əhəmiyyət",
        "why_points": [
            ("Strateji Milli Əhəmiyyət", "Ölkənin enerji və nəqliyyat infrastrukturunun gələcəyinə birbaşa təsir."),
            ("Bərpa Olunan Enerji İnteqrasiyası", "Yaşıl enerji mənbələri ilə tam uyğunlaşan texnoloji model."),
            ("EV Ekosisteminin İnkişafı", "Elektrik nəqliyyatının genişlənməsi üçün kritik infrastruktur."),
            ("Miqyaslana Bilən İnfrastruktur", "Regional genişlənmədən milli şəbəkəyə qədər strukturlaşdırılmış yol xəritəsi."),
            ("Uzunmüddətli İqtisadi Dəyər", "Dayanıqlı gəlir modeli və strateji aktiv yaradılması."),
            ("Gələcək Artım Potensialı", "Regional enerji və mobillik bazarlarında liderlik imkanı."),
        ],
        "roadmap_eyebrow": "YOL XƏRİTƏSİ",
        "roadmap_title": "Strateji İnkişaf Mərhələləri",
        "roadmap": [
            ("Faza 1", "Tədqiqat və Planlaşdırma", "Bazar analizi, texniki konsepsiya və strateji planlaşdırma."),
            ("Faza 2", "Pilot İnkişaf", "Pilot layihələrin həyata keçirilməsi və operativ modelin təsdiqi."),
            ("Faza 3", "Regional Genişlənmə", "Regional şəbəkənin formalaşdırılması və tərəfdaşlıq ekosistemi."),
            ("Faza 4", "Milli İnfrastruktur Şəbəkəsi", "Ölkə miqyasında inteqrasiya olunmuş enerji və doldurma arteriyası."),
        ],
        "philosophy_eyebrow": "LİDERLİK FİLOSOFİYASI",
        "philosophy_title": "İdarəetmə Prinsipləri",
        "philosophy": [
            ("İnnovasiya Əsaslı Liderlik", "Qabaqcıl texnologiya və strateji düşüncə ilə gələcəyə yönəli qərarlar."),
            ("Əməliyyat Mükəmməlliyi", "Beynəlxalq standartlara uyğun icra, idarəetmə və operativ səmərəlilik."),
            ("Məsul Artım", "Şəffaf idarəetmə, risklərin idarə edilməsi və davamlı korporativ inkişaf."),
            ("Davamlı İnkişaf", "Ekoloji məsuliyyət, sosial dəyər və uzunmüddətli milli maraqların balansı."),
        ],
        "closing_quote": "Təmiz enerji, mobillik və gələcək nəsilləri birləşdirən infrastruktur qururuq.",
        "closing_cta": "Strateji tərəfdaşlıq üçün əlaqə saxlayın",
        "rights": "© 2026 Boota.az - Yaşıl Şəbəkə. Bütün hüquqlar qorunur.",
    },
    "EN": {
        "nav_home": "Home",
        "hero_eyebrow": "CORPORATE PROFILE",
        "hero_title": "About BOOTA",
        "hero_sub": "Azerbaijan's Vision for the Future of Sustainable Transport and Energy Infrastructure",
        "who_eyebrow": "WHO WE ARE",
        "who_title": "A Strategic Initiative for National Infrastructure and Energy Transition",
        "who_lead": (
            "BOOTA is a strategic initiative focused on developing a nationwide network of "
            "Hybrid Electric Vehicle Charging Stations (HEVCS) and sustainable energy infrastructure."
        ),
        "who_cards": [
            ("Innovation", "Integrating advanced technology and engineering across energy and mobility systems."),
            ("Sustainability", "Long-term environmental and economic value powered by renewable energy sources."),
            ("Infrastructure", "Scalable, reliable and integrated national energy arteries."),
            ("Energy Transition", "Strategic support for Azerbaijan's green economy and clean transport agenda."),
            ("National Value", "Strengthening competitiveness and sustainable development for future generations."),
        ],
        "vision_eyebrow": "OUR VISION",
        "vision_quote": "To become the backbone of Azerbaijan's future sustainable transportation and clean energy ecosystem.",
        "mission_eyebrow": "OUR MISSION",
        "mission_quote": "Directing the power of nature to the future.",
        "mission_body": (
            "BOOTA accelerates strategic transformation in the nation's energy and transport systems "
            "by uniting nature's renewable potential with modern infrastructure."
        ),
        "pillars_eyebrow": "STRATEGIC PILLARS",
        "pillars_title": "Structural Principles of Sustainable Development",
        "pillars": [
            ("Sustainable Energy", "Clean energy generation and distribution through solar, wind and hybrid solutions."),
            ("Smart Infrastructure", "Digital management, monitoring and scalable network architecture."),
            ("Innovation & Technology", "Research, emerging technologies and future business opportunity development."),
            ("Long-Term National Impact", "Economic growth, energy security and strategic competitive advantage."),
        ],
        "why_eyebrow": "WHY BOOTA",
        "why_title": "Strategic Investment and National Significance",
        "why_points": [
            ("Strategic National Relevance", "Direct impact on the future of the nation's energy and transport infrastructure."),
            ("Renewable Energy Integration", "A technology model fully aligned with green energy sources."),
            ("EV Ecosystem Development", "Critical infrastructure for the expansion of electric mobility."),
            ("Scalable Infrastructure", "A structured path from regional expansion to a national network."),
            ("Long-Term Economic Value", "Sustainable revenue models and strategic asset creation."),
            ("Future Growth Potential", "Leadership opportunity in regional energy and mobility markets."),
        ],
        "roadmap_eyebrow": "ROADMAP",
        "roadmap_title": "Strategic Development Phases",
        "roadmap": [
            ("Phase 1", "Research & Planning", "Market analysis, technical concept and strategic planning."),
            ("Phase 2", "Pilot Development", "Pilot project execution and operational model validation."),
            ("Phase 3", "Regional Expansion", "Regional network formation and partnership ecosystem."),
            ("Phase 4", "National Infrastructure Network", "Country-wide integrated energy and charging artery."),
        ],
        "philosophy_eyebrow": "LEADERSHIP PHILOSOPHY",
        "philosophy_title": "Governance Principles",
        "philosophy": [
            ("Innovation-Driven Leadership", "Future-oriented decisions through advanced technology and strategic thinking."),
            ("Operational Excellence", "Execution, governance and operational efficiency aligned with international standards."),
            ("Responsible Growth", "Transparent governance, risk management and sustainable corporate development."),
            ("Sustainable Development", "Balance of environmental responsibility, social value and long-term national interests."),
        ],
        "closing_quote": "Building the infrastructure that connects clean energy, mobility and future generations.",
        "closing_cta": "Contact us for strategic partnership",
        "rights": "© 2026 Boota.az - Green Network. All rights reserved.",
    },
}

t = CONTENT[st.session_state.lang]
logo_b64 = get_image_b64(_LOGO_PATH)
hero_b64 = get_image_b64(_HERO_BG)
logo_html = (
    f'<a href="/" class="about-logo-link"><img src="data:image/png;base64,{logo_b64}" class="about-logo" alt="Boota.az"></a>'
    if logo_b64
    else '<a href="/" class="about-logo-link"><span class="about-text-logo">Boota.az</span></a>'
)
hero_bg = f"data:image/jpeg;base64,{hero_b64}" if hero_b64 else ""

btn_label = "🌐 EN" if st.session_state.lang == "AZ" else "🌐 AZ"
st.button(btn_label, on_click=toggle_language)


def _cards_html(items, css_class):
    return "".join(
        f'<div class="{css_class}"><div class="{css_class}-accent"></div>'
        f'<h3 class="{css_class}-title">{title}</h3>'
        f'<p class="{css_class}-text">{text}</p></div>'
        for title, text in items
    )


def _why_html(items):
    return "".join(
        f'<div class="about-why-item"><div class="about-why-marker"></div>'
        f'<div class="about-why-content"><h3>{title}</h3><p>{text}</p></div></div>'
        for title, text in items
    )


def _roadmap_html(items):
    parts = []
    for i, (phase, title, desc) in enumerate(items):
        parts.append(
            f'<div class="about-road-step" data-step="{i + 1}">'
            f'<div class="about-road-node"><span>{i + 1}</span></div>'
            f'<div class="about-road-card">'
            f'<span class="about-road-phase">{phase}</span>'
            f'<h3>{title}</h3><p>{desc}</p></div></div>'
        )
    return "".join(parts)


def _philosophy_html(items):
    return "".join(
        f'<div class="about-philo-card"><span class="about-philo-num">{i:02d}</span>'
        f'<h3>{title}</h3><p>{text}</p></div>'
        for i, (title, text) in enumerate(items, 1)
    )


page_html = (
    f'<div class="about-page">'
    f'<section class="about-hero" style="background-image:linear-gradient(rgba(3,7,18,0.72),rgba(3,7,18,0.88)),url(\'{hero_bg}\');">'
    f'<div class="about-hero-glow about-hero-glow-1"></div>'
    f'<div class="about-hero-glow about-hero-glow-2"></div>'
    f'<div class="about-topbar">{logo_html}'
    f'<a href="/" class="about-nav-home">{t["nav_home"]}</a></div>'
    f'<div class="about-hero-content">'
    f'<span class="about-eyebrow">{t["hero_eyebrow"]}</span>'
    f'<h1 class="about-hero-title">{t["hero_title"]}</h1>'
    f'<p class="about-hero-sub">{t["hero_sub"]}</p></div></section>'
    f'<section class="about-section about-who">'
    f'<div class="about-container"><span class="about-eyebrow">{t["who_eyebrow"]}</span>'
    f'<h2 class="about-section-title">{t["who_title"]}</h2>'
    f'<p class="about-lead">{t["who_lead"]}</p>'
    f'<div class="about-who-grid">{_cards_html(t["who_cards"], "about-who-card")}</div>'
    f'</div></section>'
    f'<section class="about-section about-vision">'
    f'<div class="about-vision-glow"></div>'
    f'<div class="about-container about-vision-inner">'
    f'<span class="about-eyebrow">{t["vision_eyebrow"]}</span>'
    f'<blockquote class="about-vision-quote">{t["vision_quote"]}</blockquote>'
    f'</div></section>'
    f'<section class="about-section about-mission">'
    f'<div class="about-container about-mission-grid">'
    f'<div class="about-mission-text">'
    f'<span class="about-eyebrow">{t["mission_eyebrow"]}</span>'
    f'<h2 class="about-mission-quote">{t["mission_quote"]}</h2>'
    f'<p class="about-mission-body">{t["mission_body"]}</p></div>'
    f'<div class="about-mission-visual"><div class="about-mission-ring"></div>'
    f'<div class="about-mission-core"></div></div>'
    f'</div></section>'
    f'<section class="about-section about-pillars">'
    f'<div class="about-container">'
    f'<span class="about-eyebrow">{t["pillars_eyebrow"]}</span>'
    f'<h2 class="about-section-title">{t["pillars_title"]}</h2>'
    f'<div class="about-pillars-grid">{_cards_html(t["pillars"], "about-pillar-card")}</div>'
    f'</div></section>'
    f'<section class="about-section about-why">'
    f'<div class="about-container">'
    f'<span class="about-eyebrow">{t["why_eyebrow"]}</span>'
    f'<h2 class="about-section-title">{t["why_title"]}</h2>'
    f'<div class="about-why-grid">{_why_html(t["why_points"])}</div>'
    f'</div></section>'
    f'<section class="about-section about-roadmap">'
    f'<div class="about-container">'
    f'<span class="about-eyebrow">{t["roadmap_eyebrow"]}</span>'
    f'<h2 class="about-section-title">{t["roadmap_title"]}</h2>'
    f'<div class="about-roadmap-track">{_roadmap_html(t["roadmap"])}</div>'
    f'</div></section>'
    f'<section class="about-section about-philosophy">'
    f'<div class="about-container">'
    f'<span class="about-eyebrow">{t["philosophy_eyebrow"]}</span>'
    f'<h2 class="about-section-title">{t["philosophy_title"]}</h2>'
    f'<div class="about-philo-grid">{_philosophy_html(t["philosophy"])}</div>'
    f'</div></section>'
    f'<section class="about-section about-closing">'
    f'<div class="about-closing-glow"></div>'
    f'<div class="about-container about-closing-inner">'
    f'<p class="about-closing-quote">{t["closing_quote"]}</p>'
    f'<a href="mailto:info@boota.az" class="about-closing-btn">{t["closing_cta"]}</a>'
    f'<p class="about-rights">{t["rights"]}</p>'
    f'</div></section></div>'
)

st.markdown(
    f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    #MainMenu, footer, header {{visibility: hidden;}}
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], section[data-testid="stSidebar"] {{
        display: none !important;
    }}
    .block-container {{padding: 0 !important; max-width: 100% !important; overflow-x: hidden;}}
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], section.main {{
        overflow-x: hidden !important; max-width: 100vw;
        background: #030712;
    }}
    *, *::before, *::after {{box-sizing: border-box;}}

    div[data-testid="stElementContainer"]:has(> div[data-testid="stButton"]),
    div[data-testid="stButton"] {{
        position: fixed; top: 35px; right: 5%; left: auto; z-index: 2000; width: auto;
    }}
    div[data-testid="stButton"] button {{
        background: rgba(255,255,255,0.15) !important; backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255,255,255,0.3) !important; color: white !important;
        border-radius: 50px !important; padding: 5px 20px !important; font-weight: 600 !important;
        width: auto !important; min-height: 44px;
    }}

    .about-page {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #f8fafc; background: #030712;
    }}
    .about-container {{
        max-width: 1200px; margin: 0 auto; padding: 0 6%; position: relative; z-index: 2;
    }}
    .about-eyebrow {{
        display: inline-block; color: #4ade80; font-size: 0.75rem; font-weight: 700;
        letter-spacing: 0.32em; text-transform: uppercase; margin-bottom: 20px;
    }}
    .about-section-title {{
        font-size: clamp(1.75rem, 4vw, 2.6rem); font-weight: 700; line-height: 1.25;
        margin: 0 0 24px; letter-spacing: -0.02em;
    }}
    .about-lead {{
        font-size: clamp(1.05rem, 2.2vw, 1.25rem); color: #94a3b8; line-height: 1.75;
        max-width: 820px; margin: 0 0 56px;
    }}

    .about-hero {{
        position: relative; min-height: 72vh; background-size: cover; background-position: center;
        display: flex; align-items: center; justify-content: center; overflow: hidden;
    }}
    .about-hero-glow {{
        position: absolute; border-radius: 50%; filter: blur(90px); pointer-events: none;
    }}
    .about-hero-glow-1 {{
        width: 500px; height: 500px; top: 10%; left: 10%;
        background: radial-gradient(circle, rgba(22,163,74,0.25), transparent 70%);
        animation: about-float 16s ease-in-out infinite;
    }}
    .about-hero-glow-2 {{
        width: 420px; height: 420px; bottom: 5%; right: 8%;
        background: radial-gradient(circle, rgba(14,165,233,0.18), transparent 70%);
        animation: about-float 20s ease-in-out infinite reverse;
    }}
    @keyframes about-float {{
        0%, 100% {{ transform: translate(0,0); }}
        50% {{ transform: translate(30px, -20px); }}
    }}
    .about-topbar {{
        position: absolute; top: 35px; left: 5%; right: 5%;
        display: flex; align-items: center; justify-content: space-between; z-index: 10;
    }}
    .about-logo {{ height: 64px; width: auto; background: rgba(255,255,255,0.75);
        backdrop-filter: blur(12px); padding: 8px 20px; border-radius: 50px;
        border: 1px solid rgba(255,255,255,0.4); }}
    .about-logo-link {{ text-decoration: none; }}
    .about-text-logo {{ color: white; font-size: 1.8rem; font-weight: 800; }}
    .about-nav-home {{
        color: #cbd5e1; text-decoration: none; font-size: 0.9rem; font-weight: 600;
        padding: 10px 22px; border: 1px solid rgba(255,255,255,0.15); border-radius: 50px;
        background: rgba(255,255,255,0.06); backdrop-filter: blur(8px); transition: all 0.3s;
        margin-right: 100px;
    }}
    .about-nav-home:hover {{ color: #4ade80; border-color: rgba(74,222,128,0.4); }}
    .about-hero-content {{ text-align: center; padding: 140px 8% 80px; position: relative; z-index: 2; }}
    .about-hero-title {{
        font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 800; margin: 0 0 24px;
        letter-spacing: -0.03em; line-height: 1.08;
    }}
    .about-hero-sub {{
        font-size: clamp(1.05rem, 2.5vw, 1.35rem); color: #94a3b8; max-width: 780px;
        margin: 0 auto; line-height: 1.7; font-weight: 300;
    }}

    .about-section {{ padding: 100px 0; position: relative; }}
    .about-who {{ background: linear-gradient(180deg, #030712 0%, #0a1628 100%); }}

    .about-who-grid {{
        display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px;
    }}
    .about-who-card, .about-pillar-card {{
        background: rgba(15,23,42,0.55); backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.08); border-radius: 4px;
        padding: 32px 28px; transition: border-color 0.4s, transform 0.4s;
    }}
    .about-who-card:hover, .about-pillar-card:hover {{
        border-color: rgba(74,222,128,0.25); transform: translateY(-4px);
    }}
    .about-who-card-accent, .about-pillar-card-accent {{
        width: 28px; height: 3px; background: linear-gradient(90deg, #4ade80, #0ea5e9);
        margin-bottom: 18px; border-radius: 2px;
    }}
    .about-who-card-title, .about-pillar-card-title {{
        font-size: 1.15rem; font-weight: 700; margin: 0 0 12px;
    }}
    .about-who-card-text, .about-pillar-card-text {{
        font-size: 0.95rem; color: #94a3b8; line-height: 1.65; margin: 0;
    }}

    .about-vision {{
        background: #060e18; padding: 120px 0; overflow: hidden;
    }}
    .about-vision-glow {{
        position: absolute; width: 600px; height: 600px; top: 50%; left: 50%;
        transform: translate(-50%, -50%); border-radius: 50%;
        background: radial-gradient(circle, rgba(74,222,128,0.08), transparent 65%);
        pointer-events: none;
    }}
    .about-vision-inner {{ text-align: center; }}
    .about-vision-quote {{
        font-size: clamp(1.6rem, 4.5vw, 3rem); font-weight: 300; line-height: 1.45;
        color: #f1f5f9; margin: 0; border: none; padding: 0;
        font-style: normal; letter-spacing: -0.02em;
    }}

    .about-mission {{
        background: linear-gradient(180deg, #060e18 0%, #0b1726 50%, #030712 100%);
    }}
    .about-mission-grid {{
        display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;
    }}
    .about-mission-quote {{
        font-size: clamp(2rem, 5vw, 3.2rem); font-weight: 800; line-height: 1.15;
        margin: 0 0 28px; letter-spacing: -0.02em;
        background: linear-gradient(135deg, #fff 0%, #4ade80 60%, #38bdf8 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    }}
    .about-mission-body {{ font-size: 1.1rem; color: #94a3b8; line-height: 1.75; margin: 0; }}
    .about-mission-visual {{
        position: relative; height: 320px; display: flex; align-items: center; justify-content: center;
    }}
    .about-mission-ring {{
        position: absolute; width: 260px; height: 260px; border-radius: 50%;
        border: 1px solid rgba(74,222,128,0.2);
        animation: about-spin 24s linear infinite;
    }}
    .about-mission-ring::before {{
        content: ''; position: absolute; inset: -2px; border-radius: 50%;
        background: conic-gradient(from 0deg, transparent, #4ade80, transparent, #0ea5e9, transparent);
        opacity: 0.5; animation: about-spin 12s linear infinite reverse;
    }}
    .about-mission-core {{
        width: 120px; height: 120px; border-radius: 50%;
        background: radial-gradient(circle, rgba(74,222,128,0.35), rgba(14,165,233,0.15));
        box-shadow: 0 0 60px rgba(74,222,128,0.2);
    }}
    @keyframes about-spin {{ to {{ transform: rotate(360deg); }} }}

    .about-pillars {{ background: #030712; }}
    .about-pillars-grid {{
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;
    }}

    .about-why {{
        background: linear-gradient(180deg, #030712 0%, #0a1628 100%);
    }}
    .about-why-grid {{
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;
    }}
    .about-why-item {{
        display: flex; gap: 20px; padding: 28px;
        background: rgba(15,23,42,0.45); border: 1px solid rgba(255,255,255,0.06);
        border-radius: 4px; transition: border-color 0.3s;
    }}
    .about-why-item:hover {{ border-color: rgba(74,222,128,0.2); }}
    .about-why-marker {{
        width: 4px; flex-shrink: 0; border-radius: 2px;
        background: linear-gradient(180deg, #4ade80, #0ea5e9);
    }}
    .about-why-content h3 {{
        font-size: 1.05rem; font-weight: 700; margin: 0 0 8px;
    }}
    .about-why-content p {{
        font-size: 0.92rem; color: #94a3b8; line-height: 1.6; margin: 0;
    }}

    .about-roadmap {{ background: #060e18; }}
    .about-roadmap-track {{
        display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; position: relative;
        margin-top: 48px;
    }}
    .about-roadmap-track::before {{
        content: ''; position: absolute; top: 28px; left: 12%; right: 12%; height: 2px;
        background: linear-gradient(90deg, transparent, rgba(74,222,128,0.3), rgba(14,165,233,0.3), transparent);
    }}
    .about-road-step {{ text-align: center; padding: 0 12px; }}
    .about-road-node {{
        width: 56px; height: 56px; margin: 0 auto 24px; border-radius: 50%;
        background: rgba(15,23,42,0.9); border: 2px solid rgba(74,222,128,0.4);
        display: flex; align-items: center; justify-content: center;
        font-weight: 800; color: #4ade80; position: relative; z-index: 2;
        box-shadow: 0 0 24px rgba(74,222,128,0.15);
    }}
    .about-road-card {{
        background: rgba(15,23,42,0.55); backdrop-filter: blur(16px);
        border: 1px solid rgba(255,255,255,0.08); border-radius: 4px; padding: 24px 20px;
    }}
    .about-road-phase {{
        font-size: 0.7rem; font-weight: 700; letter-spacing: 0.2em;
        color: #4ade80; text-transform: uppercase;
    }}
    .about-road-card h3 {{ font-size: 1.05rem; margin: 10px 0 8px; }}
    .about-road-card p {{ font-size: 0.88rem; color: #94a3b8; line-height: 1.55; margin: 0; }}

    .about-philosophy {{ background: linear-gradient(180deg, #060e18 0%, #030712 100%); }}
    .about-philo-grid {{
        display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px;
    }}
    .about-philo-card {{
        padding: 36px 28px; text-align: center;
        background: rgba(15,23,42,0.5); border: 1px solid rgba(255,255,255,0.07);
        border-radius: 4px;
    }}
    .about-philo-num {{
        display: block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.25em;
        color: #4ade80; margin-bottom: 16px;
    }}
    .about-philo-card h3 {{ font-size: 1.05rem; margin: 0 0 12px; }}
    .about-philo-card p {{ font-size: 0.9rem; color: #94a3b8; line-height: 1.6; margin: 0; }}

    .about-closing {{
        background: #020617; padding: 120px 0; text-align: center; overflow: hidden;
    }}
    .about-closing-glow {{
        position: absolute; width: 700px; height: 400px; top: 50%; left: 50%;
        transform: translate(-50%, -50%); border-radius: 50%;
        background: radial-gradient(ellipse, rgba(22,163,74,0.12), transparent 70%);
        pointer-events: none;
    }}
    .about-closing-quote {{
        font-size: clamp(1.5rem, 4vw, 2.4rem); font-weight: 600; line-height: 1.45;
        max-width: 900px; margin: 0 auto 40px; color: #f1f5f9;
        animation: about-fade-up 1s ease forwards;
    }}
    @keyframes about-fade-up {{
        from {{ opacity: 0; transform: translateY(24px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    .about-closing-btn {{
        display: inline-block; padding: 14px 40px; color: #4ade80;
        border: 2px solid #4ade80; border-radius: 50px; text-decoration: none;
        font-weight: 600; font-size: 1rem; transition: all 0.3s;
    }}
    .about-closing-btn:hover {{
        background: rgba(74,222,128,0.1); box-shadow: 0 0 30px rgba(74,222,128,0.2);
    }}
    .about-rights {{ margin-top: 48px; color: #475569; font-size: 0.85rem; }}

    @media (max-width: 1024px) {{
        .about-mission-grid {{ grid-template-columns: 1fr; }}
        .about-mission-visual {{ height: 240px; }}
        .about-pillars-grid, .about-why-grid {{ grid-template-columns: 1fr; }}
        .about-philo-grid {{ grid-template-columns: repeat(2, 1fr); }}
        .about-roadmap-track {{ grid-template-columns: repeat(2, 1fr); gap: 32px; }}
        .about-roadmap-track::before {{ display: none; }}
    }}
    @media (max-width: 768px) {{
        .about-section {{ padding: 72px 0; }}
        .about-hero-content {{ padding: 120px 6% 60px; }}
        .about-topbar {{ top: max(16px, env(safe-area-inset-top)); }}
        .about-nav-home {{ margin-right: 90px; font-size: 0.8rem; padding: 8px 16px; }}
        .about-logo {{ height: 48px; padding: 6px 14px; }}
        div[data-testid="stElementContainer"]:has(> div[data-testid="stButton"]),
        div[data-testid="stButton"] {{
            top: max(16px, env(safe-area-inset-top)); right: max(16px, env(safe-area-inset-right));
        }}
        .about-philo-grid, .about-roadmap-track {{ grid-template-columns: 1fr; }}
        .about-who-grid {{ grid-template-columns: 1fr; }}
    }}
    @media (hover: none) and (pointer: coarse) {{
        .about-who-card:hover, .about-pillar-card:hover {{ transform: none; }}
    }}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(page_html, unsafe_allow_html=True)
