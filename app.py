# import streamlit as st

# # Hide developer option elements globally
# st.set_option("client.toolbarMode", "minimal")

# import streamlit as st
# import base64
# import os
# import datetime
# import io

# # --- 1. PAGE CONFIG & THEME ---
# st.set_page_config(
#     page_title="Longisa County Referral Hospital", 
#     layout="wide", 
#     initial_sidebar_state="expanded"
# )

# # --- LOAD LOCAL SVG COAT OF ARMS ---
# def get_local_svg_base64(filepath):
#     clean_path = os.path.normpath(filepath.replace("file:///", ""))
#     try:
#         if os.path.exists(clean_path):
#             with open(clean_path, "rb") as f:
#                 svg_data = f.read()
#             encoded = base64.b64encode(svg_data).decode("utf-8")
#             return f"data:image/svg+xml;base64,{encoded}"
#     except Exception:
#         pass
#     return "https://cdn-icons-png.flaticon.com/512/3063/3063189.png"

# # Use exact local path
# # local_logo_path = r"C:\Users\Hi\Downloads\government-of-kenya-emblem-gok-vector-logo-seeklogo\government-of-kenya-emblem-gok-seeklogo.svg"
# # logo_base64 = get_local_svg_base64(local_logo_path)
# import requests

# # Your Render website URL
# logo_url = "https://longisa-hospital-website.onrender.com/government-of-kenya-emblem-gok-seeklogo.svg"

# response = requests.get(logo_url, timeout=30)
# response.raise_for_status()

# logo_base64 = base64.b64encode(response.content).decode("utf-8")

# print("Logo loaded successfully!")

# # Default Fallbacks
# DEFAULT_NEWS_IMG = "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&q=80&w=600"
# DEFAULT_DOC_IMG = "https://img.freepik.com/free-vector/doctor-character-background_1270-84.jpg"

# # --- CUSTOM GLOBAL HEALTH THEME CSS ---
# st.markdown("""
#     <style>
#     /* Prevent hiding the header entirely so the native sidebar toggle button remains visible */
#     [data-testid="stHeader"] {
#         background-color: rgba(0,0,0,0) !important;
#         z-index: 999;
#     }
    
#     /* Ensure the sidebar toggle button itself is styled clearly */
#     [data-testid="collapsedControl"] {
#         color: #004a99 !important;
#         background-color: #ffffff !important;
#         border-radius: 50%;
#         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
#     }
    
#     .block-container {
#         padding-top: 2rem !important;
#         padding-left: 0rem !important;
#         padding-right: 0rem !important;
#         max-width: 100% !important;
#     }
#     .main .block-container > div {
#         padding-left: 2rem !important;
#         padding-right: 2rem !important;
#     }
    
#     .stApp { background-color: #f4f7f6; }
    
#     /* End-to-End Topbar Style */
#     .gov-topbar { 
#         display: flex; 
#         align-items: center; 
#         justify-content: space-between; 
#         background-color: #ffffff; 
#         padding: 15px 40px; 
#         border-bottom: 5px solid #008080; 
#         margin-bottom: 10px; 
#         width: 100%;
#         box-shadow: 0 4px 10px rgba(0,0,0,0.06);
#     }
#     .gov-logo-section { display: flex; align-items: center; gap: 20px; }
#     .gov-logo { height: 65px; width: auto; object-fit: contain; }
    
#     .gov-title { 
#         font-family: inherit;
#         font-weight: 800; 
#         color: #004a99; 
#         font-size: 1.4rem; 
#         line-height: 1.2; 
#         letter-spacing: normal; 
#     }
#     .gov-subtitle { color: #008080; font-weight: 600; font-size: 0.9rem; }
#     .hospital-tag { 
#         text-align: right; 
#         font-family: inherit;
#         font-weight: 800; 
#         color: #004a99; 
#         font-size: 1.4rem; 
#         border-right: 4px solid #ffcc00; 
#         padding-right: 15px; 
#     }
    
#     /* Home Decor & Theme Modifications */
#     .header-box { 
#         background: linear-gradient(135deg, #004a99 0%, #0066cc 50%, #008080 100%); 
#         color: white; 
#         padding: 45px; 
#         border-radius: 12px; 
#         text-align: center; 
#         margin-bottom: 30px;
#         border-bottom: 5px solid #ffcc00;
#         box-shadow: 0 4px 15px rgba(0,74,153,0.15);
#     }
    
#     /* Image Card styling with Overflow protection */
#     .card { 
#         background-color: white; 
#         border-radius: 12px; 
#         border-left: 6px solid #008080; 
#         box-shadow: 0 4px 12px rgba(0,0,0,0.04); 
#         margin-bottom: 20px; 
#         overflow: hidden;
#         height: 100%;
#         display: flex;
#         flex-direction: column;
#     }
#     .card-content {
#         padding: 20px;
#         flex-grow: 1;
#     }
#     .card-img {
#         width: 100%;
#         height: 250px;
#         object-fit: cover;
#         display: block;
#     }
    
#     /* Professionally Sized News/Articles Style */
#     .news-card {
#         background: #ffffff;
#         border-radius: 10px;
#         border-top: 5px solid #004a99;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.05);
#         padding: 20px;
#         height: 100%;
#         display: flex;
#         flex-direction: column;
#         justify-content: space-between;
#     }
#     .news-meta {
#         font-size: 0.8rem;
#         color: #008080;
#         font-weight: bold;
#         text-transform: uppercase;
#         margin-bottom: 8px;
#     }
#     .news-title {
#         font-size: 1.2rem;
#         font-weight: 700;
#         color: #004a99;
#         margin: 5px 0 12px 0;
#         line-height: 1.3;
#     }
#     .news-text {
#         font-size: 0.9rem;
#         color: #444444;
#         line-height: 1.5;
#         flex-grow: 1;
#         margin-bottom: 12px;
#     }
    
#     .section-header { border-bottom: 3px solid #008080; padding-bottom: 10px; margin-top: 35px; margin-bottom: 25px; color: #004a99; font-weight: 700; }
#     .quick-box { background-color: #ffffff; padding: 22px; border-radius: 10px; border-top: 4px solid #004a99; height: 100%; box-shadow: 0 4px 8px rgba(0,0,0,0.03); margin-bottom: 15px; }
#     .center-card { background-color: #eef7f7; padding: 18px; border-radius: 8px; border-left: 4px solid #008080; margin-bottom: 15px; }
#     .testimonial-box { background-color: #ffffff; padding: 25px; border-radius: 10px; border-left: 6px solid #ffcc00; font-style: italic; box-shadow: 0 4px 10px rgba(0,0,0,0.03); }
#     .summary-box { background-color: #eef5fc; padding: 20px; border-radius: 10px; border: 1px solid #bce0fd; margin-top: 20px; }
#     .stButton>button { width: 100%; border-radius: 6px; font-weight: 600; }
    
#     /* Perfect Circle Profile Fixes */
#     .doctor-flex { display: flex; align-items: center; gap: 25px; }
#     .doctor-avatar-container { width: 110px; height: 110px; min-width: 110px; max-width: 110px; position: relative; }
#     .doctor-avatar { 
#         width: 110px; 
#         height: 110px; 
#         border-radius: 50% !important; 
#         object-fit: cover !important; 
#         aspect-ratio: 1 / 1 !important;
#         border: 3px solid #008080; 
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#     }
    
