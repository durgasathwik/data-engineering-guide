# Day 3: Many-to-Many & Bridge Tables

## Scenario: Employees and Projects
- **Entity A**: Employee
- **Entity B**: Project
- **Relationship**: Many-to-Many (One employee works on many projects; one project has many employees).
- **Solution**: Bridge Table `employee_projects`.

## Scenario: Orders and Products
- **Entity A**: Order
- **Entity B**: Product
- **Relationship**: Many-to-Many.
- **Solution**: Bridge Table `order_items` (also stores grain-specific details like `quantity` and `price_at_purchase`).
