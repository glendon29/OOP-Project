from blog_content import Blog

def uploadBlog(title, subtitle,content,author):
    blog_post = title + ',' + subtitle + ',' + content +',' + author +'\n'
    user_file = open('file/contents.txt', 'a')
    user_file.write(blog_post)

def processBlog():
    blogList = []
    user_file = open('file/contents.txt', 'r')
    for blist in user_file:
        list = blist.split(',')
        a=Blog(list[0],list[1],list[3],list[4])
        blogList.append(a)
    return blogList