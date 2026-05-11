# Week 4: Advanced Data Modeling Concepts

## Day 3: Many-to-Many & Bridge Tables
### Scenario: Employees and Projects
- **Entity A**: Employee
- **Entity B**: Project
- **Relationship**: Many-to-Many (One employee works on many projects; one project has many employees).
- **Solution**: Bridge Table `employee_projects`.

### Scenario: Orders and Products
- **Entity A**: Order
- **Entity B**: Product
- **Relationship**: Many-to-Many.
- **Solution**: Bridge Table `order_items` (also stores grain-specific details like `quantity` and `price_at_purchase`).

---

## Day 4: Grain Definition
- **fact_orders**: One row represents one unique order placed by a customer.
- **fact_order_items**: One row represents one unique product line item within an order.
- **fact_payments**: One row represents one successful or failed payment transaction.
- **fact_daily_sales_snapshot**: One row represents the total aggregated sales for one specific day.

---

## Day 5: Normalization vs Denormalization
- **OLTP (Normalized)**: Focuses on efficiency for writes/updates. Data is split into many tables (e.g., `customers`, `addresses`, `cities`).
- **OLAP (Denormalized)**: Focuses on efficiency for reads/reporting. Data is combined (e.g., a wide `dim_customer` table with address info included).

---

## Day 6: Slowly Changing Dimensions (SCD)
- **SCD Type 1**: Overwrite old data. Use for fixing errors (e.g., fixing a typo in a customer's name).
- **SCD Type 2**: Keep history. Use for tracking changes (e.g., tracking when a customer moves from 'City A' to 'City B' to keep historical sales attributed to the correct location).
