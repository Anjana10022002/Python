blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
for x in blog_views:
    if x > 1000:
        print("Trending")
    elif 500 <= x <= 1000:
        print("Average")
    elif x < 500:
        print("Low Traffic")
Total_views = sum(blog_views)
print("Total number of views:", Total_views)
count = 0
for x in blog_views:
    if x > 1000:
        count = count + 1
print("Count of trending posts: ", count)