#     /* =========================================================
#        SIDEBAR CUSTOMIZATIONS - COLLAPSE / EXPAND ACTIVE
#        ========================================================= */
#     [data-testid="stSidebar"] {
#         background-color: #003366 !important;
#         border-right: 5px solid #ffcc00 !important;
#     }
    
#     [data-testid="stSidebar"] .stMarkdown, 
#     [data-testid="stSidebar"] p, 
#     [data-testid="stSidebar"] h3, 
#     [data-testid="stSidebar"] span,
#     [data-testid="stSidebar"] label {
#         color: #ffffff !important;
#     }
    
#     [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
#         color: #ffcc00 !important;
#         font-weight: bold;
#         font-size: 1.1rem;
#     }
    
#     [data-testid="sidebar-user-features"] {
#         display: none !important;
#     }
    
#     .sidebar-branding { text-align: center; padding: 15px 0; border-bottom: 2px solid #ffcc00; margin-bottom: 20px; }

#     /* --- REUSABLE FOOTER STYLES --- */
#     .global-footer {
#         background-color: #002b5c;
#         color: #ffffff;
#         padding: 40px 20px;
#         margin-top: 60px;
#         border-top: 5px solid #ffcc00;
#         font-size: 0.9rem;
#     }
#     .footer-container {
#         max-width: 1200px;
#         margin: 0 auto;
#         display: flex;
#         flex-wrap: wrap;
#         justify-content: space-between;
#         gap: 30px;
#     }
#     .footer-section {
#         flex: 1;
#         min-width: 220px;
#     }
#     .footer-section h4 {
#         color: #ffcc00;
#         margin-bottom: 15px;
#         border-bottom: 2px solid #008080;
#         padding-bottom: 5px;
#         font-weight: 700;
#     }
#     .footer-section p, .footer-section ul {
#         line-height: 1.6;
#         color: #d1d8e0;
#     }
#     .footer-section ul {
#         list-style: none;
#         padding-left: 0;
#     }
#     .footer-section ul li {
#         margin-bottom: 8px;
#     }
#     .footer-bottom {
#         text-align: center;
#         padding-top: 25px;
#         margin-top: 25px;
#         border-top: 1px solid #004a99;
#         color: #a5b1c2;
#         font-size: 0.8rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- GOVERNMENT LOGO TOPBAR ---
# st.markdown(f"""
#     <style>
#     .gov-topbar {{
#         overflow: hidden;
#     }}
#     .hospital-tag {{
#         overflow: hidden;
#         white-space: nowrap;
#         width: 350px;
#         position: relative;
#     }}
#     .animated-hospital-text {{
#         display: inline-block;
#         white-space: nowrap;
#         animation: scroll-right-to-left 10s linear infinite;
#     }}
#     @keyframes scroll-right-to-left {{
#         0% {{ transform: translateX(100%); }}
#         100% {{ transform: translateX(-100%); }}
#     }}
#     </style>

#     <div class="gov-topbar">
#         <div class="gov-logo-section">
#             <img class="gov-logo" src="{logo_base64}" alt="Government of Kenya Logo">
#             <div>
#                 <div class="gov-title">GOVERNMENT OF KENYA</div>
#                 <div class="gov-subtitle">Ministry of Health &bull; Bomet County Government</div>
#             </div>
#         </div>
#         <div class="hospital-tag">
#             <div class="animated-hospital-text">
#                 LONGISA COUNTY REFERRAL HOSPITAL
#             </div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# # --- 2. INITIAL SEED DATA FOR MEDICAL STAFF ---
# if 'doctors' not in st.session_state:
#     st.session_state.doctors = [
#         {"id": "doc_1", "name": "Dr. Peris Mbatha Mutuku", "spec": "Nephrologist", "desc": "Seasoned medical professional with 12 years of experience as Consultant Physician and Lead Nephrologist.", "img": DEFAULT_DOC_IMG},
#         {"id": "doc_2", "name": "Dr. Brian Omina Odari", "spec": "Global Health Management", "desc": "Specialist with 12 years of experience in global health management and international patient coordination.", "img": DEFAULT_DOC_IMG},
#         {"id": "doc_3", "name": "Dr. Alex Gathura Kagia", "spec": "Obstetrician-Gynaecologist", "desc": "Obstetrician-Gynaecologist with eight years of specialised experience in reproductive health.", "img": DEFAULT_DOC_IMG},
#         {"id": "doc_4", "name": "Dr. Fahmo Mohamed Yusuf", "spec": "Paediatrician", "desc": "Dedicated Senior Registrar and Paediatrician with 10 years of experience in child healthcare.", "img": DEFAULT_DOC_IMG},
#         {"id": "doc_5", "name": "Dr. Joram Mugo Muthui", "spec": "Obstetrician-Gynaecologist", "desc": "Compassionate and dedicated specialist with seven years of experience in reproductive health.", "img": DEFAULT_DOC_IMG},
#         {"id": "doc_6", "name": "Dr. Lauryn Busolo Mengesa", "spec": "Obstetrician-Gynaecologist", "desc": "Obstetrician-Gynaecologist with 12 years of experience, trained at the University of Nairobi.", "img": DEFAULT_DOC_IMG}
#     ]

# # --- 3. SEED DATA FOR DEPARTMENTS (Level 5 Hospital) ---
# if 'departments' not in st.session_state:
#     st.session_state.departments = [
#         {"id": "dep_1", "name": "🩺 General & Specialized Internal Medicine", "desc": "Comprehensive clinical management of complex systemic chronic conditions, including hypertension, oncology interventions, and pulmonology."},
#         {"id": "dep_2", "name": "🤰 Obstetrics & Gynecology (Maternity)", "desc": "Comprehensive Level 5 maternal infrastructure providing advanced antenatal care, safe high-risk deliveries, neonatal monitoring, and reproductive family planning."},
#         {"id": "dep_3", "name": "👶 Pediatrics & Child Health Services", "desc": "A dedicated infant and adolescent clinic specializing in growth monitoring, immunizations, and pediatric emergency support."},
#         {"id": "dep_4", "name": "🏥 Intensive Care Unit (ICU) & High Dependency Unit (HDU)", "desc": "State-of-the-art critical care facilities supporting continuous organ support, mechanical ventilation, and post-operative monitoring."},
#         {"id": "dep_5", "name": "🧪 Dialysis & Renal Unit", "desc": "Modern medical infrastructure offering customized hemodialysis therapy and management plans for acute and end-stage kidney diseases."},
#         {"id": "dep_6", "name": "🩻 Advanced Radiology & Imaging Services", "desc": "Premium imaging diagnostics including digital X-Rays, high-resolution CT scans, digital mammography, and ultrasound screenings."},
#         # --- Additional Level 6 Departments ---
#         {"id": "dep_7", "name": "🔪 General & Cardiothoracic Surgery", "desc": "Advanced surgical theatre equipped for complex cardiothoracic, abdominal, and reconstructive procedures."},
#         {"id": "dep_8", "name": "🧠 Neurology & Neurosurgery", "desc": "Specialized care for neurological disorders, brain injury trauma, and advanced neurosurgical interventions."},
#         {"id": "dep_9", "name": "🦴 Orthopedics & Trauma Center", "desc": "Focused management of musculoskeletal injuries, fracture repairs, spinal surgery, and joint replacement procedures."},
#         {"id": "dep_10", "name": "👁️ Ophthalmology & ENT", "desc": "Specialized diagnostic and surgical services for complex eye, ear, nose, and throat conditions."},
#         {"id": "dep_11", "name": "🧬 Laboratory & Pathology Services", "desc": "High-throughput diagnostic lab offering histology, hematology, microbiology, and molecular pathology services."},
#         {"id": "dep_12", "name": "🩹 Physical Therapy & Rehabilitation", "desc": "Integrated recovery programs including physiotherapy, occupational therapy, and speech therapy for post-surgical or stroke patients."},
#         {"id": "dep_13", "name": "💊 Pharmacy & Oncology Infusion Center", "desc": "Comprehensive pharmaceutical care and dedicated facilities for chemotherapy administration and pain management."}
#     ]

