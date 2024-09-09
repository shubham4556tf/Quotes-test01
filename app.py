from flask import Flask, jsonify, request, render_template

app = Flask(__name__,template_folder = 'templates')

# Dictionary of quotes by author
quotes = {
    "Albert Einstein": "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
    "Aristotle": "We are what we repeatedly do. Excellence, then, is not an act, but a habit.",
    "Abraham Lincoln": "Whatever you are, be a good one.",
    "Alexander Graham Bell": "When one door closes, another opens; but we often look so long and so regretfully upon the closed door that we do not see the one which has opened for us.",
    "Anne Frank": "How wonderful it is that nobody need wait a single moment before starting to improve the world.",
    "Amitabh Bachchan": "Bad luck either destroys you or makes you the man you really are.",
    "A.P.J. AbdulKalam": "Dream, dream, dream. Dreams transform into thoughts, and thoughts result in action.",
    "Ada Lovelace": "That brain of mine is something more than merely mortal, as time will show.",
    "Audrey Hepburn": "Nothing is impossible, the word itself says 'I'm possible'!",
    "Aldous Huxley": "Experience is not what happens to you; it's what you do with what happens to you.",
}

# Quotes and images for personal authors
author_quotes = {
    "alberteinstein": ["Imagination is more important than knowledge.", 'static.image.jpg'],
    "mahatmagandhi": [],
    "nelsonmandela": [],
    "abigailadams":[],
  
        
}

# Home route displaying quotes
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', quotes=quotes)

# Route to count (not sure if required based on the context provided)
@app.route("/", methods=['POST'])
def count():
    i = range(1, 101)
    return render_template('index.html', i=i)

# Route for searching quotes
@app.route("/data", methods=['GET'])
def search_quotes():
    query = request.args.get("query_html", "").lower()  # Convert query to lowercase
    if query:
        # Convert keys to lowercase for case-insensitive match
        matching_key = next((key for key in quotes if key.lower() == query), None)
        if matching_key:
            quote = quotes[matching_key]
            
            return jsonify({matching_key.replace(" ", "").lower(): quote})  # Return lowercase ID
        else:
            return jsonify({"error": "Quote not found!"})
    return jsonify({"error": "No query parameter provided"}), 400

# Route for personal author quotes page
@app.route("/author/<id>", methods=['GET'])
def authorPage(id):
    id = id.lower()  # Convert ID to lowercase for matching
    qt = author_quotes.get(id)
    if qt:
        return render_template('author.html', qt=qt, id=id)
    else:
        return render_template('author.html', qt=[], id=id)
    
    
#suggesgtion 
@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('query', '').lower()
    suggestions = [name for name in quotes.keys() if query in name.lower()]
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
