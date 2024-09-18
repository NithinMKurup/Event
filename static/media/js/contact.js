function showAlert(event) {
    event.preventDefault(); // Prevent form submission

    // Show the popup message
    alert('Thank you for your response');

    // Redirect to the contact page after the message is dismissed
    setTimeout(function() {
        window.location.href = '/contact.html';
    }, 100); // Small delay to ensure alert is shown
}