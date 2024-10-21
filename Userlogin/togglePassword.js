document.addEventListener('DOMContentLoaded', function () {
    // Select elements for password toggle functionality
    const togglePassword = document.querySelector('#togglePassword');
    const password = document.querySelector('#password');

    // Add click event listener for password visibility toggle
    togglePassword.addEventListener('click', function () {
        // Check if the password is currently visible
        const isPasswordVisible = password.getAttribute('type') === 'text';

        // Toggle the input type between 'password' and 'text'
        password.setAttribute('type', isPasswordVisible ? 'password' : 'text');

        // Remove previous icon classes to ensure proper switch
        togglePassword.classList.remove('icon-view_off', 'icon-view-2');

        // Add appropriate icon class based on visibility state
        if (isPasswordVisible) {
            togglePassword.classList.add('icon-view-2'); // Closed eye icon
        } else {
            togglePassword.classList.add('icon-view_off'); // Open eye icon
        }

        // Log the updated class list to the console for debugging
        console.log(togglePassword.classList);
    });

    // Select elements for confirm password toggle functionality
    const toggleConfirmPassword = document.querySelector('#toggleConfirmPassword');
    const confirmPassword = document.querySelector('#confirmPassword');

    // Add click event listener for confirm password visibility toggle
    toggleConfirmPassword.addEventListener('click', function () {
        // Check if the confirm password is currently visible
        const isConfirmPasswordVisible = confirmPassword.getAttribute('type') === 'text';

        // Toggle the input type between 'password' and 'text'
        confirmPassword.setAttribute('type', isConfirmPasswordVisible ? 'password' : 'text');

        // Remove previous icon classes to ensure proper switch
        toggleConfirmPassword.classList.remove('icon-view_off', 'icon-view-2');

        // Add appropriate icon class based on visibility state
        if (isConfirmPasswordVisible) {
            toggleConfirmPassword.classList.add('icon-view-2'); // Closed eye icon
        } else {
            toggleConfirmPassword.classList.add('icon-view_off'); // Open eye icon
        }

        // Log the updated class list to the console for debugging
        console.log(toggleConfirmPassword.classList);
    });
});
