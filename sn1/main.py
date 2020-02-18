from flask import Flask, request, render_template
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja2')

@app.route('/divide', methods=['GET', 'POST'])
def divide():
	result = []
	result.append("OK")
	if request.method == 'POST':
		stop_f = str(request.form['stop_f'])
		stop_t = str(request.form['stop_t'])
		try:
			f = open('stop.txt', 'r')
			lines = f.readlines()
			f.close()
			flag=0
			for i, line in enumerate(lines):
				line = line.split(',')
				if stop_f == line[0] and i < len(lines):
					result.append(lines[i])
					flag+=1
				if stop_t == line[0] and i < len(lines):
					result.append(lines[i])
					flag+=1
				if flag==2:
					break
			if flag<2:
				result.append("not found")
		except EXCEPTION:
			pass
	#else:
		#return render_template('divide.jinja2', result= result)


	return render_template('divide.jinja2', result= json.dumps(result))


if __name__ == '__main__':
    app.debug = True
    app.run()
