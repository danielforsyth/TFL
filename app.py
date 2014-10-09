from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import requests


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def getEstimate():
	r = requests.get('http://countdown.tfl.gov.uk/stopBoard/58984')
	json_result = r.json()
	b = json_result['arrivals']
	l = []
	for x in b:
		if x['isRealTime']== True and x['destination'] == 'White City':
			x = str(x['routeName']) + ' ' + str(x['destination']) + ' '+ str(x['estimatedWait'])
			l.append(x)
    
	return render_template('index.html', estimates=l)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)

