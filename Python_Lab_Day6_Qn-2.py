blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
for x in blog_views:
    if x > 1000:
        print("Trending")
    elif x >= 500 and x >= 1000:
        print("Average")
    elif x <500:
        print("Low Traffic")
Total_views = sum(blog_views)
print("Total number of views:", Total_views)
count = blog_views.count("Trending")
print("Number of trending posts: ", count)
