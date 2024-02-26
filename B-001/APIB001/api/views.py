from typing import Any
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import BlogPost

class BlogPostView(View):
    """
    A view to handle CRUD operations for BlogPost objects.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Dispatch method to handle CSRF exemption and call superclass dispatch.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, ID=0):
        """
        Handle GET request to retrieve BlogPost(s) based on ID.
        """
        try:
            if ID > 0:
                post = BlogPost.objects.get(ID=ID)
                data = {'message': "Success", 'post': {'ID': post.ID, 'title': post.title, 'link': post.link}}
            else:
                posts = BlogPost.objects.all()
                if posts:
                    data = {'message': "Success", 'posts': [{'ID': post.ID, 'title': post.title, 'link': post.link} for post in posts]}
                else:
                    data = {'message': 'post not found'}
        except BlogPost.DoesNotExist:
            data = {'message': 'post not found'}
        return JsonResponse(data)
    
    def post(self, request):
        """
        Handle POST request to create a new BlogPost object.
        """
        try:
            jd = json.loads(request.body)
            BlogPost.objects.create(title=jd['title'], link=jd['link'])
            data = {'message': "Success"}
        except json.JSONDecodeError:
            data = {'message': 'Invalid JSON data'}
        except KeyError:
            data = {'message': 'Missing title or link in JSON data'}
        return JsonResponse(data)

    def put(self, request, ID):
        """
        Handle PUT request to update an existing BlogPost object.
        """
        try:
            jd = json.loads(request.body)
            post = BlogPost.objects.get(ID=ID)
            post.title = jd['title']
            post.link = jd['link']
            post.save()
            data = {'message': "Success", 'post': {'ID': post.ID, 'title': post.title, 'link': post.link}}
        except BlogPost.DoesNotExist:
            data = {'message': 'post not found'}
        except json.JSONDecodeError:
            data = {'message': 'Invalid JSON data'}
        except KeyError:
            data = {'message': 'Missing title or link in JSON data'}
        return JsonResponse(data)

    def delete(self, request, ID):
        """
        Handle DELETE request to delete a BlogPost object based on ID.
        """
        try:
            post = BlogPost.objects.get(ID=ID)
            post.delete()
            data = {'message': "Success"}
        except BlogPost.DoesNotExist:
            data = {'message': 'post not found'}
        return JsonResponse(data)
