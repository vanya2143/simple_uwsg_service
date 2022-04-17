# Simple uwsgi service
Python 3.10

## Run
### Local
1. Clone project
2. Go to project directory `cd project_path`
3. Create env `python -m venv ./venv`
4. Activate environment `source venv/bin/activate`
5. Install requirements `pip install -r requirements.txt`
6. Run project `uwsgi --ini uwsgi.ini`

### Docker
1. Build project `docker build -t simple_service .`
2. Run project `docker run -it -p 8080:8080 simple_service`
3. Now you can open in web browser http://127.0.0.1:8080

## urls
### /sum_of_two
method: GET

Accepting array of integers of any size using GET parameters.
Response of this function can be true only if sum of any two parameters equals the last one.
For example
```python
[1,2] returns False
[1, 2, 3] returns True
[1, 2, 4, 7] return False
[1, 3, 5, 7, 9, 10] returns True
```
You can pass an array to the query string using the `arr` parameter, like so:
```text
[1, 2, 3] == ?arr=1&arr=2&arr=3
```
Sample:
```shell
curl "http://127.0.0.1:8080/sum_of_two/?arr=1&arr=2&arr=3"
```
Response: `{"sum_of_two": true}`