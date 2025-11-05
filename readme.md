## Getting started



### Prerequisites

After clone this project,make sure this tool are installed on your PC, before run the project :
- open terminal on your IDE
- check python version
```bash
$ python --version
```
- this project running on python virtual environment
- install virtual environment on this project first,after clone this project
```bash
$ python -m venv .venv
```
### Running

To run the project, follow these steps:

1. Start the virtual environment by executing the command:
   ```bash
   source .venv/Scripts/activate
   ```
2. Run the locust
   ```bash
   locust -f your-locust-file.py
   ```
3. Open web interface at http://localhost:8089 on your browser
