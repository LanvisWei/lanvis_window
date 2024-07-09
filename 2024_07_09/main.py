from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>曹氏宗親會!</h1>\n <h2>人妻最高!!!!</n>"

@app.route('/hello')
def hello():
    return '<h1>別人的太太就是我的太太。</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'<h1>hello, {(username)}</h1>'
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'<h1>Post {post_id}</h1>'
