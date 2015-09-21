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


## API Routes

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
* `401` if invalid credentials
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
* `401` if invalid credentials


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
* `401` if invalid credentials
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
* `401` if invalid credentials
* `404` if employee does not exist


### Delete an employee

**DELETE:**
```
/v1/employee/:employee_id
```

**Response:** None

**Status Codes:**
* `204` if successful
* `401` if invalid credentials
* `404` if employee does not exist


### Add a project

**POST:**
```
/v1/project
```

**Body:**
```json
{
    "name": "Mira",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "description": "A fitness tracker for women",
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Mira",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "description": "A fitness tracker for women",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `201` if successful
* `400` if incorrect data provided
* `401` if invalid credentials
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
          "name": "Mira",
          "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
          "description": "A fitness tracker for women",
          "added_at": "2015-06-01T19:22:24.850544Z",
          "updated": "2015-06-01T19:22:24.850544Z"
        },
    ]
}
```

**Status Codes:**
* `200` if successful
* `401` if invalid credentials


### Get a project

**GET:**
```
/v1/project/:project_id
```

**Response:**
```json
{
    "id": 1,
    "name": "Mira",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "description": "A fitness tracker for women",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"  
}
```

**Status Codes:**
* `200` if successful
* `401` if invalid credentials
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
    "name": "Mira",
    "logo_url": "http://www.vokal.io/sites/default/files/sweet-pic.png",
    "description": "A fitness tracker for women",
    "added_at": "2015-06-01T19:22:24.850544Z",
    "updated": "2015-06-01T19:22:24.850544Z"
}
```

**Status Codes:**
* `200` if successful
* `400` if data is not provided
* `401` if invalid credentials
* `404` if project does not exist


### Delete a project

**DELETE:**
```
/v1/project/:project_id
```

**Response:** None

**Status Codes:**
* `204` if successful
* `401` if invalid credentials
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
    "name": "Paul George Beacon",
    "employee": 1
}
```

**Response:**
```json
{
    "id": 1,
    "beacon_id": "1234567890",
    "name": "Paul George Beacon",
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
    }
}
```

**Status Codes:**
* `201` if successful
* `400` if incorrect data provided
* `401` if invalid credentials
* `409` if beacon already exists  


### Get a list of beacons

**GET:**
```
/v1/beacon
```

**Notes**
One needs to send detected beacon ids as parameters
Just hitting the route /v1/beacon will not have a response

**Query Parameters:**
Beacon records are returned in the order given
(/v1/beacon?id=1&id=2&id=3&id=4)

* `id` - An integer: the beacon's id

**Response:**
```json
{
    "count": 4,
    "previous": null,
    "next": "",
    "results": [
        {
            "id": 1,
            "beacon_id": "1234567890",
            "name": "Paul George Beacon",
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
          }
        },
    ]
}
```

**Status Codes:**
* `200` if successful
* `400` if no parameters were given
* `401` if invalid credentials


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
  "name": "Paul George Beacon",
  "employee": 1
}
```

**Status Codes:**
* `200` if successful
* `401` if invalid credentials
* `404` if beacon does not exist


### Update a beacon

**PUT:**
```
/v1/beacon/:beacon_id
```

**Body:**
```json
{
    "name": "Not yo beacon!"
}
```

**Response:**
```json
{
  "id": 1,
  "beacon_id": "1234567890",
  "name": "Not yo beacon!",
  "employee": 1
}
```

**Status Codes:**
* `200` if successful
* `400` if data is not provided
* `401` if invalid credentials
* `404` if beacon does not exist


### Delete a beacon

**DELETE:**
```
/v1/beacon/:beacon_id
```

**Response:** None

**Status Codes:**
* `204` if successful
* `401` if invalid credentials
* `404` if beacon does not exist
