def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    response = (value + '\n').encode() for value in environ['QUERY_STRING'].split('&')
    return response