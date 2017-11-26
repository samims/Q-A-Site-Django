# Q-A-Site-Django
Questions &amp; Answers site developed using Django.

## Project setup

Setup virtual environment and install requirements(in this case django).
In linux you have to use the following command in project root directory. I am using ubuntu 16.04 LTS

Install venv
```
sudo apt-get install python3.5-venv
```
Setup virtua environment for this project
```
python3 -m venv myvenv
```
Activate the virtual environment
```
source myvenv/bin/activate
```
Initialize database:
```
./manage.py makemigrations
./manage.py migrate
```
## Built With

* [Django 1.11.7](https://docs.djangoproject.com/en/1.11/) - The web framework used
* [Pycharm](https://www.jetbrains.com/pycharm/) - IDE used
* [Sqlite](https://www.sqlite.org/) - Database used


## Author

* **Samiul Sk** - [Linkedin](https://www.linkedin.com/in/samiulsk/)

## Acknowledgments
* medium.com
* Abhas Anand(Asked/Suggested me to do the project)