# # --- 4. SEED DATA FOR ABOUT US, CONTACTS & HOURS ---
# if 'about_data' not in st.session_state:
#     st.session_state.about_data = {
#         "mission": "To provide high-quality, patient-centered clinical care, diagnostic interventions, and medical solutions under the principles of equity, competence, and professionalism.",
#         "vision": "To be the premiere Level 5 Referral Hospital in East Africa, recognized for excellence, innovation, and training in health delivery.",
#         "hours": """
# * **Specialist Clinics:** Mon - Fri, 8:00 AM - 5:00 PM
# * **Emergency Department:** Open 24/7 (Everyday)
# * **Inpatient Visiting Hours:** 12:30 PM - 2:00 PM & 4:30 PM - 6:30 PM Daily
#         """,
#         "contacts": """
# * **Emergency Desk Line:** +254 7480 76703
# * **General Enquiries Desk:** +254 (0) 52 22234
# * **Official Registry Mail:** admin@longisa.or.ke
# * **Mailing Address:** P.O. Box 25, Longisa, Bomet County, Kenya
#         """
#     }

# # --- 5. SEED DATA FOR ARTICLES / NEWS ---
# if 'articles' not in st.session_state: 
#     st.session_state.articles = [
#         {
#             "id": "art_1",
#             "title": "Understanding Universal Health Coverage in Bomet County",
#             "date": "March 18, 2026",
#             "content": "Longisa County Referral Hospital continues to expand accessible healthcare services under county health development initiatives. By focusing on primary healthcare models and establishing seamless local diagnostic laboratories, patients are now able to access vital treatments closer to home without travel fatigue.",
#             "img": "https://res.cloudinary.com/jlengxni/image/upload/v1784122494/BOARD_LON_kcn1cd.jpg"
#         },
#         {
#             "id": "art_2",
#             "title": "Preventive Care: Managing Hypertension Locally",
#             "date": "April 05, 2026",
#             "content": "Hypertension remains one of the leading chronic challenges in our clinics. The clinical support staff recommends routine check-ups at our wellness center. Simple dietary adjustments combined with a routine 30-minute daily walk can decrease acute cardiac complications by up to 40%.",
#             "img": "https://res.cloudinary.com/jlengxni/image/upload/v1784123012/DOC_LONG_pmlkhx.jpg"
#         },
#         {
#             "id": "art_3",
#             "title": "Triple ISO Certification Formally Awarded",
#             "date": "Latest Operational Update",
#             "content": "Longisa Hospital has formally secured environmental management and occupational safety certificates. By improving critical diagnostic pathways and updating care infrastructure, we keep serving with total adherence to national and global guidelines.",
#             "img": "https://res.cloudinary.com/jlengxni/image/upload/v1784123362/SERVING_LONG_e1esb4.jpg"
#         }
#     ]

# if 'admin_logged_in' not in st.session_state: st.session_state.admin_logged_in = False
# if 'alpha_filter' not in st.session_state: st.session_state.alpha_filter = "All"
# if 'current_tab' not in st.session_state: st.session_state.current_tab = "Home"

# # --- Language bar ---
# st.markdown("<p style='text-align: right; margin-right: 40px; color:#666; font-size:0.9rem;'>🌐 Language: English (EN) | Home 🇬🇧</p>", unsafe_allow_html=True)

# # --- 6. SIDEBAR NAVIGATION ---
# with st.sidebar:
#     st.markdown("""
#     <div class="sidebar-branding" style="text-align:center;">
#         <img src="https://res.cloudinary.com/jlengxni/image/upload/v1784122847/CONFE_fhyh4b.jpg"
#              style="
#                  width:180px;
#                  height:180px;
#                  border-radius:50%;
#                  object-fit:cover;
#                  display:block;
#                  margin:0 auto 10px auto;
#                  border:3px solid #ffffff;
#                  box-shadow:0 2px 8px rgba(0,0,0,0.2);
#              ">
#         <h3 style="margin-bottom:2px;">Longisa Admin</h3>
#         <span style="font-size:0.85rem; opacity:0.8;">
#             Secure Admin Dashboard Access
#         </span>
#     </div>
#     """, unsafe_allow_html=True)

#     st.error("🚨 **EMERGENCY LINE**\n\n+254 7480 76703")
#     st.markdown("---")

#     menu = [
#         "Home",
#         "Find a Doctor",
#         "Book an Appointment",
#         "Departments",
#         "Articles",
#         "About Us",
#         "About The Hospital",
#         "Admin Panel",
#     ]
    
#     selected_menu = st.radio("Navigation Menu", menu, index=menu.index(st.session_state.current_tab))
    
#     if selected_menu != st.session_state.current_tab:
#         st.session_state.current_tab = selected_menu
#         st.rerun()

# def set_route(route_name):
#     st.session_state.current_tab = route_name
#     st.rerun()

# # --- 7. APPLICATION LOGIC ---

# # --- TAB: HOME ---
# if st.session_state.current_tab == "Home":
#     st.markdown("""
#         <div class="header-box">
#             <h1>LONGISA COUNTY REFERRAL HOSPITAL</h1>
#             <p style='font-size:1.1rem; font-weight:400;'>SERVING WITH THE FEAR OF GOD</p>
#             <p style='font-size:1.1rem; font-weight:400;'> LEVITICUS 25:17.</p>
#         </div>
#     """, unsafe_allow_html=True)
    
#     intro_col1, intro_col2 = st.columns([1.6, 1.4], gap="large")
#     with intro_col1:
#         st.markdown("<h3 style='color:#004a99;'>Healthcare with Excellence</h3>", unsafe_allow_html=True)
#         st.write(
#             """
#             Longisa County Referral Hospital has excelled in medical expertise and service provision, 
#             deservedly earning widespread recognition throughout East Africa and beyond. 
#             By integrating advanced clinical treatment pathways with standard-setting facility 
#             infrastructure, we deliver high-impact clinical solutions to all communities.
#             """
#         )
#         col_btn1, col_btn2 = st.columns(2)
#         with col_btn1:
#             if st.button("Explore Our Clinical Services ➜", key="home_srv_btn"):
#                 set_route("Departments")
#         with col_btn2:
#             if st.button("About Us ➜", key="home_abt_btn"):
#                 set_route("About Us")
#         st.write("")
#         st.info("💡 **Quick Hotlinks Ready**\n\nNeed access parameters fast? Use the toggle menu navigation index or the Quick Access matrix panels configured directly below.")
    
