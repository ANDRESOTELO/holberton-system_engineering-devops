# API

## What is an API?
A set of rules that define how two applications interact with each other. That is, who initiates communication, what messages are sent, what responses are expected, and so on.
In object-oriented programming, the API is the set of all the public members that a class offers, i.e. the properties and functions that it offers to other objects so that they can use its services.

We cannot talk about REST without talking about HTTP protocols, which are transfer protocols. A protocol is a set of rules that define how communication is done between two entities.

To see the HTTP headers of a web site on the command line we can use the command curl -v https://example.com > /dev/null

What is REST -> Representational State Transfer, it is basically a small layer of complexity added to HTTP. It is a resource sharing protocol. Therefore a RESTful API is an API that is designed around the concepts of REST.

A REST request is based on: what is the RESOURCE on which I want to perform an action and what is the action I want to perform. A complete REST request is based on a URL and an HTTP verb (GET, PUT, POST, DELETE). A resource can be literally anything.

The flow of a REST request works similar to HTTP, but with slight modifications. The client makes an HTTP request to the server, the server interprets the request and generates the response, at some point the server realizes that certain requested resources are not its own or do not live in its location, it has to ask another server for them, so it generates another HTTP request to the other server to obtain that resource, the other server generates a response to the first server (this is the REST request), once this first server has the data from the other server, it continues with its response to the original request and returns it to the client so that the client can do what it has to do with it.

## When is it convenient to use REST?
In simple interactions
When you have limited resources (usually hardware).

## How are REST requests made?
The consumption of web services via REST is based on the use of HTTP verbs. Through them I can search for resources, create resources, modify or delete resources. (CRUD)

## How to make my own REST services?
For this we need a server capable of interpreting HTTP requests and giving HTTP responses.
Usually these communications are done through JSON formats.
The basic structure would be:
1. Know what type or method of REQUEST the server receives.
2. If it is GET do this (i.e. encode in JSON what I am requesting).
3. If it is POST do this
4. If it is PUT do this
5. If DELETE do this.

We must define what type of resources we want to expose or we are going to allow to consume. For example in our server we have a library database.

To indicate that we are going to use POST, PUT or PUT we use the -X flag as follows curl -X 'POST' http://example.com -d {what I want to input in JSON format}