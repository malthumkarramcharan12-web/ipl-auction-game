from flask import Flask, render_template, request, redirect
from players import players

app = Flask(__name__)

current_index = 0

teams = {
    "Team A": {"budget": 100, "players": []},
    "Team B": {"budget": 100, "players": []}
}

@app.route('/')
def index():
    global current_index
    player = players[current_index]
    return render_template("index.html", player=player, teams=teams)

@app.route('/bid', methods=['POST'])
def bid():
    global current_index
    team = request.form['team']
    amount = int(request.form['amount'])

    player = players[current_index]

    if amount > player["base_price"] and teams[team]["budget"] >= amount:
        teams[team]["budget"] -= amount
        teams[team]["players"].append(player["name"])
        current_index += 1

    return redirect('/')

@app.route('/next')
def next_player():
    global current_index
    current_index += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
