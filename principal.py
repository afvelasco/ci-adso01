from conexion import *

@app.route('/')
def index():
    return render_template('principal.html')

if __name__ == '__main__':
    app.run(debug=True)
