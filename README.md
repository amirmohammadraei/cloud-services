<div align="center">
  <h3 align="center">Familiarity with some cloud services</h3>
</div>
<br>

## About The Project
For example, suppose you are responsible for building a website for a fall photography exhibition. You will be given a number of photos and stories and you will be asked to add the ability to comment on existing photos to the site. In addition, you should make the site so that it works for the visually impaired, so you should also make the ability to audio file comments and stories to this site.

## Built With
* django

## Getting Started

### Prerequisites
To run this project your system must have the following programs pre-installed
* python
* pip3
* virtualenv

### Installation

1. Get a free API Key at [IBM](https://www.ibm.com/cloud/watson-text-to-speech) to use text to speech api
2. Clone the repo
   ```sh
   https://github.com/amirmohammadraei/cloud-services.git
   ```
3. Create virtualenv
   ```sh
   virtualenv .env
   ```
4. Active virtualenv
   ```sh
   source .env/bin/activate
   ```
5. Install Requirements
   ```sh
   pip3 install requirements.txt
   ```
6. Create database and role
7. cd to cloud_services directory
   ```sh
   cd cloud_services
   ```
8. Run makemigrations & migrate 
  ```sh
   python manage.py makemigrations && python manage.py migrate
   ```
9. Run project 
  ```sh
   python manage.py runserver
   ```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact
If you have any questions about how to execute, install or structure of the project, be sure to inform via the email below

amir.m.raei@tutanota.com
