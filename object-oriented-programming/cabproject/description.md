# Cab Booking System

This is a Python implementation of a Cab Booking System. The system allows customers to book cabs and drivers to manage their profiles and vehicles.

## Features

- Customers can:
  - Create a profile
  - Set their preferred payment method
  - View their booking information
  - Cancel a booking

- Drivers can:
  - Create a profile
  - Manage their vehicle information
  - View their profile along with the vehicle details

## Classes

- `Profile`: Abstract class for user types (Customer and Driver). Contains common attributes and methods.
- `Customer`: Class representing a customer profile. Inherits from `Profile` class.
- `Driver`: Class representing a driver profile. Inherits from `Profile` class and aggregates a `Vehicle` object.
- `Vehicle`: Abstract class for different vehicle types (Car, Van, Bike). Contains attributes and methods related to vehicles.
- `Car`, `Van`, `Bike`: Classes representing specific vehicle types. Inherit from `Vehicle` class.
- `PaymentMethod`: Abstract class for different payment methods (Cash, Credit Card). Contains attributes and methods related to payment methods.

## Usage

1. Create an instance of `Customer` or `Driver` class by providing the required information.
2. For customers, set their preferred payment method using the `set_payment_method` method.
3. View booking information using the `view_booking` method (applicable to customers only).
4. Cancel a booking using the `cancel_booking` method (applicable to customers only).
5. For drivers, manage their vehicle information using the `vehicle_display` method.

## Example (Actual code has complex menus to call these functions)

```python
# Create a customer profile
customer = Customer('C001', 'password123', 'John Doe', 'Male')

# Set the payment method
payment_method = customer.set_payment_method()

# View booking information
customer.view_booking(booking_info)

# Cancel a booking
customer.cancel_booking()

# Create a driver profile
driver = Driver('D001', 'password456', 'Jane Smith', 'Female', vehicle)

# Display driver profile along with vehicle information
driver.vehicle_display()
