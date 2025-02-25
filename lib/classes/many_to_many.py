class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title_getter(self):
        return self._title
    
    @title_getter.setter
    def title(self, title_value):
        if (not hasattr(self, 'title')) and (type(title_value) == str) and (5 <= len(title_value) <= 50):
            self._title = title_value
        else:
            raise Exception

    @property
    def author_getter(self):
        return self._author
    
    @author_getter.setter
    def author(self, author_value):
        if isinstance(author_value, Author):
            self._author = author_value
        else:
            raise Exception

    @property
    def magazine_getter(self):
        return self._magazine
    
    @magazine_getter.setter
    def magazine(self, magazine_value):
        if (isinstance(magazine_value, Magazine)):
            self._magazine = magazine_value
        else:
            raise Exception

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name_getter(self):
        return self._name

    @name_getter.setter
    def name(self, name_value):
        if (not hasattr(self, 'name')) and (type(name_value) == str) and (0 < len(name_value)):
            self._name = name_value
        else:
            raise Exception

    # Relationship: 1 Auther has many articles (1-to-Many Relationship):
    def articles(self):
        return [article for article in Article.all if article.author is self]

    # Relationship: 1 Author has many Magazines (through Articles) (Many-to-Many Relationship):
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        num_of_articles_by_author = [magazine.category for magazine in self.magazines()]
        if len(num_of_articles_by_author) == 0:
            return None
        return num_of_articles_by_author

class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    def name(self, name_value):
        if (type(name_value) == str) and (2 <= len(name_value) <= 16):
            self._name = name_value
        else:
            raise Exception

    @property
    def category_getter(self):
        return self._category
    
    @category_getter.setter
    def category(self, category_value):
        if (type(category_value) == str) and (0 < len(category_value)):
            self._category = category_value
        else:
            raise Exception

    # Relationship: 1 Magazine has many articles (1-to-Many Relationship)
    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    # Relationship: 1 Magazine has many authors (1-to-Many Relationship)
    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        list_of_magazine_articles = [article.title for article in self.articles()]
        if len(list_of_magazine_articles) == 0:
            return None
        return list_of_magazine_articles

    def contributing_authors(self):
        author_list = [author for author in self.contributors() if self.has_more_than_2_articles(author)]
        if len(author_list) == 0:
            return None
        else:
            return author_list


    def has_more_than_2_articles(self, author):
        article_list = [article for article in author.articles() if article.magazine is self]
        if len(article_list) > 2:
            return True
        else:
            return False
        
    # Advanced Deliverable
    @classmethod
    def top_publisher(self):
         # Check the magazines in Articles.all
        publisher_list = [article.magazine for article in Article.all]
        if len(publisher_list) == 0:
            return None
        else:
            return max(publisher_list, key=lambda p: len(p.articles()))


