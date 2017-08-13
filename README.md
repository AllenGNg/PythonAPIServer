# PythonAPIServer
A simple Python API Server using GitHub's API for Replicated Code Challenge

## **Challenge**
Given a list of GitHub User names through a POST request, using GitHub's API, return all of the usernames' IDs and Public SSH Keys in JSON. Some people may have more than one ID and Public SSH Keys.

## **Design:**
My design uses two files, one is a Client and one is a Server. The client allows the user to send in a list of usernames

## **Setting Up:**
To set up my project, the first thing you would want to do is to edit the pythonClient.py file. In that file there is a Dictionary labeled dict. For example,
`
dict = {'user-name-list': 'allengng', 'mjluck'}
`
here you will want to edit the list to include the names of the GitHub User names to search for. Another thing you must do is make sure you have `flask` and `flask-restful` installed on your computer as they are required packages to run the server. To install these 2 packages, you can simply type `pip install flask` and `pip install flask-restful`.

## **Running:**
There are 2 ways to use the API Server

**1)** I have included a makefile to make it as easy as possible. Have 2 terminals open and in one of them, type `make server` and this will start up the server. Then on the other terminal you will want to type `make client`. This will then send the POST request to the server which will then call the GitHub API for each user name included in the list. It will then output onto the terminal all of the GitHub User names' IDs and Public SSH Keys, if they have any. If the user name is not found, it will still return their user name, but will not have any ID or Key associated with them. This allows you to run the API all within your terminals.

**2)** Another way to use it is to use a seperate application such as Postman. By using the URL in the Server and Client file which is `http://127.0.0.1:5000/IDsandKeys` and setting the header as `applications/json`, you can now send in your list of usernames by using the following format, `{"user-name-list": ["allengng"]}`. Just be sure to start the server before you try and send in the POST request!

## **Example:**
I will now show an example. In the Client file you use the Dictionary `dict` to add in the usernames you want to use the GitHub API to search for. For example, if I want to search my username, it will look like this. `dict = {'user-name-list': ['allengng']}`. `'user-name-list'` is the Key and any username in the list will be serached. So, if I want to search 3 usernames it will look like this. `dict = {'user-name-list': ['allengng', 'mjluck', 'allengn']}`. So if I run the Client file with the dictionary shown as above, I will get an output as shown as below.  

