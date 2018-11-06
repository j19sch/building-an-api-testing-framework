# API specs

host: `http:localhost:8000`

## /knockknock

**GET**  
return code: 200  
return body: (string)


## /books

**GET**  
return code: 200  
return body: list of books (json)


**GET /{book-id}**  
return code: 200  
return body: book (json)

example response:
```
    {
        "author": "Gerald Weinberg", 
        "id": "9b30d321-d242-444f-b2db-884d04a4d806", 
        "pages": 182, 
        "publisher": "Dorset House Publishing", 
        "sub_title": null, 
        "title": "Perfect Software And Other Illusions About Testing", 
        "year": 2008
    }
```
    
**POST**  
return code: 201  
return body: id of created book (json)

example response:
```
    {
        "id": "3612a30e-800f-4f34-8c2c-670fd2f13a01"
    }
```

**DELETE /{book-id}**  
requires token  
return code: 200


**PUT /{book-id}**
requires token    
return code: 200  
return body: updated book (json)


## /token

**POST /{user}**  
return code: 200  
return body: token (json)
  
example response:
```
    {
        "token": "AQuKIjKwcktlzEK"
    }
```