#     with intro_col2:
#         st.markdown("##### 📸 Longisa Hospital Gallery View")
#         view_mode = st.radio("Select Facility Perspective:", ["Main Campus Entrance", "Clinical Landscape View"], horizontal=True, label_visibility="collapsed")
#         if view_mode == "Main Campus Entrance":
#             st.image("https://res.cloudinary.com/jlengxni/image/upload/v1784047255/LONGISA_GATE_dvsoxw.jpg", caption="Longisa County Referral Hospital Main Entrance Hub", use_container_width=True)
#         else:
#             st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRJuT108ODLoq3JHa1rkyouIQpv2Nx4gXERs1FKkr7wuK69mfjDbvdnWhE0-8FxIV9JmXKzzGXTCM3M3aE", caption="Clinical Facility Infrastructures at Longisa", use_container_width=True)

#     # Quick Access Section
#     st.markdown("<h2 class='section-header'>⚡ Quick Access</h2>", unsafe_allow_html=True)
#     q_col1, q_col2, q_col3 = st.columns(3, gap="medium")

#     with q_col1:
#         st.markdown("""
#             <div class="card">
#                 <img class="card-img" src="https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRr8TWHOgz46NyUcx_nVJTdSq1-FYuDpGlqX34OHrt2DW5mt0cw1JqTQVD2tH21INlSJTtYiMj71irR-Bg" alt="Doctor advising patient">
#                 <div class="card-content">
#                     <h4 style="color:#008080; margin-top:0;">👨‍⚕️ Find a Doctor</h4>
#                     <p style='font-size:0.9rem; color:#444;'>Connecting you to trusted Doctors anytime, anywhere. Whether you need a routine check-up, specialist advice, or urgent care.</p>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
#         if st.button("Search Doctors", key="qa_search_doc", use_container_width=True):
#             set_route("Find a Doctor")
            
#     with q_col2:
#         st.markdown("""
#             <div class="card">
#                 <img class="card-img" src="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcSQVZBWMrC9abAYU3MzC7K1j8r_voEL45OJ5tFuGs3GjHKAlE90PT8EAFyOvk5W5pieOhgN-oXaikNJZqo" alt="Stethoscope with passport and flight tickets">
#                 <div class="card-content">
#                     <h4 style="color:#008080; margin-top:0;">🌍 Medical Tourism</h4>
#                     <p style='font-size:0.9rem; color:#444;'>Discover our dedicated services for international patients, from travel assistance to world-class medical care. We're here to make your journey smooth.</p>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
#         if st.button("Learn More", key="qa_tourism_learn", use_container_width=True):
#             st.toast("Redirecting to International Health coordination systems...")
            
#     with q_col3:
#         st.markdown("""
#             <div class="card">
#                 <img class="card-img" src="https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQYGBSd6Vnay0IGL7dcBRCFsbpKKCRMKUKA4iBE8T5K5GCnduWlMYpC-MPf5dZOizp6iiJGLVu8EnqgEyo" alt="Red map pin pinpointing hospital building">
#                 <div class="card-content">
#                     <h4 style="color:#008080; margin-top:0;">📍 Getting to the Hospital</h4>
#                     <p style='font-size:0.9rem; color:#444;'>We want your visit to be easy. Find directions, parking infrastructure arrays, and transport info on our Location system mapping panel.</p>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
#         if st.button("Get Directions", key="qa_get_dirs", use_container_width=True):
#             st.toast("Opening routing coordination pathways...")

#     # Dynamic Outpatient Centers
#     st.markdown("<h2 class='section-header'>🏢 Outpatient Centers</h2>", unsafe_allow_html=True)
#     st.write("Learn more about our outpatient centers or choose a specific location.")
    
#     oc_col1, oc_col2, oc_col3, oc_col4 = st.columns(4)
#     with oc_col1:
#         st.markdown("""<div class='center-card'><b>🏢 Anderson Specialty Centre</b><br><small>Argwings Kodhek Road, Anderson Centre, 1st Floor</small></div>""", unsafe_allow_html=True)
#         st.markdown("""<div class='center-card'><b>🏢 Kiambu Mall</b><br><small>Kiambu Mall, 2nd Floor, Kiambu Road</small></div>""", unsafe_allow_html=True)
#     with oc_col2:
#         st.markdown("""<div class='center-card'><b>🏢 Capital Centre</b><br><small>Capital Centre, 1st floor, Mombasa Road</small></div>""", unsafe_allow_html=True)
#         st.markdown("""<div class='center-card'><b>🏢 Rosslyn Riviera</b><br><small>Rosslyn Riviera Mall, 3rd Floor, Limuru Rd</small></div>""", unsafe_allow_html=True)
#     with oc_col3:
#         st.markdown("""<div class='center-card'><b>🏢 Chandaria A & E Centre</b><br><small>Main Hospital Complex Campus</small></div>""", unsafe_allow_html=True)
#         st.markdown("""<div class='center-card'><b>🏢 Southfield Mall</b><br><small>Southfield Mall, 2nd Floor, Airport North Road</small></div>""", unsafe_allow_html=True)
#     with oc_col4:
#         st.markdown("""<div class='center-card'><b>🏢 Galleria Mall</b><br><small>Galleria Shopping Mall, 2nd Floor, Lang'ata Road</small></div>""", unsafe_allow_html=True)
#         if st.button("Explore All Locations", key="exp_all_locs_btn"):
#             st.toast("Fetching outpatient medical annex schedules...")

#     # DYNAMIC NEWS SECTION
#     st.markdown("<h2 class='section-header'>📰 Latest News & Updates</h2>", unsafe_allow_html=True)
    
#     articles_list = st.session_state.articles
#     if len(articles_list) > 0:
#         cols = st.columns(min(len(articles_list), 3), gap="medium")
#         for i, art in enumerate(articles_list[:3]):
#             with cols[i % 3]:
#                 img_src = art.get('img') if art.get('img') else DEFAULT_NEWS_IMG
#                 st.markdown(f"""
#                     <div class="news-card">
#                         <img src="{img_src}" style="width:100%; height:150px; object-fit:cover; border-radius:8px; margin-bottom:12px;">
#                         <div>
#                             <div class="news-meta">📅 {art.get('date', 'Recent Update')}</div>
#                             <div class="news-title">{art['title']}</div>
#                             <div class="news-text">{art['content'][:120]}...</div>
#                         </div>
#                     </div>
#                 """, unsafe_allow_html=True)
#                 if st.button("Read Full Story", key=f"read_home_art_{art['id']}", use_container_width=True):
#                     set_route("Articles")
#     else:
#         st.info("No news updates posted yet.")

# # --- TAB: FIND A DOCTOR ---
# elif st.session_state.current_tab == "Find a Doctor":
#     st.header("Our Specialists")
#     st.write("Get to know our doctors and their areas of expertise.")
    
#     st.markdown("### 🔍 Narrow your search")
#     filter_col1, filter_col2 = st.columns(2)
    
#     with filter_col1:
#         search_name = st.text_input("By Doctor's Name", placeholder="Type name...")
#     with filter_col2:
#         specialties_list = ["All Specialties"] + list(set([d['spec'] for d in st.session_state.doctors]))
#         search_spec = st.selectbox("By Specialty Clinic", specialties_list)
        
#     st.markdown("##### Filter by First Name")
#     alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
#     alpha_cols = st.columns(27)
#     with alpha_cols[0]:
#         if st.button("All", key="btn_all"):
#             st.session_state.alpha_filter = "All"
#     for idx, letter in enumerate(alphabet):
#         with alpha_cols[idx + 1]:
#             if st.button(letter, key=f"btn_{letter}"):
#                 st.session_state.alpha_filter = letter
                
