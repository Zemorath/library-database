# Library Database
---

## Purpose

This project was designed to create and interact with a simple database using Python and SQL. I chose to focus on a virtual library to help keep track of user's books as they buy and add them online. This represents, at least in part, the backend of a website such as goodreads that allows users to add books to various lists and keep track of ratings, book info, etc. A lot of websites now limit the amount of books a user can add to their accounts before paying for more space. Something like this, and hopefully more fleshed out in the future, would allow a user to add any number of books that they desire and be able to navigate through the list to requested data.

---

## Design

The CLI is fairly simple and straightforward. You can add owners and their books, filter populated lists by either age or favorite genre, and make any edits necessary to either of those groups. This is setup to be a one-to-many relationship between the two tables. 

Here is a quick walkthrough of the CLI.
[Link](https://youtu.be/eVRNk2zEyuI)

## Changes

Some changes I could have made that could be implemented in the future would begin with adding more information to both the books and the owners such as edition, page numbers, and ratings for the books. For owners I would like to add an email address and password to represent a log in. Another one would be filtering a list to only contain those owners that have a specific book. I.E. all those who have Red Rising by Pierce Brown. Overall, I think the flow of the CLI is good and I don't know of any changes I would make to that at this stage. 


## Features

1. Settings menu to add/drop necessary tables
2. Compact view of the owners before selecting. After selecting one owner it will show additional information
3. Can filter by age or favorite genre
4. Also compact view of the books that will show the ISBN once one is selected.
5. You always know where you are in the CLI and what it is that you are editing. Minimal request for for word input, only for menu navigation.