def process_payment(amount: float) -> str:
    """
    Stub function to simulate payment processing.
    In a real implementation, this function would interact with a payment gateway.
    
    Args:
        amount (float): The amount to be processed.

    Returns:
        str: A message indicating the payment status.
    """
    return f"Payment of {amount}₽ processed successfully. (Stub implementation)"


def get_payment_link() -> str:
    """
    Stub function to return a payment link.
    In a real implementation, this function would generate a link to a payment gateway.
    
    Returns:
        str: A URL to the payment page.
    """
    return "https://payment-gateway.example.com/checkout"  # Stub URL for payment