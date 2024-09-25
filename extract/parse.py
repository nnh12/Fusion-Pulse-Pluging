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

res = (
    """•Collaborated on the development of a management system which reduced
Proactive approach led to the development of
bug fix times by 20%.
a new tracking system for tutoring
• Assisted in the maintenance and improvement of company codebase,
appointments, increasing efficiency by 35%.
leading to a 15% increase in efficiency.
• Utilized analytical skills in solving technical issues, resulting in a 30%
reduction in client complaints.""")

result = edit.tailor_resume(res, job_description)

#print(' ')
print(result['response'])

