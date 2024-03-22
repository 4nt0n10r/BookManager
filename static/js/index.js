document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('click', (e) => {
        closeAlerts();
    });
    userMenu();
    
});

function userMenu(){

    if (document.getElementById('user-menu-button')) {
        const userMenuButton = document.getElementById('user-menu-button');
        const userMenu = document.getElementById('user-menu');

        userMenuButton.addEventListener('click', () => {
            userMenu.classList.toggle('hidden');
        });
    }

}

function closeAlerts() {
    if (document.querySelector('.alert')) {
        const alerts = document.querySelectorAll('.alert');

        alerts.forEach(alert => {
            setTimeout(() => {
                alert.remove();
            }, 3000);
        });
    }
}