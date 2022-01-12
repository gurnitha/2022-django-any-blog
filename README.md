# 2022-django-any-blog
Build Any Blog using Django v3.2.7


#### 1. Create django project 'config' inside the current dir

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. Create django apps: apps/posts and apps/marketing

        modified:   README.md
        new file:   apps/marketing/__init__.py
        new file:   apps/marketing/admin.py
        new file:   apps/marketing/apps.py
        new file:   apps/marketing/migrations/__init__.py
        new file:   apps/marketing/models.py
        new file:   apps/marketing/tests.py
        new file:   apps/marketing/views.py
        new file:   apps/posts/__init__.py
        new file:   apps/posts/admin.py
        new file:   apps/posts/apps.py
        new file:   apps/posts/migrations/__init__.py
        new file:   apps/posts/models.py
        new file:   apps/posts/tests.py
        new file:   apps/posts/views.py
        modified:   config/settings.py


#### 3. Create home page: templates, views and urls 

        modified:   README.md
        new file:   apps/posts/urls.py
        modified:   apps/posts/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/index.html


#### 4. Adding and loading static files

        modified:   README.md
        modified:   config/settings.py
        new file:   static_in_env/css/custom.css
        ...
        new file:   static_in_env/vendor/popper.js/umd/poppper.js.flow
        modified:   templates/index.html


#### 5. Create and use base template

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/index.html 


#### 6. Refactor base templates

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/shared/footer.html
        new file:   templates/shared/head.html
        new file:   templates/shared/header.html
        new file:   templates/shared/scripts.html


#### 7. Refactor index template

        modified:   README.md
        new file:   templates/home/divider.html
        new file:   templates/home/featured-posts.html
        new file:   templates/home/gallery.html
        new file:   templates/home/hero.html
        new file:   templates/home/intro.html
        new file:   templates/home/latest-posts.html
        new file:   templates/home/newsletter.html
        modified:   templates/index.html


#### 8. Adding page title

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/index.html 


#### 9. Creating blog page: template, views, urls

        modified:   README.md
        modified:   apps/posts/urls.py
        modified:   apps/posts/views.py
        new file:   static_in_env/favicon.ico
        new file:   templates/blog.html
        modified:   templates/shared/head.html
        modified:   templates/shared/header.html


#### 10. Refactor blog template

        modified:   README.md
        modified:   templates/blog.html
        new file:   templates/blog/categories.html
        new file:   templates/blog/latest-posts.html
        new file:   templates/blog/pagination.html
        new file:   templates/blog/posts.html
        new file:   templates/blog/search.html
        new file:   templates/blog/tags.html


#### 10. Moving aside files from blog folder to shared folder

        modified:   apps/posts/urls.py
        modified:   apps/posts/views.py
        renamed:    templates/blog.html -> templates/posts-list.html
        renamed:    templates/blog/categories.html -> templates/posts/categories.html
        renamed:    templates/blog/pagination.html -> templates/posts/pagination.html
        renamed:    templates/blog/posts.html -> templates/posts/posts.html
        modified:   templates/shared/header.html


#### 11. Create single post page: template, views, urls and links

        modified:   README.md
        modified:   apps/posts/urls.py
        modified:   apps/posts/views.py
        modified:   templates/home/featured-posts.html
        new file:   templates/post-single.html
        modified:   templates/posts/posts.html
        modified:   templates/shared/header.html


#### 12. Setting up postgres database

        modified:   README.md
        modified:   config/settings.py


#### 13. Setting up production's path for MEDIA and STATIC root

        modified:   README.md
        modified:   apps/posts/admin.py
        modified:   apps/posts/models.py
        modified:   config/urls.py

