# Day 1: Food Delivery App Data Model

## 1. Identified Entities
- **Customer**: A person who places orders.
- **Restaurant**: An establishment that prepares food.
- **Order**: A specific request for food by a customer.
- **Driver**: A person who delivers the order.
- **Payment**: The financial transaction for an order.

## 2. Entity Attributes
### Customer
- customer_id
- name
- email
- phone_number

### Restaurant
- restaurant_id
- restaurant_name
- address
- rating

### Order
- order_id
- customer_id
- restaurant_id
- order_status
- order_time

### Driver
- driver_id
- driver_name
- vehicle_type
- current_latitude/longitude

### Payment
- payment_id
- order_id
- amount
- payment_method

## 3. Relationships
- **Customer to Order**: One-to-Many (One customer can place many orders).
- **Restaurant to Order**: One-to-Many (One restaurant can fulfill many orders).
- **Order to Driver**: One-to-One (One order is assigned to one driver at a time).
- **Order to Payment**: One-to-One (One order has one payment record).
