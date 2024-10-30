# systemUsers/utils.py
import pandas as pd

from main_setting.models import AcademicYear, Class, Programme, Term
from admission.models import EntryCategory
from admission.models import Sponsor
from admission.models import StudentRegistration
# from main_setting.models import StudentRegistration, AcademicYear, Term, Programme, Class, EntryCategory, Sponsor

# from main_setting.models import AcademicYear, Class, Programme, Term

def import_students_from_file(file_path):
    # Detect file type and load data
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are allowed.")

    for _, row in data.iterrows():
        # Get or create related objects (foreign key fields)
        academic_year = AcademicYear.objects.get_or_create(name=row['entry_year'])[0]
        term = Term.objects.get_or_create(name=row['entry_term'])[0]
        programme = Programme.objects.get_or_create(name=row['entry_programme'])[0]
        class_name = Class.objects.get_or_create(name=row['entry_class'])[0]
        entry_category = EntryCategory.objects.get_or_create(name=row['entry_category'])[0]
        sponsor = Sponsor.objects.get_or_create(name=row['sponsor_name'])[0]

        # Create the StudentRegistration object
        StudentRegistration.objects.create(
            entry_year=academic_year,
            entry_term=term,
            entry_programme=programme,
            entry_class=class_name,
            entry_category=entry_category,
            sponsor_name=sponsor,
            registration_number=row['registration_number'],
            first_name=row['first_name'],
            last_name=row['last_name'],
            other_name=row.get('other_name', ''),
            gender=row['gender'],
            birth_date=row['birth_date'],
            nationality=row.get('nationality', 'Tanzania'),
            disability=row.get('disability', 'none'),
            next_of_kin1_name=row['next_of_kin1_name'],
            next_of_kin1_mobile_number=row['next_of_kin1_mobile_number'],
            next_of_kin1_email=row.get('next_of_kin1_email', ''),
            next_of_kin1_postal_address=row.get('next_of_kin1_postal_address', ''),
            next_of_kin2_name=row.get('next_of_kin2_name', ''),
            next_of_kin2_mobile_number=row.get('next_of_kin2_mobile_number', ''),
            next_of_kin2_email=row.get('next_of_kin2_email', ''),
            next_of_kin2_postal_address=row.get('next_of_kin2_postal_address', ''),
        )
