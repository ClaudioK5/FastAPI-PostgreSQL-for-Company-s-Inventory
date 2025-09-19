# FastAPI-PostgreSQL-for-Company-s-Inventory
This backend REST API built with FastAPI and PostgreSQL is designed to manage and track company inventory. It is part of a larger system that includes FastAPI + PostgreSQL pipeline handling customer orders and company purchases.

Together, these two services provide the foundation for the generation of a financial report on each semester.

The microservice offers two primary endpoints:

POST /inventory/ - to insert new item in the inventory;
GET /inventory/ - to retrieve all items from the inventory.
All data is saved in a PostgreSQL database (fastapi_company_inventory) and is containerized with Docker to allow easy deployment from anywhere.
