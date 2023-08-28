import os

# use the server host and port from servers environment variable if available
SERVER_HOST = os.environ.get("SERVER_HOST", "localhost") 
SERVER_PORT = os.environ.get("SERVER_PORT", 8080)
