from fastapi import FastAPI


app = FastAPI()


@app.get('/articles')
def get_articles():
    return {'articles': []}