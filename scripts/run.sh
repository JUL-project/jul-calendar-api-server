pip install -r  requirements.txt
## in linux
# gunicorn --bind 0:8000 main:app --worker-class uvicorn.workers.UvicornWorker
## in window
cd ..
uvicorn main:app --reload