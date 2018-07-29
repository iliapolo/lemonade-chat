This repository contains a small chat API for registration of users as well as viewing their 
details.

## Install

### pip

```bash
pip install https://github.com/iliapolo/lemonade-chat/archive/master.zip 
```

##### Notes

- You must install this package inside a Python3.6 environment.
- You might need to prefix the command with *sudo*, in case you are not using a virtual environment

### binary (MacOS only)

You can also simply download one self-contained binary executable:

```bash
curl -L https://github.com/iliapolo/lemonade-chat/releases/download/0.1.0/lemonade-chat-x86_64-Darwin -o lemonade-chat
chmod +x ./lemonade-chat
``` 

This method does not require a specific version of python (it actually doesn't require python to 
be installed on your machine at all) and also does not require an active 
internet connection for downloading dependencies.

It was created via [PyCI](https://github.com/iliapolo/pyci) - Check it out!


## Usage

First thing we need to do is start the chat server:

```bash
lemonade-chat server start
```

You should see something like this:

```bash
 * Serving Flask app "lemonade_chat.api.server.server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You can also start the server on a custom port by using the *--port* option.

Now we can start working with the client. The client has two entry-points:

#### User registration

```bash
lemonade-chat client register
```

You should see something like this:

```bash
Welcome to Lemonade!

What is your email address?:
```

Now simply follow the instructions.


#### View User details

```bash
lemonade-chat client view
```

Again, you should see something like this:

```bash
Welcome to Lemonade!

What is your email address?:
```

Type in your email address and you will see all your registration details.

* If you started the server on a custom port, use the **--server-port** option to let the client 
know.

* You can exit the client at any point by pressing CTRL+C

