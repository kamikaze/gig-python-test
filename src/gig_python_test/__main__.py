import uvicorn
from gig_python_test.api.http import app


uvicorn.run(app, host='0.0.0.0', port=8080)
