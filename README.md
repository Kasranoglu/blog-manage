# blog-manage

Postman collections

- This app is for Blog CMS
  


### Requirements

-  Python version: 3.9.6

-  Django version : 4.2.4

-  DB : sqlite3

### Endpoints
- In addition, for use the system, register and then login endpoints must be called.


   {{host}}/api/auth/login
   {{host}}/api/auth/register
   {{host}}/api/auth/logout




- Post lister endpoints:


   {{host}}/api/post/list
   {{host}}/api/post/details/<slug:slug>/
   {{host}}/api/post/myposts
   {{host}}/api/post/mylikes




Download [Postman Collection](docs/Postman/collection/4691031c-6716-42e7-8ef3-9e3758f41727.json).
and [Postman Environment](docs/Postman/environment/cace364d-9b7b-4d89-833a-a92de2371dea.json).






### Quick Start

1. Download pip packages with
pip install -r requirements.txt
2. start project with 
python manage.py runserver 
3. http://127.0.0.1:8000/index you can go to homepage wit this url.





   
