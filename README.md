# Django Blog Application

This is a simple Django blog application that allows you to create, view, update, and delete blog posts. It also provides a search feature to search for specific blog posts.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Views](#views)
  - [HomeView](#homeview)
  - [CreateBlogView](#createblogview)
  - [DetailsBlogView](#detailsblogview)
  - [DeleteBlogView](#deleteblogview)
  - [UpdateBlogView](#updateblogview)

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages using `pip install -r requirements.txt`.
4. Migrate the database with `python manage.py migrate`.
5. Create a superuser to manage the admin panel with `python manage.py createsuperuser`.
6. Start the development server with `python manage.py runserver`.

## Usage
1. Access the admin panel at `http://localhost:8000/admin/` and log in with the superuser credentials you created.
2. Create blog posts, authors, and comments through the admin panel.
3. Access the blog application at `http://localhost:8000/` to view, create, update, or delete blog posts.
4. Use the search feature to find specific blog posts by title.

## Views

### HomeView
- URL: `/`
- Description: Displays a list of blog posts. It supports a search feature to filter blog posts by title.

### CreateBlogView
- URL: `/create/`
- Description: Allows you to create a new blog post. It provides a form to enter the title and content of the blog post.

### DetailsBlogView
- URL: `/details/<int:id>/`
- Description: Displays the details of a specific blog post, including its title, date, content, and associated comments. It also provides a form to add new comments.

### DeleteBlogView
- URL: `/delete/<int:id>/`
- Description: Deletes a specific blog post by its ID.

### UpdateBlogView
- URL: `/update/<int:id>/`
- Description: Allows you to update an existing blog post. It pre-fills the form with the existing content of the blog post.

## Contributors
- Zeeshan Khan

Feel free to contribute to this project and make it even better!