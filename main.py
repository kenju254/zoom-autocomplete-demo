from flask import Flask, render_template, request

app = Flask(__name__)



# ** Example 5 **
# Autocomplete with Bloodhound with Remote data
@app.route('/bloohdhoundRemote', methods=['GET', 'POST'])
def bloohdhoundRemote():
	print "** bloohdhoundRemote() called"
	if request.method == 'POST':
		print "POST request"
	else:
		print "GET request"

	citynames = ['Amsterdam', 'London', 'Paris', 'Washington', 'Sydney', 'Melbourne']

	resource_list = [{'value': 'MIR:00000555', 'label': 'My WormBase RNAi'}, \
		{'value': 'MIR:11100545', 'label': 'My Wormpep'}]
	return jsonify(resource_list=resource_list, citynames=citynames)


# ** Example 4 **
# Autcomplete from multiple sources Bloodhound
@app.route('/multipleRemote', methods=['GET', 'POST'])
def multipleRemote():
	print " ** multipleRemote() called"
	if request.method == "POST":
		print "POST request"
	else:
		print "GET request"

	nba_teams = [{"team": "Boston Celtics NBA"}, {"team": "Dallas Mavericks NBA"}, {"team": "Brooklyn NBA"}]
	nhl_teams = [{"team": "New Jersey NHL"}, {"team": "Boston NHL"}, {"team": "Philadelphia NHL"}]

	return jsonify(nba_teams=nba_teams, nhl_teams=nhl_teams)


# ** Example 3 **
# Autocomplete method - called from Jinja template
@app.route('/datcomplete', methods=['GET', 'POST'])
def datcomplete():
	print "** datcomplete() called"
	if request.method == 'POST':
		print "POST request"
	else:
		print "GET request"

	# postData = request.form
	# print "** MyVar:", postData
	jsonData = request.json['variable']
	print jsonData

	new_data = [{'value': 'MIR:00000555', 'label': 'My WormBase RNAi'}, \
		{'value': 'MIR:00000545', 'label': 'My Wormpep'}]

	results = [{'value': 'MIR:00000466', 'label': 'WormBase RNAi'}, \
		{'value': 'MIR:00000031', 'label': 'Wormpep'}, {'value': 'MIR:00000186', 'label': 'Xenbase'}, \
		{'value': 'MIR:00000111', 'label': 'Resource 1'}, {'value': 'MIR:00000222', 'label': 'Resource 2'}, \
		{'value': 'MIR:00000333', 'label': 'Resource 3'}, {'value': 'MIR:00000444', 'label': 'Resource 4'}]

	results.extend(new_data)
	return jsonify(matching_results=results)



# Route to home page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def show_home():
	return render_template('index.html')

if __name__ == "__main__":
    app.run()
