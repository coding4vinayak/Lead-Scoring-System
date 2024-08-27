// Add any JavaScript you need for your application here
// For example, you could add form validation or interactivity

document.addEventListener('DOMContentLoaded', function() {
    // Example: Display an alert when the form is submitted
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        alert('Form submitted!');
        // You can add more logic here, e.g., validation before submitting
    });
});