#     if st.button("Reset Filters", key="reset_all_filters"):
#         st.session_state.alpha_filter = "All"
#         st.rerun()
                
#     if st.session_state.alpha_filter != "All":
#         st.info(f"Showing results starting with letter: **{st.session_state.alpha_filter}**")
        
#     st.markdown("---")
    
#     filtered_docs = []
#     for doc in st.session_state.doctors:
#         if search_name and search_name.lower() not in doc['name'].lower():
#             continue
#         if search_spec != "All Specialties" and doc['spec'] != search_spec:
#             continue
#         clean_first_name = doc['name'].replace("Dr. ", "").strip()
#         if st.session_state.alpha_filter != "All" and not clean_first_name.upper().startswith(st.session_state.alpha_filter):
#             continue
            
#         filtered_docs.append(doc)

#     if len(filtered_docs) == 0:
#         st.warning("No specialists match your selected filtration criteria.")
#     else:
#         for doc in filtered_docs:
#             img_style = doc['img'] if isinstance(doc['img'], str) else DEFAULT_DOC_IMG
            
#             st.markdown(f"""
#             <div class="card">
#                 <div class="card-content">
#                     <div class="doctor-flex">
#                         <div class="doctor-avatar-container">
#                             <img src="{img_style}" class="doctor-avatar">
#                         </div>
#                         <div>
#                             <h3 style="color:#004a99; margin:0 0 5px 0;">👨‍⚕️ {doc['name']}</h3>
#                             <p style='color: #008080; font-weight: bold; margin-bottom: 8px;'>{doc['spec']}</p>
#                             <p style='font-size: 0.95rem; color: #444; margin:0;'>{doc.get('desc', 'Specialist Consultant.')}</p>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
#             btn_col1, btn_col2, _ = st.columns([1.5, 1.5, 3])
#             with btn_col1:
#                 if st.button("Book an appointment", key=f"bk_{doc['id']}"):
#                     set_route("Book an Appointment")
#             with btn_col2:
#                 if st.button("View Profile", key=f"prof_{doc['id']}"):
#                     st.success(f"Profile Page details for {doc['name']} loaded successfully.")
#             st.write("")

# # --- TAB: BOOK AN APPOINTMENT ---
# elif st.session_state.current_tab == "Book an Appointment":
#     st.header("Book Appointment")
#     st.write("A simple, secure booking experience.")
#     st.markdown("---")
    
#     form_col, summary_col = st.columns([1.8, 1.2], gap="large")
    
#     with form_col:
#         st.markdown("#### 1. Select Clinical Service")
#         services_options = [
#             "-- choose a service --", "Gynae-Oncology Clinic", "Obstetrics & Antenatal", "Cardiology Clinic", "Dialysis Unit"
#         ]
#         chosen_service = st.selectbox("Select Service Unit", services_options)
        
#         st.markdown("#### 2. Preferred Location")
#         location_options = ["Main Campus Hospital", "Anderson Specialty Centre", "Kiambu Mall"]
#         chosen_location = st.selectbox("Select Location", location_options)
        
#         st.markdown("#### 3. Patient Details")
#         pat_name = st.text_input("Full Name")
#         pat_phone = st.text_input("Phone Number")
        
#     with summary_col:
#         st.markdown("<div class='summary-box'>", unsafe_allow_html=True)
#         st.markdown("### 📋 Appointment Summary")
#         st.markdown(f"**Service:** {chosen_service}")
#         st.markdown(f"**Location:** {chosen_location}")
#         if pat_name:
#             st.markdown(f"**Patient:** {pat_name}")
#         st.markdown("</div>", unsafe_allow_html=True)
        
#         if st.button("Confirm Booking", type="primary"):
#             if chosen_service == "-- choose a service --" or not pat_name or not pat_phone:
#                 st.error("Please fill in all fields.")
#             else:
#                 st.success("Booking registered successfully!")

# # --- TAB: DEPARTMENTS ---
# elif st.session_state.current_tab == "Departments":
#     st.header("🏥 Hospital Departments & Specialized Clinical Units")
#     st.write("Browse through our integrated Level 5 specialized units.")
#     st.markdown("---")
    
#     # Display in responsive grid system
#     deps = st.session_state.departments
#     for i in range(0, len(deps), 3):
#         cols = st.columns(3)
#         for idx, dep in enumerate(deps[i:i+3]):
#             with cols[idx]:
#                 st.markdown(f"""
#                     <div class='quick-box'>
#                         <h3 style="color:#004a99; margin-top:0;">{dep['name']}</h3>
#                         <p style="font-size:0.95rem; line-height:1.5; color:#444;">{dep['desc']}</p>
#                     </div>
#                 """, unsafe_allow_html=True)

# # --- TAB: ARTICLES ---
# elif st.session_state.current_tab == "Articles":
#     st.header("Medical Bulletins & Hospital Press Articles")
#     st.write("Insights directly from our clinical practitioners.")
#     st.markdown("---")
    
#     for art in st.session_state.articles:
#         img_src = art.get('img') if art.get('img') else DEFAULT_NEWS_IMG
        
#         art_col1, art_col2 = st.columns([1, 2], gap="large")
#         with art_col1:
#             st.markdown(f"""
#                 <img src="{img_src}" style="width:100%; max-height:240px; object-fit:cover; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.1)">
#             """, unsafe_allow_html=True)
#         with art_col2:
#             st.markdown(f"<h3 style='color:#004a99; margin-top:0;'>{art['title']}</h3>", unsafe_allow_html=True)
#             st.markdown(f"<span style='color:#008080; font-weight:bold; font-size:0.85rem;'>📅 PUBLISHED: {art.get('date', 'Recent Update')}</span>", unsafe_allow_html=True)
#             st.write(art['content'])
#         st.markdown("<hr style='border-color: #ddd;'/>", unsafe_allow_html=True)

# # --- TAB: ABOUT US, CONTACT & HOURS ---
# # --- TAB: ABOUT US, CONTACT & HOURS ---
# elif st.session_state.current_tab == "About Us":
#     st.header("🏢 About Us, Contact & Visiting Hours")
#     st.write("Learn more about our organizational identity, clinical operations, and contact coordinates.")
    
#     # 1. ABOUT US PROFILE
#     st.markdown("""
#         <div class="quick-box" style="margin-bottom: 30px;">
#             <h3 style="color:#004a99; margin-top:0;">📖 Our Story & Profile</h3>
#             <p>
#                 Longisa County Referral Hospital is Bomet County's premier public referral healthcare institution. 
#                 Dedicated to serving with high clinical precision, scientific innovation, and spiritual compassion, 
#                 we operate under the guiding light of our motto: <b>"Serving with the Fear of God" (Leviticus 25:17)</b>.
#             </p>
#             <p>
#                 Through years of targeted expansion under the Bomet County Government, we have grown from a localized sub-district clinic 
#                 to a robust, state-of-the-art diagnostic and clinical referral node, serving patients across the entire South Rift region 
#                 and parts of Western Kenya.
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

#     # 2. CONTACT & VISITING HOURS
#     st.divider()
#     col_visiting, col_contact = st.columns(2)

