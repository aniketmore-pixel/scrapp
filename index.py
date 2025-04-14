from app import app as application

from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes', methods=['POST'])
def recipes():
    ingredients = request.form['ingredients']
    query = '+'.join(ingredients.split(','))
    search_url = f"https://www.allrecipes.com/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    recipe_cards = soup.select('div.card__content')
    recipes_data = []

    for card in recipe_cards[:5]:
        try:
            title_tag = card.select_one('span.card__title-text')
            link_tag = card.find_parent('a')
            img_tag = card.find_previous('img')
            
            # Extracting the rating stars and the rating count
            rating_tag = card.select_one('div.mntl-recipe-star-rating')
            rating_count_tag = card.select_one('div.mntl-recipe-card-meta__rating-count-number')

            title = title_tag.get_text(strip=True) if title_tag else 'No title'
            link = link_tag['href'] if link_tag else '#'
            image = img_tag['src'] if img_tag and 'src' in img_tag.attrs else ''

            # Calculate the rating based on the number of filled stars
            stars = rating_tag.find_all('svg', class_='icon-star')
            half_stars = rating_tag.find_all('svg', class_='icon-star-half')
            rating = len(stars) + len(half_stars) * 0.5  # Full stars + half stars

            rating_count = rating_count_tag.get_text(strip=True) if rating_count_tag else 'No ratings'

            recipes_data.append({
                'title': title,
                'link': link,
                'image': image,
                'rating': f"{rating} stars ({rating_count})"
            })
        except Exception as e:
            print("Error scraping a card:", e)
            continue

    return render_template('results.html', recipes=recipes_data)

