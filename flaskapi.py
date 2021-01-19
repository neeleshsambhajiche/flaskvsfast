from flask import Flask, request, jsonify, Response
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

application = Flask(__name__)


retry_strategy = Retry(
    total=1,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=50, pool_maxsize=50)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)


@application.route("/io_job")
def io_job():
    url = "https://api.github.com"
    resp = http.get(url=url)

    # extracting data
    data = resp.json()
    respData = {
        "message": data["message"]
    }
    return jsonify(respData)



@application.route("/cpu_job")
def countdown(n=5000):
    while n > 0:
        n -= 1
    respData = {
        "n": n
    }
    return jsonify(respData)


if __name__ == "__main__":
    application.run(host='0.0.0.0',port=8080)