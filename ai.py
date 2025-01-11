import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
load_dotenv()

def gen():
  link="https://www.instagram.com/p/DDg-LBevuYq/"
  api_key = os.getenv("KEY")
  genai.configure(api_key=api_key)
  myfile = genai.upload_file("deion.mp3")
  model = genai.GenerativeModel("gemini-1.5-flash")
  var = """
  You are transcribing and structuring audio content for a micro-content platform that delivers bite-sized updates on the latest events, social gatherings, new food places, cafes, and more. The platform is tailored for quick consumption, offering curated, 60-word summaries and visually engaging content for on-the-go users.  
  translate the audio to english if it is not in english if the audio is purely music then ignore transcribing
  Your task is to transcribe the audio, identify if it is about an event, place, or gathering, and format the information into a JSON structure. If the content is not relevant (i.e., not about an event, place, or gathering), skip it and provide no output.  

  ### Guidelines for Relevant Content:  
  1. **Title**: Generate a concise and catchy title that summarizes the event.  
  2. **Description**: Write a short, engaging description (around 60 words) of the event, including key details and highlights.  
  3. **Category**: Create classification of the event, category putting into different categories (must all be in pure lowercase) (category is enum(‘event’, ‘place’, ‘restaurant’))
  4. **Offers**: If the event includes any offers (e.g., discounts, complimentary items), list them.  

  ### Python dictionary Output Format:  
  Ensure the output always follows this structure:  

  {
    "title": "Event title here",
    "description": "Engaging 60-word summary here",
    "category": "Event category here",
    "sub_category": "Event sub-category here",
    "tags": ["Tag 1", "Tag 2"],
    "offers": ["Offer 1", "Offer 2"],
    "link":"https://www.instagram.com/reel/DAX7RlLi7jO/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="
  }

  """
  # Generate content
  result = model.generate_content([myfile, var])
  try:
      # Log the raw result
      #print("Raw result text:", repr(result.text))
      
      # Strip Markdown-like formatting and whitespace
      
      clean_text = result.text.strip("```json\n").strip("```").strip()
      # Add the link parameter to the JSON
      clean_text = clean_text.rstrip("}") +","+ f'\n  "link": "{link}"\n' +  "\n"'}'
      
      # Parse the cleaned JSON
      result = json.loads(clean_text)
      
      # Print the JSON object
      return result
  except json.JSONDecodeError as e:
      print("Error parsing JSON:", e)

if __name__ == "__main__":
    gen()