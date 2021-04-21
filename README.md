# Project Teams
### **Objective**: To be able to Create/Read/Update/Delete a member from a Team


### Setup:
#### Install mySQL: https://www.mysql.com/downloads/ 
#### Clone the repository
#### `cd teams-api/TeamsProject`
#### in a virtual env: `pip install -r requirements.txt`
#### `python manage.py migrate`
#### `python manage.py runserver`

#### Get All Members 
`curl -X GET http://127.0.0.1:8000/team/member/`


#### Create New Team member 
`curl -X POST 
  http://127.0.0.1:8000/team/member/ 
  -H 'content-type: application/json' 
  -d '{
            "firstName": "Shivam",
            "lastName": "Singhal",
            "phoneNumber": "+919503182221",
            "email": "shivam1@test.com",
            "role": 1
        }'`

#### Delete Team member 
`curl -X DELETE 
  http://127.0.0.1:8000/team/member/10 
  -H 'content-type: application/json' `
  
#### Update Team member
`curl -X PUT 
  http://127.0.0.1:8000/team/member/9 
  -H 'content-type: application/json' 
  -d '{"email": "some@test.com"}'`
