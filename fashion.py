from flask import Flask, request, jsonify
import json

app = Flask(__name__)

file = open("fashion.json")
fashion_data = json.load(file)

def save_data():
    with open("fashion.json", "w") as f:
        json.dump(fashion_data, f)

@app.route('/')
def welcome():
    return "Behavioural Fashion"

# User Profile APIs
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            return jsonify(user)
    return "User not found"

@app.route('/users', methods=['POST'])
def create_user_profile():
    data = request.json
    fashion_data["users"].append(data)
    save_data()
    return "User profile created successfully"

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            user.update(data)
            save_data()
            return "User profile updated successfully"
    return "User not found"

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_profile(user_id):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            fashion_data["users"].remove(user)
            save_data()
            return "User profile deleted successfully"
    return "User not found"

# Mood and Fashion APIs
@app.route('/users/<int:user_id>/mood', methods=['GET'])
def get_user_mood(user_id):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            return jsonify({"mood": user["mood"]})
    return jsonify({"error": "User not found"})

@app.route('/users/<int:user_id>/mood', methods=['POST'])
def set_user_mood(user_id):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            user["mood"] = data["mood"]  
            save_data()
            return "Mood updated successfully"
    return "User not found"

@app.route('/outfits/suggestions/mood/<mood>', methods=['GET'])
def get_outfits_by_mood(mood):
    suggested_outfits = []
    for outfit in fashion_data["outfits"]:
        if mood in outfit["recommended_for_moods"]:
            suggested_outfits.append(outfit)
    return jsonify(suggested_outfits)

@app.route('/outfits/<int:outfit_id>/mood', methods=['GET'])
def get_outfit_mood(outfit_id):
    for outfit in fashion_data["outfits"]:
        if outfit["id"] == outfit_id:
            return jsonify({"moods": outfit["recommended_for_moods"]})
    return "Outfit not found"

@app.route('/outfits/<int:outfit_id>/mood', methods=['POST'])
def link_outfit_to_mood(outfit_id):
    data = request.json
    for outfit in fashion_data["outfits"]:
        if outfit["id"] == outfit_id:
            outfit["recommended_for_moods"].append(data["mood"])
            save_data()
            return "Outfit mood linked successfully"
    return "Outfit not found"

# Seasonal Fashion APIs
@app.route('/users/<int:user_id>/seasonal-outfits', methods=['GET'])
def get_seasonal_outfits(user_id):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            seasonal_outfits = []
            for outfit in fashion_data["outfits"]:
                if any(season in user["seasonal_preference"] for season in outfit["recommended_for_moods"]):
                    seasonal_outfits.append(outfit)
            return jsonify(seasonal_outfits)
    return "User not found"

@app.route('/users/<int:user_id>/seasonal-preference', methods=['PUT'])
def update_seasonal_preference(user_id):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            user["seasonal_preference"] = data["preferences"] 
            save_data()
            return "Seasonal preferences updated successfully"
    return "User not found"

# Activity-Based Fashion APIs
@app.route('/users/<int:user_id>/activity/<activity_type>/outfits', methods=['GET'])
def get_outfits_for_activity(user_id, activity_type):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            activity_outfits = []
            for outfit in fashion_data["outfits"]:
                if activity_type in outfit["suitable_activities"]:
                    activity_outfits.append(outfit)
            return jsonify(activity_outfits)
    return "User not found"

@app.route('/users/<int:user_id>/activity', methods=['POST'])
def log_activity(user_id):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            user["activity_log"].append(data) 
            save_data()
            return "Activity logged successfully"
    return "User not found"

@app.route('/users/<int:user_id>/activity/<activity_type>', methods=['PUT'])
def update_activity(user_id, activity_type):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            for activity in user["activity_log"]:  
                if activity["activity"] == activity_type:
                    activity.update(data)
                    save_data()
                    return "Activity updated successfully"
    return "User not found"

@app.route('/users/<int:user_id>/activity/<activity_type>', methods=['DELETE'])
def delete_activity(user_id, activity_type):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            for activity in user["activity_log"]:  
                if activity["activity"] == activity_type:
                    user["activity_log"].remove(activity)
                    save_data()
                    return "Activity deleted successfully"
    return "User not found"

# Sustainability & Ethical Fashion APIs
@app.route('/users/<int:user_id>/sustainable-fashion', methods=['GET'])
def get_sustainable_fashion(user_id):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            return jsonify(user["eco_friendly_choices"])
    return "User not found"

@app.route('/users/<int:user_id>/eco-friendly-item', methods=['POST'])
def log_eco_friendly_item(user_id):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            user["eco_friendly_choices"].append(data)
            save_data()
            return "Eco-friendly item logged successfully"
    return "User not found"

@app.route('/fashion/sustainable-items', methods=['GET'])
def get_sustainable_items():
    return jsonify(fashion_data["sustainable_items"])

@app.route('/users/<int:user_id>/sustainable-preferences', methods=['PUT'])
def update_sustainable_preferences(user_id):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            user["sustainable_preferences"] = data["preferences"]
            save_data()
            return "Sustainable preferences updated successfully"
    return "User not found"

@app.route('/outfits/sustainability/<int:outfit_id>', methods=['GET'])
def get_outfit_sustainability(outfit_id):
    for outfit in fashion_data["outfits"]:
        if outfit["id"] == outfit_id:
            return jsonify({"sustainability": outfit["sustainability"]})
    return "Outfit not found"

# Virtual Wardrobe APIs
@app.route('/users/<int:user_id>/wardrobe', methods=['GET'])
def get_virtual_wardrobe(user_id):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            return jsonify(user["virtual_wardrobe"])  
    return "User not found"

@app.route('/users/<int:user_id>/wardrobe', methods=['POST'])
def add_item_to_wardrobe(user_id):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            user["virtual_wardrobe"].append(data) 
            save_data()
            return "Item added to wardrobe"
    return "User not found"

@app.route('/users/<int:user_id>/wardrobe/<int:item_id>', methods=['PUT'])
def update_wardrobe_item(user_id, item_id):
    data = request.json
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            for item in user["virtual_wardrobe"]:  
                if item["item_id"] == item_id:
                    item.update(data)
                    save_data()
                    return "Wardrobe item updated"
    return "User or item not found"

@app.route('/users/<int:user_id>/wardrobe/<int:item_id>', methods=['DELETE'])
def remove_item_from_wardrobe(user_id, item_id):
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            for item in user["virtual_wardrobe"]:  
                if item["item_id"] == item_id:
                    user["virtual_wardrobe"].remove(item)
                    save_data()
                    return "Wardrobe item removed"
    return "User or item not found"

@app.route('/users/<int:user_id>/outfit-compatibility', methods=['GET'])
def check_outfit_compatibility(user_id):
    data = request.args
    outfit_id = data.get("outfit_id")
    for user in fashion_data["users"]:
        if user["id"] == user_id:
            for outfit in fashion_data["outfits"]:
                if outfit["id"] == int(outfit_id):
                    compatible_items = []
                
                    for item in user["virtual_wardrobe"]:
                        if any(color in item["colors"] for color in outfit["colors"]) or outfit["style"] == item["style"]:
                            compatible_items.append(item)
                    return jsonify(compatible_items)
    return "User or outfit not found"


if __name__ == '__main__':
    app.run(debug=True)
