import requests
import json
import pandas as pd

def tailor_resume(responsibilities, job_description, model="llama3"):
    url = 'http://localhost:11434/api/generate'
    headers = {'Content-Type': 'application/json'}

    # Craft the prompt for tailoring the resume responsibilities
    prompt = (
        "Modify the following text to tailor to job description:\n\n"
        f"Job Description: '{job_description}'\n\n"
        f"Text:\n{responsibilities}\n\n"
        "Tailored Responsibilities:"
    )

    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Attempt to parse the JSON response
    try:
        return response.json()
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return None

# Example usage for a Frontend Engineer position
job = (
   """ 6-10 years of experience in Financial Services preferred
 Global Project Management experience preferred
 Ability to work under pressure and manage deadlines or unexpected changes in expectations or requirements
 Proven organizational and time management skills""" 
)

resume = (
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
emotionally."""
)

if __name__ == "__main__":
    df = pd.read_excel('Fusion_test_log.xlsx')
    res = []
    for index, row in df.iterrows():
        job_description = row['Job Description']
        resume = row['Resume']
        result = tailor_resume(resume, job_description)
        res.append(result['response'])

    df['Output'] = pd.Series(res).astype(str)
    df.to_excel('Fusion_test_log.xlsx', index=False)
    print(df['Output'])
