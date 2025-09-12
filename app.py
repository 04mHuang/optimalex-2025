from flask import Flask, request, render_template

app = Flask(__name__)

SITUATIONS = ["commercial auto", "general liability", "workers compensation"]
LEVELS = ["structure", "summarize"]
FILE_TYPES = ["medical records", "deposition", "summons", "summary report"]
VALID_PROMPTS = {
  "Prompt 1": [SITUATIONS[0], LEVELS[0], FILE_TYPES[3]], # commercial auto, structure, summary report
  "Prompt 2": [SITUATIONS[1], LEVELS[1], FILE_TYPES[1]], # general liability, summarize, deposition
  "Prompt 3": [SITUATIONS[0], LEVELS[1], FILE_TYPES[2]], # commercial auto, summarize, summons
  "Prompt 4": [SITUATIONS[2], LEVELS[0], FILE_TYPES[0]], # workers compensation, structure, medical records
  "Prompt 5": [SITUATIONS[2], LEVELS[1], FILE_TYPES[2]] # workers compensation, summary, summons
}

@app.route("/")
def initialize():
  return render_template("index.html")

@app.route("/verify-prompt", methods=["POST"])
def verify_prompt():
  data = request.json
  return { "verification": data }, 200

if __name__ == "__main__":
  app.run(debug=True)
  
