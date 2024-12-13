# Smart Cart 🛒

Smart Cart is a Django-based application that simplifies the shopping experience. It uses OpenCV and Pyzbar to scan product barcodes and manage a virtual shopping cart. Users can add, remove, or edit item quantities and generate a final bill with ease.

---

## Features ✨

- **Barcode Scanning**: Real-time barcode detection using OpenCV and Pyzbar.
- **Cart Management**: 
  - Add products to the cart.
  - Remove products from the cart.
  - Edit quantities of items in the cart.
- **Automatic Bill Calculation**: Displays the total cost of all items in the cart.
- **User-Friendly Interface**: Built with Django templates for an interactive web experience.

---

## Tech Stack ⚙️

- **Backend**: Django (Python framework)
- **Barcode Scanning**: OpenCV and Pyzbar libraries
- **Frontend**: HTML, CSS, JavaScript (via Django templates)
- **Database**: SQLite (or any other Django-compatible database)
- **Libraries**:
  - OpenCV: For video capture and image processing.
  - Pyzbar: For barcode decoding.

---

## Installation 🛠️

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps to Install

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/smart-cart.git
   cd smart-cart
