from flask import Flask

app=Flask(__name__)
@app.route("/info")
def info():
	return "my name is bhavesh"
app.run()