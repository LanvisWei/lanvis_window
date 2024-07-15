from flask import Flask,render_template, request
import data

app = Flask(__name__)
@app.route("/")
def index():
    # content = 'Use our powerful <strong>mobile-first</strong> flexbox grid to build layouts of all shapes and sizes thanks to a twelve column system, six default responsive tiers, Sass variables and mixins, and dozens of predefined classes.'
    #  return render_template('index.html.jinja',left=content)

    # print(data.get_areas())
    # print(list(map(lambda value:value[0],data.get_areas())))
    selected_area = request.args.get('area')
    areas = [tup[0] for tup in data.get_areas()]
    # if selected_area is None:
    selected_area='士林區' if selected_area is None else selected_area
    detail_snaes = data.get_snaOfArea(area=selected_area)
        # print('首插')
        # return render_template('index.html.jinja', areas=areas)
    # return render_template('index.html.jinja', areas=areas, area='士林區')
    # print(areas)
    # return render_template('index.html.jinja', areas=areas)
    # else:
    #     # print(selected_area)
    # return render_template('index.html.jinja', areas=areas, show_area=selected_area)
    return render_template('index.html.jinja',areas=areas,show_area=selected_area,detail_snaes=detail_snaes)  