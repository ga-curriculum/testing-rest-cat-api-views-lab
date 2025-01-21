# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Cat API Testing Lab

| Title               | Type | Duration | Author               |
|---------------------|------|----------|----------------------|
| Cat API Testing Lab | Lab  | 3:00     | Suresh Melvin Sigera |

In this hands-on lab, students will test a Django REST API for a Cat Collector application. The lab covers testing CRUD
operations, relationships between models (`Cats`, `Toys`, `Feedings`), and proper authentication/authorization flows. 

Students will use Django's test framework along with REST framework test utilities to verify API functionality.

### Learning Objectives

Upon completion of this lab, students will be able to:

- **API Testing Fundamentals**
    - Execute CRUD operations using REST API endpoints
    - Verify API responses and status codes
    - Understand API authentication and authorization flows
    - Test API endpoint relationships and data persistence

- **REST Resource Management**
    - Test creation and management of primary resources (Cats)
    - Verify relationships between resources (Cats and Toys)
    - Validate nested resource operations (Feedings)
    - Confirm proper data persistence and retrieval

- **Prerequisites**
    - Basic understanding of HTTP methods (GET, POST, PUT, DELETE)
    - Familiarity with JSON data format
    - Access to API testing tool (Postman, cURL, or similar)
    - Valid user account credentials

**Exercise 1: Start by getting your access token**
**Exercise 2: Cat CRUD Operations**

| Method | Endpoint  | Description           |
|--------|-----------|-----------------------|
| POST   | /cats     | Create a new cat      |
| GET    | /cats     | Retrieve all cats     |
| GET    | /cats/:id | Retrieve a single cat |
| PUT    | /cats/:id | Update a cat          |
| DELETE | /cats/:id | Delete a cat          |

**Exercise 2: Cat Toy Relationships**

| Method | Endpoint  | Description           |
  |--------|-----------|-----------------------|
| POST   | /toys     | Create a new toy      |
| GET    | /toys     | Retrieve all toys     |
| GET    | /toys/:id | Retrieve a single toy |
| PUT    | /toys/:id | Update a toy          |
| DELETE | /toys/:id | Delete a toy          |

**Exercise 3: Cat Feeding Operations**

| Method | Endpoint      | Description               |
|--------|---------------|---------------------------|
| POST   | /feedings     | Create a new feeding      |
| GET    | /feedings     | Retrieve all feedings     |
| GET    | /feedings/:id | Retrieve a single feeding |
| PUT    | /feedings/:id | Update a feeding          |
| DELETE | /feedings/:id | Delete a feeding          |

**Exercise 4: Permission Testing**

| Method | Endpoint                   | Description             |
|--------|----------------------------|-------------------------|
| GET    | /cats/                     | Try Without Token       |
| GET    | /cats/[other_user_cat_id]/ | Access Other User's Cat |
| PUT    | /cats/[other_user_cat_id]/ | Update Other User's Cat |

**Testing Sequence**

- Basic CRUD Flow
    - Create a new cat
    - Verify cat details
    - Update cat information
    - Delete cat
- Toy Relationships
    - Create multiple toys
    - Add toys to cat
    - Verify toy list
    - Remove toys
- Feeding Management
    - Add multiple feedings
    - Verify feeding records
    - Update feeding details
    - Remove feedings
- Error Cases
    - Try invalid data formats
    - Test permission boundaries
    - Attempt unauthorized operations

**Extension Activities**

- Create a cat with multiple toys and feedings
- Try batch operations (multiple updates)
- Test different feeding patterns
- Verify cascade deletions

### How to submit homework

#### Setup

- Step 1. Fork the repository
- Step 2. Clone your fork

#### Submitting work

- Step 3. Push to your fork
- Step 4. Submit a pull request
- Step 4.1. Under the title, add your first and last name with the comment

In the comment section, you must add the following:

```text
* Comfortability [0 to 5]
* Completeness [0 to 5]
* What was a win?
* What was a challenge?
* Any other comments
```