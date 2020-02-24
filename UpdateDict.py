 NEW API to update the existing json file
# Current dictionaries is dictionaries.json
# This fuction is to check if new dict are identical to the current dict then nothing were updated
# if there is new values added in new dict, then it replace current dict with the new value


import json
from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

update =[]
def update_dict(old,new):
    for i in new:
        if i not in (old):
            update = old
            update.append(i)
    return update



@app.route('/update-dictionary', methods=['POST'])
def printDiffs():
    with open('dictionaries.json', 'r') as file:
        x = json.load(file)
    if request.method == 'POST':
        
        y = request.json
        diff = False
        for x_key in x:
            if x_key not in y:
                diff = True
            elif x[x_key] != y[x_key]:
                diff = True
                ans = update_dict(x[x_key], y[x_key])

                print("dictionaries.json were UPDATED")
                
        if not diff:
            return "both files are identical- nothing updated"
        
        with open('dictionaries.json', 'w') as new:
            json.dump(x, new, ensure_ascii=False, sort_keys=True)
        return jsonify(x)
    

        
if __name__ == '__main__':
    # Only for debugging while developing
    app.run(debug=False, host='0.0.0.0', port=8080)
#result =printDiffs(x,y)       
