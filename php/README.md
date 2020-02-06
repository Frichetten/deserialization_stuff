# PHP Deserialization Attacks

## Project Setup

To startup an example navigate into the directory and start a docker container with the following command:  

```bash
$ sudo docker run -it --rm -v $(pwd):/app -p 8080:8080 php bash
```  

This will start a docker container for PHP. From here navigate into the directory and start the webserver with the following command:  

```bash
$ cd /app  
$ php -S 0.0.0.0:8080
```   

From here, please review the README.md file in each example for the names of parameters to query.  

## Resources  
[1] https://www.notsosecure.com/remote-code-execution-via-php-unserialize/  
[2] https://medium.com/swlh/deserialization-bugs-in-the-wild-fe37149a7ee1  
