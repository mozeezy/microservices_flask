## Learning Microservices

##### What are microservices
- Essentially, it is an architectural style that seperates components of an application into loosely coupled services (i.e. servers).
- These services communicate with each other with an API.
- It is an alternative to the monolithic architecture - where all the different services exist in one unit. The downside to this is that if one of the services goes down, the entire architecture might be affected.

##### Breaking down the example in this repo
- Let's say that we have a bookstore application that has users and books and we want to develop a feature where a user can order a book.
- To do this, we can setup a database that stores a user's info.
- Then, we would make an API call to get the user's info from the database.
- Assuming that the user is a valid user, we would then create a function that would allow the user to order the book.

- Notice that we have two seperate servers: one that is fetching the user's info and one that is placing the order. The user service exposes an API that is used to get the user info and the order service exposes an API that is used to place an order by calling the user service to make sure that the user is a valid user.