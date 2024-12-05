// Displays toast messages
document.addEventListener('DOMContentLoaded', function () {
    const toastElList = [].slice.call(document.querySelectorAll('.toast'));
    const toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl);
    });

    // Show all toasts
    toastList.forEach(toast => toast.show());

    // Add close button functionality
    toastElList.forEach(function (toastEl) {
        const closeButton = toastEl.querySelector('.toast-close');
        if (closeButton) {
            closeButton.addEventListener('click', function () {
                const toast = new bootstrap.Toast(toastEl);  // Initialize toast instance
                toast.hide();  // Hide the toast when the close button is clicked
            });
        }
    });
});