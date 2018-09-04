from flask import Flask, render_template


app_blockbax = Flask(__name__)

@app_blockbax.route('/')
def  blockbax_start():

    return render_template('bax_home.html')

if __name__ == '__main__':
    app_blockbax.run()