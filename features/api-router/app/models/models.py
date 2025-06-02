from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    users: List["User"] = Relationship(back_populates="role")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")

    role: Optional[Role] = Relationship(back_populates="users")
    contents: List["Content"] = Relationship(back_populates="author")
    comments: List["Comment"] = Relationship(back_populates="user")

class ContentCategoryLink(SQLModel, table=True):
    content_id: Optional[int] = Field(default=None, foreign_key="content.id", primary_key=True)
    category_id: Optional[int] = Field(default=None, foreign_key="category.id", primary_key=True)

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    contents: List["Content"] = Relationship(back_populates="categories", link_model=ContentCategoryLink)

class ContentTagLink(SQLModel, table=True):
    content_id: Optional[int] = Field(default=None, foreign_key="content.id", primary_key=True)
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)

class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    contents: List["Content"] = Relationship(back_populates="tags", link_model=ContentTagLink)

from datetime import datetime

class Content(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str
    title: str
    description: str
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")

    author: Optional[User] = Relationship(back_populates="contents")
    categories: List[Category] = Relationship(back_populates="contents", link_model=ContentCategoryLink)
    tags: List[Tag] = Relationship(back_populates="contents", link_model=ContentTagLink)
    comments: List["Comment"] = Relationship(back_populates="content")

class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content_id: Optional[int] = Field(default=None, foreign_key="content.id")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    text: str
    date: datetime

    content: Optional[Content] = Relationship(back_populates="comments")
    user: Optional[User] = Relationship(back_populates="comments")
