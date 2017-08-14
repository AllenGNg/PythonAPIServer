# PythonAPIServer
A simple Python API Server using GitHub's API for Replicated Code Challenge.

## **Challenge**
Given a list of GitHub usernames through a POST request, using GitHub's API, return all of the users' IDs and Public SSH Keys in JSON format. Some users may have more than one ID and Public SSH Keys.

## **Design:**
My project has two files, one file is for a client and one file is for a server.
The client is used to call the new POST API that I have written. In lieu of using the client, the Postman application can also be used to invoke the new POST API. 
The server implements the new POST API using the Flask framework. The new POST API accepts request data that consists of a list of usernames for which the ID and public SSH key should be retrieved using a GitHub API. The POST API has the following endpoint: IDsandKey. 
The new POST API returns response data that is a dictionary that is keyed by usernames. For each user, a list of dictionaries will be returned with the ID(s) and public SSH key(s) (if the user was found in GitHub). A list is returned because some users can have more than one ID and public SSH key in GitHub. If a user is not found in GitHub, then the ID and public SSH key for that user will be set to 'N/A'. The response data also has a message field that contains an useful informational message about the processing that was just performed. 
To account for possible edge cases, the status code from calling the GitHub API is checked. If a status code of 200 is returned, then the call was successful. If a status code of 404 is returned, it means that the user was not found in GitHub and the ID and public SSH key is set to 'N/A'. If a status code of 403 is returned, it means that the user has reached the calling limit for the GitHub API that the server needs to use. Any data that was successfully retrieved prior to reaching the calling limit is returned (the message in the response data will indicate such a condition). 

### **Request Data Schema**
Key| Value Data Type| Description
----|---------|----------
`'user-name-list'`| List of Strings | The usernames to retrieve their GitHub IDs and Public SSH Keys using the GitHub API.

### **Response Data Schema**
Key| Value Data Type| Description
----|---------|-------------
`'info-message'`| String | Informational message describing the outcome of the REST API.
`'key-data'`| Dictionary| Dictionary of IDs and Public SSH Keys pertaining to their users.
`Username from Request Data` | List of Dictionaries | List of Dictionaries containging that user's ID and Public SSH Keys. They have as many dictionaries in the list as they have IDs and Public SSH Key pairs in GitHub.
`'id'`| Int | GitHub ID for the username.
`'key'`| String | Public SSH Key for the username.

## **Setting Up:**
To run the code, your system will need to have flask and flask-restful installed as they are required packages to run the server. To install these 2 packages, you can simply type `pip install flask` and `pip install flask-restful`.
To change the usernames to retrieve GitHub private keys for, edit the pythonClient.py file. In the pythonClient.py file, there is a Dictionary labeled dict. For example, `dict = {'user-name-list': 'allengng', 'mjluck'}` here you will want to edit the list to include the names of the GitHub users to search for.
By default, the port number that the flask framework is using is 5000. 

## **Running:**
There are 2 ways to use the API Server

**1)** I have included a makefile to make it as easy as possible. Open 2 terminal sessions and in one of them, type `make server` and this will start up the API server. Then on the other terminal session, you will run the client via typing `make client`. The client will then send the POST request to the server which will then call the GitHub API for each username included in the list. It will then output onto the terminal session, all of the GitHub users' IDs and Public SSH Keys, if they have any. If the user name is not found, it will still return their username, but the ID and Key will be set to 'N/A'. 

**2)** Another way to invoke the new API is to use an application such as Postman. By using the URL in the Client file which is `http://127.0.0.1:5000/IDsandKeys` and setting the header content type as `applications/json`, you can now send in your list of usernames by using the following format, `{"user-name-list": ["allengng"]}`. Just be sure to start the server prior to sending the POST request.

## **Example:**
I will now show an example of using the new API. In the client file, you update the Dictionary dict to specify the usernames you want to use the GitHub API to search for. For example, if I want to search my username, it will look like this. `{'user-name-list': ['allengng']}`. 'user-name-list' is the Key and any username in the list will be searched. So, if I want to search 3 usernames, it will look like this: `{'user-name-list': ['allengng', 'mjluck', 'allengn']}`. If I run the Client file with the dictionary shown  above (3 usernames), I will get the following output shown below.

```
All users processed.
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
Now, the output is one big dictionary. Inside that dictionary, every username searched for will be used as a key. For each of the username keys, it will have a list of dictionaries with each dictionary containing 2 Key Value pairs. One key is 'ID' and the value will have the GitHub id for that user. The second key will be 'key' and the value will be the Public SSH Key associated with that ID. Some users have more than one ID and Key. If that is the case, then the list associated with that user will have as many dictionaries as they have IDs and Keys. For examples, user "mjluck" has 3 different pairs of ID and Keys. As you can see in the sample output above, you will see he has 3 different dictionaries inside his list.

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
As you can see from the output, I now have 57 remaining out of 60. One key thing to look at is the `"reset"` timer in the `"core"` dictionary. It is in Epoch time, so to see when your limit will be reset, you can use an online Epoch time converter. If I convert that time, it is 2:23:56 PM in my local time zone. So once it passes 2:23:56 PM, my limit will be reset and I will have 60 API calls again.

## **Conclusion:**
Thanks for taking a look at my README and my code! This was the first time I have done something related to this, so it was a great learning experience and I enjoyed every bit of it!

