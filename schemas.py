"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# ClaimFlow-specific schemas

class ContactSubmission(BaseModel):
    """Inbound contact or demo request from marketing site"""
    name: str = Field(..., min_length=2, description="Full name of the requester")
    email: EmailStr = Field(..., description="Work email")
    company: Optional[str] = Field(None, description="Company name")
    message: str = Field(..., min_length=5, description="Message or use case")
    source: str = Field("website", description="Source of submission")

class Subscriber(BaseModel):
    """Newsletter signup"""
    email: EmailStr = Field(..., description="Subscriber email")
    consent: bool = Field(True, description="GDPR/consent flag")
    source: str = Field("website", description="Source of signup")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