#     with col_visiting:
#         st.subheader("⏰ Visiting Hours")
#         st.write("""
#         We kindly ask all visitors to adhere to these hours to ensure patient recovery and ward safety:
#         *   **General Wards:** 12:30 PM – 2:00 PM | 4:30 PM – 6:00 PM
#         *   **Maternity Wing:** 4:30 PM – 6:00 PM (Strict)
#         *   **ICU / HDU:** Restricted (Contact head nurse for clearance)
#         *   **Weekends/Public Holidays:** 10:00 AM – 12:00 PM | 4:00 PM – 6:00 PM
#         """)
#         st.caption("*Note: Only two visitors per patient at any given time.*")

#     with col_contact:
#         st.subheader("📞 Contact Information")
#         st.write("""
#         **General Enquiries:**
#         *   📍 Bomet–Mulot Road, Longisa
#         *   📧 longisahospital@yohoo.com
#         *   ☎️ +254 (0) 51 48 6706
        
#         **Emergency Services (24/7):**
#         *   🚑 +254 (0) 748 076 706
#         """)

# # --- TAB: ADMIN PANEL ---
    
#     # MISSION, VISION, CORE VALUES
#     m_col1, m_col2, m_col3 = st.columns(3)
#     with m_col1:
#         st.markdown("""
#             <div class="card" style="border-left-color: #004a99;">
#                 <div class="card-content">
#                     <h4 style="color:#004a99; margin-top:0;">🎯 Our Mission</h4>
#                     <p style="font-size:0.9rem; color:#444;">To provide comprehensive, accessible, affordable, and high-quality curative, preventive, and rehabilitative healthcare services to the residents of Bomet and beyond.</p>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
#     with m_col2:
#         st.markdown("""
#             <div class="card" style="border-left-color: #ffcc00;">
#                 <div class="card-content">
#                     <h4 style="color:#ffcc00; margin-top:0;">👁️ Our Vision</h4>
#                     <p style="font-size:0.9rem; color:#444;">A premier model healthcare facility providing standardized, world-class medical excellence and patient-centered clinical care in East Africa.</p>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
#     with m_col3:
#         st.markdown("""
#             <div class="card" style="border-left-color: #008080;">
#                 <div class="card-content">
#                     <h4 style="color:#008080; margin-top:0;">⭐ Core Values</h4>
#                     <p style="font-size:0.9rem; color:#444;">Compassion, Teamwork, Integrity, Professionalism, Accountability, Respect for Human Life, and Faith-led Service Delivery.</p>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
# # --- TAB: ABOUT BOMET COUNTY ---
# elif st.session_state.current_tab == "About The Hospital":
#     st.header("Longisa County Referral Hospital")
#     st.subheader("Bomet's  Healthcare Hub")
    
#     # Create two columns to hold the images side-by-side
#     img_col1, img_col2 = st.columns(2)
    
#     image_1_url = "https://res.cloudinary.com/jlengxni/image/upload/v1784101096/481478018_621577290625555_1757066875417058575_n_t2aujd.jpg"
#     image_2_url = "https://res.cloudinary.com/jlengxni/image/upload/v1784122494/BOARD_LON_kcn1cd.jpg" # Replace with your second image URL
    
#     with img_col1:
#         st.image(image_1_url, caption="Main Hospital Block", width=600)
        
#     with img_col2:
#         st.image(image_2_url, caption="Specialized Services Wing", width=680)
    
#     st.write("""
#     Longisa County Referral Hospital is the principal medical facility for Bomet County. 
#     Functioning as a vital referral center, it bridges the gap between local primary 
#     health clinics and national tertiary care.
#     """)
    
#     # Rest of your layout...
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### 🏥 Core Departments")
#         st.write("* Emergency & Critical Care\n* Maternal & Neonatal\n* Specialized Clinics")
#     with col2:
#         st.markdown("### 💡 Key Highlights")
#         st.write("* 144-bed capacity\n* Radiology Command Center\n* Regional Referral Hub")

# # --- TAB: ADMIN PANEL ---
# # --- TAB: ADMIN PANEL ---
# elif st.session_state.current_tab == "Admin Panel":
#     st.header("Secure Administration Control Room")
    
#     if not st.session_state.admin_logged_in:
#         st.markdown("### Admin Verification Required")
#         admin_pass = st.text_input("Enter Admin Password", type="password")
#         if st.button("Unlock Dashboard"):
#             if admin_pass == "admin123":
#                 st.session_state.admin_logged_in = True
#                 st.success("Authorization Granted.")
#                 st.rerun()
#             else:
#                 st.error("Incorrect credentials.")
#     else:
#         st.sidebar.success("🔑 Admin Mode Active")
#         if st.sidebar.button("Logout of Session"):
#             st.session_state.admin_logged_in = False
#             st.rerun()
            
#         admin_sub_tabs = st.tabs(["🩺 Manage Doctors", "🏢 Manage Departments", "📰 Manage News/Articles", "ℹ️ Edit About Info"])
        
#         # 1. DOCTOR MANAGEMENT SUB-TAB
#         with admin_sub_tabs[0]:
#             st.subheader("Doctor Specialist Panel")
            
#             # Sub-Section A: Add Doctor Specialist
#             with st.expander("➕ Add New Doctor Specialist", expanded=False):
#                 with st.form("new_doc_form", clear_on_submit=True):
#                     doc_name = st.text_input("Full Name (e.g., Dr. Jane Doe)")
#                     doc_spec = st.text_input("Specialty Clinical Specialty")
#                     doc_desc = st.text_area("Profile / Bio description")
#                     doc_file = st.file_uploader("Upload Profile Image", type=["jpg", "png", "jpeg"], key="doc_up")
                    
#                     doc_submit = st.form_submit_button("Save and Register Doctor")
#                     if doc_submit:
#                         if doc_name and doc_spec:
#                             img_encoded = DEFAULT_DOC_IMG
#                             if doc_file is not None:
#                                 bytes_data = doc_file.getvalue()
#                                 b64 = base64.b64encode(bytes_data).decode()
#                                 img_encoded = f"data:{doc_file.type};base64,{b64}"
                            
#                             new_doc = {
#                                 "id": f"doc_{len(st.session_state.doctors)+1}",
#                                 "name": doc_name,
#                                 "spec": doc_spec,
#                                 "desc": doc_desc,
#                                 "img": img_encoded
#                             }
#                             st.session_state.doctors.append(new_doc)
#                             st.success(f"{doc_name} registered successfully!")
#                             st.rerun()
#                         else:
#                             st.error("Name and specialty are required fields.")
            
#             # Sub-Section B: Update/Edit Doctors
#             with st.expander("✏️ Edit / Update Existing Specialists", expanded=False):
#                 doc_to_edit_id = st.selectbox("Select Doctor Specialist to Edit", options=[d["id"] for d in st.session_state.doctors], format_func=lambda idx: next(d["name"] for d in st.session_state.doctors if d["id"] == idx))
#                 doc_idx = next(i for i, d in enumerate(st.session_state.doctors) if d["id"] == doc_to_edit_id)
#                 target_doc = st.session_state.doctors[doc_idx]
                
#                 with st.form("edit_doc_form"):
#                     up_name = st.text_input("Full Name", value=target_doc["name"])
#                     up_spec = st.text_input("Specialty", value=target_doc["spec"])
#                     up_desc = st.text_area("Profile Description", value=target_doc.get("desc", ""))
#                     up_file = st.file_uploader("Replace Profile Image (Optional)", type=["jpg", "png", "jpeg"])
                    
