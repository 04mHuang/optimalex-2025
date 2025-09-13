from flask import Flask, request, render_template

app = Flask(__name__)

SITUATIONS = ["commercial auto", "general liability", "workers compensation"]
LEVELS = ["structure", "summarize"]
FILE_TYPES = ["medical records", "deposition", "summons", "summary report"]
VALID_PROMPTS = {
    # commercial auto, structure, summary report
    "Prompt 1": [
        SITUATIONS[0],
        LEVELS[0],
        FILE_TYPES[3],
    ],
    # general liability, summarize, deposition
    "Prompt 2": [
        SITUATIONS[1],
        LEVELS[1],
        FILE_TYPES[1],
    ],
    # commercial auto, summarize, summons
    "Prompt 3": [
        SITUATIONS[0],
        LEVELS[1],
        FILE_TYPES[2],
    ],
    # workers compensation, structure, medical records
    "Prompt 4": [
        SITUATIONS[2],
        LEVELS[0],
        FILE_TYPES[0],
    ],
    # workers compensation, summary, summons
    "Prompt 5": [
        SITUATIONS[2],
        LEVELS[1],
        FILE_TYPES[2],
    ],
}

@app.route("/")
def initialize():
    return render_template("index.html", valid_prompts=VALID_PROMPTS)

@app.route("/verify-prompt", methods=["POST"])
def verify_prompt():
    data = request.json
    # No checks on the actual data value (not specified)
    # Remove leading & trailing whitespace and turn into lowercase
    situation = data["situation"].strip().lower()
    level = data["level"].strip().lower()
    file_type = data["file_type"].strip().lower()
    try:
        if situation == "" or level == "" or file_type == "":
            return {"message": "Missing Data"}, 400
        # Check if request matches any of the valid prompts
        for key, prompt in VALID_PROMPTS.items():
            if (
                prompt[0] == situation
                and prompt[1] == level
                and prompt[2] == file_type
            ):
                # Return specific valid prompt
                return {"message": "Valid Prompt", "prompt": key, "details": prompt}, 200
        return {"message": "Invalid Prompt"}, 400
    except Exception as e:
        print(f"Error verifying prompt: {e}")
        return {"message": "Invalid Prompt"}, 400


if __name__ == "__main__":
    app.run(debug=True)
