import pdfplumber
import sys
import os
sys.path.append(os.path.abspath('../Llama'))
import edit

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

pdf_path = '../data/EllaGreenResume.pdf'
text = extract_text_from_pdf(pdf_path)

with open('EllaGreen.txt', 'w') as file:
    file.write(text)

job_description = (
    "We are seeking a Frontend Engineer skilled in modern JavaScript frameworks, "
    "with experience in building responsive web applications and collaborating with UX/UI teams."
)

job = (
   """Responsibilities:
  6-10 years of experience in Financial Services preferred
 Global Project Management experience preferred
 Ability to work under pressure and manage deadlines or unexpected changes in expectations or requirements
 Proven organizational and time management skills""")

res = (
    """A finance professional, I am deeply passionate about understanding
macro as well as the micro aspects affecting corporate finances.
I have engaged in providing equity fund raising, debt syndication,
M&A and investor relations services to 50+ companies across
sectors including Healthcare, Life Sciences, Energy, Industrials,
Consumer and Technology.
My 6+ years of experience across Investor Relations, Investment
Banking and Corporate Finance Advisory helped me develop
competencies including business storytelling, which is my key
professional interest area, and problem-solving, which energizes me
emotionally.
An MBA from UNC Kenan-Flagler Business School (Ranked 19th
Best Business School, US News, 2018), I have extensive experience
in business and strategy analysis, financial modelling, stock price
analysis, team management, investor communication and event
management, and pitch material presentation. 
I believe that knowledge, ability to communicate effectively, humility
and integrity are the primary ingredients of, what truly is, the net
worth of an individual.  """)

result = edit.tailor_resume(res, job)

#print(' ')
print(result['response'])

