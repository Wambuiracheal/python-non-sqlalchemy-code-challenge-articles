class Article:
    all= []

    def __init__(self, author, magazine, title):
        if not (5<= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self.author = author
        self.magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        raise AttributeError("Title cannot be reset")
    
        
class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []
    
    def add_article(self, article):
        if isinstance(article, Article):
            self._articles.append(article)

    def articles(self):
        return self._articles
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self,value):
        raise AttributeError("Author name cannot be changed")

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        Article(self,magazine,title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author, 0)+ 1
        return [author for author, count in author_count.items() if count > 2]