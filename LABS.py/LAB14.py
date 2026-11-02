books=[("Python Crash Course", "Eric Matthes", "2019", "Programming"),
          ("Automate The Boring Stuff", "Al Sweigart", "2020", "Programming"),
          ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
          ("Clean Code", "Robert C Martin", "2008", "Software Engineering")]

categories = {"Programming", "AI", "Software Engineering"}
wishlist = {"Data Science", "AI", "Web Development"}

while True:
    print("Select an option:")
    print("1. View Cataloged Books:")
    print("2. Add New Book:")
    print("3. View Unique Library Categories:")
    print("4. Add Category To Student Wishlist:")
    print("5. Run Category Gap Analysis:")
    print("6. Exit")

    choice=input("Enter choice (1-6): ").strip()

    if choice == "1":
        print("Current Library Catalog")
        for title, author, year, cat in books:
            print(f'"{title}" by {author} [{cat}]')
        print(f"Total Books: {len(books)}")


    elif choice == "2":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        category = input("Enter category: ")
                
        new_book = (title, author, category)
        books.append(new_book)
        categories.add(category)
        print("Book added successfully!")
        
    elif choice == "3":
        print("Library Categories")
        for cat in categories:
            print("-", cat)
        
    elif choice == "4":
        req_cat = input("Enter category to add to wishlist: ")
        wishlist.add(req_cat)
        print("Category added to student wishlist!")
        
    elif choice == "5":
        common = categories.intersection(wishlist)
        missing = wishlist.difference(categories)
        all_cats = categories.union(wishlist)
        
        print("Gap Analysis")
        print("Categories currently available that students want (Intersection):")
        print(common)
        print("Categories requested but NOT in library (Difference):")
        print(missing)
        print("All unique categories combined (Union):")
        print(all_cats)
        
    elif choice == "6":
        print("Exiting program.")
        break
        
    else:
        print("Invalid choice, please enter a number from 1 to 6.")