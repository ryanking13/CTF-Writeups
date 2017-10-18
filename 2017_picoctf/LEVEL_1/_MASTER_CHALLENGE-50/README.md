## Lazy Dev - 50

### Description

I really need to login to this website, but the developer hasn't implemented login yet. Can you help?

### Hint

  - Where does the password check actually occur?
  - Can you interact with the javascript directly?

### Write up

There is a password input box.

By analysing the source, you can see that there is a `client.js` file.

```javascript
//Validate the password. TBD!
function validate(pword){
  //TODO: Implement me
  return false;
}

//Make an ajax request to the server
function make_ajax_req(input){
  var text_response;
  var http_req = new XMLHttpRequest();
  var params = "pword_valid=" + input.toString();
  http_req.open("POST", "login", true);
  http_req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  http_req.onreadystatechange = function() {//Call a function when the state changes.
  	if(http_req.readyState == 4 && http_req.status == 200) {
      document.getElementById("res").innerHTML = http_req.responseText;
    }
  }
  http_req.send(params);
}

//Called when the user submits the password
function process_password(){
  var pword = document.getElementById("password").value;
  var res = validate(pword);
  var server_res = make_ajax_req(res);
}
```

validate() function is not implemented, so make_ajax_req() always get parameter 'false'.

We want to make a make_ajax_req() call with 'true' parameter.

We can do it by browsers Developer mode (F12).

(Chrome)
F12 -> console -> make_ajax_req(true)

> client_side_is_the_dark_sidea99c64effed2c2f1c9347eff536e949c
