from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Unblocker</h1>
    <form action="/proxy" method="get">
        <input type="text" name="url" placeholder="Enter URL to unblock">
        <button type="submit">Go</button>
    </form>
    """

@app.route('/proxy', methods=['GET'])
def proxy():
    url = request.args.get('url')
    if not url.startswith('http'):
        url = 'http://' + url

    try:
        response = requests.get(url)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
