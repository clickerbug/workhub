### How to Install?
1. Create a venv for python3, - `python3 -m venv ./venv`
2. Install dependencies, - `pip3 install -r requirements.txt`
3. Perform migrations - `python3 manage.py migrate`, if you dont have migration files 
already run `python3 manage.py makemigrations` to create migration files for your apps.
4. Create superuser (optional) - `python manage.py createsuperuser'
5. Run the application - `python3 manage.py runserver`

### Adding Workshops & Topics
1. Create a superuser account
2. http://127.0.0.1:8000/admin and login with it
3. Add Workshops / Topics using the UI available

### APIs
API request can be sent to localhost:8000 / http://127.0.0.1:8000/ on default

You can visit http://127.0.0.1:8000/ to see a graphiql console to debug and test
the apis after setting up the app.

#### 1. Register User
```
mutation create_user{
  registerUser(email: "abc@gmail.com", password: "password123")
  {
    returning
    {
      username
    }
  }
}
```

#### 2. Login User
Store the token returned and save it in cookie,
should be included in all future authenticated queries with
in request header as Authorization : `JWT <token>`

```
mutation login_user{
  tokenAuth(input: {
    username: "aswin",
    password: "123"
  })
  {
    token
  }
}
```
#### 3. Listing All Available Topics
```
query {
    getTopics
    {
      id
      name
      slug
    }
}
```

#### 4. Add Topics to User's Preference
Simply pass the topic id, with the auth token set in header
```
mutation add_topic{
  addUserTopics(topicID: 1)
}
```
#### 5. List Workshops
without recommendation
```
query {
  getWorkshops
  {
    id
    name
    description
    topics
    {
      id
      name
    }
  }
}
```
with recommendation
```
query {
  getRecommendedWorkshops
  {
    id
    name
    description
    topics
    {
      id
      name
      slug
    }
  }
}
```

