
## In directory run:

```
python3 -m venv my_env

source my_env/bin/activate

pip install -r requirements.txt

uvicorn project.main:app --reload

```

Uvicorn running on http://127.0.0.1:8000


Import Postman collection


Method | Path | Description
-------|------|------------ 
POST   |/articles       | create article                    
GET    |/articles       | get all articles                     
GET    |/articles/:id   | get article by id                   
PATCH  |/articles/:id   | update article                    
DELETE |/articles/:id   | delete article  


Request body when creating article
```
{
  "title": "First article",
  "body": "Body of the first article"
}
```

Request body when updating article must contain both fields
```
{
  "title": "First article",
  "body": "Updated body of the first article"
}
```