#                     update_btn = st.form_submit_button("Update Doctor Record")
#                     if update_btn:
#                         st.session_state.doctors[doc_idx]["name"] = up_name
#                         st.session_state.doctors[doc_idx]["spec"] = up_spec
#                         st.session_state.doctors[doc_idx]["desc"] = up_desc
#                         if up_file is not None:
#                             bytes_data = up_file.getvalue()
#                             b64 = base64.b64encode(bytes_data).decode()
#                             st.session_state.doctors[doc_idx]["img"] = f"data:{up_file.type};base64,{b64}"
#                         st.success("Record updated successfully!")
#                         st.rerun()
            
#             # Sub-Section C: Delete Doctor Records
#             with st.expander("❌ Delete Doctor Specialist Record", expanded=False):
#                 st.write("Warning: This operation cannot be undone.")
#                 doc_to_del = st.selectbox("Select Doctor Specialist to Delete", options=[d["id"] for d in st.session_state.doctors], format_func=lambda idx: next(d["name"] for d in st.session_state.doctors if d["id"] == idx), key="doc_del")
#                 if st.button("Delete Doctor Permanently", type="primary"):
#                     st.session_state.doctors = [d for d in st.session_state.doctors if d["id"] != doc_to_del]
#                     st.success("Doctor record deleted successfully.")
#                     st.rerun()

#         # 2. DEPARTMENT MANAGEMENT SUB-TAB
#         with admin_sub_tabs[1]:
#             st.subheader("Manage Departments")
            
#             with st.form("new_dep_form", clear_on_submit=True):
#                 st.write("Add Custom Department Unit")
#                 new_dep_name = st.text_input("Department Name (e.g., Intensive Care Unit)")
#                 new_dep_desc = st.text_area("Unit description")
                
#                 if st.form_submit_button("Create Department"):
#                     if new_dep_name:
#                         new_dep = {
#                             "id": f"dep_{len(st.session_state.departments)+1}",
#                             "name": new_dep_name,
#                             "desc": new_dep_desc
#                         }
#                         st.session_state.departments.append(new_dep)
#                         st.success(f"{new_dep_name} successfully registered!")
#                         st.rerun()
#                     else:
#                         st.error("Name field is required.")
            
#             st.markdown("#### Existing Departments")
#             for idx, dep in enumerate(st.session_state.departments):
#                 col_d1, col_d2 = st.columns([4, 1])
#                 with col_d1:
#                     st.write(f"**{dep['name']}** - {dep['desc']}")
#                 with col_d2:
#                     if st.button("Delete Department", key=f"del_dep_{dep['id']}", type="primary"):
#                         st.session_state.departments.pop(idx)
#                         st.success("Department removed.")
#                         st.rerun()

#         # 3. NEWS/ARTICLES SUB-TAB
#         with admin_sub_tabs[2]:
#             st.subheader("Manage News Articles")
#             with st.form("add_article_form_admin", clear_on_submit=True):
#                 new_title = st.text_input("Article Title")
#                 new_date = st.text_input("Date (e.g., July 15, 2026)")
#                 new_content = st.text_area("Article Content")
#                 uploaded_image = st.file_uploader("Upload Feature Image", type=["jpg", "png", "jpeg"])
                
#                 if st.form_submit_button("Publish Article"):
#                     if new_title and new_content:
#                         img_encoded = None
#                         if uploaded_image is not None:
#                             bytes_data = uploaded_image.getvalue()
#                             b64 = base64.b64encode(bytes_data).decode()
#                             img_encoded = f"data:{uploaded_image.type};base64,{b64}"
                        
#                         new_art = {
#                             "id": f"art_{len(st.session_state.articles) + 1}",
#                             "title": new_title,
#                             "date": new_date if new_date else datetime.datetime.now().strftime("%B %d, %Y"),
#                             "content": new_content,
#                             "img": img_encoded
#                         }
#                         st.session_state.articles.insert(0, new_art)
#                         st.success("Article successfully published.")
#                         st.rerun()
#                     else:
#                         st.error("Missing title or content fields.")

#         # 4. EDIT ABOUT INFO SUB-TAB
#         with admin_sub_tabs[3]:
#             st.subheader("Edit About Us Details")
#             with st.form("about_us_form"):
#                 about_mission = st.text_area("Hospital Mission", value=st.session_state.about_data["mission"])
#                 about_vision = st.text_area("Hospital Vision", value=st.session_state.about_data["vision"])
#                 about_hours = st.text_area("Operational Hours (Markdown List Format)", value=st.session_state.about_data["hours"])
#                 about_contacts = st.text_area("Contact Directories (Markdown List Format)", value=st.session_state.about_data["contacts"])
                
#                 if st.form_submit_button("Save Hospital Information Changes"):
#                     st.session_state.about_data["mission"] = about_mission
#                     st.session_state.about_data["vision"] = about_vision
#                     st.session_state.about_data["hours"] = about_hours
#                     st.session_state.about_data["contacts"] = about_contacts
#                     st.success("About Us clinical data structures updated successfully!")
#                     st.rerun()

