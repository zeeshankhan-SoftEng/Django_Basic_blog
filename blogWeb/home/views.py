import logging
from collections import defaultdict

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from home.models import Blog_Post,Comment,Author
from home.forms import BlogPostForm, CommentForm

from home.filters import register


class HomeView(View):
    template_name = 'Home.html'
    def get(self, request):
        query = request.GET.get('q')
        if query:
            data = Blog_Post.objects.filter(title__icontains=query)
        else:
            data = Blog_Post.objects.all()

        page_number = request.GET.get('page')
        paginator = Paginator(data, 10)  # Set the number of items per page.

        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        context = {'peoples': page, 'search_query': query}

        return render(request, self.template_name, context)

class CreateBlogView(View):
    template_name = 'generate_view.html'

    def get(self, request):
        form = BlogPostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            # Form is not valid, handle errors
            # You can log the errors or display them in the form
            # Logging the errors is a good practice for debugging
            # You can log the errors using the Python logging module

            # Example of logging errors
            import logging
            logger = logging.getLogger(__name__)
            logger.error('Form errors: %s', form.errors)

            # You can also pass the form with errors to the template to display them
            return render(request, self.template_name, {'form': form})


class DetailsBlogView(View):
    template_name = 'Details_view.html'

    def get(self, request, id):
        try:
            queryset = get_object_or_404(Blog_Post, id=id)
        except Http404:
            return render(request, 'not_found.html')

        data = {
            'id': queryset.id,
            'title': queryset.title,
            'date': queryset.date,
            'content': queryset.content
        }

        comments = Comment.objects.filter(blog_post=queryset)
        existing_authors = Author.objects.filter(comment__blog_post=queryset).distinct()

        # Create a dictionary to group comments by author name
        grouped_comments = defaultdict(list)

        for comment in comments:
            author_name = comment.author.name
            grouped_comments[author_name].append(comment)

        # Convert the grouped_comments dictionary to a list of tuples
        grouped_comments_list = list(grouped_comments.items())

        # Add comments and grouped_comments to the data dictionary
        data['comments'] = comments
        data['grouped_comments'] = grouped_comments_list
        data['existing_authors'] = existing_authors

        return render(request, self.template_name, context={'people': data})

    def post(self, request, id):
        queryset = get_object_or_404(Blog_Post, id=id)
        comment_form = CommentForm(request.POST)


        if comment_form.is_valid():
            author_name = request.POST.get('author')

            if author_name:
                existing_authors = Author.objects.filter(comment__blog_post=queryset, name=author_name)
                if existing_authors.exists():
                    print("true")
                    # An existing author with the same name exists
                    author = existing_authors.first()
                else:
                    # Create a new author with the given name
                    author = Author.objects.create(name=author_name)

            else:
                # Author name is not provided
                author = None


            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = queryset
            new_comment.author = author
            new_comment.save()

            return redirect('details_blog', id=id)
        print("not getting")
        comments = Comment.objects.filter(blog_post=queryset)
        data = {
            'title': queryset.title,
            'date': queryset.date,
            'content': queryset.content,
            'comments': comments,
            'comment_form': comment_form,
            'id': id
        }

        return render(request, self.template_name, context={'people': data})


class DeleteBlogView(View):

    def post(self, request, id):
        queryset = get_object_or_404(Blog_Post, id=id)
        queryset.delete()
        return redirect('/')

class UpdateBlogView(View):
    template_name = 'update_view.html'

    def get(self, request, id):
        queryset = get_object_or_404(Blog_Post, id=id)
        form = BlogPostForm(instance=queryset)
        return render(request, self.template_name, {'form': form, 'id': id})

    def post(self, request, id):
        queryset = get_object_or_404(Blog_Post, id=id)
        form = BlogPostForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            # Log the errors
            logger = logging.getLogger('django')
            logger.error(f'Error in UpdateBlogView for post with id {id}: {form.errors}')

            return render(request, self.template_name, {'form': form, 'id': id})