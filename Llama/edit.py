import requests
import json

def tailor_resume(responsibilities, job_description, model="llama3"):
    url = 'http://localhost:11434/api/generate'
    headers = {'Content-Type': 'application/json'}

    # Craft the prompt for tailoring the resume responsibilities
    prompt = (
        "Modify the following resume responsibilities to align with the job description:\n\n"
        f"Job Description: '{job_description}'\n\n"
        f"Current Responsibilities:\n{responsibilities}\n\n"
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
responsibilities = (
    "• Developed web applications using HTML, CSS, and JavaScript.\n"
    "• Collaborated with designers to implement responsive user interfaces.\n"
    "• Conducted code reviews and maintained code quality."
)

job_description = (
    "We are seeking a Frontend Engineer skilled in modern JavaScript frameworks, "
    "with experience in building responsive web applications and collaborating with UX/UI teams."
)

result = tailor_resume(responsibilities, job_description)
print(result['response'])

