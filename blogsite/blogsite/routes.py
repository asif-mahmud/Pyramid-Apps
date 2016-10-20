from .security.authorizaton import (
    HomePage,
    ShowProfile,
    EditProfile,
    EditProfile,
    AddBlog,
    EditBlog,
    ShowBlog,
    ShowAllBlogs,
    AuthPosts,
)

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/', factory=HomePage)
    config.add_route('login', '/login', factory=HomePage)
    config.add_route('logout', '/logout', factory=HomePage)
    config.add_route('register', '/register', factory=HomePage)

    config.add_route('show_profile', '/profile/{pid}', factory=ShowProfile)
    config.add_route('edit_profile', '/profile/edit/{pid}', factory=EditProfile)

    config.add_route('add_blog', '/add/blog', factory=AddBlog)
    config.add_route('edit_blog', '/edit/blog/{bid}', factory=EditBlog)
    config.add_route('show_blog', '/blog/{bid}', factory=ShowBlog)
    config.add_route('all_blogs', '/blogs', factory=ShowAllBlogs)

    config.add_route('add_post', '/add/post', factory=AuthPosts.add_post)
    config.add_route('edit_post', '/edit/post/{pid}', factory=AuthPosts.edit_post)
    config.add_route('show_post', '/post/{pid}', factory=AuthPosts.show_posts)
    config.add_route('show_all_posts', '/posts', factory=AuthPosts.show_posts)
