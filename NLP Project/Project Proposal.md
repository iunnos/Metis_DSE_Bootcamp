## Question
- My project will look use Yelp's 2019 dataset to create a model that helps people find likeminded (or people with differing opinions) individuals based on the reviews left on Yelp.
- This could be applicable to people interested in creating their own web-application looking to connect people in different ways

## Data Description
- The (Yelp Dataset)[yelp.ca/dataset] contains 5 different JSONs of data. I'll be using 3 of them, Business, Reviews, and Users.
- The Business dataset contains 150346 rows and 13 columns. Each row represents 1 business and stores the business_id (Yelp's unique identifier for the business), name (the business name), address (street business address), city, state, postal_code, latitude, longitude, stars (star rating of the business out of 5, it's a float value), review_count(the number of reviews left), is_open (0 or 1 for closed or open), attributes (attributes tagged to the business such as parking, takeout, use of credit cards, etc.), categories (list of categorical tags the business falls under), and hours
- The Review  dataset contains 6990280 and 9 columns. Each row represents 1 review and stores the review_id (Yelp's unique identifier for that specific review), user_id (unique identifier for users), business_id (unique identifier of the business that the review was left for), star (float rating of business out of 5), useful (number of times the review was rated as useful by other users), funny (number of times the review was rated as funny by other users), cool (number of times the review was rated as cool by other users), text (the review), and date.
- The User dataset contains 1987897 rows and 22 columns. Each row represents 1 user and stores user_id (unique identifier for users), name (user's first name), review_count (number of reviews written), yelping_since, useful (number of times their review have been rated useful), funny (number of times their review have been rated funny), cool (number of times their review have been rated cool), elite (Yelp elite status since, meaning they left a lot of quality reviews), friends (list of user_ids that user is friends with on Yelp), fans (number of people following the user), average_stars (float average rating that the user leaves out of 5). The next 11 columns are basically types of comments left on a User's page and the tag associated to those comments. There are 11 tags in this dataset : hot stuff (compliment_hot), write more (compliment_more), like your profile (compliment_profile), cute pic (compliment_cute), great lists (compliment_list), just a note (compliment_note), thank you (compliment_plain), you're cool (compliment_cool), you're funny (compliment_funny), good writer (compliment_writer), great photo (compliment_photos)
- From the business dataset I'll likely use business_id, name, address, city, state, star, review_count, and categories
- From the review dataset I'll likely use review_id, user_id, business_id, star, and text
- From the user dataset I'll likely use user_id, review_count, and average_stars

## Tools
- Core tools: Pandas, NLTK, scikit-learn, clustering, dimentionality reduction, topic modeling
- Time permitting I'll create a web-app with Streamlit

## MVP Goal:
- Complete initial text processing of reviews most likely for tone and sentiment and complete initial clustering of users and the reviews left based on dimension reduced data of business categories and review sentiments