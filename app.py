from flask import Flask, render_template, redirect, url_for, request
import random

# Create App
app = Flask(__name__)

# Dictionary of spotify playlists created by the boys
rl_playlists = {
    'ROCKet league (give peace a chance)': 'https://open.spotify.com/playlist/2OvZhUdhfGfX1uwzvljq7n',
    'ROCKet league 2': 'https://open.spotify.com/playlist/2zZeRdAbICnQ7TSsLN5vBC',
    'RL Jams 3': 'https://open.spotify.com/playlist/12Bj8omX9yVyxXGhh5PLRK',
    'RL Jams 4': 'https://open.spotify.com/playlist/1we478QGMNIGsWyE5oZBW1',
    'RL Quarantine Jams': 'https://open.spotify.com/playlist/3StWvMXkpwcGQ8WbCtIuZa',
    'RL Retrowave': 'https://open.spotify.com/playlist/4gI05J2uZYczyXgsSMXlNk',
    'Rocket league 7?': 'https://open.spotify.com/playlist/6MPLeUOyaRXkvRYqI9xVCQ',
    'RL8': 'https://open.spotify.com/playlist/4b5PYczGVDpyphiJAOqQxW',
    'RL (greg in ohio mix)': 'https://open.spotify.com/playlist/1E5fDpSyyZF1KaOUvaetWP',
    'rl10': 'https://open.spotify.com/playlist/1ZTRFQA1ppjegrogsaOIf7',
    'RL11 (greg in buffalo mix)': 'https://open.spotify.com/playlist/49q9c1ghiIqsWaPZafsO9i',
    '12 days of Rocket League': 'https://open.spotify.com/playlist/4DOpUin6hq6WmNxinHb6ld',
    'RL-13': 'https://open.spotify.com/playlist/2vjxqUIfCbIkdnUpchVQyR',
}

# Create the route of the home page for the app
@app.route('/', methods = ["POST", "GET"])
def index():
    
    key = random.choice(list(rl_playlists.keys()))
    random_playlist = key
    random_playlist_url = rl_playlists[key]
    
    if request.method == 'POST':
        return render_template('index.html', rl_playlists=rl_playlists, key=key,
                           random_playlist=random_playlist, random_playlist_url=random_playlist_url)
    else:
        return render_template('index.html', rl_playlists=rl_playlists)

# Create route for the 'About' page
@app.route('/about/', methods =["POST", "GET"])
def about():
    return render_template('about.html', rl_playlists=rl_playlists)

if __name__ == '__main__':
    app.run()