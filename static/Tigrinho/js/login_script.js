// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const loginBtn = document.getElementById('show-login');
    const signupBtn = document.getElementById('show-signup');
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const showRegisterLink = document.getElementById('show-register');

    loginBtn.addEventListener('click', function() {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    });

    signupBtn.addEventListener('click', function() {
        registerForm.style.display = 'block';
        loginForm.style.display = 'none';
    });

    showRegisterLink.addEventListener('click', function(event) {
        event.preventDefault();
        registerForm.style.display = 'block';
        loginForm.style.display = 'none';
    });
});
