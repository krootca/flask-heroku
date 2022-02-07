from threading import Lock

from flask import Flask, flash, render_template, request, redirect, url_for, abort, session, escape, make_response

from flask_socketio import SocketIO, send, emit


app=Flask(__name__)
socketio = SocketIO(app,   async_mode="threading")
thread = None
thread_lock = Lock()
app.secret_key="Your-secret-code"


#Edit this
@app.route("/", methods=["GET", "POST"])
def Index():
	return render_template("/index.html")

