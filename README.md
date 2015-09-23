Vivy API
====================

#### Solution
An iPad application that provides an interactive digital experience to visitors by
showcasing Vokal projects/employees along with displaying engaging messages at
different locations around the office (using beacon technology).

#### How it works
The client will be handed an ipad with the app open upon entering Vokal.
The client can view Vokal’s employees or past/current projects at any time.
The app will detect beacons as the visitor explores the office and display
messages, pictures, information accordingly.

#### API Table of Contents

1. [Admin Login](#admin-login)
1. [Add an employee](#add-an-employee)
1. [Get a list of employees](#get-a-list-of-employees)
1. [Get an employee](#get-an-employee)
1. [Update an employee](#update-an-employee)
1. [Delete an employee](#delete-an-employee)
1. [Add a project](#add-a-project)
1. [Get a list of projects](#get-a-list-of-projects)
1. [Get a project](#get-a-project)
1. [Update a project](#update-a-project)
1. [Delete a project](#delete-a-project)
1. [Add a beacon](#add-a-beacon)
1. [Get a list of beacons](#get-a-list-of-beacons)
1. [Get a beacon](#get-a-beacon)
1. [Update a beacon](#update-a-beacon)
1. [Delete a beacon](#delete-a-beacon)

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
    "is_admin": true
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
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
    "questions": {
        "What drives you?": "basketball",
        "Who inspires you? ": "basketball",
        "What’s something surprising about you?": "basketball",
        "What would you do if you won the lottery?": "basketball"
    },
}
```

**Response:**
```json
{
    "id": 1,
    "first_name": "Paul",
    "last_name": "George",
    "title": "CEO",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
    "questions": {
        "What drives you?": "basketball",
        "Who inspires you? ": "basketball",
        "What’s something surprising about you?": "basketball",
        "What would you do if you won the lottery?": "basketball"
    },
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
            "id": 1,
            "first_name": "Paul",
            "last_name": "George",
            "title": "CEO",
            "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
            "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
            "questions": {
                "What drives you?": "basketball",
                "Who inspires you? ": "basketball",
                "What’s something surprising about you?": "basketball",
                "What would you do if you won the lottery?": "basketball"
            },
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
    "id": 1,
    "first_name": "Paul",
    "last_name": "George",
    "title": "CEO",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
    "questions": {
        "What drives you?": "basketball",
        "Who inspires you? ": "basketball",
        "What’s something surprising about you?": "basketball",
        "What would you do if you won the lottery?": "basketball"
    },
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `404` if employee does not exist


### Update an employee

**PATCH:**
```
/v1/employee/:employee_id
```

**Body:**
```json
{
    "title": "Apprentice",
}
```

**Response:**
```json
{
    "id": 1,
    "first_name": "Paul",
    "last_name": "George",
    "title": "Apprentice",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "summary": "He was selected by the Pacers with the 10th overall pick of the 2010 NBA draft. In 2013, he was selected to play in his first NBA All-Star Game, received the NBA Most Improved Player Award, and was named to the All-NBA Third Team and the All-Defensive Second Team",
    "questions": {
        "What drives you?": "basketball",
        "Who inspires you? ": "basketball",
        "What’s something surprising about you?": "basketball",
        "What would you do if you won the lottery?": "basketball"
    },
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

**Notes:**
Staff is a list of all employee instance ids that have contributed to this project.
Screenshot is a dictionary of project screenshots labeled by their order. For example
the image with the key "one" should be displayed before "two" and so on.  

**Body:**
```json
{
    "name": "Parche",
    "headline": "Eliminating the valet wait",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "opportunity": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
    "solution": "blah blah blah.",
    "technology": "blah blah blah.",
    "staff": [1, 2, 3, 4, 5, 6, 7],
    "screenshot" : {
      "one": "http://www.vokal.io/sites/default/files/screenshot.png",
      "two": "http://www.vokal.io/sites/default/files/screenshot.png",
      "three": "http://www.vokal.io/sites/default/files/screenshot.png",
      "four": "http://www.vokal.io/sites/default/files/screenshot.png"
    }
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Parche",
    "headline": "Eliminating the valet wait",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "opportunity": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
    "solution": "blah blah blah.",
    "technology": "blah blah blah.",
    "staff": [1, 2, 3, 4, 5, 6, 7],
    "screenshot" : {
      "one": "http://www.vokal.io/sites/default/files/screenshot.png",
      "two": "http://www.vokal.io/sites/default/files/screenshot.png",
      "three": "http://www.vokal.io/sites/default/files/screenshot.png",
      "four": "http://www.vokal.io/sites/default/files/screenshot.png"
    },
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
            "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
            "opportunity": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
            "solution": "blah blah blah.",
            "technology": "blah blah blah.",
            "staff": [1, 2, 3, 4, 5, 6, 7],
            "screenshot" : {
              "one": "http://www.vokal.io/sites/default/files/screenshot.png",
              "two": "http://www.vokal.io/sites/default/files/screenshot.png",
              "three": "http://www.vokal.io/sites/default/files/screenshot.png",
              "four": "http://www.vokal.io/sites/default/files/screenshot.png"
            },
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
    "name": "Parche",
    "headline": "Eliminating the valet wait",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "opportunity": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
    "solution": "blah blah blah.",
    "technology": "blah blah blah.",
    "staff": [1, 2, 3, 4, 5, 6, 7],
    "screenshot" : {
      "one": "http://www.vokal.io/sites/default/files/screenshot.png",
      "two": "http://www.vokal.io/sites/default/files/screenshot.png",
      "three": "http://www.vokal.io/sites/default/files/screenshot.png",
      "four": "http://www.vokal.io/sites/default/files/screenshot.png"
    },
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `404` if project does not exist


### Update a project

**PATCH:**
```
/v1/project/:project_id
```

**Body:**
```json
{
    "name": "Parche 2"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Parche2",
    "headline": "Eliminating the valet wait",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "opportunity": "The traditional valet model doesn’t support the needs of the modern, cashless customer or offer an opportunity for reporting and analytics.",
    "solution": "blah blah blah.",
    "technology": "blah blah blah.",
    "staff": [1, 2, 3, 4, 5, 6, 7],
    "screenshot" : {
      "one": "http://www.vokal.io/sites/default/files/screenshot.png",
      "two": "http://www.vokal.io/sites/default/files/screenshot.png",
      "three": "http://www.vokal.io/sites/default/files/screenshot.png",
      "four": "http://www.vokal.io/sites/default/files/screenshot.png"
    },
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


### Add a location

**POST:**
```
/v1/location
```

**Body:**
```json
{
    "title": "Whiteboard",
    "summary": "A big big big board",
    "impact": "How this makes an impact on Vokal projects",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png"
}
```

**Response:**
```json
{
    "id": 1,
    "title": "Whiteboard",
    "summary": "A big big big board",
    "impact": "How this makes an impact on Vokal projects",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `201` if successful
* `400` if incorrect data provided
* `401` if not admin


### Get a list of locations

**GET:**
```
/v1/location
```

**Response:**
```json
{
    "count": 5,
    "previous": null,
    "next": "",
    "results": [
        {
          "id": 1,
          "title": "Whiteboard",
          "summary": "A big big big board",
          "impact": "How this makes an impact on Vokal projects",
          "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
          "added_at": "2015-06-01T19:22:24.850544Z",
          "updated": "2015-06-01T19:22:24.850544Z"
        },
        {
          "id": 2,
          "title": "Build Wall",
          "summary": "Magical TV",
          "impact": "Tells me I fucked up",
          "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
          "added_at": "2015-06-01T19:22:24.850544Z",
          "updated": "2015-06-01T19:22:24.850544Z"
        },
    ]
}
```

**Status Codes:**
* `200` if successful


### Get a location

**GET:**
```
/v1/location/:location_id
```

**Response:**
```json
{
    "id": 2,
    "title": "Build Wall",
    "summary": "Magical TV",
    "impact": "Tells me I fucked up",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `404` if location does not exist


### Update a location

**PATCH:**
```
/v1/location/:location_id
```

**Body:**
```json
{
    "impact": "Tells me when I can poop"
}
```

**Response:**
```json
{
    "id": 2,
    "title": "Build Wall",
    "summary": "Magical TV",
    "impact": "Tells me when I can poop",
    "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `400` if data is not provided
* `401` if not admin
* `404` if location does not exist


### Delete a location

**DELETE:**
```
/v1/location/:location_id
```

**Response:** None

**Status Codes:**
* `204` if successful
* `401` if not admin
* `404` if location does not exist


### Add a beacon

**POST:**
```
/v1/beacon
```

**Notes:**
The location field is the location object id the beacon is tied to.
The beacon_id is the UUID of the beacon, not the instance id.

**Body:**
```json
{
    "beacon_id": "1234567890",
    "location": 2
}
```

**Response:**
```json
{
    "id": 1,
    "beacon_id": "1234567890",
    "location": {
        "id": 2,
        "title": "Build Wall",
        "summary": "Magical TV",
        "impact": "Tells me when I can poop",
        "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
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
            "location": {
                "id": 2,
                "title": "Build Wall",
                "summary": "Magical TV",
                "impact": "Tells me when I can poop",
                "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
                "added_at": "2015-06-01T19:22:24.850544Z",
                "updated": "2015-06-01T19:22:24.850544Z"
            },
            "added_at": "2015-06-01T19:22:24.850544Z",
            "updated": "2015-06-01T19:22:24.850544Z"
        },
        {
            "id": 2,
            "beacon_id": "1111111111",
            "location": {
                "id": 1,
                "title": "Whiteboard",
                "summary": "A big big big board",
                "impact": "How this makes an impact on Vokal projects",
                "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
                "added_at": "2015-06-01T19:22:24.850544Z",
                "updated": "2015-06-01T19:22:24.850544Z"
            },
            "added_at": "2015-06-01T19:22:24.850544Z",
            "updated": "2015-06-01T19:22:24.850544Z"
        }
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
    "location": {
        "id": 2,
        "title": "Build Wall",
        "summary": "Magical TV",
        "impact": "Tells me when I can poop",
        "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
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

**PATCH:**
```
/v1/beacon/:beacon_id
```

**Body:**
```json
{
    "location": "1"
}
```

**Response:**
```json
{
    "id": 1,
    "beacon_id": "9999999999",
    "location": {
        "id": 1,
        "title": "Whiteboard",
        "summary": "A big big big board",
        "impact": "How this makes an impact on Vokal projects",
        "image_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
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
