from flask import Flask, render_template
import urllib.request,json, ssl

app = Flask(__name__)

@app.route("/")
def get_list_page():
      url = "https://rickandmortyapi.com/api/character/"
      context = ssl._create_unverified_context()
      response = urllib.request.urlopen(url, context=context)
      data = response.read()
      dict = json.loads(data)
      
      return render_template("characters.html", characters = dict["results"])
  
@app.route("/profile/<id>")
def get_profile(id):
      url = "https://rickandmortyapi.com/api/character/" + id 
      context = ssl._create_unverified_context(url)
      response = urllib.request.urlopen(url, context=context)
      data = response.read()
      dict = json.loads(data)
      
      return render_template("profile.html", profile=dict)
  
@app.route("/lista")
def get_list_characters():
    
    try:
        url = "https://rickandmortyapi.com/api/character/"
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, context=context)
        characters = response.read()
        dict = json.loads(characters)

        characters = [] 
    
        for character in dict["results"]:
         character = {
            "name": character["name"],
            "status": character["status"]
        }
        
        characters.append(character)
        
        
        return {"characters": characters}

    except Exception as e:  
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(debug=True)