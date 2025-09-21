# 🍽️ Recipe Recommendation System

A **web-based recipe recommendation system** that lets users discover top recipes based on the ingredients they have. Built with **Flask** and **BeautifulSoup**, it scrapes [AllRecipes.com](https://www.allrecipes.com/) to provide the top 5 recipes matching user input.

---

## 🖼️ Screenshots


---

## 📌 Features

- Input ingredients (comma-separated) to search for recipes.
- Scrapes **AllRecipes.com** to fetch recipe details.
- Displays top 5 recipes including:
  - Recipe title
  - Image
  - Rating & number of ratings
  - Direct link to full recipe
- Responsive and user-friendly web interface.
- Easy deployment to **Vercel** or any Python web hosting service.

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask** – Web framework
- **Requests** – HTTP requests to scrape web pages
- **BeautifulSoup4** – Parsing HTML for recipe data
- **HTML / CSS** – Responsive front-end design

---

## 📂 Project Structure

```
api/
  ├─ index.py              # Flask backend & web scraper
  └─ templates/
        ├─ index.html      # Homepage with ingredient input form
        ├─ edit.html       # Alternative input form template
        └─ results.html    # Displays top 5 recipes
requirements.txt           # Python dependencies
vercel.json                # Vercel deployment configuration
```

---

## ⚡ Setup & Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/recipe-recommendation.git
cd recipe-recommendation
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Flask app locally:**
```bash
python api/index.py
```

5. **Open in browser:**
```
http://127.0.0.1:5000/
```

---

## 🌐 Deployment on Vercel

1. Install the [Vercel CLI](https://vercel.com/docs/cli).  
2. Login and link your project:
```bash
vercel login
vercel
```
3. Vercel automatically detects `vercel.json` and deploys your Flask app.

---


## ⚠️ Notes

- This project **scrapes AllRecipes.com**, so scraping results may vary if their website structure changes.  
- Make sure to use **comma-separated ingredients** for accurate results.  
- The app currently fetches **only the top 5 recipes** for simplicity.

---

## 💡 Future Improvements

- Add **pagination** to show more recipes.  
- Integrate **user accounts** to save favorite recipes.  
- Add **filters** (dietary preferences, cuisine, cook time).  
- Enhance UI with **Bootstrap / Tailwind CSS** for a modern look.  


