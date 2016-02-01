# Cars Service
Simple python service for retrieving canned car info and emulating common HTTP-based
service issues.  Runs on port 80 with:

```
python service.py
```

## Endpoints
* ```GET /cars```:  Returns a list of cars
* ```GET /state```: Returns the state of the server (normal, slow or backedup)
* ```POST /state/slow```: Puts the service in a slow state 
* ```POST /state/backedup```: Puts the service in a backedup state
* ```POST /state/normal```: Puts the service in a normal state
