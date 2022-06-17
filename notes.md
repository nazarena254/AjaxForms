## Ajax Forms

* AJAX -stands for Asynchronous JavaScript And XML, which allows web pages to update asynchronously by exchanging data to and from the server. 
* This means you can update parts of a web page without reloading the complete web page.
* XMLHttpRequest (XHR) objects are used to interact with servers
* The server responds to the request.
* The response is captured and then server respond back with response data.

#### POST Request
To submit the form, we need to make a POST request to the server with all the form values filled by the user

#### GET Request
To check if the nickname is already taken or not by sending a GET request to the server

#### Serialize
The serialized values can be used in the URL query string when making an AJAX request

### Conclusion
AJAX is the best way to perform asynchronous tasks in Django, at least on a small scale. If you want to do an asynchronous task on a bigger scale, you could do socket programming in Django or use front-end JavaScript libraries such as Angular, Vue, or React

#### Resources
[Plural site](https://app.pluralsight.com/guides/work-with-ajax-django)