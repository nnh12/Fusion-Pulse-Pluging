import re
import requests
import json
import pandas as pd
from find_words.find import no_vid
import os

labels = [ "No video", "Fan noise", "Autoshutdown issue", "No post", "Game crash",
           "No power", "Video distortion", "GPU fan", "Miscellaneous", "Multi display",
           "Video output port", "Operating System", "No boot"]  

test = [ "H57JF24" , "3DWB144", "7QPYL44", "F9XKY24", "BVC4M34",
         "2H6R244" , "4NCYV34", "BVC4M34", "7RRVY24", "HZQCN34",
         "CBXP144", "514JF24" , "GM73724", "F9XKY24", "FSQVC14",
         "CKXX624", "GJ99K44", "62Q8S14", "B37GX34", "C5GQ144",
         "80RCN34", "7VNVY24", "9DNXT34", "7N99K44", "JFQZW34"]

correct_test = ["DLSY624", "F13T624", "CWLMR14", 
                "3Z9QC14", "F13T624",
                "JFJ0G24", "4ZZ6D14", "30J1G24", "HVWD724",
                "3PMVC14", "1P0QC14", "HVWD724"]

correct_test2 = ["4S92G24", "2P3LY24", "80T7234",
                 "FSQF724", "G649Z24", "80RVY24",
                 "1VZHZ24", "2P3LY24", "3SS1S14"] 

correct_test3 = ["JXV9X04", "DRPYL44","46KTW14", "7RP7724"]

correct_test4 = ["6GVKY24", "7W8BZ24", "H57JF24", "7RRVY24",
                 "FSQVC14", "C5GQ144", "JFQZW34"]

def generate_response(prompt, model="llama3"):
    url = 'http://localhost:11434/api/generate'
    headers = {'Content-Type': 'application/json'}
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

def create_summary(text):   
    prompt = text + "\n Extract key words"
    response = generate_response(prompt)    
    return response['response']

def extract_contactext(file_path, sheet_name, search_string):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    col = df['Service Tag']
    row_string = df[df['Service Tag'].str.contains(search_string, na=False, case=False)]
    row_indices = row_string.index.tolist()
    text = df['Contact Text'].iloc[row_indices[0]] 
    return text

def add_results(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    filtered_df = df[df['Service Tag'].isin(test)]
    filtered_df.to_excel('filtered_file.xlsx', index=False)   

def add_labels(tags, labels):
    data = {'A': tags, 'B': labels}
    df = pd.DataFrame(data)
    os.makedirs('find_words', exist_ok=True)
    file_path = os.path.join('find_words', 'output.xlsx')
    
    with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)

if __name__ == '__main__':    
   print("Original Sentences: Led feature development for social media creation app, web, backend. Implemented CI/CD pipeline")
   print(" ")   

   print("AI Feedback to tailor to frontend role: ")
   prompt = "revise this sentence to emphasize frontend skill: 'Led feature development for flagship social media creation app, web and backened. Implemented CI/CD pipleines'"
   res = generate_response(prompt)
   print(res['response'])
