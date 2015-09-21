Vivy API
====================

#### Goal
Allow visitors to connect with Vokal on a personal level, while establishing ourselves as a professional, experienced tech company.
#### Solution
Vivy is an iPad application that provides an engaging digital experience to visitors by showcasing nearby Vokal employees along with past/current Vokal projects.
#### How it works
The client will be handed an ipad with the app open upon entering Vokal.
The client can view Vokal’s past/current projects at any time.
Vokal employees will each have a keychain beacon. During the tour the iPad will show all nearby Vokal employees and the current project they are associated with. They can then tap the individual to view more information.

#### API Table of Contents

1. [Admin Login](#admin-login)
2. [Add an employee](#add-an-employee)
3. [Get a list of employees](#get-a-list-of-employees)
4. [Get an employee](#get-an-employee)
5. [Update an employee](#update-an-employee)
6. [Delete an employee](#delete-an-employee)
7. [Add a project](#add-a-project)
8. [Get a list of projects](#get-a-list-of-projects)
9. [Get a project](#get-a-project)
10. [Update a project](#update-a-project)
11. [Delete a project](#delete-a-project)
12. [Add a beacon](#add-a-beacon)
13. [Get a list of beacons](#get-a-list-of-beacons)
14. [Get a beacon](#get-a-beacon)
15. [Update a beacon](#update-a-beacon)
16. [Delete a beacon](#delete-a-beacon)

## API Routes


### Admin login

**POST:**
```
/v1/admin/login
```

**Body:**
```json
{
    "email": "johndoe@vokalinteractive.com",
    "password": "12345678"
}
```

**Response:**
```json
{
    "id": 1,
    "email": "johndoe@vokalinteractive.com",
    "name": "John Doe",
    "auth_token": "UYGgYtg76GUIHIUHiuhIUhi7y8d120dkasd0mnjv",
    "is_admin": false
}
```

**Status Codes:**
* `201` if successful
* `400` if incorrect data provided


### Add an employee

**POST:**
```
/v1/employee
```

**Body:**
```json
{
    "first_name": "Paul",
    "last_name": "George",
    "title": "CEO",
    "email": "paul.george@vokal.io",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
    "extra_info": {
        "What drives you?": "basketball",
        "Who inspires you? ": "basketball",
        "What’s something surprising about you?": "basketball",
        "What would you do if you won the lottery?": "basketball"
    },
    "project": 1
}
```

**Response:**
```json
{
    "id": 1,
    "first_name": "Paul",
    "last_name": "George",
    "title": "CEO",
    "email": "paul.george@vokal.io",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
    "extra_info": {
        "What drives you?": "basketball",
        "Who inspires you? ": "basketball",
        "What’s something surprising about you?": "basketball",
        "What would you do if you won the lottery?": "basketball"
    },
    "project": 1,
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `201` if successful
* `400` if incorrect data provided
* `401` if not admin
* `409` if employee already exists  


### Get a list of employees

**GET:**
```
/v1/employee
```

**Response:**
```json
{
    "count": 20,
    "previous": null,
    "next": "http://blahblah.com/v1/employee?page=2",
    "results": [
        {
          "first_name": "Paul",
          "last_name": "George",
          "title": "CEO",
          "email": "paul.george@vokal.io",
          "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
          "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
          "extra_info": {
              "What drives you?": "basketball",
              "Who inspires you? ": "basketball",
              "What’s something surprising about you?": "basketball",
              "What would you do if you won the lottery?": "basketball"
          },
          "project": 1,
          "added_at": "2015-06-01T19:22:24.850544Z",
          "updated": "2015-06-01T19:22:24.850544Z"
        },
    ]
}
```

**Status Codes:**
* `200` if successful


### Get an employee

**GET:**
```
/v1/employee/:employee_id
```

**Response:**
```json
{
    "first_name": "Paul",
    "last_name": "George",
    "title": "CEO",
    "email": "paul.george@vokal.io",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
    "extra_info": {
        "What drives you?": "basketball",
        "Who inspires you? ": "basketball",
        "What’s something surprising about you?": "basketball",
        "What would you do if you won the lottery?": "basketball"
    },
    "project": 1,
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `404` if employee does not exist


### Update an employee

**PUT:**
```
/v1/employee/:employee_id
```

**Body:**
```json
{
    "project": 2,
}
```

**Response:**
```json
{
    "id": 1,
    "first_name": "Paul",
    "last_name": "George",
    "title": "CEO",
    "email": "paul.george@vokal.io",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
    "extra_info": {
        "What drives you?": "basketball",
        "Who inspires you? ": "basketball",
        "What’s something surprising about you?": "basketball",
        "What would you do if you won the lottery?": "basketball"
    },
    "project": 2,
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `400` if data is not provided
* `401` if not admin
* `404` if employee does not exist


### Delete an employee

**DELETE:**
```
/v1/employee/:employee_id
```

**Response:** None

**Status Codes:**
* `204` if successful
* `401` if not admin
* `404` if employee does not exist


### Add a project

**POST:**
```
/v1/project
```

**Body:**
```json
{
    "name": "Parche",
    "headline": "Eliminating the valet wait",
    "problem": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
    "solution": "Parche partnered with Vokal for an uncommon logistical solution using a common tool, the smartphone, giving greater power and convenience to valet customers. The Parche app processes requests and payment with a single command, allowing customers to go from table to car without waiting outside or stopping for cash. Valet operators also gain the ability to monitor valet activity and eliminate the common causes of customer complaints, leaving better impressions and building repeat patronage.",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "screenshot1": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot2": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot3": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot4": "http://www.vokal.io/sites/default/files/screenshot.png"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Parche",
    "headline": "Eliminating the valet wait",
    "problem": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
    "solution": "Parche partnered with Vokal for an uncommon logistical solution using a common tool, the smartphone, giving greater power and convenience to valet customers. The Parche app processes requests and payment with a single command, allowing customers to go from table to car without waiting outside or stopping for cash. Valet operators also gain the ability to monitor valet activity and eliminate the common causes of customer complaints, leaving better impressions and building repeat patronage.",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "screenshot1": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot2": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot3": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot4": "http://www.vokal.io/sites/default/files/screenshot.png",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `201` if successful
* `400` if incorrect data provided
* `401` if not admin
* `409` if project already exists  


### Get a list of projects

**GET:**
```
/v1/project
```

**Response:**
```json
{
    "count": 20,
    "previous": null,
    "next": "http://blahblah.com/v1/employee?page=2",
    "results": [
        {
          "id": 1,
          "name": "Parche",
          "headline": "Eliminating the valet wait",
          "problem": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
          "solution": "Parche partnered with Vokal for an uncommon logistical solution using a common tool, the smartphone, giving greater power and convenience to valet customers. The Parche app processes requests and payment with a single command, allowing customers to go from table to car without waiting outside or stopping for cash. Valet operators also gain the ability to monitor valet activity and eliminate the common causes of customer complaints, leaving better impressions and building repeat patronage.",
          "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
          "screenshot1": "http://www.vokal.io/sites/default/files/screenshot.png",
          "screenshot2": "http://www.vokal.io/sites/default/files/screenshot.png",
          "screenshot3": "http://www.vokal.io/sites/default/files/screenshot.png",
          "screenshot4": "http://www.vokal.io/sites/default/files/screenshot.png",
          "added_at": "2015-06-01T19:22:24.850544Z",
          "updated": "2015-06-01T19:22:24.850544Z"
        },
    ]
}
```

**Status Codes:**
* `200` if successful


### Get a project

**GET:**
```
/v1/project/:project_id
```

**Response:**
```json
{
    "id": 1,
    "id": 1,
    "name": "Parche",
    "headline": "Eliminating the valet wait",
    "problem": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
    "solution": "Parche partnered with Vokal for an uncommon logistical solution using a common tool, the smartphone, giving greater power and convenience to valet customers. The Parche app processes requests and payment with a single command, allowing customers to go from table to car without waiting outside or stopping for cash. Valet operators also gain the ability to monitor valet activity and eliminate the common causes of customer complaints, leaving better impressions and building repeat patronage.",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "screenshot1": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot2": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot3": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot4": "http://www.vokal.io/sites/default/files/screenshot.png",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `404` if project does not exist


### Update a project

**PUT:**
```
/v1/project/:project_id
```

**Body:**
```json
{
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png"
}
```

**Response:**
```json
{
    "id": 1,
    "id": 1,
    "name": "Parche",
    "headline": "Eliminating the valet wait",
    "problem": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
    "solution": "Parche partnered with Vokal for an uncommon logistical solution using a common tool, the smartphone, giving greater power and convenience to valet customers. The Parche app processes requests and payment with a single command, allowing customers to go from table to car without waiting outside or stopping for cash. Valet operators also gain the ability to monitor valet activity and eliminate the common causes of customer complaints, leaving better impressions and building repeat patronage.",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "screenshot1": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot2": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot3": "http://www.vokal.io/sites/default/files/screenshot.png",
    "screenshot4": "http://www.vokal.io/sites/default/files/screenshot.png",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `400` if data is not provided
* `401` if not admin
* `404` if project does not exist


### Delete a project

**DELETE:**
```
/v1/project/:project_id
```

**Response:** None

**Status Codes:**
* `204` if successful
* `401` if not admin
* `404` if project does not exist


### Add a beacon

**POST:**
```
/v1/beacon
```

**Body:**
```json
{
    "beacon_id": "1234567890",
    "employee": 1
}
```

**Response:**
```json
{
    "id": 1,
    "beacon_id": "1234567890",
    "employee": {
        "id": 1,
        "first_name": "Paul",
        "last_name": "George",
        "title": "CEO",
        "email": "paul.george@vokal.io",
        "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
        "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
        "extra_info": {
            "What drives you?": "basketball",
            "Who inspires you? ": "basketball",
            "What’s something surprising about you?": "basketball",
            "What would you do if you won the lottery?": "basketball"
        },
        "project": 1,
        "added_at": "2015-06-01T19:22:24.850544Z",
        "updated": "2015-06-01T19:22:24.850544Z"
    },
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `201` if successful
* `400` if incorrect data provided
* `401` if not admin
* `409` if beacon already exists  


### Get a list of beacons

**GET:**
```
/v1/beacon
```

**Notes**
One needs to send detected beacon ids as parameters
Just hitting the route /v1/beacon will return all beacon instances

**Query Parameters:**
Beacon records are returned in the same order passed.
Beacon ids are passed by using the following format:
(/v1/beacon/?beacon_id[]=1234567890&beacon_id[]=999999999)

**Response:**
```json
{
    "count": 2,
    "previous": null,
    "next": "",
    "results": [
        {
            "id": 1,
            "beacon_id": "1234567890",
            "employee": {
              "id": 1,
              "first_name": "Paul",
              "last_name": "George",
              "title": "CEO",
              "email": "paul.george@vokal.io",
              "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
              "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
              "extra_info": {
                  "What drives you?": "basketball",
                  "Who inspires you? ": "basketball",
                  "What’s something surprising about you?": "basketball",
                  "What would you do if you won the lottery?": "basketball"
              },
              "project": 1,
              "added_at": "2015-06-01T19:22:24.850544Z",
              "updated": "2015-06-01T19:22:24.850544Z"
          },
          "added_at": "2015-06-01T19:22:24.850544Z",
          "updated": "2015-06-01T19:22:24.850544Z"
        },
    ]
}
```

**Status Codes:**
* `200` if successful


### Get a beacon

**GET:**
```
/v1/beacon/:beacon_id
```

**Response:**
```json
{
    "id": 1,
    "beacon_id": "1234567890",
    "employee": {
        "id": 1,
        "first_name": "Paul",
        "last_name": "George",
        "title": "CEO",
        "email": "paul.george@vokal.io",
        "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
        "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
        "extra_info": {
            "What drives you?": "basketball",
            "Who inspires you? ": "basketball",
            "What’s something surprising about you?": "basketball",
            "What would you do if you won the lottery?": "basketball"
        },
        "project": 1,
        "added_at": "2015-06-01T19:22:24.850544Z",
        "updated": "2015-06-01T19:22:24.850544Z"
    },
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `404` if beacon does not exist


### Update a beacon

**PUT:**
```
/v1/beacon/:beacon_id
```

**Body:**
```json
{
    "beacon_id": "9999999999"
}
```

**Response:**
```json
{
    "id": 1,
    "beacon_id": "9999999999",
    "employee": {
        "id": 1,
        "first_name": "Paul",
        "last_name": "George",
        "title": "CEO",
        "email": "paul.george@vokal.io",
        "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
        "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
        "extra_info": {
            "What drives you?": "basketball",
            "Who inspires you? ": "basketball",
            "What’s something surprising about you?": "basketball",
            "What would you do if you won the lottery?": "basketball"
        },
        "project": 1,
        "added_at": "2015-06-01T19:22:24.850544Z",
        "updated": "2015-06-01T19:22:24.850544Z"
    },
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `400` if data is not provided
* `401` if not admin
* `404` if beacon does not exist


### Delete a beacon

**DELETE:**
```
/v1/beacon/:beacon_id
```

**Response:** None

**Status Codes:**
* `204` if successful
* `401` if not admin
* `404` if beacon does not exist
