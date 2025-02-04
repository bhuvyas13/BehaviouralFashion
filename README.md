# Behavioural Fashion API Documentation

## Overview
This project is a behavioural fashion system that suggests outfits based on user preferences, moods, activities, sustainability, and more. It allows users to maintain their profiles, track their moods, activities, seasonal preferences, and outfits, as well as manage a virtual wardrobe.

## API Endpoints

### Welcome Route
- **GET /**
  - Returns a welcome message for the API.
  - **Response:** `"Behavioural Fashion"`

---

### User Profile APIs

#### 1. **GET /users/<int:user_id>**
   - Retrieve a user's profile based on the `user_id`.
   - **Response:** JSON object containing user profile data.

#### 2. **POST /users**
   - Create a new user profile.
   - **Request Body:** JSON object containing user details.
   - **Response:** `"User profile created successfully"`

#### 3. **PUT /users/<int:user_id>**
   - Update an existing user profile.
   - **Request Body:** JSON object with updated user details.
   - **Response:** `"User profile updated successfully"`

#### 4. **DELETE /users/<int:user_id>**
   - Delete a user profile based on the `user_id`.
   - **Response:** `"User profile deleted successfully"`

---

### Mood and Fashion APIs

#### 1. **GET /users/<int:user_id>/mood**
   - Retrieve the current mood of the user based on the `user_id`.
   - **Response:** JSON object with the user's current mood.

#### 2. **POST /users/<int:user_id>/mood**
   - Update the user's current mood.
   - **Request Body:** JSON object containing the new mood.
   - **Response:** `"Mood updated successfully"`

#### 3. **GET /outfits/suggestions/mood/<mood>**
   - Get outfit suggestions based on the specified mood.
   - **Response:** JSON array containing outfits suitable for the given mood.

#### 4. **GET /outfits/<int:outfit_id>/mood**
   - Retrieve the moods associated with a specific outfit.
   - **Response:** JSON object containing moods.

#### 5. **POST /outfits/<int:outfit_id>/mood**
   - Link an outfit to a mood.
   - **Request Body:** JSON object with the mood to be linked.
   - **Response:** `"Outfit mood linked successfully"`

---

### Seasonal Fashion APIs

#### 1. **GET /users/<int:user_id>/seasonal-outfits**
   - Get seasonal outfit suggestions based on the user's seasonal preferences.
   - **Response:** JSON array of seasonal outfits.

#### 2. **PUT /users/<int:user_id>/seasonal-preference**
   - Update the user's seasonal preferences.
   - **Request Body:** JSON object with updated seasonal preferences.
   - **Response:** `"Seasonal preferences updated successfully"`

---

### Activity-Based Fashion APIs

#### 1. **GET /users/<int:user_id>/activity/<activity_type>/outfits**
   - Get outfit suggestions based on a specific activity type.
   - **Response:** JSON array of outfits suitable for the activity.

#### 2. **POST /users/<int:user_id>/activity**
   - Log a new activity for the user.
   - **Request Body:** JSON object containing activity details.
   - **Response:** `"Activity logged successfully"`

#### 3. **PUT /users/<int:user_id>/activity/<activity_type>**
   - Update an existing activity log.
   - **Request Body:** JSON object with updated activity details.
   - **Response:** `"Activity updated successfully"`

#### 4. **DELETE /users/<int:user_id>/activity/<activity_type>**
   - Delete an activity from the user's activity log.
   - **Response:** `"Activity deleted successfully"`

---

### Sustainability & Ethical Fashion APIs

#### 1. **GET /users/<int:user_id>/sustainable-fashion**
   - Retrieve the sustainable fashion choices made by the user.
   - **Response:** JSON array of eco-friendly choices.

#### 2. **POST /users/<int:user_id>/eco-friendly-item**
   - Log an eco-friendly item chosen by the user.
   - **Request Body:** JSON object containing eco-friendly item details.
   - **Response:** `"Eco-friendly item logged successfully"`

#### 3. **GET /fashion/sustainable-items**
   - Get a list of all sustainable fashion items available.
   - **Response:** JSON array of sustainable items.

#### 4. **PUT /users/<int:user_id>/sustainable-preferences**
   - Update the user's sustainable fashion preferences.
   - **Request Body:** JSON object with updated preferences.
   - **Response:** `"Sustainable preferences updated successfully"`

#### 5. **GET /outfits/sustainability/<int:outfit_id>**
   - Get the sustainability information of a specific outfit.
   - **Response:** JSON object containing sustainability data for the outfit.

---

### Virtual Wardrobe APIs

#### 1. **GET /users/<int:user_id>/wardrobe**
   - Retrieve the user's virtual wardrobe.
   - **Response:** JSON array of items in the user's virtual wardrobe.

#### 2. **POST /users/<int:user_id>/wardrobe**
   - Add a new item to the user's virtual wardrobe.
   - **Request Body:** JSON object containing wardrobe item details.
   - **Response:** `"Item added to wardrobe"`

#### 3. **PUT /users/<int:user_id>/wardrobe/<int:item_id>**
   - Update an item in the user's virtual wardrobe.
   - **Request Body:** JSON object with updated item details.
   - **Response:** `"Wardrobe item updated"`

#### 4. **DELETE /users/<int:user_id>/wardrobe/<int:item_id>**
   - Remove an item from the user's virtual wardrobe.
   - **Response:** `"Wardrobe item removed"`

#### 5. **GET /users/<int:user_id>/outfit-compatibility**
   - Check the compatibility of an outfit with items in the user's wardrobe.
   - **Request Parameters:** `outfit_id` (ID of the outfit to check).
   - **Response:** JSON array of compatible items from the wardrobe.

---

## File Structure

- `fashion.json`: Stores user and fashion data (outfits, moods, preferences, etc.).
- `fashion.py`: The main Python script containing Flask routes and logic.

---

## Notes
- All responses are in JSON format.
- Data is saved to the `fashion.json` file on the server.
