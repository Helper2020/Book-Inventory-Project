from inventory_manager.models import Genre, Author, Book
import json


def run():
    with open('/home/gabriel/Documents/projects/book-info-scrape/books_info.json', 'r') as file:

        # Read json file
        json_obj= json.load(file)


        Author.objects.all().delete()
        Genre.objects.all().delete()
        Book.objects.all().delete()
          
        
        for book_info in json_obj:
            # Get or create genre
            genre = book_info['genre']
            genre_obj, _ = Genre.objects.get_or_create(name=genre)

            # Get or create author
            auth_first_name = book_info['first_name']
            auth_last_name = book_info['last_name']
            author_obj, _ = Author.objects.get_or_create(first_name=auth_first_name, last_name=auth_last_name)

            book = Book(
                title = book_info['title'],
                author = author_obj,
                synopsis = book_info['synopsis'],
                isbn = book_info['upc'],
                price = float(book_info['price']),
                quantity = int(book_info['stock']),
                genre = genre_obj,
                book_image = book_info['img_file_path']
            )
           
            book.save()
        

      