```
{u'allengn': [{u'id': u'N/A', u'key': u'N/A'}],
 u'allengng': [{u'id': 19486910,
                u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxe/5H72brc67HCYiOHYan2ZfCSqAS0IetBlfV1mDdd01I8dmotr56AbZdr/mP7Cc2CxM2yMBLEt3XPwdtouRvZHqidbTuTvOsmZPyhkI/95gCzCH6hh2iKfCqUj9dRUfayEo69rxcikzVSpuV7X1bO1nbJxHMnW+DrNFfhBfhkdCJ6mRkydJ3bYosNsj5v1Vb3QcveqAvJN6m5Os8ux20HTwdzrUjIf927H1B2h+wgT9p8TZlXNqyE9/dTX5LzamMIJ+jnWWwzytTJXTZ2Q2YnCWdd1Fvnb/vU1m8c+3ZxAOZ+JRBesO+vuKXb6wNY+u11Rr0m9G6QgzF3Rh/sAix'}],
 u'mjluck': [{u'id': 23656140,
              u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIT8RCAYHsHbyh3CiU5GaLchrpKppxr0pYD/9tVzYhLosoD0yLq/rO8TH43tu/pZ2qPdC0cB2X9R59cHSbqkpDgBdBtxctU54o1XrzZ92aK1IEWkvgrMLPgYvP0qs3aVN7fJD5TEoVKf86cLFJKUCFMt4fNv5BNWHbUlZyCgic8oPJev8RAibc48q8jVa9kDbsUM4DfKYH81vcjP+8dSUmqXUkqf+IA/zWtczR/H4iRJYBxLNH35a+MjBl+vtch5DS9fYNUHVrb0r4CsjRFBKvsmEcd5fJZNgR3z842XNo1ngv57fKXPFm6h2cDhEZ0vWH4j3c/pX/AAfQ9AOMuBAt'},
             {u'id': 23719855,
              u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDVil0UDS7vr6M90J+/dkihNQvz+VAfL25QL+/vgXAiJf48R5Ccw0CXy/xG0YGdMGK28qcig3kAxTAsmYcBTT+WLWIPtDLQu1CMJKfVEcjf0mb0yOS/NyfAtomEfcN0mrDEHSYCJzn138wOr+g+atrhBLQlkM7g7HTA5vBAmIxC96nqXnu9TJvm4zFMI4mxXP5qLuTisH8L8VAEo6XGScH73qbgEidOTrjUgJnz0Hwlu8K9JgBZuBqgyy/J/Fs/99E1ECxoQcN/Q+J/PusbboUz3ZtiJFyPg+pWY7iga4QrzPJcNFn70Md+qcSMOWw+UPfinXzCDYXHOLWBi0AZAZdP'},
             {u'id': 24692015,
              u'key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCwJGjrWJ/9OYiLCrbiE0XFryqqPsXfA/GJJWHDbP9C/ypTVHIns0CxknGMbRxLfFSTUNL1K0gA/0yGz5xF5ErUid8yoNh9/QLTRGGZr8zR2hFcXPklDZRVrOAbrw52uPxHYFod1/1iBCW0pKmTbcy5so4oLwk2rFG5b8mIteDWsaCP7nDFxhwPiibgz9f67I3vjemKpm5eiXy2GqcEtuuHI7OB/HC3DZuXgOnQ820YvX/DgmCuJRLQHhtnsg265E5v8Qspfeft6H7EzRlagixqYOulEh31q96WiS1lWq4xKUV+heofJ8vnDS7ct3ecTv4e5XOcY8gfAR9896hMybxyVUXERhxIukwyPeTqmnhlZIiYfezVqiHGdrUBHCVrZod4YXDwzz1qa4DajufpO1M5SUrdagNDUxMUqdiROR7FKB7/ImegbH0lxj6qwinn5LeK5RwNEAr0Fi7BMijTkUbQxXFFOWA+X3PQtCzMxLH+NsHn8q4IkwzQ0BgFcQn57xV+Ebp2BmJ3Sr5mvrtyopQeR/V7+DY5xe31m1XjDfU9TWHKFf2UWrdpusOQZEyWFm2OU94lPM27NsEInHNfK4Lq89WYDSUlZNE7McbvtjuR6p+h8rxVWVjeRYeXRAW12UG5hJmeZyY621tXZphpjulyPvaf1wJTNZrwm3CROi0cPQ=='}]}
```
Now, the output is one big dictionary. Inside that dictionary, every username searched for will be used as a Key. For each of the Keys, they have a list of dictionaries with each dictionary containg 2 Key Value pairs. One is ID, which has that users ID and Keys, which has the Public SSH Key associated with that ID. Now some people have more than one ID and Key, if that is the case, then the list associated with the username will as many dictionaries as they have IDs and Keys. Such as "mjluck", he has 3 different pars of ID and Keys. So if you take a look at the output, you will see he has 3 different Dictionaries inside his list.

## **Notes:**
One thing you have to be careful of is that there is a limit to the amount of calls you can make to the GitHub API in an hour. For me, it is 60 calls an hour. One way to check your limit is to use the command `curl https://api.github.com/rate_limit` For example, after I ran the client, which will call the API 3 times, I will have 57 calls left until it resets. Here is the output I get when I run the command. 
```
$ curl https://api.github.com/rate_limit
{
  "resources": {
    "core": {
      "limit": 60,
      "remaining": 57,
      "reset": 1502648636
    },
    "search": {
      "limit": 10,
      "remaining": 10,
      "reset": 1502645098
    },
    "graphql": {
      "limit": 0,
      "remaining": 0,
      "reset": 1502648638
    }
  },
  "rate": {
    "limit": 60,
    "remaining": 57,
    "reset": 1502648636
  }
}
```
As you can see from the output, I now have 57 remaining out of 60. One key thing to look at is the `"reset"` timer in the `"core"` dictionary. It is in Epoch time, so to see when your limit will be reset you can use an online Epoch time converter. If I convert that time, it is 2:23:56 PM in my local time zone. So once it passes 2:23:56 PM my limit will reset and I will have 60 API calls remaining.

## **Conclusion:**
Thanks for taking a look at my README and my code! This was the first time I have done something related to this, so it was a great learning experience and I enjoyed every bit of it!