# # --- REUSABLE FOOTER ---
# st.markdown("""
#     <div class="global-footer">
#         <div class="footer-container">
#             <div class="footer-section">
#                 <h4>About Longisa Hospital</h4>
#                 <p>We are dedicated to providing compassionate, accessible, and high-quality healthcare services to the people of Bomet County and surrounding regions under the Ministry of Health framework.</p>
#             </div>
#             <div class="footer-section">
#                 <h4>Quick Links</h4>
#                 <ul>
#                     <li>Ministry of Health Portal</li>
#                     <li>County Government of Bomet</li>
#                     <li>Universal Health Coverage Guidelines</li>
#                 </ul>
#             </div>
#             <div class="footer-section">
#                 <h4>Emergency Contact</h4>
#                 <p>Emergency Department: Open 24/7</p>
#                 <p>Ambulance Control Desk: +254 748 076 703</p>
#             </div>
#         </div>
#         <div class="footer-bottom">
#             &copy; 2026 Longisa County Referral Hospital. All Rights Reserved. Serving with the fear of God.
#         </div>
#     </div>
# """, unsafe_allow_html=True)

        with col_btn2:
            if st.button("About Us ➜", key="home_abt_btn"):
                set_route("About Us")
        st.write("")
        st.info("💡 **Quick Hotlinks Ready**\n\nNeed access parameters fast? Use the toggle menu navigation index or the Quick Access matrix panels configured directly below.")
    
    with intro_col2:
        st.markdown("##### 📸 Longisa Hospital Gallery View")
        view_mode = st.radio("Select Facility Perspective:", ["Main Campus Entrance", "Clinical Landscape View"], horizontal=True, label_visibility="collapsed")
        if view_mode == "Main Campus Entrance":
            st.image("https://res.cloudinary.com/jlengxni/image/upload/v1784047255/LONGISA_GATE_dvsoxw.jpg", caption="Longisa County Referral Hospital Main Entrance Hub", use_container_width=True)
        else:
            st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRJuT108ODLoq3JHa1rkyouIQpv2Nx4gXERs1FKkr7wuK69mfjDbvdnWhE0-8FxIV9JmXKzzGXTCM3M3aE", caption="Clinical Facility Infrastructures at Longisa", use_container_width=True)

    # Quick Access Section
    st.markdown("<h2 class='section-header'>⚡ Quick Access</h2>", unsafe_allow_html=True)
    q_col1, q_col2, q_col3 = st.columns(3, gap="medium")

    with q_col1:
        st.markdown("""
            <div class="card">
                <img class="card-img" src="https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRr8TWHOgz46NyUcx_nVJTdSq1-FYuDpGlqX34OHrt2DW5mt0cw1JqTQVD2tH21INlSJTtYiMj71irR-Bg" alt="Doctor advising patient">
                <div class="card-content">
                    <h4 style="color:#008080; margin-top:0;">👨‍⚕️ Find a Doctor</h4>
                    <p style='font-size:0.9rem; color:#444;'>Connecting you to trusted Doctors anytime, anywhere. Whether you need a routine check-up, specialist advice, or urgent care.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Search Doctors", key="qa_search_doc", use_container_width=True):
            set_route("Find a Doctor")
            
    with q_col2:
        st.markdown("""
            <div class="card">
                <img class="card-img" src="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcSQVZBWMrC9abAYU3MzC7K1j8r_voEL45OJ5tFuGs3GjHKAlE90PT8EAFyOvk5W5pieOhgN-oXaikNJZqo" alt="Stethoscope with passport and flight tickets">
                <div class="card-content">
                    <h4 style="color:#008080; margin-top:0;">🌍 Medical Tourism</h4>
                    <p style='font-size:0.9rem; color:#444;'>Discover our dedicated services for international patients, from travel assistance to world-class medical care. We're here to make your journey smooth.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Learn More", key="qa_tourism_learn", use_container_width=True):
            st.toast("Redirecting to International Health coordination systems...")
            
    with q_col3:
        st.markdown("""
            <div class="card">
                <img class="card-img" src="https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQYGBSd6Vnay0IGL7dcBRCFsbpKKCRMKUKA4iBE8T5K5GCnduWlMYpC-MPf5dZOizp6iiJGLVu8EnqgEyo" alt="Red map pin pinpointing hospital building">
                <div class="card-content">
                    <h4 style="color:#008080; margin-top:0;">📍 Getting to the Hospital</h4>
                    <p style='font-size:0.9rem; color:#444;'>We want your visit to be easy. Find directions, parking infrastructure arrays, and transport info on our Location system mapping panel.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Get Directions", key="qa_get_dirs", use_container_width=True):
            st.toast("Opening routing coordination pathways...")

    # Dynamic Outpatient Centers
    st.markdown("<h2 class='section-header'>🏢 Outpatient Centers</h2>", unsafe_allow_html=True)
    st.write("Learn more about our outpatient centers or choose a specific location.")
    
    oc_col1, oc_col2, oc_col3, oc_col4 = st.columns(4)
    with oc_col1:
        st.markdown("""<div class='center-card'><b>🏢 Anderson Specialty Centre</b><br><small>Argwings Kodhek Road, Anderson Centre, 1st Floor</small></div>""", unsafe_allow_html=True)
        st.markdown("""<div class='center-card'><b>🏢 Kiambu Mall</b><br><small>Kiambu Mall, 2nd Floor, Kiambu Road</small></div>""", unsafe_allow_html=True)
    with oc_col2:
        st.markdown("""<div class='center-card'><b>🏢 Capital Centre</b><br><small>Capital Centre, 1st floor, Mombasa Road</small></div>""", unsafe_allow_html=True)
        st.markdown("""<div class='center-card'><b>🏢 Rosslyn Riviera</b><br><small>Rosslyn Riviera Mall, 3rd Floor, Limuru Rd</small></div>""", unsafe_allow_html=True)
    with oc_col3:
        st.markdown("""<div class='center-card'><b>🏢 Chandaria A & E Centre</b><br><small>Main Hospital Complex Campus</small></div>""", unsafe_allow_html=True)
        st.markdown("""<div class='center-card'><b>🏢 Southfield Mall</b><br><small>Southfield Mall, 2nd Floor, Airport North Road</small></div>""", unsafe_allow_html=True)
    with oc_col4:
        st.markdown("""<div class='center-card'><b>🏢 Galleria Mall</b><br><small>Galleria Shopping Mall, 2nd Floor, Lang'ata Road</small></div>""", unsafe_allow_html=True)
        if st.button("Explore All Locations", key="exp_all_locs_btn"):
            st.toast("Fetching outpatient medical annex schedules...")

    # DYNAMIC NEWS SECTION
    st.markdown("<h2 class='section-header'>📰 Latest News & Updates</h2>", unsafe_allow_html=True)
    
    articles_list = st.session_state.articles
    if len(articles_list) > 0:
        cols = st.columns(min(len(articles_list), 3), gap="medium")
        for i, art in enumerate(articles_list[:3]):
            with cols[i % 3]:
                img_src = art.get('img') if art.get('img') else DEFAULT_NEWS_IMG
                st.markdown(f"""
                    <div class="news-card">
                        <img src="{img_src}" style="width:100%; height:150px; object-fit:cover; border-radius:8px; margin-bottom:12px;">
                        <div>
                            <div class="news-meta">📅 {art.get('date', 'Recent Update')}</div>
                            <div class="news-title">{art['title']}</div>
                            <div class="news-text">{art['content'][:120]}...</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("Read Full Story", key=f"read_home_art_{art['id']}", use_container_width=True):
                    set_route("Articles")
    else:
        st.info("No news updates posted yet.")

# --- TAB: FIND A DOCTOR ---
elif st.session_state.current_tab == "Find a Doctor":
    st.header("Our Specialists")
    st.write("Get to know our doctors and their areas of expertise.")
    
    st.markdown("### 🔍 Narrow your search")
    filter_col1, filter_col2 = st.columns(2)
    
    with filter_col1:
        search_name = st.text_input("By Doctor's Name", placeholder="Type name...")
    with filter_col2:
        specialties_list = ["All Specialties"] + list(set([d['spec'] for d in st.session_state.doctors]))
        search_spec = st.selectbox("By Specialty Clinic", specialties_list)
        
    st.markdown("##### Filter by First Name")
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    alpha_cols = st.columns(27)
    with alpha_cols[0]:
        if st.button("All", key="btn_all"):
            st.session_state.alpha_filter = "All"
    for idx, letter in enumerate(alphabet):
        with alpha_cols[idx + 1]:
            if st.button(letter, key=f"btn_{letter}"):
                st.session_state.alpha_filter = letter
                
    if st.button("Reset Filters", key="reset_all_filters"):
        st.session_state.alpha_filter = "All"
        st.rerun()
                
    if st.session_state.alpha_filter != "All":
        st.info(f"Showing results starting with letter: **{st.session_state.alpha_filter}**")
        
    st.markdown("---")
    
    filtered_docs = []
    for doc in st.session_state.doctors:
        if search_name and search_name.lower() not in doc['name'].lower():
            continue
        if search_spec != "All Specialties" and doc['spec'] != search_spec:
            continue
        clean_first_name = doc['name'].replace("Dr. ", "").strip()
        if st.session_state.alpha_filter != "All" and not clean_first_name.upper().startswith(st.session_state.alpha_filter):
            continue
            
        filtered_docs.append(doc)

    if len(filtered_docs) == 0:
        st.warning("No specialists match your selected filtration criteria.")
    else:
        for doc in filtered_docs:
            img_style = doc['img'] if isinstance(doc['img'], str) else DEFAULT_DOC_IMG
            
            st.markdown(f"""
            <div class="card">
                <div class="card-content">
                    <div class="doctor-flex">
                        <div class="doctor-avatar-container">
                            <img src="{img_style}" class="doctor-avatar">
                        </div>
