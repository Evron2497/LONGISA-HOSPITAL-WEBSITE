from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    # Increased to 255 to safely handle all emoji variants
    icon = Column(String(255), nullable=True) 
    description = Column(Text, nullable=False)

def init_db():
    # 1. Create tables first
    Base.metadata.create_all(bind=engine)
    # 2. Then seed
    seed_departments()

def seed_departments():
    db = SessionLocal()
    try:
        if db.query(Department).first() is not None:
            return  
        
        ui_departments = [
            {"name": "Outpatient Department (OPD)", "icon": "🏥", "description": "Providing quick consultations, diagnostics, and preventative services 24 hours a day for non-admitted clinical patients."},
            {"name": "Paediatrics & Neonatology", "icon": "👶", "description": "Dedicated medical care tailored specifically for infants, children, and adolescents, featuring advanced incubator-equipped nurseries."},
            {"name": "Internal Medicine", "icon": "🩺", "description": "Diagnosing, treating, and managing complex chronic diseases of internal organs in adults, led by expert consultant physicians."},
            {"name": "Laboratory Medicine", "icon": "🧪", "description": "24/7 high-volume chemical pathology, hematology, microbiology, and PCR testing infrastructure delivering rapid, exact diagnostic answers."},
            {"name": "Inpatient Department (IPD)", "icon": "🛏️", "description": "Providing 24/7 comprehensive inpatient services across dedicated Male, Female, and Surgical wards under continuous professional nursing care."},
            {"name": "Accident & Emergency (A&E)", "icon": "🚨", "description": "A highly responsive trauma center equipped to handle life-threatening situations, critical care rescues, and emergency ambulance drop-offs."},
            {"name": "Obstetrics & Gynaecology", "icon": "🤰", "description": "Comprehensive maternal care, modern delivery rooms, family planning, and specialized gynecological surgeries."},
            {"name": "General & Specialized Surgery", "icon": "✂️", "description": "Fully equipped state-of-the-art operating theatres handling major laparoscopic, orthopedic, and general surgical operations."},
            {"name": "Pharmacy Services", "icon": "💊", "description": "In-house pharmacy network stocked with Ministry of Health certified therapeutics, dispensing medications under strict clinical protocols."},
            {"name": "Intensive Care Unit (ICU) & HDU", "icon": "🫁", "description": "Advanced life-support technology and continuous multi-system monitoring for critically ill patients, staffed by specialized intensivists."},
            {"name": "Radiology & Diagnostic Imaging", "icon": "🩻", "description": "Equipped with multi-slice CT, high-definition ultrasound, digital x-ray, and mammography systems to aid in non-invasive diagnoses."},
            {"name": "Dental & Maxillofacial Surgery", "icon": "🦷", "description": "From general oral health cleanings and tooth restorations to complex structural maxillofacial reconstructive operations."},
            {"name": "Renal Unit (Dialysis Center)", "icon": "🫘", "description": "Providing advanced hemodialysis therapies for acute kidney injuries and end-stage renal failure patients overseen by expert nephrologists."},
            {"name": "Comprehensive Care Centre (CCC)", "icon": "🎗️", "description": "Supporting patients with chronic illnesses, infectious disease counseling, oncological therapies, and psychological support services."},
            {"name": "Physiotherapy & Rehab", "icon": "🏃", "description": "Restoring movement and physical function through targeted therapeutic exercise, manual therapy, and customized rehabilitation regimens."}
        ]

        db.bulk_insert_mappings(Department, ui_departments)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()