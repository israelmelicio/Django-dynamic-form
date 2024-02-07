# Django Dynamic Form Application

This Django application demonstrates the use of dynamic forms. It creates a form based on a JSON schema, considering required fields, dependencies, and if conditionals of the schema. This allows for the creation of complex, dynamic forms based on the structure defined in the JSON schema. (in the file `dynamic-form/schema.json`) that can be replaced with any other JSON schema.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Setting Up a Virtual Environment

It's recommended to use a Python virtual environment for development to isolate the project dependencies. You can create a virtual environment using the `venv` module:

```bash
python3 -m venv env
```

### Prerequisites

You need to have Python and Django installed on your machine. You can download Python from [here](https://www.python.org/downloads/) and Django can be installed via pip:

```bash
pip install django
```

### Setting Up the Project

Make the necessary migrations by running the following command:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running the Application

Start the Django server by running the following command:

```bash
python manage.py runserver
```

To see the dynamic form in action, navigate to `http://127.0.0.1:8000/myapp/form/` in your web browser.

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
