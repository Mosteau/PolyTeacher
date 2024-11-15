import google.generativeai as genai


# configuration de gimini IA pour l'application DJANGO Python
# configuration de la clef API
api_key=""
genai.configure(api_key=api_key)

# génération de texte
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Comment on dit manger en anglais ?")
print(response.text)
