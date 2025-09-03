#we have to add first the root dir to the system path so that Python is aware of where to find your modules
import sys
from pathlib import Path

# Get the absolute path of the codebase folder
CODEBASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = CODEBASE_DIR.parent 

# Add ROOT_DIR to sys.path so imports work
sys.path.append(str(ROOT_DIR))

#importing the libraries from lib.py
from utils.lib import convert_from_path, pyt, re, pd, file_id

class PdfExtractor:
    def text_extractor(self, input_pdf, outputpath):
        # Read in the PDF file at 500 DPI
        pdf_pages = convert_from_path(input_pdf, 500)

        #store all the pages of the pdf in a variable
        image_file_list = pdf_pages    

        #loop the saved images in image_file_list
        for image_file in image_file_list:
            img = image_file.convert('RGB')
            text = str(pyt.image_to_string(img))

        #splitting the strings on \n and |
        text_list = re.split(r'\n|\|', text)

        #remove empty value
        text_list = [x.strip() for x in text_list if x != '']

        #---------------------- details extraction ---------------------------

        #extract school
        school = text_list[1]

        #extract name 
        for txt in text_list:
            #name
            name_match = re.search(r'Name:\s*(.*)', txt)
            if name_match:
                name = name_match.group(1)
                name = name.replace(',', '')

            #date of birth
            #string = 'Date of Birth: AUGUST 31, 2000 wT Gender: MALE'
            dob_match = re.search(r"(Date of Birth: (.*?))(?: wT|$)", txt)
            if dob_match:
                dob = dob_match.group(2).strip()

            #place of birth
            pob_match = re.search(r"Place of Birth:\s(.*)", txt)
            if pob_match:
                pob = pob_match.group(1)

            #address
            address_match = re.match(r"^Address:\s(.*)", txt)
            if address_match:
                address = address_match.group(1)

            #date of claim
            date_claimed_match = re.match(r"^Date:\s(.*)", txt)
            if date_claimed_match:
                date_claimed = date_claimed_match.group(1)
                
            #gender
            a = re.search(r"Date of Birth: .*", txt)
            if a:
                a = a.group(0)
                gender_match = re.search(r"Gender: (.*)", a)
                gender = gender_match.group(1)

            #parent
            parent_match = re.search(r"Parent/Guardian: (.*?)(?: Address|$)", txt)
            if parent_match:
                parent = parent_match.group(1)
            
            #entrance credentials
            entrance_cred_match = re.search(r"Entrance Cred.: (.*?)(?: School|$)", txt)
            if entrance_cred_match:
                entrance_cred = entrance_cred_match.group(1)
            
            #date of admission
            dateof_add_match = re.search(r"Date of Admission: (.*?)(?: Date |$)", txt)
            if dateof_add_match:
                dateof_addmission = dateof_add_match.group(1)

            #degree
            degree_match = re.search(r"Degree/Curriculum: (.*)", txt)
            if degree_match:
                degree = degree_match.group(1).replace(')','').strip()

            #major
            major_match = re.search(r"Major: (.*?)(?: |$)", txt)
            if major_match:
                major = major_match.group(1)
            
            #minor
            minor_match = re.search(r"Minor: (.*)", txt)
            if minor_match:
                minor = minor_match.group(1)

        #---------------------- dataframe ---------------------------
        #making dataframe
        df = pd.DataFrame({'SCHOOL' : [school],
                   'NAME' : [name],
                   'DATE OF BIRTH' : [dob],
                   'PLACE OF BIRTH' : [pob],
                   'ADDRESS' : [address],
                   'DATE CLAIMED' : [date_claimed],
                   'GENDER' : [gender],
                   'PARENT' : [parent],
                   'ENTRANCE CREDENTIALS' : [entrance_cred],
                   'DATE OF ADMISSION' : [dateof_addmission],
                   'DEGREE' : [degree],
                   'MAJOR' : [major],
                   'MINOR' : [minor]})
        df = df.replace(r"[,-.]", "", regex=True)

        #export to csv
        df.to_csv(rf'{outputpath}\result_{file_id}.csv', index=False, sep='|')


