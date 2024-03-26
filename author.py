class Author:
    def __init__ (self, author_id, meno, bio):
        self.author_id = author_id
        self.meno = meno
        self.bio = bio

    def __str__(self):
        return f"Author ID: {self.author_id}\nName: {self.meno}\nBio: {self.bio}"


