import datetime
import csv
import os

# Function to generate the receipt HTML file
def generate_receipt_html(payer_name, amount, receipt_number, filename="receipt.html"):
    # Get the current date
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    
    # Create the HTML receipt content
    receipt_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Payment Receipt</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                color: #333;
            }}
            .receipt {{
                border: 2px solid #333;
                padding: 20px;
                width: 30%;
                margin: 0 auto;
            }}
            .receipt h2 {{
                text-align: center;
            }}
            .receipt p {{
                font-size: 18px;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                margin-top: 20px;
                color: gray;
            }}
        </style>
    </head>
    <body>
        <div class="receipt">
            <h2>Payment Receipt</h2>
            <p><strong>Receipt Number:</strong> {receipt_number}</p>
            <p><strong>Payer Name:</strong> {payer_name}</p>
            <p><strong>Amount Paid:</strong> {amount:.2f}</p>
            <p><strong>Date:</strong> {current_date}</p>
            <div class="footer">
                <p>Thank you for your payment</p>
                <p>Visit Again</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Ensure receipts/ directory exists
    if not os.path.exists("receipts"):
        os.makedirs("receipts")
    
    # Define the filename and save the HTML receipt in the receipts directory
    receipt_filename = f"receipts/receipt_{receipt_number}.html"
    try:
        with open(receipt_filename, "w") as file:
            file.write(receipt_content)
        print(f"Receipt saved to {receipt_filename}")
    except Exception as e:
        print(f"Error saving receipt HTML file: {e}")

# Function to store the transaction details in the CSV file
def store_transaction_info(payer_name, amount, receipt_number):
    # Get the current date for the transaction record
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    
    # Check if the CSV file exists, if not, create it and write the header
    csv_filename = "transactions.csv"
    try:
        # Print the path to where the file is being written
        print(f"Attempting to write to CSV file: {os.path.abspath(csv_filename)}")
        
        file_exists = os.path.isfile(csv_filename)
        with open(csv_filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            
            # Write the header only if the file is being created
            if not file_exists:
                writer.writerow(["Receipt Number", "Payer Name", "Amount Paid", "Date"])
                print("Header written to CSV file.")
            
            # Write the transaction details
            writer.writerow([receipt_number, payer_name, amount, current_date])
        print(f"Transaction details stored for {payer_name} in transactions.csv")
    except Exception as e:
        print(f"Error storing transaction info in CSV file: {e}")

# Main execution loop for up to 10 customers
receipt_number = 123456  # Start receipt number
for i in range(10):  # Loop for up to 10 customers
    payer_name = input("Enter Customer Name: ")
    amount = 0  # Reset amount for each customer
    n = int(input("Enter number of products: "))
    
    for j in range(n):
        am = float(input("Enter the Amount: "))
        amount += am  # Accumulate the total amount for the customer
    
    # Generate the receipt and store transaction information
    generate_receipt_html(payer_name, amount, receipt_number)  # Generate the receipt
    store_transaction_info(payer_name, amount, receipt_number)  # Store transaction information
    
    # Increment the receipt number for the next customer
    receipt_number += 1
