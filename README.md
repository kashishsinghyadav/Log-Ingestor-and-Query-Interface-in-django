# Log-Ingestor-and-Query-Interface-in-django
Develop a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


![Screenshot (98)](https://github.com/dyte-submissions/november-2023-hiring-kashishsinghyadav/assets/117498422/9a7e3257-890b-4004-885a-964cb269b5cd)

we Develop a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.

the database saved the data realted to field 
- level
- message
- resourceId
- timestamp
- traceId
- spanId
- commit
- metadata.parentResourceId


![Screenshot (99)](https://github.com/dyte-submissions/november-2023-hiring-kashishsinghyadav/assets/117498422/11817897-eef6-45a9-a0ab-4aefd02aa7f5)


this is how database look like click on '+' add log icon you can add the log details and if you 'http://localhost:8000/query' type this url you can - 
- search within specific date ranges.
- Utilize regular expressions for search.
- Allow combining multiple filters.
- Provide real-time log ingestion and searching capabilities.
- Implement role-based access to the query interface.



##




### Built With


* [Python-Django]
* [Html/css]]
* sqlite 





<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Django project
  ```sh
  cd ./log_ingestor_project/
  
  ```
   ```sh
  python manage.py runserver 
  
  ```

* Django adminpanel
    ```sh
    http://localhost:8000/admin/
  ```
Password=kashish
username=loginadmin
  


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. install python in your system it will also download djnago locally 
2. create django project
   ```sh
   django-admin startproject log_ingestor_project
   ```
3. Install app realted to project
   ```sh
   python manage.py startapp log_ingestor
   ```
    ```sh
    python manage.py startapp query_interface
   ```
4. Run your server
5.  ```sh
    localhost:8000/urlname 
```
