import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
load_dotenv()

def gen():
  api_key = os.getenv("KEY")
  genai.configure(api_key=api_key)
  myfile = genai.upload_file("reel.mp3")
  model = genai.GenerativeModel("gemini-1.5-flash")
  var = """
  You are transcribing and structuring audio content for a micro-content platform that delivers bite-sized updates on the latest events, social gatherings, new food places, cafes, and more. The platform is tailored for quick consumption, offering curated, 60-word summaries and visually engaging content for on-the-go users.  

  Your task is to transcribe the audio, identify if it is about an event, place, or gathering, and format the information into a JSON structure. If the content is not relevant (i.e., not about an event, place, or gathering), skip it and provide no output.  

  ### Guidelines for Relevant Content:  
  1. **Title**: Generate a concise and catchy title that summarizes the event.  
  2. **Description**: Write a short, engaging description (around 60 words) of the event, including key details and highlights.  
  3. **Category**: Create classification of the event, category putting into different categories  
  4. **Offers**: If the event includes any offers (e.g., discounts, complimentary items), list them.  

  ### Python dictionary Output Format:  
  Ensure the output always follows this structure:  

  {
    "title": "Event title here",
    "description": "Engaging 60-word summary here",
    "category": "Event category here",
    "sub_category": "Event sub-category here",
    "tags": ["Tag 1", "Tag 2"],
    "offers": ["Offer 1", "Offer 2"]
  }

  """
  # Generate content
  result = model.generate_content([myfile, var])
  try:
      # Log the raw result
      #print("Raw result text:", repr(result.text))
      
      # Strip Markdown-like formatting and whitespace
      clean_text = result.text.strip("```json\n").strip("```").strip()
      
      # Parse the cleaned JSON
      result = json.loads(clean_text)
      
      # Print the JSON object
      #print(result)
      return result
  except json.JSONDecodeError as e:
      print("Error parsing JSON:", e)

if __name__ == "__main__":
    gen()