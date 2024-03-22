document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('click', (e) => {
        closeAlerts();
    });
    userMenu();
    userMobileMenu();
    checkURL();
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

function userMobileMenu() {
    if (document.getElementById('mobile-menu-button')) {
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');

        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
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

function checkURL() {
    const url = window.location.pathname.toString();
    const selected_class = ['bg-gray-900', 'text-white'];
    if (document.getElementById('books')) {
        const books = document.getElementById('books');
        const authors = document.getElementById('authors');
        const genders = document.getElementById('genders');
        if (url.includes('books')) {
            if (!books.classList.contains(selected_class[0])) {
                selected_class.forEach(item => {
                    books.classList.add(item);
                    authors.classList.remove(item);
                    genders.classList.remove(item);
                });
            }
            if(!authors.classList.contains('text-gray-300')) {
                authors.classList.add('text-gray-300');
            }
            if(!genders.classList.contains('text-gray-300')) {
                genders.classList.add('text-gray-300');
            }
        } else if (url.includes('authors')) {
            if (!authors.classList.contains(selected_class[0])) {
                selected_class.forEach(item => {
                    authors.classList.add(item);
                    books.classList.remove(item);
                    genders.classList.remove(item);
                });
                if(!books.classList.contains('text-gray-300')) {
                    books.classList.add('text-gray-300');
                }
                if(!genders.classList.contains('text-gray-300')) {
                    genders.classList.add('text-gray-300');
                }
        } else if (url.includes('genders')) {
            console.log('hola')
            if (!genders.classList.contains(selected_class)[0]) {
                selected_class.forEach(item => {
                    genders.classList.add(item);
                    books.classList.remove(item);
                    authors.classList.remove(item);
                });
                if(!books.classList.contains('text-gray-300')) {
                    books.classList.add('text-gray-300');
                }
                if(!authors.classList.contains('text-gray-300')) {
                    authors.classList.add('text-gray-300');
                }
            }
        }
    } else if (document.getElementById('genders')) {
        const index = document.getElementById('index');
        if (url.includes('')) {
            console.log('hola');
        }
    }
    }}