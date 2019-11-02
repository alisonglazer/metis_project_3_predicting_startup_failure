import flask
from flask import request, render_template, redirect
from ag_predictor_api import fund_extract,convert, make_prediction, feature_names, feature_display_names # import from our other python file

# Initialize the app

app = flask.Flask(__name__)


# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!
# @app.route("/")
# def hello():
#     return flask.send_file("static/html/index.html")
#     # return 'Hello'
#     # return render_template('index.html')

predictions = [{}]
@app.route("/")
@app.route("/predict/", methods=["POST", "GET"])
# GET method is a request you make when you click a link on a website
# POST is like filling out a form
def predict():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template(html))" (key): "string in the textbox" (value)
    print(request.args)
    fund_vars = fund_extract(request.args)
    print(type(fund_vars))
    global x_input
    x_input = []
    x_input += fund_vars
    #
    cat_vars = convert(request.args.get('category',"Manufacturing"),4,15)
    x_input.extend(cat_vars)
    country_vars = convert(request.args.get('country',"USA"),15,20)
    x_input.extend(country_vars)
    us_state_vars = convert(request.args.get('us_state',"CA"),20,24)
    x_input.extend(us_state_vars)
    x_input.extend([0])

    global predictions
    predictions = make_prediction(x_input)
    # predictions = make_prediction([2.0,182.0, 182.0, 500000.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0])
    # break up the tuple into those two variables
    print(x_input)
    print(predictions)
    # if request.method == 'POST':
    # if predictions != [{'name': 'Fail', 'prob': 0.9644768415496009}, {'name': 'Success', 'prob': 0.03552315845039906}]:
    # # if request.args is None:
    # # if x_input != [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0]:
    #     predictions = predictions
    #     return redirect('/answer/')
    return render_template('predictor.html', x_input=x_input,
                                 feature_names=feature_names,
                                 prediction=predictions,
                                 feature_display_names=feature_display_names)
    # render template uses kwargs (**) which allows unlimited unknown args that can be taken in and do some common thing with all of them
    #feature_names came from predictor_api
    # CSS has to know these names though (x_input, feature_names, prediction)
    # even though flask does not because of kwargs

@app.route("/answer/", methods=["POST", "GET"])
def predict2():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template(html))" (key): "string in the textbox" (value)
    print(request.args)
    fund_vars = fund_extract(request.args)
    print(type(fund_vars))
    global x_input
    x_input = []
    x_input += fund_vars
    #
    cat_vars = convert(request.args.get('category',"Manufacturing"),4,15)
    x_input.extend(cat_vars)
    country_vars = convert(request.args.get('country',"USA"),15,20)
    x_input.extend(country_vars)
    us_state_vars = convert(request.args.get('us_state',"CA"),20,24)
    x_input.extend(us_state_vars)
    x_input.extend([0])

    global predictions
    predictions = make_prediction(x_input)
    # predictions = make_prediction([2.0,182.0, 182.0, 500000.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0])
    # break up the tuple into those two variables
    print(x_input)
    print(predictions)
    # if request.method == 'POST':
    # if predictions != [{'name': 'Fail', 'prob': 0.9644768415496009}, {'name': 'Success', 'prob': 0.03552315845039906}]:
    # # if request.args is None:
    # # if x_input != [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0]:
    #     predictions = predictions
    #     return redirect('/answer/')
    return render_template('answer.html', x_input=x_input,
                                 feature_names=feature_names,
                                 prediction=predictions,
                                 feature_display_names=feature_display_names)


if __name__=="__main__":
    # For local development:
    #app.run(debug=True)
    # For public web serving:
    #app.run(host='0.0.0.0')
    app.run()

# For public web serving:
# app.run(host='0.0.0.0')
